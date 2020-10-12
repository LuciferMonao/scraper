import sys;
sys.path.append("assets/scripts");

import get_all_links;
import get_all_site_texts;

counter = 0;
while True:
    counter += 12;
    get_all_links.load("./assets/data/links.json", "Coronavirus", start=counter, stop=counter+12);

    get_all_site_texts.load("./assets/data/texts/", "./assets/data/links.json", "Coronavirus", max_iter=300)

