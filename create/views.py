from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from encyclopedia import util

# Create your views here.
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['wiki-text']
        caseFoldEntries = [entry.casefold() for entry in util.list_entries()]

        if title.casefold() not in caseFoldEntries and title is not '':
            util.save_entry(title, text)
            return HttpResponseRedirect(f'/{title}')
        elif title is '':
            return render(request, 'create/create.html')
        else:
            messages.add_message(request, messages.ERROR, f'A wiki entry with the title {title} already exists.')
            return render(request, 'create/create.html', {'text': text})

    return render(request, 'create/create.html')