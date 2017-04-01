import django.contrib.auth as auth
from django.http import JsonResponse

def authenticate(request):
    '''
    :param request: HttpRequest object
    :returns: JsonResponse object

    Request post data
    =================

    Should be like that:
    {
        'username': 'stefan',
        'password': 'password123'
    }

    Return variants
    ===============
    {
        'status': 'OK'
    }
    If succeed to log the user

    {
        'text': 'Error message'
    }
    With status 500 - otherwise
    '''

    if not request.is_ajax():
        return JsonResponse({'text': 'Request is not ajax'}, status=500)

    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return JsonResponse({'status': 'OK'})
    else:
        return JsonResponse({'text': 'Username or password is invalid'}, status=500)

