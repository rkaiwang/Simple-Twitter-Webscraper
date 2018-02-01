#steps is things that you would do on the webpage

import time
from selenium.webdriver.common.keys import Keys
#function for searching
#scrape data
#function for printing


def get_url(browser, url):
    browser.get(url)


def scroll_down_x_times(x_times, body):
    for _ in range(x_times):
        body.send_keys(Keys.PAGE_DOWN)  # scrolls down
        time.sleep(0.2)  # waits so it load data from scrolling down


def print_tweets(tweets):
    for tweet in tweets:
        print(tweet.text)