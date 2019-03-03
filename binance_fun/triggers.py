class Trigger(object):

    def evaluate(self, data):
        pass


class PriceDeltaTrigger(Trigger):

    def __init__(self, alerts=[]):
        self.last_price = None
        self.alerts = alerts

    def evaluate(self, data):
        price = float(data['price'])
        if self.last_price:
            if price > self.last_price:
                info = (f"The BTCUSDT price ({price}) is higher than "
                        f"5 minutes ago ({self.last_price})")

                for alert in self.alerts:
                    alert.execute(info)

        self.last_price = price


class PercentChangeTrigger(Trigger):

    def __init__(self, threshold, alerts=[]):
        self.alerts = alerts
        self.threshold = threshold

    def evaluate(self, data):
        percent = float(data['priceChangePercent'])

        if abs(percent) is not None and abs(percent) > self.threshold:
            direction = 'up' if percent > 0 else 'down'

            info = (f"The BTCUSDT price ({data['lastPrice']}) is {direction} "
                    f"{percent}% over the last 24 hours.")

            for alert in self.alerts:
                alert.execute(info)
