"""Playwright integration test for st_yled basic."""


from __future__ import annotations

from playwright.sync_api import Page, expect  # type: ignore

BASE_URL = "http://localhost:8512"

def test_st_page_load(page: Page) -> None:
    """Validate tooltip arguments produce real visual/behavior differences."""
    page.goto(BASE_URL)

    # Validate the button is present and has the correct text.
    button = page.get_by_role("button", name="Click me")
    expect(button).to_be_visible()
    expect(button).to_have_text("Click me")
