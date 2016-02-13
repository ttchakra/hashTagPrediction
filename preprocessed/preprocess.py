import re

def preprocess(stopWordsFilename,dataFilename,outputFilename):
	
	f1=open(outputFilename,'a')
	
	with open(dataFilename,"r") as f:
		file = f.readlines()

		for line in file:
			new_line=re.sub('\s+',' ',line)
			new_line = new_line.rsplit(' ',2)[0]
			new_line = new_line.split(' ',1)[1]
			
			new_line=re.sub(',','',new_line)
			#print new_line
			new_line=re.sub('\*','',new_line)
			#print new_line
			new_line=re.sub(':','',new_line)
			new_line=re.sub('\%','',new_line)
			new_line=re.sub('!','',new_line)
			new_line=re.sub('/','',new_line)
			#new_line=re.sub('\\','',new_line)
			#print new_line
			new_line=re.sub('=','',new_line)
			new_line=re.sub('\?','',new_line)
			new_line=re.sub('"','',new_line)
			new_line=re.sub('','',new_line)
			new_line=re.sub('\...','',new_line)
			new_line=re.sub('@','https',new_line)
			new_line=re.sub('\..','',new_line)
			#new_line=re.sub(r"https",new_line)
			#print new_line
			stopwords=CheckStopwords(stopWordsFilename)



			word1=new_line.split(" ")
			#print word1

			for word in word1:
				
				#word = word.lower()
				
				if word.startswith('http'):
					word1.remove(word)
				

				if len(word) < 2 : # Skip words that are less than 3 characters, e.g. `#2`
					word1.remove(word)
			#print word1
				resultwords  = [word for word in word1 if word.lower() not in stopwords]
				result = ' '.join(resultwords)

			f1.write(result+'\n')

#main
def CheckStopwords(stopWordsFilename):

	with open(stopWordsFilename,"r") as f:
		lines=f.read()
		return lines

#print CheckStopwords("in")
preprocess("stopwords.txt","traindata.txt","train_output.txt")
