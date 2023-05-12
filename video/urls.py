from django.urls import path
from .views import FileCreateView, FileListView, HomePageView, FileDetailView , download

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('files/', FileListView.as_view(), name='files'),
    path('files/<pk>/', FileDetailView.as_view(), name='file_detail' ),
    path('upload/', FileCreateView.as_view(), name='file_create'),
    path('download/<int:file_id>/', download, name='download')
]
