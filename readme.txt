READ ME File:

*****************************************
TWITTER HASHTAG PREDICTION ALGORITHM:
*****************************************
AUTHORS:
********
Hamsalekha Venkatesh
Nivedha Padmanabhan
Tanushree Chakravorty

1) Input and output files: 
-----------------------------
    Unprocessed Input Files:
     data for student.txt-This is the unprocessed data that has both training and testing dataset.
                            traindata.txt--70% of the dataforstudent.txt is used as training data 
                            testdata.txt--30% of the dataforstudent.txt is used to testing data.

2)Clean and preprocess the train and test data: preprocess.py("training.txt")
                                                preprocess.py("tresting.txt")
--------------------------------------------------------------
    This is the preprocessing code that removes unwanted columns and special characters from the input data like the userID, latitude, longitude, all special characters, URLs
    
    2.1 TF-IDF code and removal of stop words:
    ----------------------------------------------------------
        ->tf_idf.py is the script for generating tf_idf
        ->this file applies the script on the data file(training) to generate the stop word list
        ->this list is written in 'stopwords.txt'
        ->we use this list of stop words to check against the training data and for successive runs of it.
    
3) Actual Code:
--------------------------------------------------------------
 tweet_extracts.py. This is the code that is used to generate the hash map and predict the hash tag for the testing data. It creates hash map and stores key and its corresponding hashtags in an entry of the hasmap i.e. H(keyword)-->{hashtags} 
 
 This file is invoked from its main() where it calls createHashMap("train_data.txt") and prints the generated Hashmap that is the key value pairs. It also invokes the generateHashMap(trainingdata_filename) and it also invokes the predictHashtag(testdata_filename).

4)Sample Output:
--------------------------------------------------------------
    train_output.txt --This has the cleaned version of the training data tha will be fed to the tweets_extracts.py for prediction ---> Cleaned training data
    test_output.txt-- This has the cleaned version of the testing data that will be used for testing the model ------> Cleaned testing data
    expOpFinal.txt--This file contains the predicted hashtags for the sample testing data     
    expOpAccuracy.txt---> expected output -----> contains hashtags for a small smaple data 
    genOpAccuracy.txt----> generated op with high accuracy------> contains hashtags for a medium sized testing data
    genOpLessAccuracy.txt----->with less accuracy ------> without many tweaks to the algorithm
    
5)Graphs:
--------------------------------------------------------------
In this section, we have generated and attached several graphs showing different experiments and fining tuning we performed in stages of our experiment with the recommendation model. We have tweaked our algorithm keeping in mind the nature of the training and test data and chosen our model accordingly. These changes are clearly demonstrated by graphs in every stage of the report.


---->Manual Splitting of dataforstudent.txt is done to seperate the training and test data. 






