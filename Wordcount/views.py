from django.http import HttpResponse
from django.shortcuts import render
import operator

def welcome( request ):
    return render( request, 'welcome.html' )

def homepage( request ):
    return render(request, 'home.html')

def count( request ):
    Text = request.GET[ 'Text' ]
    wordsList = Text.split()
    wordsDict = {}
    for word in wordsList:
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    wordsDict = sorted( wordsDict.items(), key=operator.itemgetter(1), reverse=True)
    return render( request, 'count.html', { 'count' : len( wordsList ), 'Text':Text, 'wordsDict':wordsDict} )

def about( request ):
    return render( request, 'about.html' )
