import itertools
from textblob import TextBlob
from textblob import Word

# class Parser is responsible to parse the tags of the statement to get all nouns, verbs, questions words and generate all patterns
class Parser(object):

	# define the tags needed to extract the nouns, the verbs, the question words.
	def __init__(self):
		self.noun_tags = ['NN','NNS','NNP','NNPS']
		self.adjective_tags = ['JJ','JJR','JJS','VBG']
		self.question_tags = ['WP','WP$','WRB','WDT']
		self.verb_tags = ['VB','VBZ','VBP','VBD','VP','VPN']
		self.neglect = ['is','are','was','were','be','am','do','did','does','doing','done','has','have','had','having']
		self.yes_no = ['is','are','was','were','do','did','does','has','have','had']
		self.separator = ' H '
	
	# parse the tags to extract the nouns
	# args:
	# 	words_tags : list of pair of the word and its tag 
	# return:
	#	list of all nouns in the statement
	def get_nouns(self,words_tags) :
		result = []
		string = ''
		for idx, (word, tag) in enumerate(reversed(words_tags)) :
			if tag in self.noun_tags :
				if string :
					string = word + ' ' + string
				else :
					string = word
			elif tag in self.adjective_tags and string : 
				string = word + ' ' + string
			elif string :
				result.append((len(words_tags)-idx, string))
				string = ''
		result.reverse()
		return result
	
	# parse the tags to extract the question words
	# args:
	# 	words_tags : list of pair of the word and its tag 
	# return:
	#	list of all question words in the statement
	def get_question_words(self,words_tags) :
		result = []
		for idx, (word, tag) in enumerate(words_tags) :
			if tag in self.question_tags :
				result.append((idx, word))
		return result

	# parse the tags to extract the verbs
	# args:
	# 	words_tags : list of pair of the word and its tag 
	# return:
	#	list of all verbs in the statement
	def get_verbs(self,words_tags) :
		result = []
		for idx, (word, tag) in enumerate(words_tags) :
			if tag in self.verb_tags :
				verbz = Word(word)
				if verbz.lemmatize("v") not in self.neglect and word not in self.neglect:
					src_verb = verbz.lemmatize("v")
					result.append((idx, src_verb))
		return result

	# generate all combinations of the keywords of the statement
	# args:
	# 	words_tags : list of pair of the word and its tag 
	# return:
	#	list of all patterns of the keywords in the statement
	def get_all_question_combinations(self, words_tags, question) :
		result = []
		result.append(question)
		nouns = self.get_nouns(words_tags)
		question_words = self.get_question_words(words_tags)
		verbs = self.get_verbs(words_tags)

		statement = []
		statement.extend(nouns)
		statement.extend(question_words)
		statement.extend(verbs)
		statement.sort()
		statement = [word[1] for word in statement]

		for l in range(len(statement), 0, -1) :
			sub_lists = list(itertools.combinations(statement, l))
			for sub_list in sub_lists :
				sample_question = ''
				for word in sub_list :
					sample_question = sample_question + self.separator + word
				
				sample_question = sample_question + self.separator
				result.append(sample_question)
		return result

	# replace n't to not
	# args:
	#	string : the string to be converted
	# return :
	#	the string after convertion
	def replace_not(self, string) :
		string = string.replace("n't"," not")
		return  string
	
	# check if the question is (YES | NO)
	# args:
	#	string : the string to be checked
	# return :
	#	true if yes/no question , otherwise false
	def check_yes_ques(self, string) :
		if string : 
			ques = string.split()[0]
			tag = TextBlob(ques)
			ques_tag = tag.pos_tags[0][1]
			print 'ques', ques, 'ques_tag', ques_tag
			if ques in self.yes_no or ques_tag == "MD" :
				return True
			else : 
				return False
		else : 
			return False