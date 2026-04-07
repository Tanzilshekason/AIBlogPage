from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )

    def test_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_creation_requires_login(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'New',
            'content': 'Content'
        })
        self.assertEqual(response.status_code, 302) # Redirect to login

    def test_post_creation_logged_in(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('post_create'), {
            'title': 'New Logged In',
            'content': 'Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.first().title, 'New Logged In')
        
    def test_like_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('like_post', args=[self.post.pk]))
        self.assertEqual(self.post.likes.count(), 1)
