import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import refactor

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.mozzartbet.com/sr#/live/sport/1'
driver.get(url)

driver.implicitly_wait(10)

matches = driver.find_elements(By.CLASS_NAME, 'live-match-v2')

match_data = []

for match in matches:
    match_info = {}

    match_id = match.get_attribute('id')
    match_info['id'] = match_id

    try:
        match_name = match.find_element(By.CLASS_NAME, 'match-summary-v2').text
        match_info['name'] = match_name
    except:
        match_info['name'] = None

    try:
        current_score = match.find_element(By.CLASS_NAME, 'part3').text
        match_info['current_score'] = current_score
    except:
        match_info['current_score'] = None

    odds = []
    try:
        odds_elements = match.find_elements(By.CLASS_NAME, 'prikaz-kvota-v1')
        for odds_element in odds_elements:
            odds.append(odds_element.text)
        match_info['odds'] = odds
    except:
        match_info['odds'] = None

    match_data.append(match_info)

driver.quit()

with open('match_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(match_data, json_file, ensure_ascii=False, indent=4)

print("Match data has been saved to match_data.json")

refactored_match_data = refactor.refactor_all_matches(match_data)

with open('refactored_match_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(refactored_match_data, json_file, ensure_ascii=False, indent=4)

print("Refactored match data has been saved to refactored_match_data.json")
