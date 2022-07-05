<h1> SCRAPEGOAT </h1>

<p align="center">
    <img src="https://user-images.githubusercontent.com/63489382/176208117-40101555-d460-4af4-8e97-0b485203a41d.png" alt="drawing" width="250"/>
</p>


<p align="center">
   Scrape data in one shot.
</p>

<p align="center">
   <a href="https://www.npmjs.com/package/@swc/core">
     <a href="https://pypi.org/project/scrapegoat/"><img src="https://img.shields.io/badge/pypi-package-blue?labelColor=black&style=flat&logo=python&link=https://pypi.org/project/scrapegoat/" alt="pypi" /></a>
   </a>
</p>

**Scrapegoat** is a python library that can be used to scrape the websites from internet based on the relevance of the given topic irrespective of language using ***Natural Language Processing***. It can be mainly used for *non-English language* to get accurate and relevant scraped text.

## Concept
Initially the data is scraped from a website  and  processed ( to remove English words if the data required is in other language). The **BERT** model is feed with processed data and topic  to compute the **cosine similarity** of the given topic with each word of the scraped data then mean of cosine similarity scores of is computed. If the mean is greater than threshold then scraped data is generated as output. Also there is a section where we are using *Adaptive threshold*.

<p align="center">
    <img src="https://github.com/Scrape-Goat/scrapegoat/blob/main/img/goatblockscrape.png" alt="drawing" width="500"/>
</p>

### BERT Model 
**BERT**, which stands for ***Bidirectional Encoder Representations from Transformers***, is based on Transformers, a deep learning model in which every output element is connected to every input element, and the weightings between them are dynamically calculated based upon their connection. The BERT framework was **pre-trained using text from Wikipedia**. The transformer is the part of the model that gives BERT its increased capacity for understanding context and ambiguity in language. The transformer does this by processing any given word in relation to all other words in a sentence, rather than processing them one at a time. By looking at all surrounding words, the Transformer allows the BERT model to understand the full context of the word, and therefore better understand searcher intent.


### Cosine Similarity
**Cosine similarity** is one of the metrics to measure the text-similarity between two documents irrespective of their size in Natural language Processing. A word can be represented in the vector form, therefore the text documents are represented in n-dimensional vector space. ***If the Cosine similarity score is 1, it means two vectors have the same orientation. The value closer to 0 indicates that the two documents have less similarity***. The Cosine similarity of two documents will range from 0 to 1.


<p align="center">
    <img src="https://github.com/Scrape-Goat/scrapegoat/blob/main/img/cos.png" alt="drawing" width="500"/>
</p>


### Multi Processing
The multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. ***The basic ideology of Multi-Processing is that if you have an algorithm that can be divided into different workers (small processors/cores), then you can speed up the program.*** Machines nowadays come with 4,6,8 and 16 cores, therefore parts of the code can be deployed in parallel.

## Using Scrapegoat
The examples/test.py file contains these
```python
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

```
