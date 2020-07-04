from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import random
import markdown2
from markdown2 import Markdown

def index(request):
    if request.method == "POST":
        print(request.POST["q"])
        if util.get_entry(request.POST["q"]) != None:
            return HttpResponseRedirect("/wiki/"+request.POST["q"])
        else:
            return HttpResponseRedirect("/wiki/results/" + request.POST["q"])
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, title):
    entry = util.get_entry(title)
    if entry != None:
        markdowner = Markdown()
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(entry),
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
        if util.get_entry(request.POST["title"]) == None:
            util.save_entry(request.POST["title"], request.POST["entry"])
            return HttpResponseRedirect("/wiki/" + request.POST["title"])
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "Title already exists!"
            })
    return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST":
        entry = request.POST["entry"]
        print(entry)
        util.save_entry(title, entry)
        return HttpResponseRedirect("/wiki/" + title)
    entry = util.get_entry(title)
    if entry != None:
        return render(request, "encyclopedia/edit.html", {
            "entry": entry,
            "title": title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Entry not found."
        })

def randomPage(request):
    elements = util.list_entries()
    randNum = random.randint(0, len(elements) - 1)
    title = elements[randNum]
    return entryPage(request, title)
