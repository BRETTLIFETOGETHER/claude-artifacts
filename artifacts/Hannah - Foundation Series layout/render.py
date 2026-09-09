import sys
from playwright.sync_api import sync_playwright

html_path = sys.argv[1]
pdf_path = sys.argv[2]

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    page = browser.new_page()
    page.goto(f"file://{html_path}")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(300)
    page.pdf(
        path=pdf_path,
        print_background=True,
        prefer_css_page_size=True,
        scale=1.0,
    )
    browser.close()
print("rendered:", pdf_path)
