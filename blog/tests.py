import os
from django.test import TestCase, Client
from django.urls import reverse
from .models import Post
from .forms import PostForm, CommentForm

class EnvironmentVariableTest(TestCase):
    def test_env_variable(self):
        # Replace 'MY_ENV_VARIABLE' with the name of your environment variable
        env_var = os.getenv('SECRET_KEY')
        self.assertIsNotNone(env_var, "Environment variable 'MY_ENV_VARIABLE' is not set")
        if env_var:
            print(f"Environment variable 'SECRET_KEY' is set to: {env_var}")
        else:
            print("Environment variable 'SECRET_KEY' not found")

class DebugEnvironmentVariableTest(TestCase):
    def test_debug_env_variable(self):
        env_var = os.getenv('DEBUG')
        self.assertIsNotNone(env_var, "Environment variable 'DEBUG' is not set")
        if env_var:
            print(f"Environment variable 'DEBUG' is set to: {env_var}")
        else:
            print("Environment variable 'DEBUG' not found")


class CloudinaryEnvironmentVariableTest(TestCase):
    def test_cloudinary_env_variable(self):
        env_var = os.getenv('CLOUDINARY_URL')
        self.assertIsNotNone(env_var, "Environment variable 'CLOUDINARY_URL' is not set")
        if env_var:
            print(f"Environment variable 'CLOUDINARY_URL' is set to: {env_var}")
        else:
            print("Environment variable 'CLOUDINARY_URL' not found")

class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form = CommentForm(data={
            'body': 'This is a valid comment.'
        })
        self.assertTrue(form.is_valid(), msg="Form should be valid when 'body' is provided.")

    def test_comment_form_invalid(self):
        form = CommentForm(data={
            'body': ''  # Empty body should be invalid
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid when 'body' is empty.")
        self.assertIn('body', form.errors, msg="Form errors should include 'body' when 'body' is empty.")
