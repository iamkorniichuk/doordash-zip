import time
import subprocess
import csv
from datetime import datetime

from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from generators import *


def run_main_flow(device, cities, output_csv):
    wait = Wait(device, 60)

    for obj in cities:
        if check_zip_code_availability(device, obj["zip_code"], wait):
            write_success_sign_up(
                obj["state"], obj["city"], obj["zip_code"], output_csv
            )
        device.terminate_app("com.doordash.driverapp")
        subprocess.run(["adb", "shell", "pm", "clear", "com.doordash.driverapp"])
        device.activate_app("com.doordash.driverapp")


def write_success_sign_up(output_csv, state, city, zip_code):
    with open(output_csv, "a", encoding="utf-8", newline="") as file:
        today = datetime.now()

        writer = csv.writer(file)

        writer.writerow([str(today), state, city, zip_code])


def check_zip_code_availability(device, zip_code, wait):
    sign_up = wait.until(
        EC.element_to_be_clickable((By.ID, "com.doordash.driverapp:id/become_a_dasher"))
    )
    sign_up.click()

    time.sleep(5)
    select_city(zip_code, wait)
    time.sleep(5)
    select_email(wait)
    time.sleep(5)
    select_phone(wait)
    time.sleep(30)
    select_personal_info(device, wait)
    time.sleep(5)
    select_car(device, wait)
    time.sleep(5)
    return is_available(wait)


def select_city(zip_code, wait):
    postal_code = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText"))
    )
    postal_code.clear()
    postal_code.click()

    time.sleep(2)
    zip_code = str(zip_code).rjust(5, "0")
    postal_code.send_keys(zip_code)

    time.sleep(5)
    city = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f'//android.view.View[contains(@text, "{zip_code}")]',
            )
        )
    )
    city.click()
    time.sleep(5)

    next = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="Next"]'))
    )
    next.click()


def select_email(wait):
    email = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText"))
    )
    email.send_keys(generate_email())

    next = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="Next"]'))
    )
    next.click()


def select_phone(wait):
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


def select_personal_info(device, wait):
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


def select_car(device, wait):
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

    is_birth_flow = device.find_element(
        By.XPATH, '//android.view.View[@text="Date of Birth"]'
    )
    if is_birth_flow:
        birt_car_select_flow(wait)
    else:
        default_car_select_flow(wait)


def birt_car_select_flow(wait):
    birth_date = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText"))
    )
    birth_date.send_keys()

    next = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@text="Continue"]')
        )
    )
    next.click()


def default_car_select_flow(wait):
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


def is_available(wait):
    try:
        wait.until(
            EC.any_of(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//android.widget.TextView[@text="Scan your driver\'s license"]',
                    )
                ),
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//android.widget.Button[@text="Download Android App"]',
                    )
                ),
            )
        )

        return True
    except TimeoutException:
        return False
