import requests
from bs4 import BeautifulSoup
import pandas as pd


#function to scrape the url

def scrape_product(search_url):
  """
    Scrapes product URLs from the provided Amazon search page URL.

    Args:
        search_url (str): The URL of the Amazon search page to scrape.

    Returns:
        list: A list of product URLs extracted from the search page.
    """
  headers = {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
      }

  #sending a get request to fetch the webpage content
  response = requests.get(search_url, headers= headers)

  #checking weather the request was successful
  if response.status_code == 200:

    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content,"html.parser")

    #list to store extracted product urls
    product_links = []

    # Find all <a> tags that contain product links (filtered by class_)
    for link in soup.find_all("a",href = True, class_= "a-link-normal s-no-outline"):
      # Construct the full URL for the product by appending the relative href to the base URL
      full_url = "https://www.amazon.in/" + link["href"]
      product_links.append(full_url)
          
    return product_links
  # If the request was unsuccessful, print an error message
  else:
    print("failed to fetch data from amazon.status code: {response.status_code}")
    return[]

# function to scrape the url for a product
def main():
  """
    Main function that orchestrates the scraping of multiple product pages and saves the URLs to a CSV file.
    
    - Loops through multiple pages of search results.
    - Scrapes product URLs from each page.
    - Saves all scraped product URLs to a CSV file.

  """
  # Base URL for the search results (e.g., for wireless headphones)
  base_url = "https://www.amazon.in/s?k=wireless+headphones&crid=22A0OJAZ43XVK&sprefix=wireless+headphones%2Caps%2C220&ref=nb_sb_noss_2"
  
  # List to store all the product URLs
  all_urls = []

  # Loop through the first two pages (you can adjust the range as needed)
  for page in range(1,3):

    #adding pagination parameter
    paginated_url = f"{base_url}&page = {page}"

    print(f"Scraping page{page}...")  # to get notified that the page has been scraped

    # Scrape product URLs from the current page
    product_urls = scrape_product(paginated_url)

    # Add the scraped URLs to the all_urls list
    all_urls.extend(product_urls)

  # Create a DataFrame from the list of URLs
  df = pd.DataFrame(all_urls,columns = ["Product URL"])

  # Save the DataFrame to a CSV file
  df.to_csv("amazon_product_urls.csv",index = False)
  print("Scrapping completed")


# Run the main function if this script is executed
if __name__=="__main__":
  main()



