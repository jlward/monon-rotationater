from django.shortcuts import render

from .forms import Form


def index(request):
    form = Form()
    context = dict(
        form=form,
    )
    return render(
        request=request,
        template_name='index.html',
        context=context,
    )
