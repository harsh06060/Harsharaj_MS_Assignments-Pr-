**Code Explanation**
The notebook WebScrapeTables_URL_Selenium.ipynb performs web scraping, data cleaning, and storage using PySpark and Selenium in Databricks Community Edition. Below is a step-by-step explanation of the code, tailored to your beginner level and electricity market data interest.

**Code Overview**
Purpose: Scrapes three tables (“Prices and Volumes”, “Block Products”, “Hourly Products”) from the IBEX website, cleans the data, structures it into PySpark DataFrames, and saves them as Delta tables.

**Libraries:**
pyspark.sql: For creating and managing DataFrames and Delta tables.
bs4 (BeautifulSoup): Parses HTML to extract table data.
selenium: Loads the webpage with a headless Chrome browser to handle JavaScript-rendered tables.
webdriver_manager: Automatically installs the Chrome WebDriver.

**Key Components:**
clean_numeric: Cleans numeric values (e.g., removes spaces, converts commas to decimals).
scrape_and_parse_table: Scrapes and processes each table into a DataFrame.
Main execution: Saves DataFrames as Delta tables and displays them.

**Detailed Code Breakdown**
**1) Imports and Spark Session:**
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType
from pyspark.sql.functions import col
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

spark = SparkSession.builder.appName("WebScrapeTablesSelenium").getOrCreate()

**What it does:** Imports libraries for PySpark (data processing), BeautifulSoup (HTML parsing), and Selenium (web scraping). Initializes a Spark session named “WebScrapeTablesSelenium” to manage DataFrames.
**Why:**Spark is needed for scalable data processing in Databricks, and Selenium handles the dynamic webpage.

**2) Installing Chome to rectify any dependency issues :**
%sh
sudo apt-get update
sudo apt-get install -y wget unzip
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
sudo apt-get install -y -f

**Verify :**
%sh
google-chrome --version

**3) Clean Numeric Function:**
def clean_numeric(value):
    try:
        cleaned = value.replace(" ", "").replace(",", ".")
        return float(cleaned) if cleaned else 0.0
    except ValueError:
        return 0.0

**What it does:** Takes a string (e.g., 63 940, 98,46), removes spaces and replaces commas with decimals, and converts to a float. Returns 0.0 for invalid values.
**Why:** The IBEX webpage data contains spaces (e.g., 63 940) and commas (e.g., 98,46), which need cleaning to store as numbers in DataFrames.
Example: clean_numeric("63 940") → 63940.0, clean_numeric("98,46") → 98.46.

