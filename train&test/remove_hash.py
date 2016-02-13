import re


f1=open("removed_hashtag.txt","w")

with open("sample_tweetsbig.txt","r") as f:
	for line in f:
		new_line=re.sub('#',' ',line)
		f1.writelines(new_line)

    