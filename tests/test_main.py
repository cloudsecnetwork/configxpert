import unittest
from unittest.mock import patch
from io import StringIO
import argparse
from main import main

class TestMainFunction(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(f='data/firewall.conf', d='fortinet'))
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_function_fortinet(self, mock_stdout, mock_parse_args):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Security Check Results:", output)  # Modify this assertion to match your actual output

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(f='data/device_config.txt', d='cisco'))
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_function_cisco(self, mock_stdout, mock_parse_args):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Security Check Results:", output)  # Modify this assertion to match your actual output

if __name__ == '__main__':
    unittest.main()
