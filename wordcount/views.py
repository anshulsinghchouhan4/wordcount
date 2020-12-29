from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request,'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	dict1 = {}
	for i in wordlist:
		if i in dict1:
			dict1[i] += 1
		else:
			dict1[i] = 1
	total = len(wordlist)
	dictlist = dict1.items()
	#print(dictlist)
	sortedlist = sorted(dictlist,key=operator.itemgetter(1),reverse = True)
	
	return render(request,'count.html',{'dict1':dictlist,'total':total,'sortedlist':sortedlist})
	
def about(request):
	return render(request,'about.html')