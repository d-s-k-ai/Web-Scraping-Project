# Amazon Product Scraper and Details Extractor

## **Overview**
This project consists of two Python-based scripts for web scraping and automation on Amazon:
1. **Product URL Scraper**: Extracts product URLs from Amazon search result pages and saves them in a CSV file.
2. **Product Details Extractor**: Retrieves product details (title, price, and reviews) from the URLs and simulates interactions like adding a product to the cart.

---

## **Features**
### **1. Product URL Scraper**
- Scrapes product URLs from Amazon search result pages.
- Handles multiple pages of search results using pagination.
- Saves extracted product URLs in a CSV file.

### **2. Product Details Extractor**
- Extracts product details (title, price, and review count) from provided URLs.
- Handles missing or unavailable product information gracefully.
- Simulates user interactions, such as adding a product to the cart.
- Saves extracted details in a CSV file.

---

## **Tools and Libraries Used**
- **`requests`**: Sends HTTP requests to fetch webpage content (used in URL scraper).
- **`BeautifulSoup`**: Parses and extracts HTML elements (used in URL scraper).
- **`pandas`**: Saves extracted data into structured CSV files.
- **`selenium`**: Automates browser interactions for extracting product details and simulating user actions.
- **`webdriver_manager`**: Simplifies WebDriver setup for Selenium.

---

## **How It Works**
### **1. Product URL Scraper**
1. **Input**: A base search URL for Amazon is provided.
2. **Scraping**: The script sends requests to Amazon's search result pages, parses the HTML content, and extracts product links.
3. **Pagination**: Loops through multiple pages to gather all available product URLs.
4. **Output**: Extracted URLs are saved in a CSV file named `amazon_product_urls.csv`.

### **2. Product Details Extractor**
1. **Input**: A CSV file containing product URLs (e.g., `amazon_product_urls.csv`).
2. **Extraction**: The script uses Selenium to load each product page and extract details (title, price, reviews).
3. **Interaction**: Simulates adding the first product to the cart.
4. **Output**: Extracted product details are saved in a CSV file named `amazon_product_details.csv`.

---

## **Usage Instructions**
### Prerequisites
- Python 3.7 or higher installed.
- Install required libraries by running:
  ```bash
  pip install requests beautifulsoup4 pandas selenium webdriver-manager
  ```

### Running the Scripts
#### **1. Product URL Scraper**
1. Clone this repository or copy the script.
2. Ensure the base search URL in the code matches your target query.
3. Run the script:
   ```bash
   python url_scraper.py
   ```
4. The extracted product URLs will be saved in `amazon_product_urls.csv`.

#### **2. Product Details Extractor**
1. Ensure `amazon_product_urls.csv` exists and contains product URLs.
2. Run the script:
   ```bash
   python details_extractor.py
   ```
3. The extracted product details will be saved in `amazon_product_details.csv`.

---

## **Challenges and Solutions**
### **1. URL Scraper**
1. **Anti-Scraping Measures**:
   - Amazon may block automated requests.
   - **Solution**: Added custom headers with a user-agent to mimic browser behavior.
2. **Inconsistent HTML Structure**:
   - Missing or variable elements in the HTML caused scraping errors.
   - **Solution**: Added checks to skip invalid entries and handle exceptions.
3. **Pagination Formatting Issues**:
   - Incorrect URL formatting for pagination resulted in failed requests.
   - **Solution**: Debugged and ensured the URL structure was correctly formatted.

### **2. Details Extractor**
1. **Dynamic Content Loading**:
   - Product details were not fully loaded when scraping.
   - **Solution**: Used Selenium's `WebDriverWait` to ensure elements were loaded before extraction.
2. **Missing Product Information**:
   - Some pages lacked price or reviews.
   - **Solution**: Added exception handling to assign default values (e.g., "N/A").

---

## **Suggestions for Improvement**
- Use **proxies** or **random delays** in the URL scraper to avoid detection by Amazon's anti-scraping mechanisms.
- Expand the details extractor to retrieve additional information like product descriptions or ratings.
- Implement multithreading or asynchronous requests for improved performance when scraping large datasets.
- Enhance error handling for network timeouts and unexpected webpage changes.

---
