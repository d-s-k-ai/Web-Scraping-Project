from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import re


# Function to extract product details (title, price, reviews) from a given product URL
def extract_product_details(driver,url):
    """
    Extracts the product title, price, and reviews from the Amazon product page.

    Args:
        driver (webdriver.Chrome): Selenium WebDriver instance to interact with the webpage.
        url (str): The URL of the product page to scrape details from.

    Returns:
        dict: A dictionary containing the product title, price, and review count.
    """
    driver.get(url)
    time.sleep(1)

    try:
         title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "productTitle"))).text
    except Exception as e:
        title = "N/A"
        print(f"Error extracting reviews: {e}")

    # Extract product price and remove non-numeric characters

    try:
        price_text = driver.find_element(By.CLASS_NAME,"a-price-whole").text
        price = float(re.sub(r'[^\d.]', '', price_text))
    except Exception as e:
        price = "N/A"
        print(f"Error extracting reviews: {e}")

    # Extract the number of reviews

    try:
        reviews_text = driver.find_element(By.CSS_SELECTOR,".a-size-base .a-color-base").text
        reviews = int(re.search(r'\d+', reviews_text).group())
    except Exception as e:
        reviews = "N/A"
        print(f"Error extracting reviews: {e}")

    # Return the extracted details as a dictionary

    return {"Title": title, "price": price, "Reviews": reviews}


# Function to simulate interacting with the product page (e.g., adding the product to the cart)
def simulate_interaction(driver, url):
    """
    Simulates adding a product to the shopping cart.

    Args:
        driver (webdriver.Chrome): Selenium WebDriver instance to interact with the webpage.
        url (str): The URL of the product page to simulate interaction on.

    """
    driver.get(url)
    
    try:
        # Wait for the "Add to Cart" button to become clickable and click it
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
            )
        add_to_cart_button.click()
        time.sleep(1)
        print("product added to cart successfully")

    except Exception as e:
        print("Could not product to the cart",e)

def main():
    """
    Main function that orchestrates the product details extraction and simulation of interactions.

    - Reads product URLs from a CSV file.
    - Extracts product details from each URL.
    - Saves the extracted details into a CSV file.
    - Simulates interaction on the first product URL.
    """
    try:
        # Read the product URLs from the CSV file
        df = pd.read_csv("amazon_product_urls.csv")
        if "Product_URL" not in df.columns:
            print("The file does not contain the required 'product_urls' column.")
            return

        product_urls = df["Product_URL"].tolist()
        if not product_urls:
            print("No product URLs found in the file.")
            return
    except FileNotFoundError:
        print("The file 'amazon_product_urls.csv' does not exist.")
        return
    
    
    #initialize selenium WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    #extract product details

    product_details= []
    for url in product_urls:
        print(f"processing: {url}")
        try:
            details = extract_product_details(driver,url)
            product_details.append(details)
        except Exception as e:
            print(f"Error processing {url}:{e}")


    #save product details to a csv file
    print(f"Extracted product details: {product_details}")
    details_df = pd.DataFrame(product_details)
    if not details_df.empty:
        details_df.to_csv("amazon_product_details.csv", index=False)
        print("Product details saved to 'amazon_product_details.csv'.")
    else:
        print("No product details were extracted.")

    #simulating interaction on the first product url
    if product_urls:
        print("Simulating interaction on first product")
        simulate_interaction(driver, product_urls[0])
    
    # Close the WebDriver instance
    driver.quit()

if __name__ == "__main__":
    main()