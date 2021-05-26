import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk import text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
# Create your views here.

def home(request):
    return render(request, 'home.html')


def runAlgo(userCode):

    text = userCode
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    freqTable = dict()

    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0

    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    
    average = int(sumValues/len(sentenceValue))
    summary = ''

    for sentence in sentences:
        if(sentence in sentenceValue) and (sentenceValue[sentence] > (1.2*average)):
            summary += " " + sentence

    return summary



def store(request):
    userCode = request.GET['usrCode']
    summary = runAlgo(userCode)
    df = pd.read_csv('dataset3.csv')
    dfTemp = pd.DataFrame([[userCode, summary]], columns=['Code', 'Summary'])
    dfFinal = df.append(dfTemp, ignore_index=True)
    dfFinal.to_csv('dataset3.csv', index=False)
    return render(request, 'home.html', {'summary' : summary, 'userCode' : userCode})





