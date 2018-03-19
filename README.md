# Aadhaar Search Engine Crawler based on seCrawler
Find Aadhaar cards thanks to Google.

This project is based on the work of @xtt129's seCrawler.

## Prerequisites
* Python 2.7
* Scrapy

## How to search
Run the following command:

```scrapy crawl AadhaarSpider -a keyword="aadhaar meri pehachan filetype:pdf" -a se=google -a pages=10```

The result would be stored in the "urls.txt" under the current directory.
