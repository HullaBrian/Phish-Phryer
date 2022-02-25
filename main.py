import requests
from bs4 import BeautifulSoup


from dotenv import load_dotenv
import os
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

URL = "https://projectstem.org/users/sign_in"
# URL = "https://www.coolmathgames.com/login"

domain = URL[URL.index("//")+2:URL[URL.index("//"):].index(".")+URL.index("//")]

if (domain + ".html") not in os.listdir():
    print(f"No record of {domain} found.\nRetrieving html...", end="")
    html = requests.get(URL)
    with open(f"{domain}.html", "w+") as file:
        file.writelines(html.text)
    print("Done!")

print(f"Reading html of {domain}...", end="")
with open(f"{domain}.html", "r") as file:
    html = file.read()
print("Done!")

print("Getting website...", end="")
soup = BeautifulSoup(html, features="html.parser")
soup.prettify()
print("Done!")

emailBoxTag = ""  # Store all tag data
passWordBoxTag = ""  # Store all tag data

foundEmail = False
foundPassword = False
print("Searching for inputs...", end="")
for label in soup.find_all("label"):
    if "email" in label.string.lower() or "username" in label.string.lower() or "userid" in label.string.lower().replace(" ", "") or "loginid" in label.string.lower().replace(" ", ""):
        if label.next_sibling.next_sibling is None:
            emailBoxTag = label.next_sibling
        else:
            emailBoxTag = label.next_sibling.next_sibling
        foundEmail = True
    if "password" in label.string.replace(" ", "").lower():
        if label.next_sibling is not None and label.next_sibling.name == "input":
            passWordBoxTag = label.next_sibling
        elif label.next_sibling.next_sibling.next_sibling.name is None:
            passWordBoxTag = label.parent.next_sibling.next_sibling
        elif label.next_sibling.next_sibling.next_sibling.name == "a":
            passWordBoxTag = label.next_sibling.next_sibling.next_sibling
        else:
            passWordBoxTag = label.next_sibling.next_sibling
        foundPassword = True


if foundEmail and foundPassword:
    print("Done!")
else:
    print("ERROR:")
    if not foundPassword:
        print("\tCould not find password input!")
        exit()
    if not foundEmail:
        print("\tCould not find email/username/id input!")
        exit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import XPATHer

driver = webdriver.Chrome()
driver.get(URL)

emailXPATH = XPATHer.extract(emailBoxTag)
passwordXPATH = XPATHer.extract(passWordBoxTag)

print("Entering data...", end="")
emailInput = driver.find_element(By.XPATH, emailXPATH)
emailInput.send_keys(username)
passwordInput = driver.find_element(By.XPATH, passwordXPATH)
passwordInput.send_keys(password)
print("Done!\nSubmitting data...", end="")
passwordInput.submit()
print("Done!")

time.sleep(20)
