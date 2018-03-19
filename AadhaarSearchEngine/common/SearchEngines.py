SearchEngines = {
    'google': 'https://www.google.com/search?q={0}&start={1}',
    'bing': 'http://www.bing.com/search?q={0}&first={1}',
    'baidu': 'http://www.baidu.com/s?wd={0}&pn={1}'
}

SearchEngineResultSelectors= {
    'google': '//h3/a/@href',
    'bing': '//h2/a/@href',
    'baidu': '//h3/a/@href',
}