from django.urls import path
from .views import upload_log, process_analytics, get_summary

urlpatterns = [
    path("upload-log/", upload_log, name="upload_log"),
    path("process-analytics/", process_analytics, name="process_analytics"),
    path("run-kafka/", get_summary, name="run_kafka"),
]
