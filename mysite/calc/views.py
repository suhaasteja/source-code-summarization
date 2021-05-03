import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')


def runAlgo(userCode):
    #algorithm that generates summary
    return "summary of code"



def store(request):
    userCode = request.GET['usrCode']
    summary = runAlgo(userCode)
    df = pd.read_csv('dataset3.csv')
    dfTemp = pd.DataFrame([[userCode, summary]], columns=['Code', 'Summary'])
    dfFinal = df.append(dfTemp, ignore_index=True)
    dfFinal.to_csv('dataset3.csv', index=False)
    return render(request, 'home.html', {'summary' : summary})





