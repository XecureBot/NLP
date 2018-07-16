import pandas as pd
import nltk
from nltk.corpus import stopwords,state_union
from nltk.tokenize import  sent_tokenize,word_tokenize,PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
# nltk.download('PorterStemmer')
ps=PorterStemmer()
lemmatizer = WordNetLemmatizer()

data = pd.read_csv('abcnews-date-text.csv', error_bad_lines=False);
words=word_tokenize(str(data))
# print(words)
l=[]
new_words = [] 
fwords=[]
stop_words=set(stopwords.words("french"))
print(stop_words)
for word in words:
	if(word!= "," and len(word)>=3 and word not in stop_words):
		new_words.append(lemmatizer.lemmatize(word))
		fwords.append(ps.stem(new_words))
print(new_words)		
# print(fwords)