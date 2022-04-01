from JobsSpider import JobsSpider
from scrapy.crawler import CrawlerProcess

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'LOG_LEVEL': 'ERROR',
        "FEEDS": {
            "jobs.json": {"format": "json"},
        },
    })

    process.crawl(JobsSpider)
    process.start()
