import requests
from bs4 import BeautifulSoup
def scrape_books(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            rating = book.find("p", class_=["star-rating"])["class"][1]  
            print(f"📖 Title: {title}")
            print(f"💰 Price: {price}")
            print(f"⭐ Rating: {rating}\n")
    else:
        print(f"Failed to retrieve page. Status Code: {response.status_code}")
url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
scrape_books(url)
