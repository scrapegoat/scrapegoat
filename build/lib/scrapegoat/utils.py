from bs4 import BeautifulSoup                      # For Scraping from website
import requests                                    # For Scraping from website
import re                                          # Text Processing
from googletrans import Translator                 # For Translating
from scipy import spatial                          
from sent2vec.vectorizer import Vectorizer     

class automate:
    def __init__(self):
        pass

    def remove_words(self, line):
        '''
        This Function is mainly used for removing English Charaters for A-Z and a-z.
        This is for smooth translation and clean the data while scraping.
        '''
        line = re.sub(r"\b[A-Za-z]+\b", "", line)
        return re.sub(" +", " ", line).strip()

    def isEnglish(self, s):
        '''
        This is a function which checks if the word is english or not. For the purpose
        of cleaning the data while scraping.
        Arguments: 
            s : str type -> inputs string 
        Returns:
            bool type 
        '''
        try:
            s.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True

    def get_text(self, url,tag='p'):
        '''
        This Method returns the Language Specific text removing the english characters. We have mailnely
        used p tag 
        Arguments: 
            str type -> url
            str type -> tag='p'(default)
        Returns: 
            str type -> text (Kannada sentences scraped form web)
        '''
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        p = soup.find_all(tag)
        text=''
        for pp in p:
            text+=pp.get_text()
            text+=" "
        text.replace('\n','').replace('\u200c','')
        text = text.split()
        Text = ""
        for t in text:
            if not self.isEnglish(t):
                Text+=t
                Text+=" "
        Text = self.remove_words(Text)
        return Text

    def translate_to_eng(self, text):
        '''
        This Method translates the Kannada(for our case) to English using Google translation API
        Argument : 
            str type -> text (Kannada)
        Returns : 
            str type -> text (English)
        '''
        translator = Translator(service_urls=['translate.googleapis.com'])
        return str(translator.translate(text, dest='en')).split('text=')[-1].split('pronunciation=')[0]

    def get_similarityScore(self, text, topic):
        '''
        This Method caculates the similarity score of the given text and topic. It uses BERT Model 
        for getting the cosine similarity score of the sentence vectors.
        '''
        sentences = [text, topic]
        vectorizer = Vectorizer()
        vectorizer.bert(sentences)
        vectors_bert = vectorizer.vectors
        dist = dict()
        dist[0] = spatial.distance.cosine(vectors_bert[0], vectors_bert[1])
        return dist[0]

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