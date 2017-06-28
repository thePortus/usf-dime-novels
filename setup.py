try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': "dimenovels",
    'packages': [
        "usf_dime_novels",
        "usf_dime_novels.common",
        "usf_dime_novels.db"
        "usf_dime_novels.scraper"
    ],
    'install_requires': ['requests', 'BeautifulSoup4', 'peewee', 'selenium'],
    'version': "0.0.1",
    'description': "Python module to interact with the digital Dime Novel " +
    "collection from the University of South Florida",
    'author': "David J. Thomas",
    'author_email': "dave.a.base@gmail.com",
    'url': "https://github.com/thePortus/dimenovels",
    'download_url': "https://github.com/thePortus/" +
    "dimenovels/archive/master.zip",
    'keywords': [
        "Dime Novels"
    ],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Sociology :: History"
    ],
}

setup(**config)
