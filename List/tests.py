from django.http import HttpRequest
from django.test import TestCase
from django.http import HttpResponse
from List.views import home_page

class HomePageTest(TestCase):
    def test_home_page_about_todolist(self):
        request = HttpRequest
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>ToDoList</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

