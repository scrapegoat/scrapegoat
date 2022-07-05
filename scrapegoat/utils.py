from bs4 import BeautifulSoup                      
import requests                                    
from googletrans import Translator                 
import wikipediaapi
from googlesearch import search
from numpy import dot
from numpy.linalg import norm
import numpy as np
from bs4.element import Comment
from sentence_transformers import SentenceTransformer, util



def translate(text, lang='en'):
    '''
    translate  it to any language using google api
    '''
    translator = Translator()
    return translator.translate(text, dest=lang).text


class automate:
    def __init__(self):
        pass

    def translate(self, text, lang='en'):
        '''
        Arguments: 
    	    text : str type -> text are the Kannada sentences scraped form web
            lang : str type -> language of the data which needs to be scraped | Range: 
									  According to google language codes
        translate  it to any language using google api
        '''
        translator = Translator()
        return translator.translate(text, dest=lang).text
    
    def get_similarityScore(self, text, topic):
        '''
        This Method caculates the similarity score of the given text and topic. It uses BERT Model 
        for getting the cosine similarity score of the sentence vectors.
        '''        
        model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
        query_embedding = model.encode(text)
        passage_embedding =  model.encode(topic)
        return util.dot_score(query_embedding, [passage_embedding]).detach().numpy()[0][0]

    def getWiki(self, topic, lang):
        ''''
        This method gets the wiki page text in given language
        '''
        wiki_lang = wikipediaapi.Wikipedia(lang)
        # print(self.translate(topic, lang))
        wiki_page = wiki_lang.page(self.translate(topic, lang))
        # print(wiki_page.exists())
        if wiki_page.exists():
            return wiki_page.summary.split('\n')[0]
        return topic

    def cosine_similarity(self, list_1, list_2):
        cos_sim = dot(np.asarray(list_1), np.asarray(list_2)) / (norm(np.asarray(list_1)) * norm(np.asarray(list_2)))
        return cos_sim


class search_links:
    def __init__(self, lang, topic, n_links=50, pause=2):
        self.lang = lang
        self.topic = topic
        self.links = []
        self.n_links = n_links
        self.pause = pause

    def translate(self, text, lang='en'):
        translator = Translator()
        return translator.translate(text, dest=lang).text
    
    def search_(self):
        
        # to search
        query_translated = self.translate(self.topic, self.lang)
        for link in search(query_translated,tld="co.in", num=self.n_links, stop=self.n_links,
                         pause=self.pause, lang=self.lang):
            self.links.append(link)
        
        return self.links


class scrape:
    def __init__(self, url):
        self.url = url

    def tag_visible(self, element):
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

    
    def text_from_html(self, body):
        '''
        The text is extracted from the html
        '''
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)


    def get_text(self):
        '''
        This Method returns the Language Specific text removing the english characters. We have mailnely
        used p tag 
        Arguments: 
            str type -> url
            str type -> tag='p'(default)
        Returns: 
            str type -> text (Kannada sentences scraped form web)
        '''
        url = self.url

        try:
            page = requests.get(url,  headers={'User-Agent': 'Mozilla/5.0'}).text
        except Exception:
            raise "Please check the Url path"
        text = self.text_from_html(page)
        text.replace('\n','').replace('\u200c','')
        
        return text

