import requests
import json
from pprint import pprint
from time import sleep
from binance_fun.alerts import EmailAlert
from binance_fun.triggers import PriceDeltaTrigger, PercentChangeTrigger

with open('config.json', 'r') as fp:
    config = json.load(fp)

email_alert = EmailAlert(key=config['mailgun_key'],
                         domain=config['mailgun_domain'],
                         to=config['email_to'])
API_URLS = {'price': 'https://api.binance.com/api/v1/ticker/price',
            '24hr': 'https://api.binance.com/api/v1/ticker/24hr'}
INTERVAL = 5


def run():
    trigger_map = {'price': [PriceDeltaTrigger(alerts=[email_alert])], '24hr': [PercentChangeTrigger(threshold=0.00, alerts=[email_alert])]}

    while True:
        print("Checking Price API")
        results = {}
        for k, v in API_URLS.items():
            response = requests.get(v, params={'symbol': 'BTCUSDT'}).json()
            results[k] = response
        pprint(results)

        for api, triggers in trigger_map.items():
            for trigger in triggers:
                trigger.evaluate(results[api])

        sleep(INTERVAL)


if __name__ == '__main__':
    run()
