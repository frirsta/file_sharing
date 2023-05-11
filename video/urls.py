from django.urls import path
from .views import FileCreateView, FileListView, download

urlpatterns = [
    path('', FileListView.as_view(), name='files'),
    path('upload/', FileCreateView.as_view(), name='file_create'),
    path('download/<int:file_id>/', download, name='download')
]
