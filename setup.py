from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='podfox', zip_safe=False,
    entry_points={
        'console_scripts': [
            'podfox = podfox.__init__:main'
        ]
    },
    install_requires=[
        'colorama>=0.3.7,<=0.3.9',
        'docopt==0.6.2',
        'feedparser==5.2.1',
        'requests>=2.11.1,<=2.18.1',
        'tqdm==4.14.0',
        ],
    )
