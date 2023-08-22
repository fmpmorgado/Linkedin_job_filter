import webbrowser
from filter import Filter

def search(filter: Filter):
    """
    Process the filter data and calls the search link
    """
    experience_values = ['internship', 'entry', 'associate', 'mid-level', 'director', 'executive']
    site_values = ['on-site', 'remote', 'hybrid']

    link = 'https://www.linkedin.com/jobs/search/?'
    link += '&keywords=('

    # Include job title
    try:
        if len(filter.job) >= 1:
            for index, job_name in enumerate(filter.job):
                link += job_name
                if index == len(filter.job)-1: break
                link += ' OR '
            link += ')'
    except:
        pass

    # Exclude job titles
    try:
        if len(filter.exclude_job) >= 1:
            link += ' NOT ('
            for index, job_name in enumerate(filter.exclude_job):
                link += job_name
                if index == len(filter.exclude_job)-1: break
                link += ' OR '
            link += ')'
    except:
        pass

    # Include companies
    try:
        if len(filter.company) >= 1:
            link += ' AND ('
            for index, company_name in enumerate(filter.company):
                link += '"' + company_name + '"'
                if index == len(filter.company)-1: break
                link += ' OR '
            link += ')'
    except: 
        pass

    # Exclude companies
    try:
        if len(filter.exclude_company) >= 1:
            link += ' NOT ('
            for index, company_name in enumerate(filter.exclude_company):
                link += '"' + company_name + '"'
                if index == len(filter.exclude_company)-1: break
                link += ' OR '
            link += ')'
    except:
        pass

    # Include location
    try:
        if len(filter.location) >= 1:
            link += ' AND ('
            for index, location_name in enumerate(filter.location):
                link += location_name
                if index == len(filter.location)-1: break
                link += ' OR '
            link += ')'
    except:
        pass

    # Exclude location
    try:
        if len(filter.exclude_location) >= 1:
            link += ' NOT ('
            for index, location_name in enumerate(filter.exclude_location):
                link += location_name
                if index == len(filter.exclude_location)-1: break
                link += ' OR '
            link += ')'
    except:
        pass

    # Include Onsite/Remote
    try:
        link += '&f_WT='
        for index, state in enumerate(filter.site):
            if state.lower() in site_values:
                link += str(site_values.index(state) + 1)
            else:
                raise ValueError("site-remote keyword is wrong") 
            if index == len(filter.site)-1: break
            link += '%2C'
    except:
        pass

    # Include maximum post time
    try:
        link += f'&f_TPR=r{filter.time_post}'
    except:
        pass

    # Include experience
    try:
        link += '&f_E='
        for index, state in enumerate(filter.experience):
            if state.lower() in experience_values:
                link += str(experience_values.index(state) + 1)
            else:
                raise ValueError("Experience keyword is wrong")
            if index == len(filter.experience)-1: break
            link += '%2C'
    except:
        pass

    # Linkedin requires location specification
    link += f'&location={filter.global_location}'

    webbrowser.open(link)