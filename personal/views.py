from django.shortcuts import render

def about_me(request):
    """
    View function to render the 'About Me' page.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: Renders the 'personal/about_me.html' template.
    """
    return render(request, 'personal/about_me.html')


def index(request):
    """
    View function to render the homepage.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: Renders the 'personal/index.html' template.
    """
    return render(request, 'personal/index.html')


def installing_bootstrap(request):
    """
    View function to render the 'Installing Bootstrap' tutorial page.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: Renders the 'personal/installing_bootstrap.html' template.
    """
    return render(request, 'personal/installing_bootstrap.html')
