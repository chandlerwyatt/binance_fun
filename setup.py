try:
    from setuptools import setup
except ImportError:
    from dsutils.core import setup

config = {
    'description': 'Binance Fun',
    'author': 'Chandler Wyatt',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'quietbeats@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['binance_fun'],
    'script': [],
    'name': 'binance_fun'
}

setup(**config)
