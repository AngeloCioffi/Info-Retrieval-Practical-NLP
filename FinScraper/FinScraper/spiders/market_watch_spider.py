import scrapy


class MarketWatchSpider(scrapy.Spider):
    name = "market_watch"
    start_urls = [
        'https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true',
        'https://www.marketwatch.com/search?q=facebook&m=Keyword&rpp=100&mp=2005&bd=false&rs=true&o=101',
    ]

    def parse(self, response):
        #follow links to articles
        for href in response.css('searchResult + a::attr(href)'):
            yield response.follow(href, self.parse_article)

    def parse_article(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'title': extract_with_css('h1#article-headline::text')
        }