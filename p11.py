import nltk
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
dict = {}
file = open('a1.txt')
while 1:
    sentence = file.readline()
    print sentence
    if not sentence:break

    for i in sentence.split():
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
            #print tagged
            #list(list(tuple(str, str)))
        for j in tagged:
            count = 0
            for k in j:
                count = count + 1
                if count ==1:
                    str = k
                else:
                    dict[str]=k
                    print dict[str] , str

    pos_count=0
    neg_count=0
    for i in sentence.split():
         print i
         if dict[i]=="JJ":
            id = swn.senti_synset(i+".a"+".01")
         if dict[i]=="JJS":
            id = swn.senti_synset(i+".s"+".01")
            print id.pos_score , id.neg_score
            if id.pos_score >id.neg_score:
               pos_count = pos_count + 1
            elif id.pos_score < id.neg_score:
                neg_count = neg_count + 1

    print pos_count , neg_count

    if neg_count%2==1:
        print "The sentence is positive"

    else:
       print "The sentence is negative"


