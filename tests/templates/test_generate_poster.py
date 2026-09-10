import playwright.sync_api as sync
import re

from playwright.sync_api import expect


def test_generate_button_enabled_after_text_input(page):

    page.goto("https://poster-app-flame.vercel.app/create?template=community-28bbae90-252d-4649-aea0-4d36d1455fd6")

    textarea = page.get_by_label("Your content")
    generate_poster_button = page.get_by_role("button", name="Generate poster")

    expect(generate_poster_button).to_be_disabled()

    textarea.fill("SOME_TEXT")

    expect(generate_poster_button).to_be_enabled()
