Web scraping is the data scraping process used for extracting data from websites.
The web scraper folder consists of main.py and scraper folder.
The main script fetches the summary using wikipedia API and scrapes the full contente using Beautifulsoup.The scraper folder consista of wikipedia_api.py file which fetches summary of wikipedia page.
The scraper file also consists wikipedia_html.py file which extracts full text from wikipedia page.
The save_data.py file is used to extract data to CSV file.  By adding these files the webscarping process takes place.
The requirements.txt and README.md files are added too. By running these the web scraping process takes place.


docker commands:


docker run -v ${PWD}:/app -it --name scraper-container-100 web-scraper-main




docker run -d --name scraper-container web-scraper-main tail -f /dev/null#   D e v o p s - l e a r n i n g  
 #   D e v o p s - l e a r n i n g  
 #   D e v o p s - l e a r n i n g  
 #   D e v o p s - l e a r n i n g  
 