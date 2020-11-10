from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# NASA Latest Mars News
def scrape_news():
	browser = init_browser()

	# Latest Mars News
	url = "https://mars.nasa.gov/news/"
	browser.visit(url)
	html = browser.html
	soup = bs(html, 'html.parser')

	news_title = soup.find('div', class_='content_title').find('a').text
	news_p = soup.find('div', class_='article_teaser_body').text

	mars_data = {
		"news_title": news_title,
		"news_p": news_p
	}

	browser.quit()

	return mars_data

# Featured Image
def scrape_image():
	featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(featured_image_url)
	image_html = browser.html
	image_soup = bs(image_html, 'html.parser')

	featured_image_url = f"https://www.jpl.nasa.gov{image_soup.find('div', class_='img').img['src']}"

	mars_data = {
		"featured_image": featured_image_url
	}

	brower.quit()

	return mars_data

# Mars Facts
def scrape_facts():
	mars_url = "https://space-facts.com/mars/"
	browser.visit(mars_url)

	facts_table = pd.read_html(mars_url)
	facts_df = facts_table[0]
	facts_df.columns = ['Description', 'Value']
	html_table = facts_df.to_html()

	mars_data = {
		"mars_facts": html_table
	}

	brower.quit()

	return mars_data

# Mars Hemispheres
def scrape_hemispheres():
	hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(hemispheres_url)
	hemisphere_html = browser.html
	hemisphere_soup = bs(hemisphere_html, 'html.parser')

	# Find all hemispheres
	all_hems = hemisphere_soup.find_all('div', class_="item")

	hemisphere_image_urls = []
	base_url = 'https://astrogeology.usgs.gov'

	# Create for loop to visit link for each hemisphere
	for hem in all_hems:
	    
	    # Find hemisphere title
	    title = hem.find('h3').text
	    
	    # Find link to full image
	    link_url = hem.find('a', class_='itemLink product-item')['href']
	    
	    # Go to site to get the html with the full image url
	    browser.visit(base_url + link_url)
	    
	    # Create soup object of html with full image url
	    link_html = browser.html
	    soup = bs(link_html, 'html.parser')
	    
	    # Get image url
	    full_img = base_url + soup.find('img', class_='wide-image')['src']
	    
	    # Append info into dictionary
	    hemisphere_image_urls.append({
	        "title": title,
	        'img_url': full_img
	    })
	mars_data = {
		"hemisphere_images": hemisphere_image_urls
	}
	
	# Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
