from django.http import JsonResponse

def validate(request):
    post = request.POST

    if 'language' not in post or 'title' not in post or 'category' not in post or 'content' not in post:
        return {'valid': 'false', 'cause': 'Form is incomplete'}
    if post['language'] != 'pl' and post['language'] != 'en':
        return {'valid' : 'false', 'cause': 'Invalid language'}
    if not post['category'] or not post['content'] or not post['title'] or not post['language']:
        return {'valid': 'false', 'cause': 'One or more fields are empty'}
    return {'valid': 'true'}

def add_post(request):
    '''
    :param request: HttpRequest
    :return: JsonResponse

    Validates request, and returns
    {
        'status': 'OK'
    }
    if everythong is ok or
    Status 500, with error text in:
    {
        'text': 'Here will be eror code'
    }
    
    Valid request
    =============
    Request is valid if it's like:
    {
        'title': 'Some title',
        'content': 'content',
        'language': 'pl', #(Could be 'en' too)
        'category': 'category'
    }

    Date will be set automatically to current system time
    '''

    if not request.is_ajax():
        return JsonResponse({'text': 'ajax request required'}, status=500)

    validation_result = validate(request)
    if validation_result['valid'] == 'false':
        return JsonResponse({'text': validation_result['cause']}, status=500)
    else:
        return JsonResponse({'status': 'OK'})
