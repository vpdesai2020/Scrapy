import scrapy

class TitleExtract(scrapy.Spider):
    name='PopularBooks'
    start_urls=[
        'https://www.flipkart.com/books/fiction-books/kannada~language/pr?sid=bks,wbi&otracker=categorytree'
    ]

    def parse(self, response):
        all_div_books=response.css('div._3O0U0u')#_3O0U0u is the div containes books title
        book_title= all_div_books.css('._2cLu-l::text').extract()
        yield{'Books':book_title}