class JobScrape:

  def __init__(self, sit_name):
    """Having the job sites in a list means
    we can check on initialisation and throw an error
    if the site is unavailable"""
    
    sites = [{"monster": {
      "url":"https://www.monster.ie/jobs/search/",
      "query_format":"?q={keywords}&where={city}&cy={country}",
      "results": "#ResultsContainer",
    }}]


  def _format_monster():
    pass

  def _scrape_site():
    pass

  def get_jobs():
    pass