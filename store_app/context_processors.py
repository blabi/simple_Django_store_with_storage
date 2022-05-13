from datetime import datetime


def footer_contex(request):
    ctx = {
        'now': datetime.timezon().now(),
        'version': 'version 0.5'
        
    }
    return ctx