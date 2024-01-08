# Web-Scraping
A python script that scrapes data from a website containing a large amount of data.  
The website used for scraping is https://attestazione.net/SoaEngine?Page=%7B%7D, there are 1474 pages at the moment with links leading to a more detailed description of the data. The scraper follows these links and extracts the necessary fields from these pages and converts them to a CSV file that can be used for various analytical purposes.  

# Performance

There are two ways you can scrape the data. The first method uses ordinary loops, but due to the high volume of pages each containing about 20 links that each lead to a page with multiple fields, the time taken can vary based on the speed of the system and network and is overall slow. If your device has great Multiprocessing power, there is an option to enable multiprocessing that reduces the time taken by more than half the time taken without multiprocessing.  
Below is an image of the terminal output showing the time taken by the script to scrape two pages (approx. 40 links) with and without multiprocessing.  

<img width="1680" alt="terminal_with_performance" src="https://github.com/omr-hk/Web-Scraping/assets/111275526/1f34260f-0ae3-41dd-855e-0306abe50a70">  

# Output  

The output of the scraper follows the same order as the website if multiproessing is not used and the order differs if multiprocessing is enabled. The final output csv file for the two pages looks like this:  

<img width="1680" alt="no_multiprocessing" src="https://github.com/omr-hk/Web-Scraping/assets/111275526/9a05aae6-46ad-41b1-9a1d-5fda402c4c08">  

The device used to design, build and test the scraper is an M1 Macbook Air with 8Gb RAM.
