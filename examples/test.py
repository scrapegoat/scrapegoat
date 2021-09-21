
url = 'https://kannada.asianetnews.com/central-government-jobs/hal-is-recruiting-apprentice-posts-and-check-details-qzbcph'
topic = "engineering"
cores = 6
if __name__=="__main__":
    import scrapegoat as sg 
    from scrapegoat.utils import automate
    from scrapegoat.multiprocess import getLinkData
    text, mean = getLinkData(url=url, topic=topic, language='kn', cores=cores)
    print(text, mean)
