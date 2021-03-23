import base64
import binascii
import os
import subprocess
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from selenium import webdriver

import parsepdf
from pdf2excel import Ui_MainWindow


class MainWindowView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setupUi(self)
        self.init_ui()

        self.screenshot_path = "./snapshot"

    def init_ui(self):
        self.show()

    def run_chrome(self):
        # "C:\Program Files\Google\Chrome\Application\chrome.exe"
        cmdstring = '"' + self.chromeUrl.text() + '" --remote-debugging-port=9222'
        subprocess.Popen(cmdstring, shell=True, stdout=subprocess.DEVNULL)

    def pdf2text(self):
        self.invoice_filenames, self.invoice_codes, self.invoice_nums, self.invoice_dates, self.invoice_valid_codes, self.invoice_tax_codes, self.invoice_totals = parsepdf.parse_pdf_2_excel()

    def start_check(self):
        if not os.path.exists(self.screenshot_path):
            os.mkdir(self.screenshot_path)

        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9222")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
        self.driver.maximize_window()

        self.data_index = 0
        self.invoice_check()

    def check_captcha(self):
        # 提交验证码
        self.driver.find_element_by_id('yzm').send_keys(self.captchaValue.text())
        time.sleep(1)
        self.driver.find_element_by_id('checkfp').click()
        time.sleep(2)

        try:
            popup = self.driver.find_element_by_css_selector('#popup_ok')
            print("验证码输入错误，请重输!")
            popup.click()

            self.driver.find_element_by_css_selector('#yzm_img').click()  # 刷新验证码
            self.driver.find_element_by_id('yzm').clear()
            time.sleep(1)

            self.yzm()

        except:
            time.sleep(2)
            self.screen_shot()

    def next(self):
        self.data_index += 1
        if self.data_index >= len(self.invoice_codes):
            self.data_index = len(self.invoice_codes) - 1
        self.invoice_check()

    def previous(self):
        self.data_index -= 1
        if self.data_index < 0:
            self.data_index = 0
        self.invoice_check()

    def screen_shot(self):
        self.driver.save_screenshot(os.path.join(self.screenshot_path,
                                                 self.invoice_codes[self.data_index] + "_" + self.invoice_nums[
                                                     self.data_index] + ".png"))

    def invoice_check(self):
        currentCheck = self.invoice_filenames[self.data_index] + "\n" + self.invoice_codes[self.data_index] + "\n" + \
                       self.invoice_nums[self.data_index]
        self.currentCheckLabel.setText(currentCheck)

        time.sleep(2)
        self.driver.get("https://inv-veri.chinatax.gov.cn/")
        try:  # 如果谷歌浏览器提示非私密链接
            self.driver.find_element_by_id('fpdm')
        except:
            self.driver.find_element_by_id("details-button").click()
            time.sleep(1)
            self.driver.find_element_by_id('proceed-link').click()
            time.sleep(2)
        self.driver.find_element_by_id('fpdm').send_keys(self.invoice_codes[self.data_index])
        self.driver.find_element_by_id('fphm').send_keys(self.invoice_nums[self.data_index])
        self.driver.find_element_by_id('kprq').send_keys(self.invoice_dates[self.data_index].strftime("%Y%m%d"))
        self.driver.find_element_by_id('kjje').send_keys(self.invoice_valid_codes[self.data_index])

        time.sleep(2)

        try:
            self.yzm()
            false = 0
        except Exception:
            print("Exception")
            false = 1
        except:
            print("base64图片获取有误，请等待刷新")
            false = 1

        while false:
            self.driver.refresh()
            self.driver.find_element_by_id('fpdm').send_keys(self.invoice_codes[self.data_index])
            self.driver.find_element_by_id('fphm').send_keys(self.invoice_nums[self.data_index])
            self.driver.find_element_by_id('kprq').send_keys(self.invoice_dates[self.data_index].strftime("%Y%m%d"))
            self.driver.find_element_by_id('kjje').send_keys(self.invoice_valid_codes[self.data_index])

            time.sleep(6)

            try:
                self.yzm()
                false = 0

            except binascii.Error as msg:
                try:
                    if self.driver.find_element_by_id('popup_message').text == "验证码请求次数过于频繁，请1分钟后再试！":
                        print("验证码请求次数过于频繁，1分钟后程序将自动跳转2")  # 起作用的是这个
                        popup = self.driver.find_element_by_css_selector('#popup_ok')
                        popup.click()
                        time.sleep(60)
                except:
                    print("base64图片获取有误，请等待刷新%s" % msg)
                false = 1

    def yzm(self):

        img_str = self.driver.find_element_by_id("yzm_img").get_attribute('src')
        img_str = img_str.split(",")[-1]  # 删除前面的 “data:image/jpeg;base64,”
        img_str = img_str.replace("%0A", '\n')  # 将"%0A"替换为换行符

        self.captchaImgLabel.setScaledContents(True)
        self.captchaImgLabel.setPixmap(QPixmap(QImage.fromData(base64.b64decode(img_str))))

        # 输出提示文字
        dic = {"黄色": "yellow", "红色": "red", "蓝色": "blue"}
        text = self.driver.find_element_by_id("yzminfo").text
        self.captchaTextLabel.setText(text)
        if text == "请输入验证码文字":
            self.captchaTextLabel.setStyleSheet("color:black")
        else:
            self.captchaTextLabel.setStyleSheet("color:" + dic[text[9:11]])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowView()
    window.show()
    sys.exit(app.exec_())
