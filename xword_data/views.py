from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import  Clue
from .form import DrillForm
# Create your views here.

clue = Clue.objects.order_by("?").first()
def drill_get(request):
    context = {'clue_entry': clue.entry,
               'clue_puzzle':clue.puzzle}
    return render(request, 'xword_data/drill.html', context)


def drill_post_incorrect(request):
    if request.method == 'POST':
        form = DrillForm(request.POST)
        if form.field.value() != clue.entry:
            messages.error(request, f'not correct')
            HttpResponse(status=200)
            return redirect('drill')


def drill_post_correct(request):
    if request.method == 'POST':
        form = DrillForm(request.POST)
        if form.field.value() == clue.entry:
            return render(request,'xword-answer')



