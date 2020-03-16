from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'message':'Oh! Hello There'})

#def work(request):
 #   return HttpResponse('Chao! form work')

def count(request):
    fulltext=request.GET['fulltext']
    #pull this out of url to fulltext
    #print(fulltext)
    wordlist=fulltext.split()
    #split() splits the words
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    
    #sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':worddictionary.items()})
    

def about(request):
    return render(request,'about.html')
