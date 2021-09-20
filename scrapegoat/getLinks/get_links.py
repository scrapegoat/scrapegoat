from GoogleNews import GoogleNews         
from googletrans import Translator 

class search_links:
    def __init__(self, lang, topic, n_link=10):
        self.lang = lang
        self.topic = topic
        self.links = []
        self.n_link = n_link

    def translate(self, text, lang='en'):
        translator = Translator(service_urls=['translate.googleapis.com'])
        return str(translator.translate(text, dest=lang)).split('text=')[-1].split('pronunciation=')[0]
    
    def search(self):
        googlenews = GoogleNews()
        googlenews.set_lang(self.lang)
        googlenews.search(self.translate(self.topic, self.lang))
        x=0
        while len(self.links)<self.n_link:
            result = googlenews.page_at(x)
            for res in result:
                if len(self.links)<self.n_link:
                    self.links.append(res["link"])
            x+1
        return self.links

# url = 'https://kannada.asianetnews.com/central-government-jobs/hal-is-recruiting-apprentice-posts-and-check-details-qzbcph'
# topic = "engineering"
# s = search_links('kn',topic)
# print(s.search())
