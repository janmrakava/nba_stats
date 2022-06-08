# %% [markdown]
# # Web Scraper

# %% [markdown]
# ##### Install libraries before your work

# %% [markdown]
# %pip install beautifulsoup4
# %pip install lxml
# %pip install selenium==2.48.0
# %pip install pandas
# %pip install html5lib
# %pip install openpyxl
# %pip install numpy

# %% [markdown]
# ### Scraper of NBA statistics for 25 seasons

# %%
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

od = 1996
do = 97

writer = pd.ExcelWriter('excelFiles/stats.xlsx')

ListDo = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']

while do != 22:
    season = f"{od}-{do}"
    url = f"https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&Season={season}&SeasonType=Regular%20Season&PerMode=Totals"

    driver = webdriver.Chrome() 
    driver.get(url)
    
    try: 
        element = Select(WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select'))
        ))
    except ElementNotVisibleException:
        print("The selected element is not visible! Try it again.")
    except NoSuchElementException:
        print("The selected element was not found.")
    except:
        print("The script was killed by unexpected error.")
        raise

    element.select_by_visible_text('All')
    html = driver.page_source
    
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table')

    df = pd.read_html(str(table))[0]
    
    # replacing old team shortcuts with the new ones
    df['TEAM'] = df['TEAM'].replace(['NOH', 'NJN', 'NOK', 'CHH', 'VAN', 'SEA'], ['NOP', 'BKN', 'NOP', 'CHA','MEM', 'OKC'])
    
    df[['PLAYER', 'TEAM', 'AGE', 'GP', 'W', 'L', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 
        'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 
        'PF', 'FP', 'DD2', 'TD3', '+/-'
        ]].to_excel(writer, sheet_name=f"{season}", index=False)
    writer.save()
    
    # add seasons 00 - 09 into URL
    od += 1
    if isinstance(do, int):
        do += 1
    
    if od >= 1999 and od <= 2009:
        if ListDo:
            do = ListDo.pop(0)  
        else:
            do = 10
    driver.close()        
print("Scraping finished!")


