from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title='Test Post', body='Test body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.body)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'New Post',
            'body': 'New post body',
        })
        self.assertEqual(response.status_code, 302)  # redirect after success
        self.assertEqual(Post.objects.last().title, 'New Post')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post.pk]), {
            'title': 'Updated Title',
            'body': 'Updated body',
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
# Create your tests here.
