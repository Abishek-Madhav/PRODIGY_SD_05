import csv
import requests
from bs4 import BeautifulSoup

def scrape_product_information(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find product information (replace these with actual HTML tags of the website)
        product_names = soup.find_all('h3')  # Update this with the appropriate HTML tag
        product_prices = soup.find_all('p', class_='price_color')  # Update this with the appropriate HTML tag
        product_ratings = soup.find_all('p', class_='star-rating')  # Update this with the appropriate HTML tag


        # Create a list to store the data
        data = []

        # Iterate through the found elements and extract information
        for name, price, rating in zip(product_names, product_prices, product_ratings):
            product_name = name.text.strip()
            product_price = price.text.strip()
            product_rating = rating.text.strip()

            # Append the data to the list
            data.append([product_name, product_price, product_rating])

        return data
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def save_to_csv(data, output_file='product_data.csv'):
    # Save the data to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Product Name', 'Price', 'Rating'])
        csv_writer.writerows(data)

if __name__ == "__main__":
    # Replace this URL with the actual URL of the e-commerce website you want to scrape
    e_commerce_url = 'http://books.toscrape.com'

    # Scrape product information
    scraped_data = scrape_product_information(e_commerce_url)

    if scraped_data:
        # Save the data to a CSV file
        save_to_csv(scraped_data)
        print("Data successfully scraped and saved to product_data.csv.")