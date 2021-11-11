from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Sheet
from .forms import SheetForm


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'latest_sheet_list'

    # Return in reverse order (Newest to oldest)
    def get_queryset(self):
        return Sheet.objects.order_by('-pub_date')


class ResultsView(generic.DetailView):
    model = Sheet
    template_name = 'pages/results.html'


class UpdateView(generic.UpdateView):
    model = Sheet
    template_name = 'pages/update.html'
    fields = [
        #'title',
        #'category',
        't_img',
        't_debut',
        't_form',
        't_affil',
        't_bday',
        't_bplace',
        't_age',
        'body',
        #'section1',
        #'section2',
        #'section3',
        #'section4',
        #'section5',
        'rank_s',
        'rank_e',
        'rank_m',
        'rank_i',
        'rank_r',
        'rank_t',
        'section6',
    ]


def sheet_entry_view(request):
    form = SheetForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "pages/entry.html", context)
