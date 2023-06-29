import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert


@pytest.mark.usefixtures('setup')
class TestMain:
    @allure.feature('Тест банка')
    @allure.story('Тест главной страницы')
    @allure.title('Тест 1')
    def test1(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выводит текст'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div/label').text
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert element == 'Your Name :', 'Ошибка!'

    @allure.feature('Тест банка')
    @allure.story('Тест добавления пользователя')
    @allure.title('Тест 2')
    def test2(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Вводит данные'):
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input').send_keys('Yuri')
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input').send_keys('Boyka')
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input').send_keys('E537017')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()

    @allure.feature('Тест банка')
    @allure.story('Тест выбора пользователя')
    @allure.title('Тест 3')
    def test3(self):
        with allure.step('Открывает ссылку'):
            Alert(self.browser).accept()
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает пользователя'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div/select').send_keys('Harry Potter')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выводит текст'):
             element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/strong/span').text
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert element == 'Harry Potter', 'Ошибка!'


    @allure.feature('Тест банка')
    @allure.story('Тест добавления пользователя')
    @allure.title('Тест 4')
    def test4(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Вводит данные'):
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input').send_keys('Tony')
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input').send_keys('Monthanna')
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input').send_keys('E6547343')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()


    @allure.feature('Тест банка')
    @allure.story('Тест выбора пользователя')
    @allure.title('Тест 5')
    def test5(self):
        with allure.step('Открывает ссылку'):
            Alert(self.browser).accept()
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает пользователя'):
            element = self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select').send_keys('Harry Potter')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает Валюту'):
             self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/select').send_keys('Dollar')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
             self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()



    @allure.feature('Тест банка')
    @allure.story('Тест выбора пользователя')
    @allure.title('Тест 6')
    def test6(self):
        with allure.step('Открывает ссылку'):
            Alert(self.browser).accept()
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[3]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Вводит данные'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/form/div/div/input').send_keys('Harry')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выводит текст'):
          element = self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[4]/span[2]').text
        assert element == '1005', 'Ошибка!'


    @allure.feature('Тест банка')
    @allure.story('Тест выбора пользователя')
    @allure.title('Тест 7')
    def test7(self):
        with allure.step('Открывает ссылку'):
              self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
         self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[3]').click()
         allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Вводит данные'):
         self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/form/div/div/input').send_keys('Hermoine')
         allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выводит текст'):
          element = self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[4]').text
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert element == '1001 1002 1003', 'Ошибка!'

    @allure.feature('Тест банка')
    @allure.story('Вход пользователя')
    @allure.title('Тест 8')
    def test8(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает пользователя'):
            element = self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/form/div/select').send_keys('Hermoine Granger')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выводит текст'):
          element = self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/strong/span').text
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert element == 'Hermoine Granger', 'Ошибка!'

    @allure.feature('Тест банка')
    @allure.story('Просмотр транзакций')
    @allure.title('Тест 9')
    def test9(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[1]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Тест банка')
    @allure.story('Просмотр транзакций')
    @allure.title('Тест 10')
    def test10(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает пользователя'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select').send_keys('Hermoine Granger')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает Валюту'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/select').send_keys('Dollar')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()

    @allure.feature('Тест банка')
    @allure.story('Тест кнопки Home')
    @allure.title('Тест 11')
    def test11(self):
        with allure.step('Открывает ссылку'):
            Alert(self.browser).accept()
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/button[1]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выводит текст'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/strong').text
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert element == 'XYZ Bank', 'Ошибка!'

    @allure.feature('Тест банка')
    @allure.story('Тест добавления пользователя')
    @allure.title('Тест 12')
    def test12(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Вводит данные'):
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input').send_keys('Tyler')
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input').send_keys('Durden')
            self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input').send_keys('E7547452')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()

    @allure.feature('Тест банка')
    @allure.story('Просмотр транзакций')
    @allure.title('Тест 13')
    def test13(self):
        with allure.step('Открывает ссылку'):
            Alert(self.browser).accept()
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает пользователя'):
            element = self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select').send_keys('Albus Dumbledore')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Выбирает Валюту'):
            element = self.browser.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/select').send_keys('Pound')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()

    @allure.feature('Тест банка')
    @allure.story('Проверка сброса транзакций')
    @allure.title('Тест 14')
    def test14(self):
        with allure.step('Открывает ссылку'):
            Alert(self.browser).accept()
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Тест банка')
    @allure.story('Проверка кнопки назад')
    @allure.title('Тест 15')
    def test15(self):
        with allure.step('Открывает ссылку'):
            self.browser.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx')
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Нажимает кнопку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
