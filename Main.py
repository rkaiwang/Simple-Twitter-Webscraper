#Implementation of page object pattern

from selenium import webdriver
from steps import scraper_functions
from page.search_page import body_element_locator
from page.search_page import get_tweets
import nltk

def main():
    #set up variables
    browser = webdriver.Chrome('/Users/kai/PycharmProjects/Twitter_webscraper/chromedriver')
    base_url = u'https://twitter.com/search?q='
    query = u'%23ArtificialIntelligence&src=tyah'
    url = base_url + query
    scroll_down_number = 20

    scraper_functions.get_url(browser, url)
    #time.sleep(1) #waits for one second to wait for URL to load, since searching right away doesn't work

    body = body_element_locator(browser)
    scraper_functions.scroll_down_x_times(scroll_down_number, body)

    tweets = get_tweets(browser)
    #scraper_functions.print_tweets(tweets)
    tweets_string = ''
    for tweet in tweets:
        tweets_string += tweet.text

    tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(tweets_string)

    # A new list to hold the lowercased words
    words = []

    # Looping through the tokens and make them lower case
    for word in tokens:
        words.append(word.lower())

    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')

    words_ns = []
    for word in words:
        if word not in stopwords and (word != 'artificial' or word != 'intelligence'):
            words_ns.append(word)

    freqdist = nltk.FreqDist(words_ns)

    freqdist.plot(10)

main()


#further project idea: automatically scrape multiple pages, scrape all across twitter



