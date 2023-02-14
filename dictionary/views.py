from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.


def dictionary_page(request):
    search = ''
    meaning = ''
    synonym = ''
    antonym = ''
    if request.method == "POST":
        search = request.POST.get('search')
        dict = Dictionary(search)
        meaning = dict.meanings()
        synonym = dict.synonyms()
        antonym = dict.antonyms()
    return render(request, "dictionary/dictionary.html", {
        'search': search.capitalize(),
        'meanings': meaning,
        'synonyms': synonym,
        'antonyms': antonym
    })
