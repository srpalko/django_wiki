from django.shortcuts import render

from . import util

from markdown2 import Markdown

from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

markdowner = Markdown()

# display a list of all wiki entries
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


# display a wiki entry
def display_entry(request, entry):
    entry_markdown = util.get_entry(entry)
    if entry_markdown is None:
        return render(request, "encyclopedia/entry.html", {"entry_html": "<h1>That entry does not exist.</h1>"})

    entry_html = markdowner.convert(entry_markdown)
    return render(request, "encyclopedia/entry.html", {"entry_html": entry_html, "title": entry})



 
