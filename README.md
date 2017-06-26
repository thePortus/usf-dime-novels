# USF Dime Novel Digital Collection

[![Build Status](https://travis-ci.org/thePortus/usf-dime-novels.svg?branch=master)](https://travis-ci.org/thePortus/usf-dime-novels)[![Coverage Status](https://coveralls.io/repos/github/thePortus/usf-dime-novels/badge.svg?branch=master)](https://coveralls.io/github/thePortus/usf-dime-novels?branch=master)

Python module to interact with the digital Dime Novel collection from the [University of South Florida](https://www.usf.edu).

[By David J. Thomas](mailto:dave.a.base@gmail.com), [thePortus.com](http://thePortus.com)<br>
Instructor of Ancient History and Digital Humanities<br>
Department of History<br>
University of South Florida

*For students of the Digital Humanities*

---

## CURRENTLY IN DEVELOPMENT, NOT INTENDED FOR RELEASE

---

The [University of South Florida's Digital Collections](http://digital.lib.usf.edu/) houses a repository of [historic dime novels](http://digital.lib.usf.edu/dimenovels). Spanning multiple collections with publications spanning many decades, the collection houses a wealth of information. Dime novels have long been a subject of scholarly interest, often reflecting evolving social and cultural concerns. Yet, performing a 'distant reading' of these texts is not easy. This scraper project provides easy automation for acquiring this data in formats designed for text analysis.

Beyond scraping the dime novels, this repo was designed to be reconfigurable, providing templates for performing advanced Python webscraping with only a semester or so of training (you will need to understand classes and inheritence). To do so, simply clone the repo, and make changes needed. The scraper module will provide base templates, create your own scraper that inherits the template to begin scraping pages. You will also need to create data models in the db module to reflect the data that you want to store from the scrape. Once you have scraped successfully, use the export module to output your data into .csvs or .txts. See documentation throughout each of these modules on how to accomplish this.

---
## Installation

_Knowledge requirements_: A beginner-intermediate understanding of Python and a beginner knowledge of command-line interface. For excellent tutorials on these subjects, check out Codecademy's tutorials on [Python](https://www.codecademy.com/learn/python) and [CLI](https://www.codecademy.com/learn/learn-the-command-line).

_Optional: works best if installed in a virtual environment_. [Directions for OSX, Linux](https://virtualenvwrapper.readthedocs.io/en/latest/), or if on [Directions for Windows](https://pypi.python.org/pypi/virtualenvwrapper-win)

To install the module...
```python
# Clone the repo and move inside the directory
git clone https://github.com/thePortus/dimenovels.git
cd dimenovels
# Install the Python dependencies
pip3 install -r requirements.txt
```

This module also requires that you install Selenium webdriver for your browser of choice. To do so, visit one of the following...
1. [Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
2. [Mozilla Firefox](https://github.com/mozilla/geckodriver/releases)
Download the driver, and place it somewhere in your $PATH (most likely your user folder). [Check here for further details](http://selenium-python.readthedocs.io/installation.html#drivers)

---

_For developers_, automated test running provided by nose2 and coverage. Tests require Firefox webdrivers (see above).

To run tests, make a separate virtualenv. Then, navigate to the repo root directory, enter `pip install -r requirements/testing.txt`. Set an environment variable named USF_DIME_NOVEL_DB to 'testing'. Finally, run the tests with `nose2`. Test and coverage results will print to screen and also save in the htmlcov subdirectory.

---
