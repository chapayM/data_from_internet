import scrapy
from scrapy.http import HtmlResponse
from parser_job.items import ProjectParserSjItem
from parser_job.functions import min_max_salary_sj


class SjRuSpider(scrapy.Spider):
    name = "sj_ru"
    allowed_domains = ["superjob.ru"]
    start_urls = ["https://tatarstan.superjob.ru/vakansii/voditel.html"]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='_1IHWd _6Nb0L _37aW8 _1isik f-test-button-dalshe f-test-link-Dalshe']"
                                   "/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        urls_vacancies = response.xpath("//span[@class='_26gg2 _3oXMw _2LaRg hbKbL rIDaO oDIMq _33qju _1ZV-S']/a"
                                        "/@href").getall()
        for url_vacancy in urls_vacancies:
            yield response.follow(url_vacancy, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        vacancy_name = response.css("h1::text").get()
        vacancy_salary = min_max_salary_sj(response.xpath("//span[@class='_4Gt5t _3Kq5N']//text()").getall())
        vacancy_url = response.url

        yield ProjectParserSjItem(
            name=vacancy_name,
            #salary= vacancy_salary,
            min_salary=vacancy_salary[0],
            max_salary=vacancy_salary[1],
            currency=vacancy_salary[2],
            period=vacancy_salary[3],
            url=vacancy_url
        )
