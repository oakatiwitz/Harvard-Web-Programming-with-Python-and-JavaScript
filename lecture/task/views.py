# import library forms from django
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

#task = []
class NewTaskForm(forms.Form):
    # the label name will show on web 
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=4)

# Create your views here.
def index(request):
    # this is to make a different session for individual ex when we open this websit together it will show difeerent page for each session
    if "task" not in request.session:
        request.session["task"] = []

    return render(request, "task/index.html", {
        "task": request.session["task"]       
    })

def add(request):
    if request.method == "POST":
        # request.POST contain all the data that user submitted on th form
        form = NewTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["task"]
            request.session["task"] += [data]
            #After append the data, it will go back to index page
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html",{
        "form": form
            })
    return render(request, "task/add.html",{
        "form": NewTaskForm()
    })