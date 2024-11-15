import os
from django.test import TestCase

class EnvironmentVariableTest(TestCase):
    def test_env_variable(self):
        # Replace 'MY_ENV_VARIABLE' with the name of your environment variable
        env_var = os.getenv('SECRET_KEY')
        self.assertIsNotNone(env_var, "Environment variable 'MY_ENV_VARIABLE' is not set")
        if env_var:
            print(f"Environment variable 'SECRET_KEY' is set to: {env_var}")
        else:
            print("Environment variable 'SECRET_KEY' not found")
