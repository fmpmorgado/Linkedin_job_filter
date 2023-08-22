from typing import List

class Filter:
    """
    Class to store the filters used for LinkedIN search
    """

    def __init__(self):

        #Job keywords to search
        self.job = None

        #Job keywords to exclude
        self.exclude_job = None

        #Company to search
        self.company = None

        #Company to exclude
        self.exclude_company = None

        #Location to search for jobs (default = Worldwide)
        self.global_location = 'Wordwide'

        #Location to search
        self.location = None

        #Location to exclude
        self.exclude_location = None

        #Set on-site/remote option
        self.site = None

        #Set time of the oldest post
        self.time = 31*24*60*60

        #Set experience level
        self.experience = None


    def set_job_keywords(self, keywords: List[str]) -> int:
        self.job = keywords

    def set_exclude_job_keywords(self, keywords: List[str]) -> int:
        self.exclude_job = keywords

    def set_company_keywords(self, keywords: List[str]) -> int:
        self.company = keywords

    def set_exclude_company_keywords(self, keywords: List[str]) -> int:
        self.exclude_company = keywords

    def set_global_location(self, keywords: str) -> int:
        self.global_location = keywords
    
    def set_location_keywords(self, keywords: List[str]) -> int:
        self.location = keywords

    def set_exclude_location_keywords(self, keywords: List[str]) -> int:
        self.exclude_location = keywords

    def set_site(self, keywords: List[str]) -> int:
        self.site = keywords

    def set_time_post(self, time: int) -> int:
        self.time_post = time

    def set_experience(self, keywords: List[str]) -> int:
        self.experience = keywords