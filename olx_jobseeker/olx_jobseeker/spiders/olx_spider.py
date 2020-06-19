import scrapy


class OlxSpider(scrapy.Spider):
    name = 'jobs'

    def start_requests(self):
        url = 'https://www.olx.pl/praca/?page=1'
        
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'olx-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        
