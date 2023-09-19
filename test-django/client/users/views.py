import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, HttpRequest, HttpResponse, JsonResponse

storage = FileSystemStorage()

from .models import Downloads


# Create your views here.
@login_required()
def handshake(request: HttpRequest):
    if request.user.is_authenticated:
        return JsonResponse({'message': f'Hello, {request.user.username}!'})
    else:
        return JsonResponse({'error': 'You are not authenticated!'})

@login_required()  
def download(request: HttpRequest):
    path = settings.MEDIA_ROOT / 'test_download.txt'
    if os.path.exists(path):
        # with open(path, 'rb') as fh:
        Downloads.objects.create(user=request.user)
        return FileResponse(open(path, 'rb'), as_attachment=True, filename='test_download.txt')
        # response = HttpResponse(fh.read(), content_type="application/text")
        # response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
        # return response
        # return JsonResponse({'message': f'Hello, starting download for {request.user.username}!'})
    else:
        return JsonResponse({'error': 'File does not exist!'}, status=404)
