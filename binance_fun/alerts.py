import requests


class Alert(object):

    def execute(self, info):
        pass


class EmailAlert(Alert):

    url = "https://api.mailgun.net/v3/"

    def __init__(self, key, domain, to):
        self.domain = domain
        self.key = key
        self.to = to

    def execute(self, info):
        print(f"Sending email with info: {info}")
        data = {"from": "Mailgun Sandbox <postmaster@sandbox8aef451fb107442ba0"
                        "c03e402b3a0ab6.mailgun.org>",
                "to": self.to,
                "subject": "BTC Price Alert",
                "text": info}

        full_url = self.url + self.domain + "/messages"

        return requests.post(
            url=full_url,
            auth=("api", self.key),
            data=data)
