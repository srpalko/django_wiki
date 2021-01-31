from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from random import choice
from encyclopedia import util

# Create your views here.
def randomwiki(request):
    wikiList = util.list_entries()
    randomArticle = choice(wikiList)
    return HttpResponseRedirect(f'/{randomArticle}')
