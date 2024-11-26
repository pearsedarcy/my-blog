from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post, Comment

class PostDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a post with updated fields
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            body='Test body',
            author=self.user,
            published=True  # Ensure the post is marked as published
            # 'published_date' field removed as per the updated model
        )
        # Create an approved comment
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='Approved comment',
            approved=True
        )

    def test_post_detail_with_valid_slug(self):
        url = reverse('post_detail', kwargs={'slug': self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_with_invalid_slug(self):
        url = reverse('post_detail', kwargs={'slug': 'invalid-slug'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_authenticated_user_can_post_comment(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('post_detail', kwargs={'slug': self.post.slug})
        response = self.client.post(url, {'body': 'New comment'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful post
        self.assertTrue(Comment.objects.filter(body='New comment').exists())

    def test_comments_displayed_to_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('post_detail', kwargs={'slug': self.post.slug})
        response = self.client.get(url)
        self.assertContains(response, 'Approved comment')

    def test_comments_displayed_to_anonymous_user(self):
        url = reverse('post_detail', kwargs={'slug': self.post.slug})
        response = self.client.get(url)
        self.assertContains(response, 'Approved comment')
