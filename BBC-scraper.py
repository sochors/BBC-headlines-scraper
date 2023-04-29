from bs4 import BeautifulSoup
import requests

bbc_url = "https://www.bbc.com/news"
bbc_request = requests.get(bbc_url)

bbc_soup = BeautifulSoup(bbc_request.content, "html.parser")

bbc_main_headline = bbc_soup.find(class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor")
bbc_headlines = bbc_soup.find_all(class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")

print(f"MAIN STORY: {bbc_main_headline.text.upper()}")

for i, headline in enumerate(bbc_headlines[:10]):
    print(f"{i+1}: {headline.text.strip()}")