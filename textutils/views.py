# By Swapnil
from django.http import HttpResponse
from django.shortcuts import render


# Code 7
def index(request):
    params = {
        'name': 'Swapnil',
        'Address': 'Nagpur',
        'Planet': 'That Blue Planet',
    }
    return render(request, 'index.html', params)


def analyse(request):
    # Get The Text
    dj_text = (request.GET.get('text', 'default'))
    # Check Box
    dj_remove_punctuation = (request.GET.get('remove_punctuation', 'off'))
    dj_full_capitalize = (request.GET.get('full_capitalize', 'off'))
    dj_char_counter = (request.GET.get('char_counter', 'off'))

    if dj_char_counter == "on":
        analyzed_len = len(dj_text)
        params = {
            'purpose': 'Character Counter',
            'analysed_text': analyzed_len,
        }
        return render(request, 'analyse.html', params)
    elif dj_remove_punctuation == "on" and dj_full_capitalize == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        analyzed = analyzed.upper()
        params = {
            'purpose': 'Removed Punctuations & Uppercased',
            'analysed_text': analyzed,
        }
        return render(request, 'analyse.html', params)

    elif dj_remove_punctuation == "on" and dj_full_capitalize == "off":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Removed Punctuations',
            'analysed_text': analyzed,
        }
        print(params)
        return render(request, 'analyse.html', params)

    elif dj_remove_punctuation == "off" and dj_full_capitalize == "on":
        analyzed = dj_text.upper()
        params = {
            'purpose': 'Uppercase',
            'analysed_text': analyzed,
        }
        return render(request, 'analyse.html', params)

    else:
        return HttpResponse('Error')
