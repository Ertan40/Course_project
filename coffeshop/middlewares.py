from django.shortcuts import render


class HandleExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
    # handle server errors (status code >= 500),
    # while the custom 404 page will handle client-side errors (status code 404)
        if response.status_code >= 500:
            return render(request, '404.html')

        return response
