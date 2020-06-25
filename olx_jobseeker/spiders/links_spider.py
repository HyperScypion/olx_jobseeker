import sys
import scrapy
from ..items import OlxJobseekerItem
sys.path.append('../../utils')
from utils import cleaner


class LinksSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://www.olx.pl/praca/?page=1']

    def parse(self, response):

        offer_wrapper = response.css('div.offer-wrapper')

        for data in offer_wrapper:
            items = OlxJobseekerItem()

            title = data.css('strong::text').extract()
            link = data.css('h3.lheight22 a::attr(href)').get()

            try:
                salary_from = data.css('span.price-label::text')[0].extract()
                salary_to = data.css('span.price-label::text')[1].extract()
            except IndexError:
                salary_from = 0
                salary_to = 0

            items['title'] = title
            items['link'] = link
            items['salary_from'] = salary_from
            items['salary_to'] = salary_to    
            
            
            req = scrapy.Request(link, self.parse_offer, dont_filter=True)
            req.meta['items'] = items
            yield req

        next_page = response.css('span.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, dont_filter=True)


    def parse_offer(self, response):
        items = response.meta['items']
        resp = response.css('div.lheight20').extract()
        res = [cleaner.clean_data(data) for data in resp]
        items['description'] = res
        yield items
        