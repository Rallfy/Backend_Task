# Backend_Task

Hello,

### Task 1
For Task 1, I began by analyzing the website structure and learning about the BeautifulSoup library for web scraping. I focused on identifying the key product details needed for the JSON file and locating them within the HTML. I opted to save the link to each product’s details page in the JSON file.

To gather the required details, I chose to scrape them directly from a pop-up on the main page, accessible via a "details" button, rather than navigating to individual product pages. This approach allowed for a more efficient scrape, focusing on a single page instead of multiple pages. However, I included each product’s individual link in the JSON file as a backup, so the full details can still be accessed if needed.

### Task 2
For Task 2, I tested a few different methods for displaying the data in a readable table format. My initial approach involved using the Pandas library, but I found the default formatting limited and not ideal for displaying a large number of rows. After further exploration, I decided to use the PrettyTable library, which produced a cleaner and more visually appealing table layout.

To standardize the table, I:

 - Created consistent column names
 - Used regex to separate numbers from their units in key specs
 - Removed the phi symbol (φ) from the diameter spec, leaving only the numeric value

**Thank you for reviewing!**
