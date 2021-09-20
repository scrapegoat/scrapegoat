from scipy import spatial                       
from sent2vec.vectorizer import Vectorizer         

class get_similarity:
	'''
	Arguments:
        text        : str type -> text to topic which needs to be compared
        topic       : str type -> topic is the topic which needs to be compared
	'''
	def __init__(self, text, topic):
		self.__text = text
		self.__topic = topic

	def get_similarityScore(self):
		'''
        This Method caculates the similarity score of the given text and topic. It uses BERT Model 
        for getting the cosine similarity score of the sentence vectors.
        '''
		sentences = [self.__text, self.__topic]
		vectorizer = Vectorizer()
		vectorizer.bert(sentences)
		vectors_bert = vectorizer.vectors
		dist = dict()
		dist[0] = spatial.distance.cosine(vectors_bert[0], vectors_bert[1])
		return dist[0]

# g = get_similarity(' is a 2012 superhero film, based on the Marvel Comics superhero team of the same name. The film is a sequel to Iron Man, The Incredible Hulk, Iron Man 2, Thor, and Captain America:','Avengers')
# print(g.get_similarityScore())
