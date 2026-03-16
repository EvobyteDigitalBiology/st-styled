"""Playwright integration test for the tooltip custom component.

Planned checks in this single test case:
1. Verify `width` changes actual rendered width via bounding boxes.
2. Verify `background_color` changes computed background color.
3. Verify `shadow` changes computed box-shadow value.
4. Verify `show=False` results in hidden tooltip on initial render.
5. Verify dismiss action keeps tooltip hidden after clicking close.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect  # type: ignore

BASE_URL = "http://localhost:8512"


def test_tooltip_argument_semantics_and_dismiss_behavior(page: Page) -> None:
    """Validate tooltip arguments produce real visual/behavior differences."""
    page.goto(BASE_URL)
    page.wait_for_selector("text=Tooltip Component Integration Test", timeout=15000)
    page.wait_for_selector("#tooltip-test-basic", timeout=15000)
    page.wait_for_selector("#tooltip-test-variant", timeout=15000)
    page.wait_for_selector("#tooltip-test-hidden", state="attached", timeout=15000)

    baseline = page.locator("#tooltip-test-basic")
    variant = page.locator("#tooltip-test-variant")
    hidden = page.locator("#tooltip-test-hidden")

    baseline_box = baseline.bounding_box()
    variant_box = variant.bounding_box()

    assert baseline_box is not None, "Expected baseline tooltip bounding box."
    assert variant_box is not None, "Expected variant tooltip bounding box."
    assert variant_box["width"] > baseline_box["width"], (
        f"Expected variant width ({variant_box['width']}) to be greater than "
        f"baseline width ({baseline_box['width']})."
    )

    baseline_bg = baseline.evaluate("el => getComputedStyle(el).backgroundColor")
    variant_bg = variant.evaluate("el => getComputedStyle(el).backgroundColor")
    assert baseline_bg != variant_bg, (
        f"Expected background colors to differ, got baseline={baseline_bg} "
        f"variant={variant_bg}."
    )

    baseline_shadow = baseline.evaluate("el => getComputedStyle(el).boxShadow")
    variant_shadow = variant.evaluate("el => getComputedStyle(el).boxShadow")
    assert baseline_shadow != variant_shadow, (
        f"Expected box-shadow to differ, got baseline={baseline_shadow} "
        f"variant={variant_shadow}."
    )

    hidden_display = hidden.evaluate("el => getComputedStyle(el).display")
    assert (
        hidden_display == "none"
    ), f"Expected hidden tooltip display to be none, got {hidden_display}."

    close_button = page.locator("#close-test-basic")
    expect(close_button).to_be_visible()
    close_button.click()

    baseline_display_after_close = baseline.evaluate(
        "el => getComputedStyle(el).display"
    )
    assert baseline_display_after_close == "none", (
        "Expected baseline tooltip to be hidden after close click, "
        f"got display={baseline_display_after_close}."
    )
