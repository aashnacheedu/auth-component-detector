"""
Core logic for detecting authentication components in website HTML.

This module:
- Fetches raw HTML from a URL
- Parses the markup
- Identifies authentication-related elements such as
  password inputs and login forms
- Returns structured results
"""
import requests


def fetch_html(url: str) -> str:
    """
    Fetch raw HTML from the given URL.

    Raises:
        requests.HTTPError if the request fails
    """
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text

from bs4 import BeautifulSoup

def find_auth_components(html: str) -> list[str]:
    """
    Identify authentication-related HTML components.

    Detection strategy:
    - Locate <input type="password"> elements
    - Return the enclosing <form> if present
    """
    soup = BeautifulSoup(html, "html.parser")
    components = []

    password_inputs = soup.find_all("input", {"type": "password"})

    for pwd in password_inputs:
        form = pwd.find_parent("form")
        if form:
            components.append(str(form))
        else:
            components.append(str(pwd))

    return components

def analyze_url(url: str) -> dict:
    """
    Analyze a URL for authentication components and return structured results.
    """
    html = fetch_html(url)
    components = find_auth_components(html)

    return {
        "url": url,
        "authentication_found": bool(components),
        "components": components
    }
