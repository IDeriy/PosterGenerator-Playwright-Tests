import requests


def test_templates_api_response_structure():
    """Verify templates API status, response structure, required fields, and field types."""

    response = requests.get(
        "https://poster-app-flame.vercel.app/api/templates"
    )

    # Verify that the API request is successful.
    assert response.status_code == 200

    templates = response.json()

    # Verify that the response body is a list of templates.
    assert isinstance(templates, list)

    # Verify that the API returns at least the expected minimum number of templates.
    assert len(templates) >= 82

    for template in templates:
        # Verify that every template is an object.
        assert isinstance(template, dict)

        # Verify required fields.
        assert "id" in template
        assert "name" in template
        assert "category" in template
        assert "layoutFamily" in template

        # Verify required field types.
        assert isinstance(template["id"], str)
        assert isinstance(template["name"], str)
        assert isinstance(template["category"], str)
        assert isinstance(template["layoutFamily"], str)