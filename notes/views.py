from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Document

# Create your views here.


def notes_page(request):
    user = request.user
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all().filter(user=user)

    if request.method == "POST":
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()

            return redirect('/notes/?docid=%i' %docid)
        else:
            document = Document.objects.create(user=user, title=title, content=content)

            return redirect('/notes/?docid=%i' %document.id)

    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document
    }

    return render(request, "notes/notes.html", context)


def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('/notes/?docid=0')
