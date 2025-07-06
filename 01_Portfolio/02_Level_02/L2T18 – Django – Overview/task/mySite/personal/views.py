from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime

# Create your views here.

# Index


def index(request):
    """Renders the index html in teh browser.
    Args:
        request (_type_): _Http request containing all the request data.
    Returns:
        _type_: _Http response that is responsible for rendering the requested
        html page along with the date and title.
    """
    context = {
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'page_title': 'Home'
    }
    return render(request, 'personal/index.html', context)

# Resume


def resume(request):
    """Renders the index html in teh browser.
    Args:
        request (_type_): _Http request containing all the request data.
    Returns:
        _type_: _Http response that is responsible for rendering the requested
        html page along with the date and title.
    """
    context = {
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'page_title': 'Resume'
    }

    return render(request, 'personal/resume.html', context)


# Contact


def contact(request):
    """Renders the index html in teh browser.
    Args:
        request (_type_): _Http request containing all the request data.
    Returns:
        _type_: _Http response that is responsible for rendering the requested
        html page along with the date and title.
    """
    context = {
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'page_title': 'Home'
    }
    return render(request, 'personal/contact.html', context)
 