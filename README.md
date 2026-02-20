## -Profile Manager-

Profile Manager is a small but powerful automation tool that stores website login profiles and automatically logs in using Selenium.  
It helps you avoid typing usernames and passwords repeatedly while learning real browser automation.

Think of it as your personal login assistant for testing and automation practice.

---

## -What This Project Does-

Instead of manually logging into websites every time, this tool:
- Saves login details in a config file
- Opens the browser automatically
- Fills in credentials
- Clicks the login button for you

It’s simple, perfect for learning Selenium automation, and it's practical but do you really think you need to use this???

---

## -Features-

- Store multiple website login profiles  
- Config based automation system  
- Clean and modular Python code  
- Command line interface  
- Easy to extend for new websites  

---

## -Requirements-

- Python 3.x  
- Selenium  
- Google Chrome installed  
- ChromeDriver installed  

---

## -Installation-

Clone the repository:

git clone https://github.com/vyanmadai7/ProfileManager.git  
cd ProfileManager  

Create and activate virtual environment:

python3 -m venv venv  
source venv/bin/activate  

## -Install Selenium:-

pip install selenium  

---

## -Usage-

Run the program:

python main.py github  

Here, `github` is the profile name from the profiles configuration file.

---

## -Adding a New Website Profile-

Open:

config/profiles_example.json  

Copy its structure and create your own file:

config/profiles.json  

Fill in:

- login_url – Website login page  
- username – Your username/email  
- password – Your password  
- username_xpath – XPath of username field  
- password_xpath – XPath of password field  
- login_button_xpath – XPath of login button  

Then run:

python main.py <profile_name>  

---

## -Important Security Note-

The real `profiles.json` file is ignored by Git to protect your private credentials.  
Only `profiles_example.json` is included so others can create their own safely.

---

## -Disclaimer-

This project is made for educational purposes and automation practice only.  
Do not use it for unauthorized access to any website.

---

## -License-

This project is licensed under the MIT License.  
You are free to use, modify, and share it — just keep the license included.
