from appium.webdriver import Remote
from appium.webdriver.appium_service import AppiumService
from appium.options.common.base import AppiumOptions


class AndroidDevice:
    def __init__(self):
        self.server = AppiumService()

        self.server_args = ["-p", "4723", "-pa", "/wd/hub"]
        self.driver_options = AppiumOptions().load_capabilities(
            {
                "platformName": "Android",
                "automationName": "UiAutomator2",
                "platformVersion": "11.0",
                "deviceName": "AndroidEmulator",
                "appPackage": "com.android.settings",
                "appActivity": ".Settings",
                "language": "en",
                "locale": "US",
            }
        )

    def __enter__(self):
        self.server.start(args=self.server_args)
        self.driver = Remote(
            "http://localhost:4723/wd/hub", options=self.driver_options
        )
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        self.server.stop()
