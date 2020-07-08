import scrapy
from ..items import BookDetailsItem
class TitleExtract(scrapy.Spider):
    name='PopularBooks'
    start_urls=[
        'https://www.flipkart.com/books/fiction-books/kannada~language/pr?sid=bks,wbi&otracker=categorytree'
    ]

    def parse(self, response):
        items=BookDetailsItem()
        all_div_books=response.css('div._3O0U0u')#_3O0U0u is the div containes books title

        for books in all_div_books:

            book_title= books.css('._2cLu-l::text').extract()
            rating=books.css('.hGSR34::text').extract()
            price=books.css('._1vC4OE::text').extract()

            items['Book_title']=book_title
            items['Rating']=rating
            items['Price']=price


            yield items