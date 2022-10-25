from playwright.sync_api import sync_playwright


url = 'https://the-internet.herokuapp.com/'
username = 'tomsmith'
password = 'SuperSecretPassword!'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    
    page.goto(url)
    page.locator('xpath=/html/body/div[2]/div/ul/li[21]/a').click()
    page.fill('input#username', username)
    page.fill('input#password', password)
    page.click('button[type=submit]')
    print('Login successful!') if page.is_visible(':has-text("You logged into a secure area!")') else print('Login failed!')
    
    page.close()
    browser.close()
    