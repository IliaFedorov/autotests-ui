from playwright.sync_api import Page, expect
from typing import Pattern
from tools.logger import get_logger

logger = get_logger("CHECK_URL")

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        logger.info(f"Checking current url: {expected_url.pattern}")
        expect(self.page).to_have_url(expected_url)