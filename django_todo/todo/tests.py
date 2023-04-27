from django.test import TestCase
import unittest
from .models import Todo

class TodoModelTestCase(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title='Test todo',
        )

    def test_todo_title(self):
        self.assertEqual(self.todo.title, 'Test todo')

