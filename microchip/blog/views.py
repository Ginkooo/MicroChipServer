from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def get_posts(request):
    '''
    :param request: HttpRequest object, which should be in json format
    :returns: Json in format like beyond.

    Example return
    ==============

    { posts:
        [
            {
                title: example title,
                content: example content
                date : 26-02-2017,
                language: pl,
                author: rafix
            },
            {
                title: example title2,
                content: example content2,
                date : 26-03-2017,
                language: en,
                author: ator
            }
        ]
    }

    Request json example
    ====================

    GET /posts?language=pl&count=3&category=space

    If no count param specified, method will return all posts matching other params.
    You can skip other params to acquire simillar effect.

    Invalid request
    ===============

    If request is not made by ajax, server is returning error 500

    Errors
    ======
    Error messages (In Code 500 etc. are returned in 'text' key.
    '''

    if (not request.is_ajax()):
        return JsonResponse({'text': 'Resquest seems not to be ajax'}, status=500)
    return JsonResponse({'text': 'It works!'}, status=200)
