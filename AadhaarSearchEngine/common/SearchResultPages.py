from SearchEngines import SearchEngines


class SearchResultPages:
    totalPage = 0
    keyword = None,
    searchEngineUrl = None
    currentPage = 0
    searchEngine = None

    def __init__(self, keyword, search_engine, total_page):
        self.searchEngine = search_engine.lower()
        self.searchEngineUrl = SearchEngines[self.searchEngine]
        self.totalPage = total_page
        self.keyword = keyword

    def __iter__(self):
        return self

    def _currentUrl(self):
        return self.searchEngineUrl.format(self.keyword, str(self.currentPage * 10))

    def next(self):
        if self.currentPage < self.totalPage:
            url = self._currentUrl()
            self.currentPage = self.currentPage + 1
            return url
        raise StopIteration
