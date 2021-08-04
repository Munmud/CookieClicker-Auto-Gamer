from selenium import webdriver
import time


chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get('https://orteil.dashnet.org/cookieclicker')  # version 2.031

time.sleep(5)


def upgrade_Click():
    """Click upgraded element if available"""
    try:
        available_upgrades = driver.find_elements_by_css_selector(
            '#upgrades .crate.upgrade.enabled')
        for upgrade_button in available_upgrades:
            try:
                upgrade_button.click()
                break
            except:
                print("No application button, upgrade_Click skipped.")
    except:
        print('upgrade_Click List view not found')


def buy_cookie_generator():
    """Buy cookie generator if building cnt <20"""
    try:
        available_buildings = driver.find_elements_by_css_selector(
            '#products .product.unlocked.enabled')
        available_buildings.reverse()
        for buy_button in available_buildings:

            price = None
            price_text = buy_button.find_element_by_xpath(
                ".//*[contains(@class, 'owned')]").text
            price_string = str(price_text)
            if (price_string == ''):
                price = 0
            price = int(price)
            if(price == 20):
                continue

            try:
                buy_button.click()
                break
            except:
                print("No application button, cookie_generator skipped.")
    except:
        print('cookie_generator List view not found')


def notification_close():
    notifications = driver.find_elements_by_css_selector('#notes .close')
    for close_button in notifications:
        try:
            close_button.click()
            break
        except:
            print("Cannot close notification, skipped")


cookie = driver.find_element_by_id('bigCookie')
time_now = time.time() + 2

while True:
    try:
        cookie.click()
        if (time.time() > time_now):
            upgrade_Click()
            buy_cookie_generator()
            notification_close()
            time_now = time.time()+10
    except:
        print("No application button, cookie button skipped.")


# driver.quit()

# Mi4wMzF8fDE2MjgwMDc3OTY2NzM7MTYyODAwNzc5NjY3MzsxNjI4MDU0NzI0OTczO0hhcHB5IExpdHRsZSBNdWZmaW47cG9yd218MTExMTExMDExMDAxMDAxMDAxMDEwfDIwOTU5NTg0OC4yMTUxNTkyNzsxNzU4MzA3NDI2Ny4yMTMyNzs3MDI5MzQ7MDs1MzU2MzUzMDUwLjIwNTc1NDs0NDswOzA7MDswOzA7MDswOzA7MDswOzA7MDswOzA7MDswOzswOzA7MDswOzA7MDswOy0xOy0xOy0xOy0xOy0xOzA7MDswOzA7NTA7MDswOzA7MDsxNjI4MDE2Mzg0NjIxOzA7MDs7NDE7MDswOzIwMDA5MzEuOTI4NjA4NTQ2O3wxMjAsMTIwLDE5NjAwNzkwNjEsMCwsMCwxMjA7MTA2LDEwNiwzNTYwMDEwNzEsMCwsMCwxMDY7ODksODksMzQxNDcyMzYzLDAsLDAsODk7NzIsNzIsNjYyMjQyNjI0LDAsLDAsNzI7NTYsNTYsMjA1NDExMTM1OSwwLCwwLDU2OzM5LDM5LDM4ODE5ODA5NDcsMCwsMCwzOTsyMSwyMSwyODQ2OTk4OTAwLDAsLDAsMjE7MiwyLDEyMzgzNDg3OCwwLCwwLDI7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwO3wxMTExMTExMTExMTEwMDExMTExMTExMTExMTExMTExMTExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTAxMTExMTExMTExMTExMTEwMTAxMDAwMTExMTEwMTAwMDAwMDAwMDAwMDAwMDEwMTAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMTAwMDAwMDExMTAwMDAwMDAwMDEwMDAwMDAwMDAwMDExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTB8MTExMTExMDAwMDAwMDAwMDExMTExMTAwMDAwMDAwMTExMTExMTEwMDExMTExMDExMDExMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMDAwMDAwMDAwMDAwMDAwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTAwMDAxMDAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMHx8
