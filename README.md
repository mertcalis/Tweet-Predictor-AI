# Tweet-Predictor-AI
Self-Designed AI that predicts author's gender

This project aims to predict a tweet’s author either man or woman. The 
algorithm uses supervised learning. That means a collection of tweets with labels is gathered by twitter. 
And the code is basically getting the label at the end of the sentences first, and then taking the 
tweet and dividing it into words. After that, it adds words to each label’s word list 
(womenWordList or menWordList). In this way, the words and weights data set has been 
created for men and women separately.


## Features

- Import a txt file and it clusters the tweets.
- Most frequent word (via gender)
- Prediction of the gender of the author
- Creates a database of tweets
- Confidence graph

[Warning][df1] : Tweets must be labeled as /1 or /0 at the end

> #### Possible Upgrades
>  - Predict age and region (predicting according to emojies and structures of sentences)
>  - Get some general ideas of the specified hashtagged tweet. (#VoteForPresident or somth)
>  - Using API instead of txt file to get tweets

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Algorithms

> At the beginning, the algorithm is designed which divide unlabelled tweets
into words and for each word checks the occurrence of the word in womenWords and 
menWords. And add the occurrences for each word. After that, if the feminity (words’
occurrence in womenWords list) is higher it returns 0, which means prediction is woman, else 
1, means a prediction is a man.

```sh
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
```

The confidence of the algorithm which is shown in Figure 1 is 44.230769230769. After t
hat, a problem is identified, caused by women using Twitter more. An example situation is sho
wn in the figure below

![image](https://user-images.githubusercontent.com/44343742/194770426-7fb8adb4-8822-453f-adf2-5a8e2faab3a1.png)

Then, the new upgraded algorithm is designed that takes percentages for each word 
instead of just occurrence numbers. In this way, some characteristic words (over 80%) affect
more than a number.

```sh
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
```


## Results

The first and upgraded version of the algorithm have been tried for data sets which have 
different lengths as 20, 100, and 200. Comparison is done and resulted graph is given in 
Figure below and it is observed that upgraded version of algorithm gives better results.

![image](https://user-images.githubusercontent.com/44343742/194770434-5c7714d0-8318-4d33-9cbc-102a8ffe2338.png)



## License

MIT
