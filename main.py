from selenium import webdriver
import time
import json


def load_config():
    with open('config.json') as f:
        return json.load(f)
    
def ActivateKP(username, password, edge_path):
    
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("ignore-certificate-errors")

    capabilities = {
        'acceptInsecureCerts': True
    }

    driver = webdriver.Edge(executable_path=edge_path, options=edge_options, capabilities=capabilities)

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

    apply_button = driver.find_element_by_xpath("//input[@type='button' and @value='Apply']")
    apply_button.click()

    time.sleep(1)
    driver.get("https://192.168.1.1/html/parental_control_inter.html")


    radio_button = driver.find_element_by_xpath("//input[@type='radio' and @name='parent_control_enable' and @value='1']")
    radio_button.click()
    time.sleep(1)
    apply_button = driver.find_element_by_xpath("//input[@type='button' and @value='Apply']")
    apply_button.click()
    driver.quit()

def DeactivateKP(username, password, edge_path):

    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("ignore-certificate-errors")

    capabilities = {
        'acceptInsecureCerts': True
    }

    driver = webdriver.Edge(executable_path=edge_path, options=edge_options, capabilities=capabilities)

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

    radio_button = driver.find_element_by_id("firewall_low")
    radio_button.click()
    time.sleep(1)

    apply_button = driver.find_element_by_xpath("//input[@type='button' and @value='Apply']")
    apply_button.click()

    time.sleep(1)
    driver.get("https://192.168.1.1/html/parental_control_inter.html")


    radio_button = driver.find_element_by_xpath("//input[@type='radio' and @name='parent_control_enable' and @value='0']")
    radio_button.click()
    time.sleep(1)
    apply_button = driver.find_element_by_xpath("//input[@type='button' and @value='Apply']")
    apply_button.click()
    driver.quit()


config = load_config()
DeactivateKP(config['username'], config['password'], config['edge_path'])