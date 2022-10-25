from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://www.saucedemo.com/')
    page.fill('input#user-name', 'standard_user')
    page.fill('input#password', 'secret_sauce')
    page.click('input[type=submit]')
    page.is_visible('#page_wrapper')
    html = page.inner_html('#page_wrapper')
    
    soup = BeautifulSoup(html, 'html.parser')
    items_list = soup.find_all('div', class_='inventory_item_name')
    prices_list = soup.find_all('div', class_='inventory_item_price')
    for index, item in enumerate(items_list):
        print(f'{item.text} costs {prices_list[index].text}.\n')
