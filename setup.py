try:
    from setuptools import setup
except ImportError:
    from dsutils.core import setup

config = {
    'description': 'Exercise 46',
    'author': 'Chandler Wyatt',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'quietbeats@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'script': [],
    'name': 'ex46'
}

setup(**config)