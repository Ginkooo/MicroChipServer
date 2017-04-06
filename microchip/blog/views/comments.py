from django.http import JsonResponse
from blog.models import Comment

def assemble_result(comments):
    ret = []
    for comment in comments:
        subcomments = [c for c in comments if c.parent_comment is not None and c.parent_comment.id == comment.id]
        comments[:] = [c for c in comments if not c in subcomments]
        ret.append( {
                'id': comment.id,
                'author': comment.author,
                'content': comment.content,
                'date': comment.date,
                'subcomments': assemble_result(subcomments)
                } )
    return ret

def get_comments_for_post(request):
    '''
    :param request: HttpRequest object.
    :returns: JsonResponse object

    How to do a request
    ===================
    You simply provide JSON like:
    {
        'id': '5'
    }
    To get all comments for post with id 5

    Exaple return
    =============
    {
        'comments': [
            {
                'id': '40',
                'author': 'Jack Spedicy 2',
                'conenent': 'Mars in 2 years',
                'date': 24-12-2017,
                'subcomments: [
                    {
                        'id': '42',
                        'author': 'Jack Spedicy 2',
                        'conenent': 'Mars in 2 years',
                        'date': 24-12-2017,
                        'subcomments: []
                    },
                    {
                        'id': '44',
                        'author': 'Jack Spedicy 2',
                        'conenent': 'Mars in 2 years',
                        'date': 24-12-2017,
                        'subcomments: []
                    }
                    ]
            },
            {
                'id': '50',
                'author': 'Jack Spedicy 2',
                'conenent': 'Mars in 2 years',
                'date': 24-12-2017,
                'subcomments: [
                    {
                        'id': '56',
                        'author': 'Jack Spedicy 2',
                        'conenent': 'Mars in 2 years',
                        'date': 24-12-2017,
                        'subcomments: []
                    },
                    {
                        'id': '65',
                        'author': 'Jack Spedicy 2',
                        'conenent': 'Mars in 2 years',
                        'date': 24-12-2017,
                        'subcomments: []
                    }
                    ]
            }
            ]
    }

    Error
    =====
    If error occurs, JsonResponse in standard format is returned, with error message in 'text' field, with status 500.
    '''

    if not request.is_ajax():
        return JsonResponse({'text': 'Request have to be made using ajax'}, status=500)
    try:
        post_id = request.POST['id']
        db_result = list(Comment.objects.filter(post__id=post_id))
    except Exception as e:
        return JsonResponse({'text': str(e)}, status=500)
    result = assemble_result(db_result)
    return JsonResponse({'comments': result})
