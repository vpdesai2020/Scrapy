import scrapy

class TitleExtract(scrapy.Spider):
    name='Title'
    start_urls=[
        'https://www.google.com/'
    ]

    def parse(self, response):
        title=response.css('title::text').extract() #remove title tag and extract only text
        yield {'titletext':title}

        