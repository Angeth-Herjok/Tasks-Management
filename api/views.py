# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from tasks.models import Task
from .serializers import TaskSerializer
from attachment.models import Attachment
from .serializers import AttachmentSerializer
from comments.models import Comment
from .serializers import CommentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = request.POST or request.body
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class TaskDetailView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        data = request.POST or request.body
        serializer = TaskSerializer(instance=task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=204)




# Attachment

@method_decorator(csrf_exempt, name='dispatch')
class AttachmentListView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        attachments = Attachment.objects.filter(task=task)
        serializer = AttachmentSerializer(attachments, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        data = request.POST or request.body
        serializer = AttachmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(task=task)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class AttachmentDetailView(View):
    def get(self, request, task_id, attachment_id):
        task = get_object_or_404(Task, pk=task_id)
        attachment = get_object_or_404(Attachment, pk=attachment_id, task=task)
        serializer = AttachmentSerializer(attachment)
        return JsonResponse(serializer.data)

    def put(self, request, task_id, attachment_id):
        task = get_object_or_404(Task, pk=task_id)
        attachment = get_object_or_404(Attachment, pk=attachment_id, task=task)
        data = request.POST or request.body
        serializer = AttachmentSerializer(instance=attachment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, task_id, attachment_id):
        task = get_object_or_404(Task, pk=task_id)
        attachment = get_object_or_404(Attachment, pk=attachment_id, task=task)
        attachment.delete()
        return JsonResponse({'message': 'Attachment deleted successfully'}, status=204)





# Comments


@method_decorator(csrf_exempt, name='dispatch')
class CommentListView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        comments = Comment.objects.filter(task=task)
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        data = request.POST or request.body
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(task=task)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class CommentDetailView(View):
    def get(self, request, task_id, comment_id):
        task = get_object_or_404(Task, pk=task_id)
        comment = get_object_or_404(Comment, pk=comment_id, task=task)
        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data)

    def put(self, request, task_id, comment_id):
        task = get_object_or_404(Task, pk=task_id)
        comment = get_object_or_404(Comment, pk=comment_id, task=task)
        data = request.POST or request.body
        serializer = CommentSerializer(instance=comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, task_id, comment_id):
        task = get_object_or_404(Task, pk=task_id)
        comment = get_object_or_404(Comment, pk=comment_id, task=task)
        comment.delete()
        return JsonResponse({'message': 'Comment deleted successfully'}, status=204)
