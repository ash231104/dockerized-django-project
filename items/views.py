from django.http import JsonResponse

def item_list(request):
    return JsonResponse({"message": "Hello from /items/"})
