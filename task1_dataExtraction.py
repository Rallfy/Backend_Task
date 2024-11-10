from bs4 import BeautifulSoup
import requests
import json

url = "https://www.optosigma.com/eu_en/optics/lenses/spherical-lenses/plano-convex-spherical-lenses/n-bk7-plano-convex-lenses-ar-400-700nm-SLB-P-M.html"


page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') # parse the page html content

product_section = soup.find("div", class_="product-grid-container")
products = product_section.find_all("tr", class_="grouped-item")

# create a dictionary to store saved products
product_data = {}

# the extraction of the main details for every prod. 
for product in products:
    product_id = product.find("span", class_="sku-cell").text.strip()
    product_name = product.find("a", class_="link").text.strip()
    product_link = product.find("a", class_="link")["href"]
    product_price = product.find("span", class_="price").text.strip()

    # create another dictionary for the detailed specs
    details = {}
    details_section = product.find("td", class_="grouped-item-spec")
    
    specs = details_section.find_all("tr")
    for spec in specs:
        label = spec.find("th", class_="col label").text.strip()
        value = spec.find("td", class_="col data").text.strip()
        details[label] = value

    
    # add product information to the main product dictionary
    product_data[product_id] = {
        "name": product_name,
        "link": product_link,
        "price": product_price,
        "details": details
    }

# save extracted data in the json file
with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(product_data, file, indent=4, ensure_ascii=False)
    print("Product data saved!")








