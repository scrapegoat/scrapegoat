from scrapegoat.utils import automate
from getLinks.get_links import search_links
from scrapegoat.main import getLinkData
from scrapegoat.main import generateData
import time
import pandas as pd 

url = 'https://kannada.asianetnews.com/central-government-jobs/hal-is-recruiting-apprentice-posts-and-check-details-qzbcph'
topic = "engineering"
cores = 6
max_bert_len = 512


if __name__ == '__main__':

    folder_path = 'data\\'
    threshold = 0.2
    df = pd.read_csv('updated_finace_table.csv')
    for top,link in zip(df['topic'],df['Link2']):
      
        text, mean = getLinkData(url=link, topic=top, language='kn', cores=6)
        if mean>threshold:
        # threashold adjustment code
            # if i>5:
            #     threshold = (threshold+mean)/2
            with open(folder_path+top+".txt",'w', encoding = 'utf-8') as f:
                f.write(text)
                f.close()
           
