from appium.webdriver.appium_service import AppiumService
import time

appium_service = AppiumService()

def start():
    print("Server Started ",appium_service.start(args=['--address', '127.0.0.1', '-p', '4444']))

def stop():
    print(appium_service.stop())

def status():
    print(appium_service.is_listening)
