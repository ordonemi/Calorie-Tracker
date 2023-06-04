from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Entry

class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_entered")

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(CreateView):
    model = Entry
    fields = ["title", "description"]
    success_url = reverse_lazy("entry-list")

class EntryUpdateView(UpdateView):
    model = Entry
    fields = ["title", "description"]
   
    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")