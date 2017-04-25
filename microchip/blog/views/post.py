from django.http import JsonResponse
from django.db.models import Q
from blog.models import Post, Content

def get_posts(request):
    '''
    :param request: HttpRequest object, which should be in json format
    :returns: Json in format like beyond.

    Example return
    ==============

    { posts:
        [
            {
                id: 5,
                title: example title,
                content: example content
                date: 26-02-2017,
                category: cats
                language: pl,
                author: rafix,
                link: about-cats-1
            },
            {
                id: 6,
                title: example title2,
                content: example content2,
                date: 26-03-2017,
                category: spaceships,
                language: en,
                author: ator
                link: about-dogs-1
            }
        ]
    }

    Request example
    ====================

    GET /posts?language=pl&count=3&category=space


    If language param is not specified, default is 'pl'

    Posts are returned in descending order, for practical reasons.

    Invalid request
    ===============

    If request is not made by ajax, server is returning error 500

    Errors
    ======
    Error messages (In Code 500 etc.) are returned in 'text' key.
    '''

    if (not request.is_ajax()):
        return JsonResponse({'text': 'Resquest seems not to be ajax'}, status=500)

    response = {
            'posts':
            [
            ]
            }

    language = request.GET['language'] if 'language' in request.GET else 'pl'
    count = int(request.GET['count']) if 'count' in request.GET else 0

    if count == 0:
        db_result = Post.objects.filter(category=request.GET['category']) if 'category' in request.GET else Post.objects.all()
    else:
        db_result = Post.objects.filter(category=request.GET['category'])[:count] if 'category' in request.GET else Post.objects.all()[:count]

    db_result = db_result[::-1]

    for post in db_result:

        post = {
                'id': post.id,
                'title': post.content.english_title if language == 'en' else post.content.polish_title,
                'content': post.content.english_content if language == 'en' else post.content.polish_content,
                'date': post.date,
                'category': post.category,
                'language': language,
                'author': post.author,
                'link': post.content.english_link if language == 'en' else post.content.polish_link
                }
        response['posts'].append(post)

    return JsonResponse(response)

def get_post(request):
    link = request.GET.get('link', None)
    language = request.GET.get('language', None)
    try:
        if language == 'en':
            content = Content.objects.get(english_link=link)
            post = Post.objects.get(content=content)
        else:
            content = Content.objects.get(content=content)
            post = Post.objects.get(content=content)
    except Exception as e:
        return JsonResponse({'text': str(e)}, status=500)
    return JsonResponse({
                        'id': post.id,
                        'content': post.content.polish_content if language == 'pl' else post.content.english_content,
                        'category': post.category,
                        'author': post.author,
                        'title': post.content.polish_title if language == 'pl' else post.content.english_title,
                        'date': post.date
                        })
