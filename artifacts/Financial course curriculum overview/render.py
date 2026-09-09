import pathlib
from playwright.sync_api import sync_playwright

HTML = pathlib.Path("catalog.html").resolve()
OUT = pathlib.Path("Finances_Campaign_Catalog.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{HTML}", wait_until="networkidle")
    page.pdf(
        path=str(OUT),
        prefer_css_page_size=True,
        print_background=True,
    )
    browser.close()

size = OUT.stat().st_size // 1024
print(f"PDF rendered: {OUT} | {size} KB")
