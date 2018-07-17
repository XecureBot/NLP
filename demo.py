from nltk.tokenize import  sent_tokenize,word_tokenize,PunktSentenceTokenizer
from nltk.corpus import stopwords,state_union
from nltk.stem import PorterStemmer
# import tk
import nltk
ps=PorterStemmer()
ex="pythoning pythoned pythoner"
ex1="in inn win sin singwg"
# nltk.download('nltk.draw')

print(sent_tokenize(ex))
print(word_tokenize(ex))
for i in word_tokenize(ex):
	print (i)
word=word_tokenize(ex)
w=[]
stop_words=set(stopwords.words("english"))
print(len(stop_words))
for i in word:
	print(i)
	if i not in stop_words:
		print(i)
		w.append(i);
print(w)
for i in w:
	print(ps.stem(i))
print(ps.stem('1233'))
# # txt="heloo d dd  dd dddddddddd dddd dddfjdjd rej dsijf as gng kdf jf kcjd"
# tr=state_union.raw("2005-GWBush.txt")
# s=state_union.raw("2006-GWBush.txt")
# c=PunktSentenceTokenizer(tr)
# t=c.tokenize(s)
# # print(tr)
# def p():
# 	try:
# 		for i in t:
# 			w=nltk.word_tokenize(i)
# 			tag=nltk.pos_tag(w)
# 			chunk=r"""chunk: {<RB.?>*<VB.?>*<NNP><NN>?} """
# 			chunkp=nltk.RegexpParser(chunk)
# 			chunked=chunkp.parse(tag)
# 			chunked.draw()
# 			print(chunked);
# 		print(tag)
# 	except Exception as e:
# 		print(str(e))
# p()

# lookup_dict = {'rt':'Retweet', 'dm':'direct message', "awsm" : "awesome", "luv" :"love"}
# def _lookup_words(input_text):
#     words = input_text.split() 
#     print(words)
#     new_words = [] 
#     for word in words:
#     	print(word)
#         if word.lower() in lookup_dict:
#             word = lookup_dict[word.lower()]
#         new_words.append(word)
#         # print(new_words)
#         new_text = " ".join(new_words) 
#     return new_text
# input_text1=str(input("enter a string"))
# print(type(input_text1))
# print(input_text1)
# _lookup_words(input_text1)

# from nltk import word_tokenize, pos_tag
# import matplotlib

# # text = "I am learning Natural Language Processing on Analytics Vidhya"
# text="i have to pay fine"
# tokens = word_tokenize(text)
# # %matplotlib inline
# print(pos_tag(tokens))
