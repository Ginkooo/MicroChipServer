from django.http import JsonResponse
from blog.models import Image
import sys


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

    print(request.POST)
    image = request.POST['attachment']
    tags = request.POST['tags']

    try:
        image_entity = Image(image_file=image)
        image_entity.tags.add(*tags)
        image_entity.full_clean()
        image_entity.save()
    except Exception as e:
        return JsonResponse({'text': str(e)}, status=500)
    return JsonResponse({'url': image_entity.url})
