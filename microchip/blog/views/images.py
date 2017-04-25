from django.http import JsonResponse
from blog.models import Image
from django.contrib.auth.decorators import login_required
import sys

@login_required()
def upload_image(request):
    '''
    Post to this view, to upload image

    POSTed json should be like:

    {
        'image': image_content,
        'tags': ['tag1', 'tag2', 'tag3']
    }
    tags list must be provided, even if it is empty

    Retunrns
    ========

    {
        'url': relative_url_to_image
    }

    If there was an error:

    {
        'text': error_text
    }
    with status 500
    '''

    image = request.FILES['image']
    tags = request.POST['tags']

    try:
        image_entity = Image(image_file=image)
        image_entity.full_clean()
        image_entity.save()
        image_entity.tags.add(*tags)
    except Exception as e:
        return JsonResponse({'text': str(e)}, status=500)
    return JsonResponse({'url': image_entity.image_file.url})


def get_images(request):
    '''
    Gets images.

    You have to provide POST like:

    {
        'tags': ['tag1', 'tag2']
    }
    or
    {
        'id': 1
    }

    Providing tags and id returns images like there is no id provided.
    '''
    try:
        images = []
        if 'tags' in request.POST and len(request.POST['tags']):
            images = Image.objects.filter(tags__name__in=request.POST.getlist('tags')).distinct()
        elif 'id' in request.POST and request.POST['id']:
            images.append(Image.objects.get(pk=request.POST['id']))
    except Exception as e:
        return JsonResponse({'text': str(e)}, status=500)
    response = {'images': []}
    for image in images:
        response['images'].append(
            {
                'id': image.id,
                'tags': list(image.tags.names()),
                'url': image.image_file.url,
                'width': image.image_file.width,
                'height': image.image_file.height,
            }
        )
    return JsonResponse(response)

@login_required()
def delete_image(request):
    '''
    Deletes image with given id

    POST example
    ============

    {
        'id' : 2
    }

    Error with status 500 and details in text.

    Success with status 200 and {'status': 'OK'}
    '''
    try:
        image_id = request.POST['id']
        Image.objects.get(pk=image_id).delete()
    except Exception as e:
        return JsonResponse({'text': str(e)}, status=500)
    return JsonResponse({'status': 'OK'})
