# -*- coding: utf-8 -*-
import scrapy
import news_reader.spiders.text_analyzer as text_analyzer

class InvestingSpider(scrapy.Spider):
    name = 'Investing'
    allowed_domains = ['investing.com']
    start_urls = [
      'https://investing.com/news/stock-market-news', 
      'https://www.investing.com/news/forex-news', 
      'https://www.investing.com/news/economy',
      'https://www.investing.com/news/technology-news',
      'https://www.investing.com/news/commodities-news'
    ]

    def parse(self, response):
      for article in response.css("section article.articleItem"):
        link = article.css(".textDiv a.title:not(.articleDetails):not(.js-external-link)::attr(href)").extract_first()
        if(link is not None):
          yield response.follow(link, self.parse_article)
  
    def parse_article(self, response):
        link = response.url
        title = response.css("h1.articleHeader::text").extract_first()
        content = ''.join(response.css(".articlePage p ::text").extract())
        yield {'link': link, 'title': title, 'sentiment': text_analyzer.getTextAnalysis(content)}