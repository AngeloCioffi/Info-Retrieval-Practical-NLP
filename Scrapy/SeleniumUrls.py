from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

searchURLs = ["https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true",
 			  "https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true&o=101",
 			  "https://www.marketwatch.com/search?q=amazon&m=Keyword&rpp=100&mp=2005&bd=false&rs=true",
 			  "https://www.marketwatch.com/search?q=amazon&m=Keyword&rpp=100&mp=2005&bd=false&rs=true&o=101"]


driver = webdriver.Firefox()
data = {}

for searchURL in searchURLs:
	try:
		driver.get(searchURL)
		articleURLs = driver.find_elements_by_class_name("searchresult")
		urls = list()

		for x in articleURLs:
			urls.append(x.find_element_by_css_selector('a').get_attribute('href'))

		for url in urls:
			if "marketwatch.com" in url:
				driver.get(url)
				if "marketwatch.com" in driver.current_url:
					articleBody = driver.find_elements_by_xpath('//div[@id="article-body"]/p')
					articleString = ""
					for sentence in articleBody:
						sentenceText = sentence.text
						articleString += sentenceText

					data[url] = {
						'title': driver.find_element_by_css_selector('h1#article-headline').text,
						'article': articleString,
						'date': driver.find_element_by_xpath('//p[@id="published-timestamp"]/span').text
					}
	except:
		pass
	

with open('MarketWatchData.txt', 'w') as outfile:
	json.dump(data, outfile)

driver.close()