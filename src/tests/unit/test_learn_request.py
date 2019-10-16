from unittest import TestCase
from unittest.mock import patch
import src.learn_request


class TestGet(TestCase):

    def test_getparam(self):
        with patch('requests.get') as mocked_get:
            src.learn_request.get_param()
            mocked_get.assert_called_with('http://httpbin.org/get', params={'name': 'Ashish'})
