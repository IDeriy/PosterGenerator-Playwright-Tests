import re

from playwright.sync_api import expect


def test_select_celebration_category(page):
    """
    checks filter selection, URL, active state, text
    """

    page.goto("https://poster-app-flame.vercel.app/templates/")

    celebration_button = page.get_by_role("button", name="🎉 Celebration(11)", exact=True)
    celebration_button.click()

    expect(page).to_have_url("https://poster-app-flame.vercel.app/templates?category=celebration")
    expect(celebration_button).to_have_class(re.compile("bg-blue-600"))
    expect(page.get_by_text("11 templates in 🎉 Celebration")).to_be_visible()


def test_celebration_category_shows_11_templates(page):
    """
    checks the actual number of cards
    """

    page.goto("https://poster-app-flame.vercel.app/templates/")

    celebration_button = page.get_by_role("button", name="🎉 Celebration(11)", exact=True)
    celebration_button.click()

    expect(page).to_have_url("https://poster-app-flame.vercel.app/templates?category=celebration")

    cards = page.locator("button.group")
    expect(cards).to_have_count(11)


def test_open_template_after_filtering(page):
    page.goto("https://poster-app-flame.vercel.app/templates/")

    celebration_button = page.get_by_role("button", name="🎉 Celebration(11)")
    celebration_button.click()
    expect(page).to_have_url("https://poster-app-flame.vercel.app/templates?category=celebration")
    celebration_card = page.get_by_role("button", name="Celebration Tropical")
    celebration_card.click()
    expect(page).to_have_url("https://poster-app-flame.vercel.app/create?template=celebration-003")

    expected_text = page.get_by_role("heading", name="Create your poster")
    expect(expected_text).to_be_visible()
