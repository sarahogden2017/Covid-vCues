import scrapy


class Spider1Spider(scrapy.Spider):
    '''
    Spider to collect images from reliable sources of COVID-19 information
    '''
    name = "spider1"

    def start_requests(self):
        '''
        Request all urls in input file -- outputReal.txt
        '''
        # with open('../outputReal.txt', 'r') as f:
        #     urls = f.readlines()
        urls = ['https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters','https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19-pregnancy-and-childbirth']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
        Parse the response and extract image urls
        '''
        for img in response.css('img'):
            img_url = img.attrib.get('src')
            if img_url:
                yield {
                    'image_urls': [response.urljoin(img_url)]
                }
