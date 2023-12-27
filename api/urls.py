from django.urls import path
from .views import TaskListView, TaskDetailView, AttachmentListView, AttachmentDetailView, CommentListView, CommentDetailView

# from .import views
 

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:task_id>/attachments/', AttachmentListView.as_view(), name='attachment-list'),
    path('tasks/<int:task_id>/attachments/<int:attachment_id>/', AttachmentDetailView.as_view(), name='attachment-detail'),
    path('tasks/<int:task_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('tasks/<int:task_id>/comments/<int:comment_id>/', CommentDetailView.as_view(), name='comment-detail'),
]

