# Hello! Welcome to my first python project. 
This project use for class UltimatePython. The target of this project is to create an automatic input bot by reading the data in csv file (by pandas) and input to the input form in target website (by selenium). And prevent some error because of data in csv file such as input duplicate data or wrong input condition (ex. username too short ...) and show the result after finish the process (use pyautogui -> alert).

### Because of privacy of network condition so the link of input form in website in the code is in local server so you can't access to that network.

<!-- ![](img/Login_page.PNG) -->
<img src="img/Login_page.PNG" width="500">

---
## Library
1. selenium
2. pandas
3. pyautogui
4. os, sys, json

---
## How it work ?
1. First at the login page there are like to go to register page. Click it!

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="img/Login_page.PNG" width="250">

2. In register page there are some textbox to fill.

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="img/Register_Page.PNG" width="400">

3. Use `pandas` to read the csv file in folder "Data/inputData.csv" as dataframe. And use `selenium` to find element and fill the data.
