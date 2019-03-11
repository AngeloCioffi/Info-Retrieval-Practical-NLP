from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

searchURLs = ["https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true",
 			  "https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true&o=101",
 			  "https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true&o=201",
 			  "https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true&o=301"]


driver = webdriver.Firefox()
data = {}

for searchURL in searchURLs:
	try:
		driver.get(searchURLs[0])
		articleURLs = driver.find_elements_by_class_name("searchresult")
		urls = list()

		for x in articleURLs:
			urls.append(articleURLs[1].find_element_by_css_selector('a').get_attribute('href'))
			file.write(url + "\n")

			for url in urls:
				if "marketwatch.com" in urls[0]:
					driver.get(urls[0])
					if "marketwatch.com" in driver.current_url:
						articleBody = driver.find_elements_by_xpath('//div[@id="article-body"]/p')
						articleString = ""
						for sentence in articleBody:
							sentenceText = sentence.text
							articleString += sentenceText

						data[urls[0]] = {
							'title': driver.find_element_by_css_selector('h1#article-headline').text,
							'article': articleString
						}
	except:
		pass
	

with open('MarketWatchData.txt', 'w') as outfile:
	json.dump(data, outfile)

driver.close()