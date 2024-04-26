import csv
import json
from datetime import datetime
import random
import secrets
import string
import subprocess
import time

from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from devices import AndroidDevice


def generate_email():
    adjectives = [
        "adorable",
        "adventurous",
        "aggressive",
        "agreeable",
        "alert",
        "alive",
        "amused",
        "angry",
        "annoyed",
        "annoying",
        "anxious",
        "arrogant",
        "ashamed",
        "attractive",
        "average",
    ]
    nouns = [
        "human",
        "dog",
        "way",
        "art",
        "world",
        "information",
        "map",
        "family",
        "government",
        "health",
    ]
    return f"{random.choice(adjectives)}_{random.choice(nouns)}@gmail.com"


def generate_phone():
    numbers = "".join([str(random.randint(1, 9)) for _ in range(7)])
    return "312" + numbers


def generate_first_name():
    options = [
        "James",
        "Robert",
        "John",
        "Michael",
        "David",
        "William",
        "Richard",
        "Joseph",
        "Thomas",
        "Christopher",
    ]
    return random.choice(options)


def generate_last_name():
    options = [
        "Smith",
        "Johnson",
        "Brown",
        "Jones",
        "Garcia",
        "Miler",
        "Davis",
        "Rodriguez",
        "Martinez",
    ]
    return random.choice(options)


def generate_password():
    symbols = string.ascii_letters + string.digits + string.punctuation
    return "".join([secrets.choice(symbols) for _ in range(10)])


def write_success_sign_up(state, city, zip_code):
    with open("results.csv", "a", encoding="utf-8", newline="") as file:
        today = datetime.now()

        writer = csv.writer(file)

        writer.writerow([str(today), state, city, zip_code])


def try_sign_up(device, wait, code):
    sign_up = wait.until(
        EC.element_to_be_clickable((By.ID, "com.doordash.driverapp:id/become_a_dasher"))
    )
    sign_up.click()

    postal_code = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText"))
    )
    postal_code.click()
    time.sleep(1)

    code = str(code).rjust(5, "0")
    postal_code.send_keys(code)

    time.sleep(5)
    city = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f'//android.view.View[contains(@text, "{code}")]',
            )
        )
    )
    city.click()
    time.sleep(5)

    next = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="Next"]'))
    )
    next.click()

    email = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText"))
    )
    email.send_keys(generate_email())

    next = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="Next"]'))
    )
    next.click()
    time.sleep(5)

    phone = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText"))
    )
    phone.send_keys(generate_phone())

    sign_up = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@text="Sign up"]')
        )
    )
    sign_up.click()
    time.sleep(20)

    edit_texts = device.find_elements(By.XPATH, "//android.widget.EditText")
    first_name = edit_texts[0]
    first_name.send_keys(generate_first_name())

    no_middle_name = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.CheckBox[@text="No middle name"]')
        )
    )
    no_middle_name.click()

    last_name = edit_texts[2]
    last_name.send_keys(generate_last_name())

    password_text = generate_password()

    password = edit_texts[3]
    password.send_keys(password_text)

    confirm_password = edit_texts[4]
    confirm_password.send_keys(password_text)

    next = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@text="Continue"]')
        )
    )
    next.click()

    vehicle_type = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '(//android.view.View[@text="Vehicle Type"])[2]')
        )
    )
    vehicle_type.click()

    car = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Car"]',
            )
        )
    )
    car.click()

    make = wait.until(
        EC.element_to_be_clickable((By.XPATH, '(//android.view.View[@text="Make"])[2]'))
    )
    make.click()

    bmw = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="BMW"]',
            )
        )
    )
    bmw.click()

    model = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '(//android.view.View[@text="Model"])[2]')
        )
    )
    model.click()

    i3 = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="i3"]',
            )
        )
    )
    i3.click()

    color = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '(//android.view.View[@text="Color"])[2]')
        )
    )
    color.click()

    white = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="White"]',
            )
        )
    )
    white.click()

    insurance = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.CheckBox"))
    )
    insurance.click()

    next = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@text="Continue"]')
        )
    )
    next.click()

    try:
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//android.widget.TextView[@text="Scan your driver\'s license"]',
                )
            )
        )
        return True
    except TimeoutException:
        return False


if __name__ == "__main__":
    with AndroidDevice(proxy=("us-pr.oxylabs.io", "10000")) as device:
        wait = Wait(device, 60)

        with open("cities.json") as file:
            cities = json.load(file)

        for obj in cities:
            if try_sign_up(device, wait, obj["zip_code"]):
                write_success_sign_up(obj["state"], obj["city"], obj["zip_code"])
            device.terminate_app("com.doordash.driverapp")
            subprocess.run(["adb", "shell", "pm", "clear", "com.doordash.driverapp"])
            device.activate_app("com.doordash.driverapp")
