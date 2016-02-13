from nltk.corpus import stopwords

stop = stopwords.words('english')
result_f = open('result.txt', 'a')

with open("train_data_sample.txt", "rw+")as f:
    sentence=f.readlines()
    word=i for i in sentence.split() if i not in stop]
     result_f.write(word)