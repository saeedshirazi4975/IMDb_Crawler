from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
#import json

BASEDIR = Path(__file__).parent
driver_path = Path.joinpath(BASEDIR, 'driver/chromedriver')
results_path = Path.joinpath(BASEDIR, 'results/')


ch_opt = Options()
ch_opt.set_headless(headless=True)


def crawler(q):
    
    query = str(q)
    
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=ch_opt) #, chrome_options=ch_opt
    
    driver.get("https://www.imdb.com/")

    driver.find_element_by_css_selector("#nav-search-form > div.search-category-selector.sc-htoDjs.jAJuqP").click()
    driver.find_element_by_css_selector("#navbar-search-category-select-contents > ul > a:nth-child(2)").click()

    srch_input = driver.find_element_by_css_selector("#suggestion-search")
    srch_input.send_keys(q, Keys.RETURN)
    
    results = driver.find_elements_by_class_name("findResult")
    
    if len(results) == 0 :
        return f'There is no result for {query}'
    else:
        if len(results) > 5:
            results = results[0:5]


        links = []
        imgs = []
        titles = []
        storylines = []

        for result in results:
            links.append(result.find_elements_by_tag_name("a")[0].get_attribute("href"))
            titles.append(result.find_element_by_class_name("result_text").get_attribute('innerText'))

        for link in links:
            driver.get(link)

            try:
                imgs.append(driver.find_element_by_css_selector(".poster").find_element_by_tag_name("img").get_attribute("src"))
            except:
                imgs.append('')

            try:
                storylines.append(driver.find_element_by_css_selector("#titleStoryLine > div:nth-child(3) > p > span").get_attribute("innerText"))
            except:
                storylines.append('')

        driver.close()

        data = pd.DataFrame({
            'titles': titles,
            'links': links,
            'storylines': storylines,
            'imgs': imgs
        })

        return data


if __name__ == "__main__":
    q = input('Enter something to searsh :  ')
    rs = crawler(q)
    print(rs)
    fileName = f'{q}.json'
    filePath = Path.joinpath(results_path, fileName)
    rs.to_json(filePath)
    
