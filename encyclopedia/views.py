from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util



def index(request):
    if request.method == "POST":
        print(request.POST["q"])
        if util.get_entry(request.POST["q"]) != None:
            return HttpResponseRedirect("/"+request.POST["q"])
        else:
            return HttpResponseRedirect("/results/" + request.POST["q"])
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, title):
    entry = util.get_entry(title)
    if entry != None:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "title": title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Entry not found."
        })

def results(request, query):
    elements = util.list_entries()
    entries = []
    for e in elements:
        if query in e:
            entries.append(e)
    return render(request, "encyclopedia/results.html", {
        "entries": entries
    })

def create(request):
    if request.method == "POST":
        util.save_entry(request.POST["title"], request.POST["entry"])
        return HttpResponseRedirect(reverse("index"))
    return render(request, "encyclopedia/create.html")
