from datetime import datetime


def footer_contex(request):
    ctx = {
        'now': datetime.now(),
        'version': 'version 0.5'
        
    }
    return request, ctx