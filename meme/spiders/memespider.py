import scrapy


class MemeSpider(scrapy.Spider):
    name = "meme"
    start_urls = ["https://www.memedroid.com/"]

    def parse(self, response):
        for count, img in enumerate(response.css("img.grey-background::attr(src)").getall()):
            yield {"img_id": count, "img": img}
