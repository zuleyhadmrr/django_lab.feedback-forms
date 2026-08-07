from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')

    else:
        form = FeedbackForm()

    return render(request, 'feedback/form.html', {'form': form})


def feedback_success(request):
    return render(request, 'feedback/success.html')
