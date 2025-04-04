import requests
from bs4 import BeautifulSoup

url = "https://ir.dominos.com/news-releases/news-release-details/dominos-pizzar-announces-2015-financial-results"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
b1 = soup.find("div", class_="node__content")

if b1 is not None:
    content_div = b1.find("div", class_="xn-content")  
    if content_div is not None:
        paragraphs = content_div.find_all("p")

        keywords = [
            "same store sales",
            "global retail sales",
            "net store growth",
            "EPS",
            "earnings per share"
        ]

        important_points = []
        for p in paragraphs:
            text = p.get_text(strip=True)
            if any(keyword.lower() in text.lower() for keyword in keywords):
                important_points.append(text)

        print(" Important Financial Highlights (2015):\n")
        for i, point in enumerate(important_points, 1):
            print(f"{i}. {point}\n")
    else:
        print("Could not find the 'xn-content' div.")
else:
    print("Could not find 'node_content' div") 


import pandas as pd

df = pd.DataFrame(important_points, columns=["Financial Highlights"])
df.to_csv("dominos_2015_financials.csv", index=False)
