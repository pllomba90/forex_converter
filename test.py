import unittest
import requests
from app import app, get_currencies, get_descriptions, convert_currencies, validate_inputs

class TestApp(unittest.TestCase):

    def test_validate_inputs(self):
        codes = ["USD", "EUR", "GBP"]
        self.assertTrue(validate_inputs("100", "USD", "EUR", codes))
        self.assertFalse(validate_inputs("100", "JPY", "EUR", codes))
        self.assertFalse(validate_inputs("abc", "USD", "EUR", codes))
        self.assertFalse(validate_inputs("100", "USD", "JPY", codes))

    def test_get_currencies(self):
        with app.test_client() as client:
            response = client.get('/get-currencies')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, list)
            self.assertIn('USD', response.json)
            self.assertIn('EUR', response.json)

    def test_get_descriptions(self):
        with app.test_client() as client:
            response = client.get('/get_descriptions')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, dict)
            self.assertIn('USD', response.json)
            self.assertEqual(response.json['USD'], 'United States Dollar')
            self.assertIn('EUR', response.json)
            self.assertEqual(response.json['EUR'], 'Euro')

    def test_convert_currencies(self):
        with app.test_client() as client:
            response = client.get('/convert-currencies?starting_currency=USD&amount=10&converting_currency=EUR')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'converted amount:', response.data)
            self.assertIn(b'8.32', response.data)
            self.assertIn(b'Euro', response.data)

    def test_convert_currencies_invalid_amount(self):
        with app.test_client() as client:
            response = client.get('/convert-currencies?starting_currency=USD&amount=invalid&converting_currency=EUR')
            self.assertEqual(response.status_code, 302)
            response = client.get('/convert-currencies?starting_currency=USD&amount=-10&converting_currency=EUR')
            self.assertEqual(response.status_code, 302)
