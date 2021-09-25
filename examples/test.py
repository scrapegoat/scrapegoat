url = "https://hindi.newslaundry.com/2021/01/22/loan-developing-countries-and-epidemics#:~:text=120%20%E0%A4%A8%E0%A4%BF%E0%A4%AE%E0%A5%8D%E0%A4%A8%20%E0%A4%94%E0%A4%B0%20%E0%A4%AE%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%AE%20%E0%A4%86%E0%A4%AF,8.1%20%E0%A4%85%E0%A4%B0%E0%A4%AC%20%E0%A4%A1%E0%A5%89%E0%A4%B2%E0%A4%B0%20%E0%A4%B9%E0%A5%8B%20%E0%A4%97%E0%A4%AF%E0%A4%BE."
topic = "Debt of developing countries"
language = 'hi'

if __name__=="__main__":
    from scrapegoat.utils import automate
    from scrapegoat.main import getLinkData
    text,score = getLinkData(url, topic, language=language, tag='p')
    print(text, score)