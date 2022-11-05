from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    # analyze the text
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./|?@#$%^&*_`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove New lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(charactercounter=="on"):
        analyzed = ""
        count=0
        for char in djtext:
                analyzed = analyzed + char
                count = count + 1
        params = {'purpose': 'Count Characters', 'analyzed_text': count}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps !="on"):
        return HttpResponse("Please choose any appropriate option...")
    return render(request, 'analyze.html', params)


