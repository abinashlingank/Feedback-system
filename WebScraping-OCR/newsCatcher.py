from newscatcher import Newscatcher, describe_url
import json
import time

websites = ['nytimes.com', 'cronachediordinariorazzismo.org', 'libertaegiustizia.it']
obj = {
    "sender":"sNews",
    "news":[]
}
for website in websites:
    nyt = Newscatcher(website = website)
    results = nyt.get_news()
    print(website)
    count = 0
    articles = results['articles']
    for article in articles[:10]:   
        count+=1
        cont = str(count) + ". " + article["title"]  + "\n\t\t" + article["summary"]  + "\n\n"
        obj["news"].append(cont)
        print(cont)
        time.sleep(0.33)
with open("sres.json","w") as f:
    json.dump(obj, f)