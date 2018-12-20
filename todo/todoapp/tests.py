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
        self.view = views.CreateView.as_view()
        self.each_view = views.ToDoDetailsView.as_view()
        self.uri = '/todolist/'
        self.todo_data = {
            "name":"Create masterpiece",
            "description":"Gala tommorow need to work on something now",
            "done":False
        }

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
        response = self.each_view(
            request
        )
        self.assertEqual(
            response.status_code, 200
        )

    def test_post_todoitem(self):
        """
            Test creation of a todo item
        """
        request = self.factory.post(
            self.uri,
            self.todo_data
        )
        response = self.view(
            request
        )
        self.assertEqual(
            response.status_code, 201
        )

    def test_update_todoitem(self):
        """
            Test updating a todoitem
        """
        request = self.factory.put(
            self.uri + '1/',
            {
                "name":"Something",
                "description":"Another something",
                "done":"True"
            }
        )
        response = self.each_view(
            request
        )
        self.assertEqual(
            response.status_code, 
            201
        )