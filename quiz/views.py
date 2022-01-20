from django.shortcuts import render

def index (request):
    renderPage = 'quiz/index.html'
    step = request.GET.get('step', 0)
    context = {
        'step': step,
        'nextStep': step+1
    }

    return render(request, renderPage, context)

def change_step (request, step):
    renderPage = 'quiz/index.html'
    context = {
        'step': step,
        'nextStep': step+1
    }

    return render(request, renderPage, context)