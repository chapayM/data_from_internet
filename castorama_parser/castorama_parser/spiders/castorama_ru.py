import scrapy
from scrapy.http import HtmlResponse
from ..items import ProjectParserCastoramaItem
from scrapy.loader import ItemLoader
from ..functions import good_name_clear, price_clear


class CastoramaRuSpider(scrapy.Spider):
    name = 'castorama_ru'
    allowed_domains = ['castorama.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://www.castorama.ru/catalogsearch/result/?q={kwargs.get('search')}"]

    # start_urls = ['http://castorama.ru/']

    def parse(self, response: HtmlResponse):
        print(response.url)
        next_page = response.xpath("//a[@class='next i-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[contains(@class, 'product-card__name')]")
        for link in links:
            yield response.follow(link, callback=self.goods_parse)

    def goods_parse(self, response: HtmlResponse):
        good_name = good_name_clear(response.xpath("//h1/text()").getall())
        price = price_clear(response.xpath("//span[@class='price']//text()").getall())
        link = response.url
        images = response.xpath("//div[@class='js-zoom-container']//@data-src").getall()
        #product_characteristics_keys = response.xpath("//div[contains(@class, 'product-block')]//dl[contains(@class, 'specs-table')]/dt/span[contains(@class, 'specs-table__attribute-name')]/text()").getall()
        #product_characteristics_values = response.xpath("//div[contains(@class, 'specifications')]//dd[contains(@class, 'specs-table__attribute-value')]/text()").getall()
        yield ProjectParserCastoramaItem(
            good_name=good_name,
            price=price,
            link=link,
            images=images,
            #product_characteristics_keys=product_characteristics_keys,
            #product_characteristics_values=product_characteristics_values
        )
