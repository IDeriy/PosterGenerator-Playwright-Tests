from playwright.sync_api import expect
import pytest
import re

@pytest.mark.parametrize("language",["English", "עברית", "Русский"],ids=["English", "Hebrew", "Russian"])

def test_language_option_is_visible(page, language):
    """Verify that each supported language option is visible."""

    page.goto("https://poster-app-flame.vercel.app/create?template=community-28bbae90-252d-4649-aea0-4d36d1455fd6")

    language_button=page.get_by_role("button",name=language,exact=True)

    expect(language_button).to_be_visible()


@pytest.mark.parametrize("button_name, expected_language",
    [
        ("English", "English"),
        ("עברית", "Hebrew"),
        ("Русский", "Russian"),
    ],
    ids=["English", "Hebrew", "Russian"])

def test_change_poster_language_buttons(page,button_name,expected_language):
    """Verify that selecting a language updates its button state and language text."""

    page.goto("https://poster-app-flame.vercel.app/create?template=community-28bbae90-252d-4649-aea0-4d36d1455fd6")

    language_button=page.get_by_role("button",name=button_name,exact=True)
    language_button.click()

    expect(language_button).to_have_class(re.compile("border-blue-600"))
    expect(
        page.get_by_text(f"AI will write the poster in {expected_language}")
    ).to_be_visible()


@pytest.mark.parametrize(
    "button_name, placeholder_pattern",
    [
        ("English", r"[A-Za-z]"),
        ("עברית", r"[\u0590-\u05FF]"),
        ("Русский", r"[А-Яа-я]"),
    ],
    ids=["English", "Hebrew", "Russian"]
)

def test_change_poster_language_placeholder(page,button_name,placeholder_pattern):
    """Verify that the placeholder matches the selected language."""

    page.goto("https://poster-app-flame.vercel.app/create?template=community-28bbae90-252d-4649-aea0-4d36d1455fd6")

    language_button = page.get_by_role("button", name=button_name, exact=True)
    language_button.click()

    textarea = page.get_by_label("Your content")
    placeholder = textarea.get_attribute("placeholder")
    if button_name in ("English","Русский"):
        assert not re.search(r"[\u0590-\u05FF]",placeholder)


    expect(textarea).to_have_attribute(
        "placeholder",
        re.compile(placeholder_pattern)
    )









