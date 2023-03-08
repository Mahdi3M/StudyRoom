from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.


def dictionary_page(request):
    search = ''
    meanings = ''
    synonym = ''
    antonym = ''
    if request.method == "POST":
        search = request.POST.get('search')
        dict = Dictionary(search)
        meanings = dict.meanings()
        synonym = dict.synonyms()
        antonym = dict.antonyms()
    return render(request, "dictionary/dictionary.html", {
        'search': search.capitalize(),
        'meanings': meanings,
        'synonyms': synonym,
        'antonyms': antonym
    })
