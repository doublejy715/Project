from selenium import webdriver

url = "https://www.naver.co.kr/"

browser = webdriver.PhantomJS(executable_path='/usr/local/Caskroom/phantomjs/2.1.1/phantomjs-2.1.1-macosx/bin/phantomjs')

browser.implicitly_wait(3)
browser.get(url)
browser.save_screenshot("/Users/mac-jjy/Desktop/Project/Soul_news.png")
browser.quit()