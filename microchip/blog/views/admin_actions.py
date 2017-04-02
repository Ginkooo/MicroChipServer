from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from blog.models import Post, Content
from datetime import datetime

@login_required()
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
        'english_title': 'some english title', #Must be set
        'polish_title: 'jakiś polski tytuł', #Must be set
        'polish_content': 'jakiś polski kontent',  #Might be not set, or be empty
        'english_content': 'some english content', #Might be not set, or be empty
        'polish_link': 'jakiś-polski-link', #Must be set
        'english_link': 'some-english-link', #Must be set
        'category': 'category',
    }

    Date will be set automatically to current system time
    '''

    if not request.is_ajax():
        return JsonResponse({'text': 'ajax request required'}, status=500)

    post = request.POST

    polish_title = post['polish_title'] if 'polish_title' in post else None
    english_title = post['english_title'] if 'english_title' in post else None
    polish_content = post['polish_content'] if 'polish_content' in post else None
    english_content = post['english_content'] if 'english_content' in post else None
    polish_link = post['polish_link'] if 'polish_link' in post else None
    english_link = post['english_link'] if 'english_link' in post else None
    author = post['author'] if 'author' in post else None
    category = post['category'] if 'category' in post else None
    date = datetime.now()

    try:
        content = Content(polish_content=polish_content, english_content=english_content, polish_title=polish_title, english_title=english_title, polish_link=polish_link, english_link=english_link)

        content.full_clean()
        content.save()

        post = Post(content=content, author=author, category=category, date=date)
        post.full_clean()
        post.save()
    except ValidationError as e:
        return JsonResponse({'text': str(e)}, status=500)

    return JsonResponse({'status': 'OK'})

@login_required()
def delete_post(request):
    if not request.is_ajax():
        return JsonResponse({'text': 'Request is not made by ajax'}, status=500)
    try:
        Post.objects.get(id=request.POST['id']).delete()
    except:
        return JsonResponse({'text': 'Cannot delete such a post'}, status=500)
    return JsonResponse({'status': 'OK'})

@login_required()
def edit_post(request):
    if not request.is_ajax():
        return JsonResponse({'text': 'ajax is required'}, status=500)
    pk = request.POST.pop('id', None)[0]
    post = request.POST

    post_info = {}
    content_info = {}

    if 'english_title' in post: content_info['english_title'] = post['english_title']
    if 'polish_title' in post: content_info['polish_title'] = post['polish_title']
    if 'english_content' in post: content_info['english_content'] = post['english_content']
    if 'polish_content' in post: content_info['polish_content'] = post['polish_content']
    if 'english_link' in post: content_info['english_link'] = post['english_link']
    if 'polish_link' in post: content_info['polish_link'] = post['polish_link']
    if 'author' in post: post_info['author'] = post['author']
    if 'category' in post: post_info['category'] = post['category']

    try:
        content = Post.objects.get(pk=pk).content
        for key, value in content_info.items():
            setattr(content, key, value)
        content.full_clean()
        content.save()

        post_info['content'] = content
        post = Post.objects.get(pk=pk)
        for key, value in post_info.items():
            setattr(post, key, value)
        post.full_clean()
        post.save()

    except ValidationError as e:
        return JsonResponse({'text': str(e)}, status=500)
    return JsonResponse({'status': 'OK'})
