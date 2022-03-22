from email.message import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def send_email(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        recipient = request.POST.get('send_to')

        data = {
            'status': 'success',
            'message': f'Successfully sent email to {recipient}'
        }
        mail(username, recipient)
        return JsonResponse(data)

    return render(request, 'email_templates/home.html')


def mail(username: str, receiver: str):
    html_path = 'email_templates/welcome.html'
    context_data = {'username': username}
    email_html_template = get_template(html_path).render(context_data)
    email_msg = EmailMessage('Welcome',
                             email_html_template,
                             settings.APPLICATION_EMAIL,
                             [receiver, ],
                             reply_to=[settings.APPLICATION_EMAIL, ])
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)
