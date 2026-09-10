
from playwright.sync_api import expect


def test_generate_button_enabled_after_text_input(page):
    """Verify that the Generate poster button becomes enabled after entering text."""

    page.goto("https://poster-app-flame.vercel.app/create?template=community-28bbae90-252d-4649-aea0-4d36d1455fd6")

    textarea = page.get_by_label("Your content")
    generate_poster_button = page.get_by_role("button", name="Generate poster")

    expect(generate_poster_button).to_be_disabled()

    textarea.fill("SOME_TEXT")

    expect(generate_poster_button).to_be_enabled()


def test_generate_poster_after_text_input(page):
    """Verify that generating a poster redirects the user to the Editor page."""

    page.goto("https://poster-app-flame.vercel.app/create?template=community-28bbae90-252d-4649-aea0-4d36d1455fd6")

    textarea = page.get_by_label("Your content")
    generate_poster_button = page.get_by_role("button", name="Generate poster")
    textarea.fill("SOME_TEXT")

    expect(generate_poster_button).to_be_enabled()
    generate_poster_button.click()
    print("URL",page.url)

    page.wait_for_url("**/editor/local-*")
    expect(page.get_by_role("heading",name="Editor").to_be_visible())
