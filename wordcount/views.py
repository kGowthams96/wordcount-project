from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{"login": "Please enter the details"})

def count(request):
    yourtext=request.GET['fulltext']
    words=yourtext.split()
    wordcountdic={}
    for word in words:
        if word in wordcountdic:
            wordcountdic[word]+=1
        else:
            wordcountdic[word]=1
    sortedcount= sorted(wordcountdic.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'text':yourtext,"count":len(words),'wordcountdic':sortedcount})

def about(request):
    return render(request,'about.html')