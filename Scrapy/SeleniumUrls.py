from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

#file = open("MarketWatchURLs.txt", "w")

driver = webdriver.Firefox()
driver.get("https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true")
articleURLs = driver.find_elements_by_class_name("searchresult")
urls = list()
for x in articleURLs:
	urls.append(x.find_element_by_css_selector('a').get_attribute('href'))
	#file.write(url + "\n")

data = {}
for url in urls:
	if "marketwatch.com" in url:
		print(url)
		driver.get(url)
		if "marketwatch.com" in driver.current_url:
			data[url] = {
				'title': driver.find_element_by_css_selector('h1#article-headline').text,
				'article': driver.find_element_by_xpath('//div[@id="article-body"]/p').text
			}

with open('MarketWatchData.txt', 'w') as outfile:
	json.dump(data, outfile)

driver.close()
#file.close()