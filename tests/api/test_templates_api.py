

import requests


def test_templates_api_returns_expected_count():
    """Verify that the templates API returns the expected number of templates."""

    response = requests.get("https://poster-app-flame.vercel.app/api/templates")

    assert response.status_code == 200


    templates = response.json()
    print(type(templates))

    assert len(templates) ==82





