from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for Kaufland app
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11.0",  # Adjust based on your emulator's version
    "deviceName": "Android Emulator",
    "appPackage": "com.kaufland.app",  # Replace with Kaufland's package name
    "appActivity": "com.kaufland.app.MainActivity",  # Replace with Kaufland's main activity
    "automationName": "UiAutomator2"
}

# Start the Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    # Example login automation for Kaufland
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.kaufland.app:id/username"))  # Replace with actual ID
    )
    password_field = driver.find_element(By.ID, "com.kaufland.app:id/password")  # Replace with actual ID
    login_button = driver.find_element(By.ID, "com.kaufland.app:id/login_button")  # Replace with actual ID

    username_field.send_keys("your_username")
    password_field.send_keys("your_password")
    login_button.click()

    # Example: Extract information
    info_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.kaufland.app:id/info"))  # Replace with actual ID
    )
    info_text = info_element.text

    # Save information to a file
    with open("info.txt", "w") as file:
        file.write(info_text)

finally:
    driver.quit()
