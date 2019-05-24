from django.shortcuts import render


def index(request):
    context = dict()
    return render(
        request=request,
        template_name='index.html',
        context=context,
    )
