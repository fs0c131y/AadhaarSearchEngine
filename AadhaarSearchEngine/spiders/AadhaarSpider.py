import scrapy

from scrapy.spiders import Spider
from AadhaarSearchEngine.common.SearchResultPages import SearchResultPages
from AadhaarSearchEngine.common.SearchEngines import SearchEngineResultSelectors
from scrapy.selector import Selector


class AadhaarSpider(Spider):
    name = 'AadhaarSpider'
    allowed_domains = ['bing.com', 'google.com', 'baidu.com']
    start_urls = []
    websites = []
    keyword = None
    searchEngine = None
    selector = None

    def __init__(self, keyword, se='bing', pages=1, *args, **kwargs):
        super(AadhaarSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        page_urls = SearchResultPages(keyword, se, int(pages))
        for url in page_urls:
            self.start_urls.append(url)

    def parse(self, response):
        for url in Selector(response).xpath(self.selector).extract():
            website = url.split("/")[2]
            if website not in self.websites:
                self.websites.append(website)

        for website in self.websites:
            keyword = 'site:' + website + ' intext:"Your Aadhaar No" filetype:pdf'
            page_urls = SearchResultPages(keyword, self.searchEngine, 10)
            for url in page_urls:
                yield scrapy.Request(url, callback=self.parse_aadhaar)

    def parse_aadhaar(self, response):
        for url in Selector(response).xpath(self.selector).extract():
            yield {'url': url}
