"""
Looks like tesseract engine has to be installed for this
and its easily configured in linux than windows


😇 so atha pannni test pannunga vro
"""

import pytesseract as tsrct
import cv2 as cv
import json
obj = {
    "sender":"oNews",
    "news":[]
}
img = cv.imread("news.webp")
res = tsrct.image_to_string(img)
obj["news"].append(res)
with open("ores.json", "w") as f:
    json.dump(obj,f)