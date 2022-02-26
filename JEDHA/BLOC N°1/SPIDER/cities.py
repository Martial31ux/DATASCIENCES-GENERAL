import scrapy


class CitiesSpider(scrapy.Spider):
    name = 'cities'

    #allowed_domains = ['https://one-week-in.com/35-cities-to-visit-in-france/']
    start_urls = ['https://one-week-in.com/35-cities-to-visit-in-france']

    def parse(self, response):
        
        for idx, city in enumerate(response.css('div.entry-content ol li')):
            town = city.css('a::text').get()
            yield {'id' : idx+1,
                'city' : town}
