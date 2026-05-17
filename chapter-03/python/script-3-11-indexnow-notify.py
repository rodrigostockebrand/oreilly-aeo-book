"""
Script 3.11 — IndexNow Notifier

Notifies IndexNow-supporting search and answer engines (Bing, Yandex, Seznam,
Naver, and partners) about content changes so they can re-crawl quickly.
Useful for AEO because faster re-indexing means fresh content reaches
retrieval-augmented answer engines sooner.

Setup:
    1. Generate an IndexNow key (any 8-128 char hex string)
    2. Publish it at https://<your-host>/<key>.txt with the key as the file body
    3. Replace INDEXNOW_KEY and SITE_HOST below
    4. Run: python script-3-11-indexnow-notify.py

Requires:
    pip install requests

Companion code for "Answer Engine Optimization" (O'Reilly) — Chapter 3.
"""

import requests

INDEXNOW_KEY = "a1b2c3d4e5f6a7b8"
SITE_HOST = "example.com"


def notify_indexnow(urls):
    """Notify IndexNow-supporting engines about content changes."""
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"https://{SITE_HOST}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    response = requests.post(
        "https://api.indexnow.org/indexnow",
        json=payload,
        headers={"Content-Type": "application/json"},
    )
    return response.status_code


# Example usage
updated_urls = [
    "https://example.com/guides/aeo-basics",
    "https://example.com/blog/new-llm-crawlers-2026",
]

status = notify_indexnow(updated_urls)
print(f"IndexNow response: {status}")
# 200 = success, 202 = accepted
