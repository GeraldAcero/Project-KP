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

def DeactivateKP():
    pass