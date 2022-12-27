#created by faizan
import operator

from django.http import HttpResponse
from django.shortcuts import render
from . import counter


def home(request):
    return render(request, 'index.html',{'key1':'I am coming from python code'})
    #return HttpResponse('<h1>Welcome this response is working</h1>')

def result(request):
    #age=request.GET['user_age']
    article = request.GET['article']
    dic_words_sorted, word_count = counter.count(article)
    # print("ITS DICT here")
    # print(dic_words_sorted)
    return render(request, 'result.html', {'article':article, 'word_count':word_count, 'dict_words':dic_words_sorted})
