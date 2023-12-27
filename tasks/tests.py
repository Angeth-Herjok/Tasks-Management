
# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task

class TaskModelTestCase(TestCase):
    def test_task_str_representation(self):
        task = Task(title='Reading')
        self.assertEqual(str(task), 'Reading')

    def test_task_defaults(self):
        task = Task(title='Reading')
        self.assertFalse(task.completed)
        self.assertEqual(task.description, '')

class TaskListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_task_list_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)

    def test_task_creation(self):
        data = {'title': 'Reading'}
        response = self.client.post(reverse('task-list'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)

class TaskDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title='Reading')

    def test_task_detail_view(self):
        response = self.client.get(reverse('task-detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_task_update(self):
        data = {'title': 'Task Updated'}
        response = self.client.put(reverse('task-detail', args=[self.task.pk]), data=data)
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Task Updated')

    def test_task_deletion(self):
        response = self.client.delete(reverse('task-detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
