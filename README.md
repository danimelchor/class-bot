![version](https://img.shields.io/badge/version-1.0.1-blue)
![license](https://img.shields.io/badge/license-MIT-green)

# **Boston University COVID-19 Bot**

## **Requirements**

This bot uses a framework called [selenium](https://selenium-python.readthedocs.io/). Therefore, it requires what is called a "chromedriver" executable. Please download it from [here](https://chromedriver.chromium.org/downloads) and save it with the name `mac_chromedriver`.

To check your version of chrome, open chrome and click on the 3 dots on the top right, then click settings. All the way at the bottom there should be an "About Chrome" link. There you will be able to find your current Chrome version with the format `9X.X.X.X` where we are only interested in the first two numbers.

## **Setup**

This bot is created with python. First, you will need to have python installed (which usually comes by default). To check if you have it run:

```bash
python -V
```

Then, you will also need python's package installer [pip](https://pypi.org/project/pip/) (which also usually comes by default). To check if you have it run:

```bash
pip -V
```

Then, to install its dependencies run

```bash
pip install -r requirements.txt
```

_Note: you may want to user a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for the installed packages_

## **Usage**

To start using the bot, go into main.py and change the configuration. You also need to create a file called `.env` that has the true contents of `.env.example`. Then, you will need to run:

```bash
python main.py
```

## **Contributions**

I am open to any type of contribution/suggestion. Just open a pull request directly to master and I will review your code and merge it. Please make sure your code is well formatted using [black](https://github.com/psf/black).

## **Terms of usage**

I have made it as a project to make the process of registering for a class easier. Please make sure you comply with BU t's terms of usage and don't use the bot for any malicious actions. I am in no way responsible for your actions with this code.

###### By [Daniel Melchor](https://danielmelchor.com) (Class of 2024)
