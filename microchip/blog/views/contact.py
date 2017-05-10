from django.http import JsonResponse
from blog.models import Contact


def is_contact_filled(request):
    '''
    get this view, to check if contact info had been provided already
    '''
    count = Contact.objects.all().count()
    if count == 1:
        return JsonResponse({'filled': 'true'})
    elif count == 0:
        return JsonResponse({'filled': 'false'})
    else:
        return JsonResponse({'text': 'Table contact contains more that 1 contact row'}, status=500)


def edit_contact_info(request):
    '''
    Provide post like:
    {
        'phone': '34234232',
        'email': 'some@email.com',
        'address': 'someadress'
    }
    To change contact data
    '''
    if not Contact.objects.all().count() == 1:
        return JsonResponse({'text': 'There if more than 1 contact row, contact with administrator'}, status=500)
    try:
        phone = request.POST.get('phone', Contact.objects.all()[0].phone)
        email = request.POST.get('email', Contact.objects.all()[0].email)
        address = request.POST.get('address', Contact.objects.all()[0].address)

        contact = Contact.objects.all()[0]
        contact.phone = phone
        contact.email = email
        contact.address = address
        contact.full_clean()
        contact.save()

    except Exception as e:
        return JsonResponse({'text': str(e)})
    return JsonResponse({'status': 'OK'})

def create_contact(request):
    '''
    POST to this view, providing address, email and phone to create a contact
    '''
    if not Contact.objects.all().count() == 0:
        return JsonResponse({'text': 'You cant create contact if there is one already, use edit contact'}, status=500)
    try:
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']

        contact = Contact(phone=phone, email=email, address=address)
        contact.full_clean()
        contact.save()
    except Exception as e:
        return JsonResponse({'text': str(e)}, status=500)
    return JsonResponse({'status': 'OK'})


def get_contact_info(request):
    '''
    GET this view to get contact info
    '''
    try:
        contact = Contact.objects.all()[0]
    except:
        return JsonResponse({'text': 'There is no contact yet'}, status=500)
    return JsonResponse({'phone': contact.phone,
                         'email': contact.email,
                         'address': contact.address})
