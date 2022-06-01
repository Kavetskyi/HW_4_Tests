import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.class_test = Employee('Sara', 'Smith', 10)

    def test_email(self):
        self.assertEqual(self.class_test.email, 'Sara.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.class_test.fullname, 'Sara Smith')

    def test_apply_raise(self):
        self.class_test.apply_raise()
        self.assertEqual(self.class_test.pay, 10)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_requests):
        mock_requests.return_value.text = "data"
        self.assertEqual(self.class_test.monthly_schedule('june'), 'data')


if __name__ == '__main':
    unittest.main()
