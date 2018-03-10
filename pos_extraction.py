import nltk
#nltk.download("averaged_perceptron_tagger")

def verb_noun(tagged):
	hobbies=list()
	tagged_len=len(tagged)
	for i in range(0,tagged_len):
		if(str(tagged[i][1]) in ["VB","VBD","VBG","VBN","VBP","VBZ"]):
			for j in range(i+1,tagged_len):
				if(str(tagged[j][1]) in ["NN","NNP","NNS","NNPS"]):
					hobby=tagged[i][0]+tagged[j][0]
					hobbies.append(hobby)
					break
			hobby=tagged[i][0]
			hobbies.append(hobby)
	return hobbies
	




#sentence = """At eight o'clock on Thursday morning
#... Arthur didn't feel very good."""
#sentence2="""i'm not feeling good"""
#sen3="""I would play guitar. I would paint. I would love to dance."""
sen3="""I love to read and dance. I love listening to music while cooking at the same time. I love to explore new places and roam about. I love visiting historical places."""
#sen4= """I am going to read this book in the flight"""
tokens = nltk.word_tokenize(sen3)
#tokens1 = nltk.word_tokenize(sen4)
#print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)
#tagged1 = nltk.pos_tag(tokens1)
hobby=verb_noun(tagged)
print(hobby)
#for word in tagged:
#	if(word[1]=="""NN"""):
		#print(word)
		
	#print(tagged1[1][1])
#finding noun in the text
#for word in tagged:
#	if(word[1]=="VB" or "VBD" or "VBN"):
#		while(word[1]!="NN"):
#			print("####")
			#continue
#		combi=word[0]
		#print(combi)
		
#finding word after a noun


