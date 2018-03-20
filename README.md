# Aadhaar Search Engine Crawler
Find Aadhaar cards thanks to Google.

This project is based on the work of @xtt129's seCrawler.

## Prerequisites
* Python 2.7
* Scrapy

## How to install

Clone this repository

`git clone https://github.com/fs0c131y/AadhaarSearchEngine`

Then install the dependencies

`sudo pip install -r requirements.txt`

## How to run it
Run the following command:

```scrapy crawl AadhaarSpider -a keyword="aadhaar meri pehachan filetype:pdf" -a se=google -a pages=10```

The result would be stored in the "urls.txt" under the current directory.

## How to contribute
I'm far from being a Python expert, contributions are more than welcome!

## Contact
You can contact me on Twitter @fs0c131y or by e-mail fs0c1311@gmail.com
