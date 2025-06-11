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
Imports and Spark Session:
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType
from pyspark.sql.functions import col
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

spark = SparkSession.builder.appName("WebScrapeTablesSelenium").getOrCreate()

**What it does: **
Imports libraries for PySpark (data processing), BeautifulSoup (HTML parsing), and Selenium (web scraping). Initializes a Spark session named “WebScrapeTablesSelenium” to manage DataFrames.
Why: Spark is needed for scalable data processing in Databricks, and Selenium handles the dynamic webpage.

**Clean Numeric Function:**
def clean_numeric(value):
    try:
        cleaned = value.replace(" ", "").replace(",", ".")
        return float(cleaned) if cleaned else 0.0
    except ValueError:
        return 0.0

