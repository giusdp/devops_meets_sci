import unittest
from main import short_url_encode
import short_url


class TestShortUrlEncode(unittest.TestCase):
    def test_encode_integer(self):
        data = 12345
        encoded_data = short_url.encode_url(data)
        self.assertEqual(encoded_data, short_url_encode(data))

    def test_encode_string(self):
        data = "Hello, world!"
        encoded_data = short_url.encode_url(int.from_bytes(data.encode(), "big"))
        self.assertEqual(encoded_data, short_url_encode(data))

    def test_invalid_data_type(self):
        data = [1, 2, 3]
        with self.assertRaises(ValueError):
            short_url_encode(data)


if __name__ == "__main__":
    unittest.main()
