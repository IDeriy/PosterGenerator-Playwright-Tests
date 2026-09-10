import re
from playwright.sync_api import expect


def test_homepage_loads(page):
    page.goto("https://poster-app-flame.vercel.app")
    page.wait_for_url("https://poster-app-flame.vercel.app")

    print(page.title())
    assert page.title() == "Poster Generator"


def test_navigate_to_template(page):
    page.goto("https://poster-app-flame.vercel.app/")

    page.get_by_role("link", name="Get started").click()

    page.wait_for_url("**/templates")

    print("URL after click:", page.url)

    assert page.url.endswith("/templates")


def test_open_template_in_editor(page):
    page.goto("https://poster-app-flame.vercel.app/templates/")

    page.get_by_role("button", name="Beer Event").click()

    page.wait_for_url("**/create?template=community-*")

    assert "/create?template=community-" in page.url
    expect(page.get_by_text("Create your poster")).to_be_visible()


def test_invalid_project_id(page):
    page.goto("https://poster-app-flame.vercel.app/editor/local-invalid")

    assert "/editor/local-" in page.url
    expect(page.get_by_text("Loading project…")).to_be_hidden(timeout=10000)

    expect(page.get_by_text("Project not found in this browser")).to_be_visible(timeout=1000)


def test_back_to_homepage(page):
    page.goto("https://poster-app-flame.vercel.app/templates")

    locator = page.get_by_role("link", name="Back to home")
    locator.click()

    print("Visible:", locator.is_visible())
    print("Href:", locator.get_attribute("href"))

    page.wait_for_url("https://poster-app-flame.vercel.app/")

    assert page.url == "https://poster-app-flame.vercel.app/"
    expect(
        page.get_by_role("heading", name="Poster Generator")
    ).to_be_visible()


def test_back_to_templates_from_create_page(page):
    page.goto("https://poster-app-flame.vercel.app/create?template=community-28bbae90-252d-4649-aea0-4d36d1455fd6")
    locator = page.get_by_role("link", name="Back to templates")
    print("Visible:", locator.is_visible())
    print("Href:", locator.get_attribute("href"))

    locator.click()

    page.wait_for_url("**/templates")
    assert page.url.endswith("/templates")
    expect(
        page.get_by_role("heading", name="Choose a template")
    ).to_be_visible()
