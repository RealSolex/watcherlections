from browser import driver
if __name__ == '__main__':
    driver = driver()
    driver.get_login()
    driver.enter_to_subject('Джава')
   #driver.close_driver(10)