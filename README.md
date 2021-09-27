<h1> SCRAPEGOAT </h1>

![Alt text](https://github.com/Scrape-Goat/scrapegoat/blob/main/img/goatlogoscrape.png?raw=true "Title")   
 
**Scrapegoat** is a python library that can be used to scrape the websites from internet based on the relevance of the given topic irrespective of language using ***Natural Language Processing***. It can be mainly used for *non-English language* to get accurate and relevant scraped text.

## Concept
Initially the data is scraped from a website  and  processed ( to remove English words if the data required is in other language). The **BERT** model is feed with processed data and topic  to compute the **cosine similarity** of the given topic with each word of the scraped data then mean of cosine similarity scores of is computed. If the mean is greater than threshold then scraped data is generated as output. Also there is a section where we are using *Adaptive threshold*.

![Alt text](https://github.com/Scrape-Goat/scrapegoat/blob/main/img/goatblockscrape.png?raw=true "Title")  
### BERT Model 
**BERT**, which stands for ***Bidirectional Encoder Representations from Transformers***, is based on Transformers, a deep learning model in which every output element is connected to every input element, and the weightings between them are dynamically calculated based upon their connection. The BERT framework was **pre-trained using text from Wikipedia**. The transformer is the part of the model that gives BERT its increased capacity for understanding context and ambiguity in language. The transformer does this by processing any given word in relation to all other words in a sentence, rather than processing them one at a time. By looking at all surrounding words, the Transformer allows the BERT model to understand the full context of the word, and therefore better understand searcher intent.


### Cosine Similarity
**Cosine similarity** is one of the metrics to measure the text-similarity between two documents irrespective of their size in Natural language Processing. A word can be represented in the vector form, therefore the text documents are represented in n-dimensional vector space. ***If the Cosine similarity score is 1, it means two vectors have the same orientation. The value closer to 0 indicates that the two documents have less similarity***. The Cosine similarity of two documents will range from 0 to 1.

![Alt text](https://github.com/Scrape-Goat/scrapegoat/blob/main/img/cos.png?raw=true "Title")

### Multi Processing
The multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. ***The basic ideology of Multi-Processing is that if you have an algorithm that can be divided into different workers (small processors/cores), then you can speed up the program.*** Machines nowadays come with 4,6,8 and 16 cores, therefore parts of the code can be deployed in parallel.

## Using Scrapegoat
The examples/test.py file contains these
```python
url = 'https://kannada.asianetnews.com/central-government-jobs/hal-is-recruiting-apprentice-posts-and-check-details-qzbcph'
topic = "engineering"
cores = 6
language = 'kn'

if __name__=="__main__":
    from scrapegoat.utils import automate
    from scrapegoat.multiprocess import getLinkData
    text,score = getLinkData(url=url, topic=topic, language=language, cores=cores)
    print(text, score)

```
