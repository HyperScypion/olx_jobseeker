import scrapy
from ..items import OlxJobseekerItem

class LinksSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://www.olx.pl/praca/']

    def parse(self, response):

        items = OlxJobseekerItem()

        # next_page = response.css('a.pageNextPrev').xpath('@href').extract()
        offer_wrapper = response.css('div.offer-wrapper')

        for data in offer_wrapper:
            title = data.css('strong::text').extract()
            link = data.css('h3.lheight22 a').xpath('@href').extract()
            try:
                salary_from = data.css('span.price-label::text')[0].extract()
                salary_to = data.css('span.price-label::text')[1].extract()
            except IndexError:
                salary_from = 0
                salary_to = 0

            items['title'] = title
            items['description'] = ''
            items['link'] = link
            items['salary_from'] = salary_from
            items['salary_to'] = salary_to
            yield items