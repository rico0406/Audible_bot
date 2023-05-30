# Amazon Audible Web Scraper v1.0.0

This is the v1.0.0 release of the Amazon Audible Web Scraper program. The program allows you to scrape information about books from the Amazon Audible website. You can choose between two different methods to use the program: running the script directly or using the pre-built executable file.

## Method 1: Running the Script

### Prerequisites

To run the script, make sure you have the following:

- Python 3.x installed on your machine.
- The Selenium library installed (`pip install selenium`).
- Google Chrome web browser installed.
- ChromeDriver executable compatible with your Chrome version (available at https://sites.google.com/a/chromium.org/chromedriver/downloads).

### Usage

To use the Amazon Audible Web Scraper script, follow these steps:

1. Clone or download the program files from the v1.0.0 release on GitHub.
2. Install the necessary dependencies (e.g., Selenium) by running `pip install -r requirements.txt`.
3. Place the ChromeDriver executable in a location accessible by the program.
4. Open the `program.py` file in a text editor.
5. Modify the `web` variable to the URL of the Audible page you want to scrape.
6. Run the program using a Python interpreter (`python program.py`).

The program will start a headless Chrome browser, navigate to the specified Audible page, scrape the book information, and save it to a CSV file named `books.csv` in the same directory as the program.

**Note:** Make sure to comply with the terms of service of the Audible website and any legal restrictions regarding web scraping.

## Method 2: Using the Pre-built Executable

### Prerequisites

To use the pre-built executable file, ensure that you have the following:

- The Chrome web browser installed on your machine.

### Usage

To use the pre-built executable file, follow these steps:

1. Download the executable file from the v1.0.0 release on GitHub.
2. Place the executable file in a directory of your choice.
3. Open a terminal or command prompt and navigate to the directory where the executable file is located.
4. Run the executable file by typing its name (e.g., `program.exe` on Windows, or `./program` on Linux or macOS).

The program will start executing and perform the web scraping process using a headless Chrome browser. It will navigate to the default Audible page specified in the script and save the book information to a CSV file named `books.csv` in the same directory as the executable.

**Note:** Make sure to comply with the terms of service of the Audible website and any legal restrictions regarding web scraping.

## Additional Information

- The program utilizes the Selenium library to automate web browser interactions. It uses a headless Chrome browser, which means the browser window will not be visible during execution. If you prefer to see the browser window, remove the `options.add_argument('--headless')` line or set it to `'--headless'` to enable headless mode.
- The program waits for specific elements to be present on the page using the `WebDriverWait` class to ensure reliable scraping. You can adjust the wait times (currently set to `5` seconds) if needed.
- Pagination logic is implemented to scrape all available pages of books on the Audible website. The program locates the last page number and iterates through each page, scraping book information. If there are no more pages, the program will terminate.
- Book information is stored in separate lists (`book_title`, `author`, `run_time`, `price`) as the scraping progresses. Once all pages have been scraped, the program creates a Pand

as DataFrame and saves it as a CSV file named `books.csv`.
- The program handles exceptions that may occur during scraping, such as the absence of the "Next" button on the last page.

## Disclaimer

This program is provided as-is and is intended for educational purposes only. It is your responsibility to comply with the terms of service of the Audible website and any legal restrictions related to web scraping. Use this program responsibly and at your own risk.

Please note that scraping websites without permission may be against the website's terms of service and can potentially lead to legal consequences.