import scrapy


class ContentSpider(scrapy.Spider):
    name = "content"

    start_urls = [
        'https://www.springerprofessional.de/wasserwirtschaft-4-2019/16592584'
    ]


    def parse(self, response):
        for index, article in enumerate(response.css('section.teaser')):

            title = article.css('.issue__item-title::text').get()
            url = 'https://www.springerprofessional.de/' + article.css('section.teaser > a::attr(href)').get()

            author = article.css('.teaser__authors::text').get()
            # Using ternary conditions to put empty string instead of putting null - for articles with an author name 
            author_name = author if author else ''

            category_and_date = article.css('.tag-line--default::text').get().replace("\n", " ").strip().split(" | "),
            date = category_and_date[0][0]
            category = category_and_date[0][1]
            year = date.split('.')[-1]

            
            yield{
                'number': index + 1,
                'date': date,
                'year': year,
                'category': category,
                'title' : title,
                'author': author_name,
                'url': url
            }


# Added  FEED_EXPORT_ENCODING = 'utf-8'  to settings.py, so special characters appear
