from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.drive_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(self.drive_path, options=self.options)


if __name__ == '__main__':
    chrome = ChromeAuto()