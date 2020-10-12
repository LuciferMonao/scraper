import json;
import requests;
import sys;
from time import gmtime, strftime
from bs4 import BeautifulSoup;


def load (texts_folder_url, links_file_url, search, max_iter=600):
    with open(links_file_url, "r") as f:
        links = json.load(f);

    def get_date (element):
        return int(element.get("date"));

    def save_data (data):
        with open(texts_folder_url + search + ".json", "r") as f:
            old_data = json.load(f);

        dump = {**old_data, **data}

        with open(texts_folder_url + search + ".json", "w") as f:
            json.dump(dump, f);

    links.sort(key=get_date);

    texts = {}
    done = 0;
    with open(texts_folder_url + search + ".json", "r") as f:
        old_data = json.load(f);
    links_done = list(old_data.keys());

    for element in links:
        done += 1;
        if done > max_iter:
            break;
        if element["search"] != search:
            done += -1;
            continue;
        if element["link"] in links_done:
            done += -1;
            continue;
        url = element["link"]
        page_data = requests.get(url);
        soup = BeautifulSoup(page_data.text, features="lxml");

        texts[element["link"]] = []

        for a in soup.find_all('p', class_="css-0"):
            texts[element["link"]].append(a.getText());
        
        print(f"loading_text_pages: DONE {done} / {max_iter}");
        save_data(texts);
        texts = {};
    
    


#load("../data/texts/", "../data/links.json", "Coronavirus");