from scrapegoat.utils import automate
from scrapegoat.utils import search_links
import os
from sentence_transformers import SentenceTransformer


def getLinkData(url, topic, language='en', tag='p'):
	'''
	This Function will get the data from the link and returns the similarity score and text

	Arguments: 
		url  			: str type -> url is the link to scraped 
		topic 			: str type -> topic is the topic which needs to be compared
		language		: str type -> language of the data which needs to be scraped | Range: 
									  According to google language codes
		tag 			: str type -> tag='p'(default)

    Returns: 
    	text 			: str type -> text are the Kannada sentences scraped form web
    	mean 			: int type -> cosine similarity score 
	'''
	try:
		# t1 = time.time()
		auto = automate()
		tex = auto.get_text(url) # Get the text
		# texts = ""
		sim_score = auto.get_similarityScore(tex, topic)

		# if len(tex)<1000:
		# 	return None
		# tt = [' '.join(tex.split()[i*200:(i+1)*200]) for i in range(len(tex.split())//200 + 1)]

		# if language!='en':
		# 	texts = auto.translate_to_eng(tt[0])
		# else:
		# 	texts = tex 
		return tex, sim_score

	except Exception as e:
		print(e)


def generateData(topic, language='en', folder_path=None, adaptive_threshold=True, threshold=0.45,
    tag='p', n_links=10):
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
		links = search_links(language, topic, n_link=n_links).search()

		for i,link in enumerate(links):
			# Looping through each links 
			text, mean = getLinkData(url=link, language=language, topic=topic,tag='p')
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
		links = search_links(language, topic, n_link=n_links).search()
		# links = search_links(language, topic, n_link=n_links).google()
		links = list(set(links))
		
		# Looping through each links 
		for i,link in enumerate(links):
			try:
				text, mean = getLinkData(url=link, topic=topic,language=language, tag='p')
			except:
				print("Not Possible to Get the Text")
			if mean>threshold:
				with open(folder_path+"{0000}".format(i) +".txt",'w', encoding = 'utf-8') as f:
					f.write(text)
					f.close()

