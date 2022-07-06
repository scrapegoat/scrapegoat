from scrapegoat.utils import automate
from scrapegoat.utils import search_links
from scrapegoat.utils import scrape
from scrapegoat.utils import translate
import os
from tqdm import tqdm


def getLinkData(url, topic, language='en'):
    '''
    This Function will get the data from the link and returns the similarity
        score and text

    Arguments:
                url  			: str type -> url is the link to scraped
                topic 			: str type -> topic is the topic which needs to be
                                    compared
                language		: str type -> language of the data which needs to be
                                    scraped |  Range: According to google
									language codes

        Returns:
                text 			: str type -> text are the any sentences
                                    scraped form web
                mean 			: int type -> cosine similarity score
    '''

    try:
        auto = automate()
        tex = scrape(url=url).get_text()
        sim_score = auto.get_similarityScore(
            tex, auto.getWiki(topic, language))
        return tex, sim_score

    except Exception as e:
        print(e)


def generateData(topic,
                 language='en',
                 folder_path=None,
                 adaptive_threshold=True,
                 threshold=0.25,
                 n_links=100,
				 ):
    '''
	This Function will generate the data from links, which is obtained via
	google search and computes the similarity score of the scraped data and
	if the score is greater than the threashold it will store the text in
	a file in the given folder

    Arguments:
            topic 				: str type -> topic is the topic which needs to be
                                     compared
            language			: str type -> language of the data which needs to be
                                scraped | Range: According to google language
								codes
            folder_path 		: str type -> folder path for storing text scraped
            adaptive_threshold  : bool type-> True or False For Adaptive Mean
                                    Calculation | Range: [True,False]
            threshold 			: int type -> value for allowing text to be scraped
									| Range: [0,1]
            n_links				: int type -> number of links to be scraped

    Returns:
            None
    '''

    # If Folder Path is not given then it creates a folder called data and
    # stores the files in that folder
    if folder_path is None:
        try:
            folder_path = 'data'
            os.mkdir('data')
        except FileExistsError:
            pass

    # If User has selected Adaptive Threashold then below code will execute
    # For 1st 5 iterations the threashold will be 0.1 and then it changes
        # accordingly
    if adaptive_threshold:
        # search_links Function will collect n_links if specified otherwise it
        # takes 50 as default argument
        topic = translate(topic, language)
        links = search_links(language, topic, n_links=n_links).search_()

        for i, link in enumerate(tqdm(links, desc="Generating Data.. ")):
            # Looping through each links
            text, mean = getLinkData(url=link, language=language, topic=topic)
            if mean > threshold:
                # threashold adjustment code
                if i > 5:
                    threshold = (threshold+mean)/2
                try:
                    if text is not None:
                        with open(os.path.join(folder_path, "{0000}").format(i) +
                                  ".txt", 'w', encoding='utf-8') as f:
                            f.write(text)
                            f.close()
                except Exception:
                    pass

    # If adaptive_threshold is False then below code will execute
    else:
        # LinkCollection Function will collect n_links if specified otherwise
        # it takes 50 as default argument
        links = search_links(language, topic, n_links=n_links).search_()
        links = list(set(links))

        # Looping through each links
        for i, link in enumerate(tqdm(links, desc="Generating Data.. ")):
            try:
                text, mean = getLinkData(
                    url=link, topic=topic, language=language)
            except Exception:
                print("Not Possible to Get the Text")

            # threashold adjustment code
            if mean > threshold:
                try:
                    if text is not None:
                        with open(os.path.join(folder_path, "{0000}").format(i) +
                                  ".txt", 'w', encoding='utf-8') as f:
                            f.write(text)
                            f.close()
                except Exception:
                    pass
