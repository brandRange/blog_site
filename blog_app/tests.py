from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com", password= "secret"
        )

        cls.post = Post.objects.create(
            title = "Some title you know",
            body = "Great post content",
            author = cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "Some title you know")
        self.assertEqual(self.post.body, "Great post content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Some title you know")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")