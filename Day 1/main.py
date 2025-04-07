


# main.py - Main script to run the Wikipedia scraper

import sys
import os
import requests
from bs4 import BeautifulSoup
import csv

# Ensure 'scraper' module is correctly detected (you can keep this if you want to organize the structure)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_wikipedia_summary(topic):
    """
    Fetches the summary of a Wikipedia page using requests and BeautifulSoup.
    """
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the first paragraph of the page summary
        summary_paragraph = soup.find('div', {'class': 'reflist'}).find_previous('p').get_text()
        return summary_paragraph
    except Exception as e:
        return f"Error: {e}"

def get_wikipedia_sections(topic):
    """
    Fetches the sections of a Wikipedia page using requests and BeautifulSoup.
    """
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all the section headers (h2, h3, etc.)
        section_headers = soup.find_all(['h2', 'h3'])
        sections = [header.get_text(strip=True) for header in section_headers]
        return sections
    except Exception as e:
        return f"Error: {e}"

def scrape_wikipedia_content(url):
    """
    Scrapes the full content of the Wikipedia page using BeautifulSoup and requests.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all paragraphs <p> from the content
        paragraphs = soup.find_all('p')
        content = [para.get_text() for para in paragraphs]
        return content
    except Exception as e:
        return f"Error: {e}"

def save_to_csv(data, filename):
    """
    Saves the scraped data to a CSV file directly in the main script.
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            writer.writeheader()
            writer.writerows([dict(zip(data.keys(), row)) for row in zip(*data.values())])
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    topic = "Web scraping"  # Change this to any Wikipedia topic
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"

    try:
        # Fetch summary using BeautifulSoup and requests
        summary = get_wikipedia_summary(topic)
        print("\nSummary:\n", summary)

        # Fetch sections using BeautifulSoup and requests
        sections = get_wikipedia_sections(topic)
        print("\nSections:")
        for section in sections:
            print("-", section)

        # Scrape full content using BeautifulSoup and requests
        content = scrape_wikipedia_content(url)
        print("\nFirst Paragraph:\n", content[0] if content else "No content available.")

        # Prepare data for saving to CSV
        data = {
            "Title": [topic],
            "Summary": [summary],
            "Sections": [", ".join(sections)],
            "Content": [" ".join(content)]
        }
        
        # Save data to CSV directly in main.py
        save_to_csv(data, "wikipedia_scraped_data.csv")

        print("\nData saved successfully.")

    except Exception as e:
        print(f"Error: {e}. Please check your inputs or internet connection.")

if __name__ == "__main__":
    main()
