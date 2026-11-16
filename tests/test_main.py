import unittest
from main import clean_lines, clean_url

class UrlCleanerTests(unittest.TestCase):
    def test_removes_tracking_and_default_port(self):
        self.assertEqual(clean_url("HTTPS://Example.COM:443/a?utm_source=x&keep=1"), "https://example.com/a?keep=1")

    def test_deduplicates_after_normalization(self):
        values = clean_lines(["https://EXAMPLE.com/?utm_campaign=x", "https://example.com/"])
        self.assertEqual(values, ["https://example.com/"])

if __name__ == "__main__":
    unittest.main()
