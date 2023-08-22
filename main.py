from filter import Filter
from search import search

def main():
    filter = Filter()
  
    #Job keywords
    filter.set_job_keywords(['aerospace'])
    #filter.set_exclude_job_keywords([])

    #Company keywords
    filter.set_company_keywords(['Airbus'])
    #filter.set_exclude_company_keywords([])

    #Location keywords
    filter.set_global_location('Worldwide')
    filter.set_location_keywords(['Italy','Parma'])
    #filter.set_exclude_location_keywords(['Italy'])

    #Selection of on-site/remote options 
    #['remote', 'hybrid', 'on-site']
    #filter.set_site(['remote', 'hybrid', 'on-site'])
    
    #Selection of time filter
    #filter.set_time_post(24*60*60)

    #Selection of experience options
    #['internship','entry','associate','mid-level','director','executive']
    #filter.set_experience(['internship'])

    search(filter)

if __name__ == "__main__":
    main()