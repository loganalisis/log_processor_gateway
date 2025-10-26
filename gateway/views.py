import os, requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from dotenv import load_dotenv

load_dotenv()

LOG_SERVICE_URL = "http://log-processor-v2-shubham-roy021-dev.apps.rm3.7wse.p1.openshiftapps.com"
ANALYTICS_SERVICE_URL = "http://analytics-service-v2-shubham-roy021-dev.apps.rm3.7wse.p1.openshiftapps.com"

@api_view(["POST"])
def upload_log(request):
    """Forward file upload to Log Processor service"""
    file = request.FILES.get("file")
    if not file:
        return JsonResponse({"error": "No file uploaded"}, status=400)
    
    try:
        files = {'file': file}
        res = requests.post(f"{LOG_SERVICE_URL}/upload/", files=files, timeout=30)
        return JsonResponse(res.json(), status=res.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["POST"])
def process_analytics(request):
    """Forward analytics processing request to Analytics Service"""
    try:
        unique_key = request.data.get("unique_key")
        if not unique_key:
            return JsonResponse({"error": "unique_key is required"}, status=400)
        
        res = requests.post(f"{ANALYTICS_SERVICE_URL}/dashboard/", json={"unique_key": unique_key})
        return JsonResponse(res.json(), status=res.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["POST"])
def get_summary(request):
    """Fetch latest summary from analytics"""
    try:
        unique_key = request.data.get("unique_key")
        if not unique_key:
            return JsonResponse({"error": "unique_key is required"}, status=400)
        
        res = requests.post(f"{ANALYTICS_SERVICE_URL}/add/", json={"unique_key": unique_key})
        return JsonResponse(res.json(), status=res.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
