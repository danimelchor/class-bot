# Import selenium
import urllib
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv
from urllib import parse
from time import sleep

from logger import Logger

# Init
logger = Logger()
load_dotenv()

# Absolute paths for CRON
current_path = os.path.dirname(os.path.realpath(__file__))


class Bot:
    def __init__(self, hidden: bool = True, every: int = 10):
        self.hidden = hidden
        self.username = os.getenv('username')
        self.password = os.getenv('password')

        if every >= 1.5:
            self.every = every
        else:
            raise Exception(
                "Sorry, this is way too fast and you can get in trouble. Try values >= 1.5s/call"
            )
        self.logged_in = False

    def start(self, url: str) -> None:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        if self.hidden:
            options.add_argument("--headless")

        # Location of your chrome driver
        DRIVER_PATH = f"mac_chromedriver"
        DRIVER_PATH = os.path.join(current_path, DRIVER_PATH)

        # Initiate chrome and wait for load
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

        # Save driver
        self.driver = driver

        # Go to registration page
        self.check_class(url)

    def login(self) -> None:
        """
        Logins the user with the provided credentials inside config
        """
        login_username = self.driver.find_element_by_xpath(
            '//*[@id="j_username"]'
        )
        login_username.send_keys(self.username)

        login_password = self.driver.find_element_by_xpath(
            '//*[@id="j_password"]'
        )
        login_password.send_keys(self.password)

        self.driver.find_element_by_xpath(
            '//*[@id="wrapper"]/div/form/button'
        ).click()

        sleep(2)

        iframe = self.driver.find_element_by_xpath('//*[@id="duo_iframe"]')
        self.driver.switch_to.frame(iframe)

        self.driver.find_element_by_xpath(
            '//*[@id="auth_methods"]/fieldset/div[1]/button'
        ).click()

        self.driver.switch_to.parent_frame()

        self.logged_in = True

    def check_class(self, url: str) -> None:
        while True:
            self.driver.get(url)

            if not self.logged_in:
                self.login()

                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.title_is('Add Classes - Display'))

            try:
                self.driver.find_element_by_xpath(
                    '/html/body/form/table/tbody/tr[3]/td[1]/input'
                ).click()

                self.driver.find_element_by_xpath(
                    '/html/body/form/center[2]/table/tbody/tr/td[1]/input'
                ).click()
            except Exception:
                logger.log("Class not found")

            sleep(self.every)


if __name__ == "__main__":
    # --------------------------------------------- #
    # --------------- CONFIG HERE ----------------- #
    # --------------------------------------------- #
    HIDDEN = False
    CLASS_COLLEGE = "CAS"
    CLASS_DEPARTMENT = "CS"
    CLASS_NUMBER = "411"
    CLASS_SECTION = "A1"
    MAKE_CALL_EVERY_X_SECONDS = 5  # every 5 seconds

    # Dont touch
    bot = Bot(hidden=HIDDEN, every=MAKE_CALL_EVERY_X_SECONDS)
    base_url = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1636079002?"
    params = {
        "ModuleName": "reg/add/browse_schedule.pl",
        "SearchOptionDesc": "Class Number",
        "SearchOptionCd": "S",
        "ViewSem": "Spring 2021",
        "KeySem": "20223",
        "AddPlannerInd": "",
        "College": CLASS_COLLEGE,
        "Dept": CLASS_DEPARTMENT,
        "Course": CLASS_NUMBER,
        "Section": CLASS_SECTION
    }
    base_url += parse.urlencode(params)

    bot.start(base_url)
