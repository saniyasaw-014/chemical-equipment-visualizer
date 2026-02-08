from django.urls import path
from django.http import JsonResponse
from .views import UploadCSV, LatestSummary
from .views import UploadCSV, LatestSummary, UploadHistory

def test_api(request):
    return JsonResponse({"status": "API working"})

urlpatterns = [
    path('test/', test_api),
    path('upload/', UploadCSV.as_view()),
    path('summary/latest/', LatestSummary.as_view()),
    path('history/', UploadHistory.as_view()),
]
