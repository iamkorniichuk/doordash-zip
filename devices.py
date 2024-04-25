from typing import Tuple

from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import Remote
from appium.webdriver.appium_service import AppiumService
from appium.options.common.base import AppiumOptions


class AndroidDevice:
    def __init__(self, proxy: Tuple[str, str] = None):
        self.server = AppiumService()

        self.proxy = proxy
        self.server_args = [
            "-p",
            "4723",
            "-pa",
            "/wd/hub",
        ]
        self.driver_options = AppiumOptions().load_capabilities(
            {
                "platformName": "Android",
                "automationName": "UiAutomator2",
                "platformVersion": "11.0",
                "deviceName": "MyAndroid30",
                "app": "doordash-dasher.apk",
                "language": "en",
                "locale": "US",
                "fullReset": True,
            }
        )

    def __enter__(self):
        self.server.start(args=self.server_args)
        self.driver = Remote(
            "http://localhost:4723/wd/hub", options=self.driver_options
        )
        if self.proxy:
            self.set_proxy(self.driver, self.proxy)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        self.server.stop()

    @classmethod
    def set_proxy(cls, driver, proxy):
        wait = Wait(driver, 20)
        driver.activate_app("com.android.settings")

        network = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[1]',
                )
            )
        )
        network.click()

        wifi = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]',
                )
            )
        )
        wifi.click()

        wifi_settings = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//android.widget.ImageView[@content-desc="Settings"]',
                )
            )
        )
        wifi_settings.click()

        edit = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//android.widget.TextView[@content-desc="Modify"]',
                )
            )
        )
        edit.click()

        try:
            advanced_options = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//android.view.View[@content-desc="Drop down list Advanced Options"]',
                    )
                )
            )
            advanced_options.click()
        except TimeoutException:
            pass
        else:
            proxy_dropdown = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//android.widget.Spinner[@resource-id="com.android.settings:id/proxy_settings"]',
                    )
                )
            )
            proxy_dropdown.click()

            manual = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Manual"]',
                    )
                )
            )
            manual.click()

            hostname = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//android.widget.EditText[@resource-id="com.android.settings:id/proxy_hostname"]',
                    )
                )
            )
            hostname.send_keys(proxy[0])

            port = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//android.widget.EditText[@resource-id="com.android.settings:id/proxy_port"]',
                    )
                )
            )
            port.send_keys(proxy[1])

            save = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//android.widget.Button[@resource-id="android:id/button1"]',
                    )
                )
            )
            save.click()
        finally:
            driver.terminate_app("com.android.settings")
