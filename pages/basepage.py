import os
from datetime import datetime
import imagehash
from PIL import Image, ImageFilter, ImageEnhance
import shutil
from pytesseract import pytesseract
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configfile


class BasePage:
    driver = ""

    def __init__(self, d):
        self.driver = d

    def _click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def _enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def _adb_input_text(self, text):
        import os
        os.system('adb shell input text "' + text + '"')

    def _press_keyevent(self, character):
        li = [[str(i) for i in range(10)], [i for i in range(7, 17)]]
        dict1 = dict(zip(li[0], li[1]))
        import string
        li = [list(string.ascii_uppercase[:]), [i for i in range(29, 55)]]
        dict2 = dict(zip(li[0], li[1]))
        dict1.update(dict2)
        dict1['*'] = 155

        if character == "?":
            self._adb_input_text('\\?')
        else:
            self.driver.press_keycode(dict1[character])

    def _clear_text(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
        element.sendKeys(Keys.CONTROL + "a")
        element.sendKeys(Keys.DELETE)

    def _get_element(self, locator):
        return self.driver.find_element(*locator)

    def _get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def _get_element_from_list(self, locator, text):
        if locator[0] == By.ID:
            return self.driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().resourceId("' + locator[
                    1] + '")).getChildByText(new UiSelector().className("android.widget.TextView"),"' + text + '")'
            )
        elif locator[0] == By.CLASS_NAME:
            return self.driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().className("' + locator[
                    1] + '")).getChildByText(new UiSelector().className("android.widget.TextView"),"' + text + '")'
            )

    def _get_text(self, locator):
        return self.driver.find_element(*locator).text

    def _get_value_from_textbox(self, locator):
        return self.driver.find_element(*locator).get_attribute("value")

    def _get_value_from_combobox(self, locator):
        element = self.driver.find_element(*locator)

    def _select_dropdown(self, locator, text):
        element = self.driver.find_element(*locator)

    def _wait_for_element(self, locator, condition, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        if condition == "visibility":
            return wait.until(EC.visibility_of_element_located(locator))
        elif condition == "clickable":
            return wait.until(EC.element_to_be_clickable(locator))
        elif condition == "presence":
            return wait.until(EC.presence_of_element_located(locator))
        elif condition == "invisibility":
            return wait.until(EC.invisibility_of_element_located(locator))
        elif condition == "staleelementreferenceexception":
            wait = WebDriverWait(self.driver, timeout, ignored_exceptions=[StaleElementReferenceException])
            return wait.until(EC.presence_of_element_located(locator))

    def _wait_for_elements(self, locator, condition, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        if condition == "visibility":
            return wait.until(EC.visibility_of_any_elements_located(locator))
        elif condition == "presence":
            return wait.until(EC.presence_of_all_elements_located(locator))

    # Boolean functions
    def _is_present(self, locator, time_out=5):
        try:
            self._wait_for_element(locator, "presence", time_out)
            return True
        except NoSuchElementException as err:
            return False
        except TimeoutException as err:
            return False

    def _wait_for_activity(self, activity_name, time_out=5):
        counter = 0
        while True:
            time.sleep(0.5)
            counter += 1
            if activity_name in self.driver.current_activity and counter <= time_out:
                break

    def _swipe_element_to_middle(self, element, timeduration=2800):
        rect = element.rect
        size = self.driver.get_window_size()
        winy = (size["height"] // 2)
        if rect["y"] > winy + 200:
            self.driver.swipe(rect['x'], rect['y'], rect['x'], winy, timeduration)

    def _take_element_screenshot(self, locator, path=None):
        if path is None:
            os.mkdir("temp")
            path = r"temp/" + datetime.now().strftime("%d_%m_%y_%H%M%S") + ".png"
        self.driver.find_element(*locator).screenshot(path)
        return path

    def _take_screenshot(self, path=None):
        if path is None:
            if not os.path.exists('temp'):
                os.makedirs("temp")
            path = r"temp/" + datetime.now().strftime("%d_%m_%y_%H%M%S") + ".jpg"
        self.driver.save_screenshot(path)
        return path

    def _image_comparison(self, image1_path, image2_path, cutoff=5):
        hash0 = imagehash.average_hash(Image.open(image1_path))
        hash1 = imagehash.average_hash(Image.open(image2_path))
        return hash0 - hash1 < cutoff

    def _flush_temp_directory(self):
        shutil.rmtree('temp', ignore_errors=True)

    def _get_text_by_tesseract(self, image_path):
        pytesseract.tesseract_cmd = configfile.tesseract_path
        im = Image.open(image_path)
        im = im.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(2)
        im = im.convert('1')
        im.save(image_path)
        text = pytesseract.image_to_string(Image.open(image_path))
        return text

    def _close_keyboard(self):
        if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()
