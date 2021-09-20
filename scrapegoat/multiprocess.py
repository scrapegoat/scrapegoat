from itertools import product
import numpy as np
from multiprocessing import Pool 
from utils import automate
from getLinks.get_links import search_links
import time
import os

def getLinkData(url, topic, language='en', cores=2, max_bert_len=512, tag='p'):
	'''
	This Function will get the data from the link and returns the similarity score and text

	Arguments: 
		url  			: str type -> url is the link to scraped 
		topic 			: str type -> topic is the topic which needs to be compared
		language		: str type -> language of the data which needs to be scraped | Range: 
									  According to google language codes
		cores: 			: int type -> cores (2 is default) | Range: [1, number of cores in the cpu]
		max_bert_len: 	: int type -> max_bert_len with max value of 512(default) | Range: [1,512]
		tag 			: str type -> tag='p'(default)

    Returns: 
    	text 			: str type -> text are the Kannada sentences scraped form web
    	mean 			: int type -> mean is the Mean value of similarity score 
	'''
	try:
		t1 = time.time()
		auto = automate()
		tex = auto.get_text(url, tag=tag) # Get the text
		texts = ""

        # translation cannot be done directly so splitting the sentences and translating 
        # and combining 
        # Multiprocessing Code for translating 
		if language!='en':
			p = Pool(cores)
			texts = ' '.join(p.starmap(auto.translate_to_eng, product(tex.split('.'))))
			p.close()
			p.join() 
		else:
			texts = tex 
            
		tot_split = len(texts)//max_bert_len
		mean = 0

        # BERT Model has max lenght of 512 so we need to sentences into n chunks 
		splitted_text = []
		for jj in range(tot_split):
			splitted_text.append(texts[jj*max_bert_len:(jj+1)*max_bert_len])

        # Multiprocessing Code for calculating Similarity Score
		p = Pool(cores)
		result = p.starmap(auto.get_similarityScore, product(splitted_text,[topic]))
		p.close()
		p.join()

		# # Taking the mean of the cosine similarity 
		mean = np.mean(np.asarray(result))

		t2 = time.time()
		return tex, mean

	except Exception as e:
		print(e)


def generateData(topic, lang='en', folder_path=None, adaptive_threshold=True, threshold=0.10,
    cores=2, max_bert_len=512, tag='p', n_links=10):
	'''
	This Function will generate the data from links, which is obtained via google search and 
	computes the similarity score of the scraped data and if the score is greater than the 
	threashold it will store the text in a file in the given folder

	Arguments: 
		topic 				: str type -> topic is the topic which needs to be compared
		language			: str type -> language of the data which needs to be scraped | Range: According to 
										  google language codes
		folder_path 		: str type -> folder path for storing the text scraped
		adaptive_threshold  : bool type-> True or False For Adaptive Mean Calculation | Range: [True,False]
		threshold 			: int type -> value for allowing text to be scraped  |  Range: [0,1]
		cores 				: int type -> cores (2 is default) | Range: [1, number of cores in the cpu]
		max_bert_len 		: int type -> max_bert_len with max value of 512(default) | Range: [1,512]
		tag 				: str type -> tag='p'(default)
		n_links				: int type -> number of links to be scraped 

	Returns:
		None
	'''

	# If Folder Path is not given then it creates a folder called data and stores the files
	# in that folder
	if folder_path==None:
		try:
			folder_path = 'data\\'
			os.mkdir('data')
		except:
			pass

    # If User has selected Adaptive Threashold then below code will execute 
    # For 1st 5 iterations the threashold will be 0.1 and then it changes accordingly
	if adaptive_threshold:
		# search_links Function will collect n_links if specified otherwise it takes 
		# 50 as default argument 
		links = search_links(lang, topic, n_links=n_links).search()
		for i,link in enumerate(links):
			# Looping through each links 
			text, mean = getLinkData(url=link, topic=topic, cores=cores, max_bert_len=512, tag='p')
			if mean>threshold:
			# threashold adjustment code
				if i>5:
					threshold = (threshold+mean)/2
				with open(folder_path+"{0000}".format(i) +".txt",'w', encoding = 'utf-8') as f:
					f.write(text)
					f.close()

	# If adaptive_threshold is False then below code will execute
	else:
		# LinkCollection Function will collect n_links if specified otherwise it takes 
		# 50 as default argument 
		links = search_links(lang, topic, n_links=n_links).search()
		# Looping through each links 
		for i,link in enumerate(links):
			text, mean = getLinkData(url=link, topic=topic, cores=cores, max_bert_len=512, tag='p')
			if mean>threshold:
				with open(folder_path+"{0000}".format(i) +".txt",'w', encoding = 'utf-8') as f:
					f.write(text)
					f.close()
