from django.shortcuts import render

from .forms import Form


def populate_bucket(names, bucket, count):
    for _ in range(count):
        try:
            name = names.pop(0)
        except IndexError:
            return
        bucket.append(name)


def index(request):
    blue_bucket = []
    green_bucket = []
    red_bucket = []
    initial = dict(
        blue=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
        green=['1', '2', '3', '4', '5', '6', '7', '8', '9'],
        red=['1', '2', '3', '4', '5', '6', '7', '8'],
    )
    form = Form(initial=initial)
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            names = form.cleaned_data['names']
            populate_bucket(names, blue_bucket, form.cleaned_data['blue'])
            populate_bucket(names, green_bucket, form.cleaned_data['green'])
            populate_bucket(names, red_bucket, form.cleaned_data['red'])
            # If there extra names left over, move them to blue.
            blue_bucket += names
    context = dict(
        form=form,
        blue_bucket=blue_bucket,
        green_bucket=green_bucket,
        red_bucket=red_bucket,
    )
    return render(
        request=request,
        template_name='index.html',
        context=context,
    )
