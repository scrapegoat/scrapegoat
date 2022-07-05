from scrapegoat.main import getLinkData
from scrapegoat.main import generateData


if __name__=="__main__":
    # scrape one link and get the relevence score
    topic = " cricket"
    language = 'kn'
    url = "https://vijaykarnataka.com/sports/cricket/news/ind-vs-eng-brian-lara-congratulates-jasprit-bumrah-for-breaking-his-world-record-in-test-cricket/articleshow/92628545.cms"
    text,score = getLinkData(url, topic, language=language)
    print(score)


    # scrape and download data
    topic = " cricket"
    language = 'hi'
    generateData(topic, language, n_links=20)

