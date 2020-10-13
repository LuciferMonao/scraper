import json;
import requests;
import sys;
from time import gmtime, strftime

def load (text_file_url, search):
    with open(text_file_url, "r") as f:
        texts = json.load(f);
    results = {};
    for element in search:
        results[element] = 0;
    for link in texts:
        for text_part in texts[link]:
            for word in results:
                results[word] += str(text_part).count(word);
    
    return results;