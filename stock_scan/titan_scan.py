from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TITAN&illiquid=0&smeFlag=0&itpFlag=0')

s_date = browser.find_element_by_css_selector('#LastUpdatedDiv')
s_name = browser.find_element_by_css_selector('#companyName')
s_price = browser.find_element_by_css_selector('#lastPrice')
s_open = browser.find_element_by_css_selector('#open')
s_high = browser.find_element_by_css_selector('#dayHigh')
s_low = browser.find_element_by_css_selector('#dayLow')
s_close = browser.find_element_by_css_selector('#closePrice')
s_preclose = browser.find_element_by_css_selector('#previousClose')
s_yrhigh = browser.find_element_by_css_selector('#high52 > font')
s_yrlow = browser.find_element_by_css_selector('#low52 > font')
s_vwap = browser.find_element_by_css_selector('#vwap')
s_lowerband = browser.find_element_by_css_selector('#lowpriceBand')
s_upperband = browser.find_element_by_css_selector('#upperpriceBand')



date = s_date.text
name = s_name.text
price = s_price.text
open = s_open.text
high = s_high.text
low = s_low.text
close = s_close.text
preclose = s_preclose.text
yearhigh = s_yrhigh.text
yearlow = s_yrlow.text
vwap = s_vwap.text
lowerband = s_lowerband.text
upperband = s_upperband.text


print("             ")
print("Date : ",date)
print("             ")
print("Name     ::  ",name)
print("             ")
print("Price    ::  ",price)
print("Open     ::  ",open)
print("High     ::  ",high)
print("Low      ::  ",low)
print("Close    ::  ",close)
print("Preclose ::  ",preclose)
print("Vwap     ::  ",vwap)
print("             ")
print("Year high  ::  ",yearhigh)
print("Year low   ::  ",yearlow)
print("Lowerband  ::  ",lowerband)
print("Upperband  ::  ",upperband)
print("               ")

browser.close()

