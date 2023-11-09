from pathlib import Path
# Desired Capabilities
desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "deviceName": "6d3d9bf3",
    "app": str(Path(__file__).parent) + r"/utilities/Test App/General-Store.apk"
}

# Command_executor url i.e. Appium server url
server_url = "http://localhost:4724/wd/hub"


# Tesseract path - Note: Install tesseract from https://sourceforge.net/projects/tesseract-ocr-alt/files/
tesseract_path = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
