# Library for this project

 - [pandas](https://pandas.pydata.org/)  >>> Read and write data in dataframe format
 - [selenium](https://www.selenium.dev/) >>> Automate web browser
 - [pyinstaller](https://www.borntodev.com/2020/07/07/%E0%B9%81%E0%B8%9B%E0%B8%A5%E0%B8%87%E0%B9%84%E0%B8%9F%E0%B8%A5%E0%B9%8C-python-%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99-exe-%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B9%86/) >> for create the .exe file `pip install pyinstaller`

## Selenium update
[ReadThis](https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium)
- Using xpath:
    > element = find_element_by_xpath("element_xpath")

    Needs be replaced with:
    > element = driver.find_element(By.XPATH, "element_xpath")

```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
```

# pyinstaller
```pip
    pyinstaller --onefile --noconsole main.py
```