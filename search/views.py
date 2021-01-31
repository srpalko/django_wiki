from encyclopedia.views import display_entry
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from encyclopedia import util


# Create your views here.

# search for a wiki entry
def index(request):
    # get value from search box
    if request.method == 'POST':
        value = request.POST['q']
        
        # check to see if the word typed is a valid page. If so, go there.
        if util.get_entry(value) is not None:
            return HttpResponseRedirect(f'/{value}')

        # if not in list, check to see if typed search is a substring of any titles and display a results list.
        entries = util.list_entries()
        filteredEntries = [entry for entry in entries if value.casefold() in entry.casefold()]

        if filteredEntries == []:
            notFoundResponse = 'There are no entries that match that search.'
            return render(request, 'search/index.html', {'notFoundResponse': notFoundResponse})

        return render(request, 'search/index.html', {'filteredEntries': filteredEntries})





