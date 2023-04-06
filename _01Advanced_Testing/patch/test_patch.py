from unittest import TestCase
from unittest.mock import patch
import patch_tutorial as PT


class TestPatchTutorial(TestCase):
    def test_get_user_input_human(self):
        responses = ('haroun', 'taha', '23', 'n')
        expected = "You are haroun taha, and you're 23 years old."

        with patch('builtins.input', side_effect=responses):
            self.assertEqual(PT.get_user_input(), expected)
