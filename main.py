import sys;
from pathlib import Path
sys.path.append("assets/scripts");

import get_all_links;
import get_all_site_texts;
import find_appearances_in_files;
import get_all_appearing_words;




search = str(sys.argv[1]) if len(sys.argv) >= 2 else "Coronavirus";

try: 
    to = int(sys.argv[3]) if len(sys.argv) >= 4 else 100;
    start = int(sys.argv[3]) if len(sys.argv) >= 4 else 0;
    count = int(sys.argv[3]) if len(sys.argv) >= 4 else 12;
except ValueError:
    print(find_appearances_in_files.load("./assets/data/texts/" + search + ".json", [str(sys.argv[2])]));
    print(find_appearances_in_files.load("./assets/data/texts/" + search + ".json", ["Grüne", "CDU", "SPD", "FDP", "AFD", "CSU"]));
    exit();

texts_path = Path("./assets/data/texts/" + search + ".json"); 
if not texts_path.exists(): 
    with open("./assets/data/texts/" + search + ".json", "w") as f: f.write("{}");

links_path = Path("./assets/data/links/" + search + ".json");
if not links_path.exists():
    with open("./assets/data/links/" + search + ".json", "w") as f: f.write("[]");

counter = start;

while True:
    counter += count;
    if 0 == get_all_links.load("./assets/data/links/", search, start=counter, stop=counter+count):
        break;

    get_all_site_texts.load("./assets/data/texts/", "./assets/data/links/", search, max_iter=300)

    if counter*count >= to:
        break;

for element in get_all_appearing_words.load("./assets/data/texts/" + search + ".json"):
    print(element["name"] + ": " + str(element["amount"]))