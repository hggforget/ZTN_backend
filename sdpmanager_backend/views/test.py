from django.shortcuts import render


def test(request):
    print("sdasd")
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'test.html', context)