import os
import unittest


class TestTokensIsExists(unittest.TestCase):
    """Check is existing tokens"""
    def test_owm_token_is_exists(self):
        self.assertNotEqual(os.getenv('YOUR_OWN_TOKEN', ""), "")

    def test_telegram_bot_token_is_exists(self):
        self.assertNotEqual(os.getenv('YOUR_TELEGRAM_BOT_TOKEN', ""), "")


if __name__ == '__main__':
    unittest.main()
