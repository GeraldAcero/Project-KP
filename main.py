from selenium import webdriver


edge_driver_path = ""
local_network_url = ""
username = ""
password = ""
def ActivateKP():
    
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("ignore-certificate-errors")

    capabilities = {
        'acceptInsecureCerts': True
    }

    driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options, capabilities=capabilities)

    driver.get(local_network_url)

    username_input = driver.find_element_by_id("user_name")
    username_input.send_keys(username)

    password_input = driver.find_element_by_id("loginpp")
    password_input.send_keys(password)

    login_button = driver.find_element_by_id("login_btn")
    login_button.click()

def DeactivateKP():
    pass