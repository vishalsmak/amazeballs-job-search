import scrapy
from ExtractKeywords import ExtractKeywords

page_count = 0
job_count = 0
total_jobs = 0

class JobsSpider(scrapy.Spider):
    search_query = 'technical'
    base_url = 'https://www.indeed.com'
    jobs_url = f'{base_url}/jobs?q={search_query}&start='
    name = 'jobs'
    start_urls = [
            jobs_url,
        ]

    def parse(self, response):
        global page_count
        global total_jobs
        total_jobs = self.GetJobCount(response)
        page_count += 1
        print(f'Onto Page number : {page_count} , jobs scraped : {job_count}, remaining jobs to scrape : {total_jobs - job_count}')

        for job in response.xpath('.//a[contains(@id, "job")]'):
            link = self.GetLink(job)
            if link:
                yield scrapy.Request(url=link, callback=self.parse_job)
            else:
                continue

        next_page_url = self.get_next_page_url()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        else:
            yield None

    def get_next_page_url(self):
        try:
            if (total_jobs >= job_count):
                return f'{self.jobs_url}{page_count * 10}'
            else:
                return ""
        except:
            return ""

    def parse_job(self, response):
        global job_count
        job_count += 1
        yield {
                'id':job_count,
                'title':self.GetTitle(response),
                'company':self.GetCompany(response),
                'link':response.url,
                'desc': ExtractKeywords().extract(self.GetDescription(response))
            }

    def GetJobCount(self, response):
        try:
            return int(response.xpath('.//div[@id="searchCountPages"]').extract_first().split(" ")[-2].replace(',', ''))
        except:
            return 0

    def GetTitle(self, job):
        try:
            return job.xpath('.//h1[contains(@class, "title")]/text()').extract_first()
        except:
            return "NOT_FOUND"

    def GetCompany(self, job):
        try:
            company = job.xpath('.//div[@class="jobsearch-CompanyInfoContainer"]//a/text()').extract_first()
            if company:
                return company
            else:
                return job.xpath('.//div[@class="jobsearch-CompanyInfoContainer"]//div[text()]/text()').extract_first()
        except:
            return "NOT_FOUND"

    def GetLink(self, job):
        try:
            return self.base_url + job.xpath('@href').extract_first()
        except:
            return ""

    def GetDescription(self, job):
        try:
            lines = job.xpath('.//div[@id="jobDescriptionText"]/descendant-or-self::*/text()').extract()
            return ' '.join(lines)
        except:
            return "NOT_FOUND"
