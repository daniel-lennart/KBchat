# tests/test_settings.py

import unittest
import importlib
from unittest.mock import patch
from src.config import settings
import os

class TestSettings(unittest.TestCase):

    # Setup and Teardown methods to ensure a consistent environment
    def setUp(self):
        self.original_env = dict(os.environ)
    
    def tearDown(self):
        os.environ.clear()
        os.environ.update(self.original_env)

    def test_environment_variables_loaded(self):
        # Here we're patching the environment to simulate the .env content
        with patch.dict(os.environ, {'EMBEDDING_MODEL_NAME': 'test-model'}):
            importlib.reload(settings)  # Reload the settings module
            self.assertEqual(settings.EMBEDDING_MODEL_NAME, 'test-model')

    def test_default_values(self):
        # Here we're patching the environment to simulate the absence of the .env content
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(settings.EMBEDDING_MODEL_NAME, 'sentence-transformers/all-mpnet-base-v2')  # Assuming this is the default value

if __name__ == '__main__':
    unittest.main()
