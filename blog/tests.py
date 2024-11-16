import os
from django.test import TestCase
from dotenv import load_dotenv

class EnvironmentVariableTest(TestCase):
    def setUp(self):
        load_dotenv()

    def test_env_variable(self):
        # Replace 'MY_ENV_VARIABLE' with the name of your environment variable
        env_var = os.getenv('SECRET_KEY')
        self.assertIsNotNone(env_var, "Environment variable 'MY_ENV_VARIABLE' is not set")
        if env_var:
            print(f"Environment variable 'SECRET_KEY' is set to: {env_var}")
        else:
            print("Environment variable 'SECRET_KEY' not found")

class DebugEnvironmentVariableTest(TestCase):
    def setUp(self):
        load_dotenv()

    def test_debug_env_variable(self):
        env_var = os.getenv('DEBUG')
        self.assertIsNotNone(env_var, "Environment variable 'DEBUG' is not set")
        self.assertIn(env_var.lower(), ['true', 'false'], "Environment variable 'DEBUG' should be 'True' or 'False'")
        if env_var:
            print(f"Environment variable 'DEBUG' is set to: {env_var}")
        else:
            print("Environment variable 'DEBUG' not found")
