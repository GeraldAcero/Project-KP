from selenium import webdriver
import time

edge_driver_path = "EDGE PATH"

username = "USER"
password = "PASS"

def ActivateKP():
    
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("ignore-certificate-errors")

    capabilities = {
        'acceptInsecureCerts': True
    }

    driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options, capabilities=capabilities)

    driver.get("https://192.168.1.1/html/login_pldt.html")

    username_input = driver.find_element_by_id("user_name")
    username_input.send_keys(username)


    password_input = driver.find_element_by_id("loginpp")
    password_input.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element_by_id("login_btn")
    login_button.click()
    time.sleep(5)

    driver.get("https://192.168.1.1/html/firewall_enable_inter.html")

    radio_button = driver.find_element_by_id("firewall_medium")
    radio_button.click()

    time.sleep(1)

def DeactivateKP():
    pass