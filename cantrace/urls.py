
from django.urls import path

from .views import upload, analysis, TraceListView, TraceDetailView

app_name = 'cantrace'

urlpatterns = [
    path('', upload, name='upload'),
    path('analysis/', analysis, name='analysis'),
    path('trace/', TraceListView.as_view(), name='traceList'),
    path('trace/<int:pk>', TraceDetailView.as_view(), name='traceDetail'),

]