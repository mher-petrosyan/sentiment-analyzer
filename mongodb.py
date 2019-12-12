import os
import pymongo
from google.cloud import translate
from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

#Mongo DB 
client = MongoClient("localhost", 27017, maxPoolSize=50)
db = client["sportfeed"]
collection = db['articles']
one_article = collection.find({})

#Google translate
translate_client = translate.Client()
all_titles = "/home/mher/all_english.txt"
non_english_titles = "/home/mher/non_english.txt"
target = 'en'
translation = translate_client.translate(
    all_titles,
    target_language=target)

#vader
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score
write_file = "results.txt"    

a = open(all_titles, 'w')
b = open(non_english_titles, 'w')

for document in one_article:
    if document.get("title", '') != None: # stugum enq for title uni
        text = document.get("title", '') # title@ get enq anum
        if document["language"] != "ENGLISH" : # yete language keyn ENGLISH chi apa execute anel if-ic nerqev
            b.write("title"  + '\n')
            file_size = os.path.getsize("/home/mher/non_english.txt") 
            print(file_size)
#            if file_size >= 204800:
#                a.write(u'Translation: {}'.format(translation['translatedText']) + '\n')
#        else:    
#            a.write(text + '\n')

#with open(all_titles, 'r') as filehandle:
#    filecontent = filehandle.read()
#with open(write_file, 'a') as result:
#    result.write(str(sentiment_analyzer_scores(filecontent)) + '\n')

b.close()
result.close()
filehandle.close()