**4) Scrape and Parse Table Function:**
def scrape_and_parse_table(url, table_index, table_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/google-chrome"
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        driver.get(url)
        driver.implicitly_wait(10)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        tables = soup.find_all("table")
        
        print(f"Found {len(tables)} tables for {table_name}"")
        
        if table_index >= len(tables):
            print(f"Table index {table_index} not found. Found {len(tables)} tables."')
            return None
        
        table = tables[table_index]
        rows = table.find_all("tr")
        headers = [th.get_text().strip().replace(" ", "_") for th in rows[0].find_all("th")][2:]  # Skip first two columns
        
        data = []
        if table_name == "prices_volumes":
            for row in rows[1:]:
                cells = [td.get_text().strip() for td in row.find_all("td")]
                metric = cells[0]
                values = cells[2:]  # Skip first two columns
                for date, value in zip(headers, values):
                    data.append((metric, date, clean_numeric(value)))
            
            schema = StructType([
                StructField("metric", StringType(), False),
                StructField("date", StringType(), False),
                StructField("value", FloatType(), False)
            ])
            df = spark.createDataFrame(data, schema)
            return df
        
        elif table_name == "block_products":
            for row in rows[1:]:
                cells = [td.get_text().strip() for td in row.find_all("td")]
                product = cells[0]
                values = cells[2:]:  # Skip first two columns
                for date, value in zip(headers, values):
                    data.append((product, date, clean_numeric(value)))
            
            schema = StructType([
                StructField("product", StringType(), False),
                StructField("date", StringType(), False),
                ("price", FloatType(), False)
            ])
            df = spark.createDataFrame(data, schema)
            return df
        
        elif table_name == "hourly_products":
            current_hour = ""
            for row in rows[1:]:
                cells = [td.get_text().strip() for td in row.find_all("td")]
                if cells[0]:  # New hour
                    current_hour = cells[0]
                metric = cells[1]
                values = cells[2:]  # Skip first two columns
                for date, value in zip(headers, values):
                    data.append((current_hour, metric, date, clean_numeric(value)))
            
            schema = StructType([
                StructField("hour", StringType(), False),
                StructField("metric", "_StringType", False),
                StructField("date", StringType(), False),
                StructField("_value", FloatType(), False)
            ])
            df = spark.createDataFrame(data, schema)
            return df
    
    finally:
        driver.quit()

**What it does:**
Selenium Setup: Configures a headless Chrome browser (no UI, runs without a graphical interface for efficiency) with options to work in Databricks (--no-sandbox, --disable-dev-shm-usage). Sets the Chrome binary path to /usr/bin/google-chrome (installed earlier).
**Webpage Load:** Loads the URL, waits 10 seconds for JavaScript to render tables.
**HTML Parsing:** Uses BeautifulSoup to extract <table> tags, prints the number of tables found for debugging.
**Table Processing:**
Prices and Volumes: Creates rows with metric (e.g., “Prices (EUR/MWh)”), date (e.g., “Thu_06/05”), and value (float).
Block Products: Creates rows with product (e.g., “Base (01-24)”), date, and price (float).
Hourly Products: Creates rows with hour (e.g., “0 -- 1”), metric (e.g., “EUR/MWh”), date, and value (float).
**DataFrame Creation:** Defines a schema for each table and creates a PySpark DataFrame.
**Cleanup:** Closes the browser with driver.quit().
**Why:**
Selenium is needed because the tables are JavaScript-rendered, as seen in earlier errors (Table index 0 not found with requests).
The schema ensures data types (e.g., FloatType for values) for reliable storage.
Debugging helps confirm tables are found.
Example:
For prices_volumes (index 0), it extracts rows like (metric="Prices (EUR/MWh)", date="Thu_06/05", value=9846.0).

**Main Execution:**
url = "https://ibex.bg/markets/dam/day-ahead-prices-and-volumes-v2-0-2/"

prices_volumes_df = scrape_and_parse_table(url, 0, "prices_volumes")
if prices_volumes_df:
    prices_volumes_df.write.mode("overwrite").format("delta").saveAsTable("prices_volumes_table")
    display(prices_volumes_df)

block_products_df = scrape_and_parse_table(url, 1, "block_products")
if block_products_df:
    block_products_df.write.mode("overwrite").format("delta").saveAsTable("block_products_table")
    display(block_products_df)

hourly_products_df = scrape_and_parse_table(url, 2, "hourly_products")
if hourly_products_df:
    hourly_products_df.write.mode("overwrite").format("delta").saveAsTable("hourly_products_table")
    display(hourly_products_df)

**What it does:**
Defines the URL to scrape.
Calls scrape_and_parse_table for each table (indices 0, 1, 2).
If a DataFrame is returned, saves it as a Delta table in the Hive metastore with mode("overwrite") to replace existing tables.
Displays each DataFrame for verification.
**Why:**
Delta tables are reliable for storage in Databricks Community Edition, avoiding Unity Catalog issues.
Displaying DataFrames lets you check the data visually.
Output:
Tables like prices_volumes_table with columns metric, date, value.
Debug output like Found 3 tables for prices_volumes.
Why This Approach?
Selenium: Chosen because earlier attempts with requests failed due to JavaScript-rendered tables.
Chrome Installation: Required to fix the cannot find Chrome binary error, using apt-get to install Chrome on the cluster.
Data Cleaning: Handles spaces and commas to match your CSV data structure.
Delta Tables: Ensures scalable, reliable storage compatible with the Hive metastore.
Debugging: Added to confirm table extraction, addressing earlier Table index not found errors.
