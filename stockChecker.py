from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
import winsound, time

driver = Chrome()
# time to wait for site to finish loading
driver.implicitly_wait(5)

# all urls
amazon = 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG?ref_=ast_sto_dp'
walmart = 'https://www.walmart.com/ip/PlayStation-5-Console/363472942'
target = 'https://www.target.com/p/playstation-5-console/-/A-81114595'
bestbuy = 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'
gamestop = 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New'

# bestbuy and gamestop don't seem to work, but i'll keep them in the loop
# for manual inspection
# could change the element it searches for to the id or class name

sites = [amazon, walmart, target, bestbuy, gamestop]

# list of xpaths for each site
carts = ['//*[@id="add-to-cart-button"]',
         '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button',
         '//*[@id="viewport"]/div[5]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/button',
         # best buy changes button code for each new session so this doesn't work
         '//*[@id="fulfillment-add-to-cart-button-6228635"]/div/div/div/button[remove_this_if_fixed]',
         # gamestop xpath remains the same for available and unavailable items, results in false positives
         '//*[@id="primary-details"]/div[4]/div[13]/div[3]/div/div[1]/button[remove_this_if_fixed]'
         ]

while True:
    for i in range(len(sites)):
        driver.get(sites[i])
        try:
            cart = driver.find_element_by_xpath(carts[i])
            if cart:
                for _ in range(5):
                    winsound.Beep(frequency=440, duration=5000)
                    time.sleep(2)
                break
        except NoSuchElementException:
            pass