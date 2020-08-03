import os


class TestTokensIsExists:
    """Check is existing tokens"""

    def test_owm_token_is_exists(self):
        assert os.getenv('YOUR_OWM_TOKEN', "") != ""

    def test_telegram_bot_token_is_exists(self):
        assert os.getenv('YOUR_TELEGRAM_BOT_TOKEN', "") != ""
