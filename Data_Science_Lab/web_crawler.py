import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Extract all hyperlinks from a given webpage
def get_links(url):
    # Send HTTP GET request to the target URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Use a set to store unique links (no duplicates)
    links = set()

    # Loop through all <a> (anchor) tags on the webpage
    for anchor in soup.find_all('a'):
        href = anchor.get('href')  # Extract the hyperlink reference

        # If the href is a full (absolute) URL, add it directly
        if href and href.startswith('http'):
            links.add(href)
        else:
            # Otherwise, join it with the base URL to form a full URL
            full_url = urljoin(url, href)
            links.add(full_url)

    # Return the set of collected links
    return links

# Perform a simple web crawl starting from the given URL
def crawl(start_url, max_depth=3, max_links_to_print=10):
    visited = set()                # Keep track of visited URLs to avoid repeats
    queue = [(start_url, 0)]       # Queue stores (URL, depth) tuples

    # Continue crawling while there are URLs left in the queue
    while queue:
        current_url, depth = queue.pop(0)  # Get the first URL and its depth

        # Skip if the URL is already visited or the depth limit is reached
        if current_url in visited or depth > max_depth:
            continue

        # Display which URL is being crawled and its depth level
        print(f"Depth: {depth}, Crawling: {current_url}")

        try:
            # Extract all links from the current webpage
            links = get_links(current_url)

            # Mark this URL as visited
            visited.add(current_url)

            # Add extracted links to the queue for further crawling
            # Limit the number of new links to avoid excessive crawling
            queue.extend((link, depth + 1) for i, link in enumerate(links) if link not in visited and i < max_links_to_print)

        except Exception as e:
            # Handle and print any errors that occur during crawling
            print(f"Error crawling {current_url}: {e}")

# Main Execution
if __name__ == "__main__":
    seed_url = ("https://www.google.com")   # Starting point (root URL)
    crawl(seed_url, max_links_to_print=2)   # Start crawling with link limit = 2