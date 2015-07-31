# -*- coding: utf-8 -*-
import scrapy
from craig.items import CraigItem
from scrapy import Selector

class SpideySpider(scrapy.Spider):
    name = "spidey"
    allowed_domains = ["craigslist.co.in"]
    start_urls = (
        'http://indore.craigslist.co.in/',
        'http://bhubaneswar.craigslist.co.in/'
    )

    def parse(self, response):
        response = Selector(response)
        titles = response.xpath("//*[@id='center']//li")
        items = []
        for element in titles:
        	item = CraigItem()
        	item["title"] = element.xpath("a/span/text()").extract()[0]
        	item["link"] = element.xpath("a/@href").extract()[0]
        	items.append(item)
        return items


