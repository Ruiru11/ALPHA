from rest_framework.test import APITestCase, APIRequestFactory

from todoapp import views

class TestTodos(APITestCase):
    """
        Tests all endpoints involving todos
    """
    def setUp(self):
        """
            This is the setup method
        """
        self.factory = APIRequestFactory()
        self.view = views.TodoView.as_view()
        self.uri = '/todos/'

    def test_get_all_todos(self):
        """
            Test fetching all todo items
        """
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200
        )

    def test_get_one_specific(self):
        """
            Test fetching a specific todo item
        """
        request = self.factory.get(self.uri + '/1/')
        response = self.view(
            request
        )
        self.assertEqual(
            response.status_code, 200
        )