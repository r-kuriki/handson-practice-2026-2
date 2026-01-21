# ...existing code...
import unittest

from checker import validate_email


class TestValidateEmail(unittest.TestCase):
    def test_valid_emails(self):
        valids = [
            "taro.sato@example.com",
            "hanako.tanaka@example.co.jp",
            "kenta.ito@example.net",
            "yusuke.yamamoto@example.com",
        ]
        for e in valids:
            with self.subTest(email=e):
                self.assertTrue(validate_email(e))

    def test_invalid_emails(self):
        invalids = [
            "jiro.suzuki_example.com",
            "一郎@test",
            "naomi.watanabe@",
            "",
            "noatsign.com",
            "a@b",
        ]
        for e in invalids:
            with self.subTest(email=e):
                self.assertFalse(validate_email(e))


if __name__ == "__main__":
    unittest.main()
# ...existing code...