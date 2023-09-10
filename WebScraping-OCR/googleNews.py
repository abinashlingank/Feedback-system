from pygooglenews import GoogleNews
import json
import time

gn = GoogleNews()
# top = gn.top_news()
top = gn.geo_headlines("India")

entries = top["entries"]
count = 0
obj = {
  "sender":"gNews",
  "news":[]
  }
for entry in entries:
  count = count + 1
  cont = str(count) + ". " + entry["title"] + "\n"
  obj["news"].append(cont)
  print(cont)
  time.sleep(0.05)
with open("gres.json","w") as f:
  json.dump(obj, f)