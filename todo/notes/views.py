from django.shortcuts import render, redirect
from notes.forms import AddNoteForm
from notes.models import Note


def index(request):
    notes = Note.objects.all()
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(**form.cleaned_data)
            return redirect("index")
    else:
        form = AddNoteForm()
    return render(request, "note_list.html", {"notes": notes, "form": form})