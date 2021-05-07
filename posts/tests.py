from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()
        # Create a blogpost
        test_post = Post.objects.create(author=testuser1, title='Blog title', body='NOBODY talks about you...')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEquals(author, 'testuser1')
        self.assertEquals(title, 'Blog title')
        self.assertEquals(body, 'NOBODY talks about you...')
