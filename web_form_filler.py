import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormFiller:
    def __init__(self, url, dc):
        self.url = url
        self.dc = dc
        self.driver = None

    def fill_form(self):
        # 启动浏览器并访问网页
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)

        # 等待页面加载
        time.sleep(5)

        # 获取网页内容并传递给BeautifulSoup
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 使用BeautifulSoup定位元素
        element1 = soup.find_all('p')
        string = str(element1)  # 转换为字符串类型
        pattern = re.compile(r'[\u4e00-\u9fa5]+')  # 匹配中文字符的正则表达式
        result = pattern.findall(string)  # 使用正则表达式匹配中文字符
        print('匹配到的文本信息：',result)

        # 遍历 result 列表，依次匹配字典中的内容
        matched_list = []  # 用于存储匹配成功的内容
        for item in result:
            for key in self.dc.keys():
                if key in item:
                    matched_list.append(str(self.dc[key]))
        print(matched_list)

        # 找到所有输入框
        input_boxs = self.driver.find_elements(By.TAG_NAME, "input")
        print('检索到的输入框信息：',input_boxs)

        # 遍历所有输入框并填写内容
        # for i in range(len(matched_list)):
        i = 0
        for input_box in input_boxs:
            input_box.send_keys(matched_list[i])
            i += 1
            if i == len(matched_list):
                break

        # 等待提交按钮可点击
        submit_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.submit a.fb_submitBtn")))

        # 点击提交按钮
        submit_button.click()

        # 关闭浏览器
        self.driver.quit()
