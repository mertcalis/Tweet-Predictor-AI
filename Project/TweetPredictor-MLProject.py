#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Product Name : Tweet Predictor
#Author : Mert Çalış
#------------------------------------

#Summary : The algorithm uses supervised learning. There are data set of tweets which are labeled as written by woman or man. My code will predict unlabeled tweet is written
#          by woman or man via common words.

#Possible Upgraded Version : Predict age and region.(And predicting according to emojies and structures of sentences)



#Requirements: Data set, String tokenizer, File Reader, Confidence calculation, Max repeated words written by women and men.

import numpy as np
import string

menWords = []
womenWords = []

"""
    The function takes a string and label.Tokenize the string and add the array of given label.If label is wrong throws IllegalLabelException
    Label = 1 means MAN
    Label = 0 means WOMAN
    
    
    @param String text: A tweet
    @param int label: 1 or 0 dependent on sex of author
"""
def distributeWordsToArrays(text,label):
    
    words = text.split()
    
    if(label==1):
        menWords.extend(words)
    elif(label==0):
        womenWords.extend(words)
    else:
        raise ValueError("IllegalLabelException")


"""
    The Function Reads File with given File Name
    
    @param String fileName: Better to be in txt format
    @returns: an list of elements in txt file line by line
"""
def readData(fileName):
   
    f = open(fileName,'r')
    f.close()

    with open(fileName,errors="ignore") as f:
        labeledTweets = f.readlines()
        labeledTweets = {x.replace('\n', '') for x in labeledTweets}
        return labeledTweets

def tweetFixer(tweet,label):
    newText =""
    
    if(label==0):
        newText = tweet.replace("/0", "", 1)
        
    elif(label==1):
        newText = tweet.replace("/1", "", 1)
    else:
        print("Wrong label!!")
        
    newText = newText.translate(str.maketrans('','',string.punctuation))
    newText = newText.lower()
    return newText
"""
    The function takes a list of labeled tweets and labels together. Checks at the end whether 0 or 1. And seperates labels from tweets and delegates the parameters
    (label and tweet) to distrubute function
    
    @param List type Strings
"""
def getTweets(labeledTweets):
    for tweet in labeledTweets:
        label = int(tweet[-1])
        tweetText = tweetFixer(tweet,label)

        distributeWordsToArrays(tweetText,label)

data = readData("updatedDataSetV2.txt")
getTweets(data)


# In[9]:


"""
    The function returns number of occurrence of given word in menWords list.
    @param word : String
    @returns count : int
"""
def getOccurrenceOfWordInMen(word):
    return menWords.count(word)
"""
    The function returns number of occurrence of given word in womenWords list.
    @param word : String
    @returns count : int
"""
def getOccurrenceOfWordInWomen(word):
    return womenWords.count(word)

"""
    This function returns most frequent word in given list
    
    @param arr : list
"""
def getMostFrequentWord(arr):
    return max(arr,key=arr.count)

getMostFrequentWord(womenWords)


# In[10]:


def predict(tweet):
    mascularity = 0
    feminity = 0
    
    tweet = tweet.translate(str.maketrans('','',string.punctuation))
    tweet = tweet.lower()
    
    wordSet = tweet.split()
    
    for word in wordSet:
            mascularity + getOccurrenceOfWordInMen(word)
            feminity + getOccurrenceOfWordInWomen(word)
            
    if(mascularity > feminity):
        return 1
    else:
        return 0

def predictPlus(tweet):
    wordSet = tweet.split()
    menRates = []
    womenRates = []
    
    for word in wordSet:
        mWeight = getOccurrenceOfWordInMen(word)
        fWeight = getOccurrenceOfWordInWomen(word)
        
        if(mWeight==0 and fWeight==0):
            continue
        else:
            menRates.append(100*mWeight/(mWeight+fWeight))
            womenRates.append(100*fWeight/(mWeight+fWeight))
    #print(menRates)
    #print(womenRates)
    if(sum(menRates)>sum(womenRates)):
        return 1
    else:
        return 0
    
tw = "I am going to the movies tomorrow"
#print("Prediction is: ",predict(tw))
#print("Prediction is: ",predictPlus(tw))

def checkConfidence(unlabelledTweetSet):
    confidenceResults = []
    for t in unlabelledTweetSet:
        label = int(t[-1])
        tweetText = tweetFixer(t,label)
        prediction = predictPlus(tweetText)
        
        if(label==prediction):
            confidenceResults.append(True)
        else:
            confidenceResults.append(False)
            
    return confidenceResults.count(True)*100/len(confidenceResults)
        
checkConfidence(data)


# In[ ]:





# In[ ]:





# In[ ]:




