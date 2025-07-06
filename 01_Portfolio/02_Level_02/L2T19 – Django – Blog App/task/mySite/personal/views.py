from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime

# Create your views here.

# Index


def index(request: HttpRequest) -> HttpResponse:
    """Renders the index html in the browser.
    Args:
        request (_type_): _HttpRequest containing all the request data.
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


def resume(request: HttpRequest) -> HttpResponse:
    """ Renders the resume html page in the browser.
    Args:
        request (HttpRequest):_The HttpRequest containing the request data.
    Returns:
        HttpResponse: Responds with the necessary HTML along with the date and
        time.
    """
    context = {
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'page_title': 'Resume'
    }
    return render(request, 'personal/resume.html', context)


# Contact


def contact(request: HttpRequest) -> HttpResponse:
    """ Renders the contact html page in the browser.
    Args:
        request (HttpRequest):_The HttpRequest containing the request data.
    Returns:
        HttpResponse: Responds with the necessary HTML along with the date and
        time.
    """
    context = {
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'page_title': 'Home'
    }
    return render(request, 'personal/contact.html', context)
