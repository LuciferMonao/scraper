import json;
import requests;
import sys;
from bs4 import BeautifulSoup;




def load (links_file_url, iter_count=0):
    def get_main_site_data (url = "https://sz.de"):
        page_data = requests.get(url);
        soup = BeautifulSoup(page_data.text, features="lxml");
        
        links = [];
        keep = ["reise", "karriere", "wissen", "thema", "auto", "kultur", "panorama", "bildung", "politik"]

        for a in soup.find_all('a', href=True):
            for element in keep:
                if "https://www.sueddeutsche.de/" + element + "/" in a["href"] and len("https://www.sueddeutsche.de/" + element + "/") < len(a["href"]):
                    links.append(a["href"]);
            
        return(links);
        



    with open(links_file_url, "r") as f:
        links = json.load(f);


    do_length = len(get_main_site_data());
    done = 0;

    link_data = get_main_site_data();

    for i in range(0, iter_count):
        for element in link_data:
            links_amount_start = len(links);
            if not element in links:
                links.append(element);
                for element in get_main_site_data(url=element):
                    if not element in links:
                        links.append(element);
            print(f"DID: {len(links) - links_amount_start}")
            
            done += 1;
            print(f"{done}/{do_length}")
        link_data = links;






    with open(links_file_url, "w") as f:
        json.dump(links, f);