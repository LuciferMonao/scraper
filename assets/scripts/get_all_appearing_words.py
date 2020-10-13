import json;
import requests;
import sys;
from time import gmtime, strftime

def load (text_file_url, min_words=30):
    with open(text_file_url, "r") as f:
        texts = json.load(f);
    results = {};


    for link in texts:
        for text_part in texts[link]:
            text_part = text_part.translate("./,-&|<>\][()}{%$§\"*+#-'_:;");
            for word in text_part.split(" "):
                if not word.lower() in results:
                    results[word.lower()] = 1;
                else:
                    results[word.lower()] += 1;
    

    word_list = [];
    for word in results:
        if results[word] > min_words:
            word_list.append({"name": word, "amount": results[word]});
        
    def get_amount (element):
        return int(element.get("amount"));

    word_list.sort(key=get_amount);

    return word_list;