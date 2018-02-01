#page contains functions that locates data about things on the webpage

#add locators


def body_element_locator(browser):
    return browser.find_element_by_tag_name('body')


def get_tweets(browser):
    return browser.find_elements_by_class_name('tweet-text')