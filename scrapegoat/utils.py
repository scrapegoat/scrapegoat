from bs4 import BeautifulSoup                      
import requests                                    
import re                                         
from googletrans import Translator                 
import wikipediaapi
from googlesearch import search
from numpy import dot
from numpy.linalg import norm
import numpy as np
from bs4.element import Comment
from sentence_transformers import SentenceTransformer, util


def tag_visible(element):
    '''
    The content of the below tags will be
    added to the text
    '''
    if element.parent.name in ['h1', 'h2', 'h3', 'h4', 'p',
                               'title', 'ul', 'li', 'span']:
        return True
    if isinstance(element, Comment):
        return True
    return False


def text_from_html(body):
    '''
    The text is extracted from the html
    '''
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


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

    def get_text(self, url):
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
        text = text_from_html(page)
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
        # time.sleep(1)
        translator = Translator()
        return translator.translate(text).text

    def get_similarityScore(self, text, topic):
        '''
        This Method caculates the similarity score of the given text and topic. It uses BERT Model 
        for getting the cosine similarity score of the sentence vectors.
        '''        
        model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
        query_embedding = model.encode(text)
        passage_embedding =  model.encode(topic)
        return util.dot_score(query_embedding, [passage_embedding]).detcah().numpy()[0][0]

    def getWiki(self, topic):
        wiki_lang = wikipediaapi.Wikipedia('en')
        wiki_page = wiki_lang.page(topic)
        if wiki_page.exists():
            return wiki_page.summary.split('\n')[0]
        return topic
    
    def cosine_similarity(self, list_1, list_2):
        cos_sim = dot(np.asarray(list_1), np.asarray(list_2)) / (norm(np.asarray(list_1)) * norm(np.asarray(list_2)))
        return cos_sim


class search_links:
    def __init__(self, lang, topic, n_link=10):
        self.lang = lang
        self.topic = topic
        self.links = []
        self.n_link = n_link

    def translate(self, text, lang='en'):
        translator = Translator()
        return translator.translate(text, dest=lang).text
    
    def search(self):
        
        # to search
        query_translated = self.translate(self.topic, self.lang)
        
        for link in search(query_translated, tld="co.in", num=50, stop=50,
                         pause=2, lang='kn'):
            self.links.append(link)
        
        return self.links
        # googlenews = GoogleNews()
        # googlenews.set_lang(self.lang)
        # googlenews.search(self.translate(self.topic, self.lang))
        
        # x=0
        # while len(self.links)<self.n_link:
        #     result = googlenews.page_at(x)
            
        #     for res in result:
        #         if len(self.links)<self.n_link:
        #             self.links.append(res["link"])
        #     x=x+1
        # return self.links

