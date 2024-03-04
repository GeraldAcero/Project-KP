from selenium import webdriver
import time
import json
import os


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

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_terminal()
    print("""
-------------------------------------------------------------------------------- 

  _____   _____    ____        _  ______  _____  _______            _  __ _____  
 |  __ \ |  __ \  / __ \      | ||  ____|/ ____||__   __|          | |/ /|  __ \ 
 | |__) || |__) || |  | |     | || |__  | |        | |     ______  | ' / | |__) |
 |  ___/ |  _  / | |  | | _   | ||  __| | |        | |    |______| |  <  |  ___/ 
 | |     | | \ \ | |__| || |__| || |____| |____    | |             | . \ | |     
 |_|     |_|  \_\ \____/  \____/ |______|\_____|   |_|             |_|\_\|_|     
                                                                                 
--------------------------------------------------------------------------------              
""")
    print("1. Activate")
    print("2. Deactivate")
    print("3. Exit")
    print("")

# config = load_config()
# DeactivateKP(config['username'], config['password'], config['edge_path'])
    
display_menu()