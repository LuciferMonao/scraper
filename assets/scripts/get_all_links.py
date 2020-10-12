import json;
import requests;
import sys;
from time import gmtime, strftime
from bs4 import BeautifulSoup;




def load (links_file_url, search, start=1, stop=30):
    def get_search_data (search = "Coronavirus", stop = 11, start = 1):
        links = [];
        for page in range(start, stop):
            url = "https://sz.de/news/page/" + str(page) + "?search=" + search;
            page_data = requests.get(url);
            soup = BeautifulSoup(page_data.text, features="lxml");

            keep = ["reise", "karriere", "wissen", "thema", "auto", "kultur", "panorama", "bildung", "politik"]

            for a in soup.find_all('a', class_="entrylist__link"):
                for element in keep:
                    if "https://www.sueddeutsche.de/" + element + "/" in a["href"] and len("https://www.sueddeutsche.de/" + element + "/") < len(a["href"]):
                        links.append(a["href"]);
            print(f"get_search_data: DID {page - start} / {stop - start}");
                    
        return(links);
    
        



    with open(links_file_url, "r") as f:
        links = json.load(f);


    done = 0;

    link_data = get_search_data(search=search, start=start, stop=stop);

    do_length = len(link_data)
    for element in link_data:
        links_amount_start = len(links);
        if not element in links:
            links.append({"link": element, "date": strftime("%Y%m%d%H%M%S", gmtime()), "search": search});
        if len(links) - links_amount_start > 0:
            print(f"add_to_link_list: DID {len(links) - links_amount_start}");
            print(f"add_to_link_list: DONE {done}/{do_length}");
        done += 1; 


    with open(links_file_url, "w") as f:
        json.dump(links, f);