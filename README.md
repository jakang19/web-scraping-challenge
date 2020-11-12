# web-scraping-challenge
## Background
To build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page

## mission_to_mars
This directory contains the Jupyter Notebook `mission_to_mars.ipynb` with the code that scrapes the following information:
### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

### Mars Facts

* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

- - -
The jupyter notebook code was then converted into Python script `scrape.py`.
The file `app.py` uses MongoDB with Flask templating to create a new HTML page that displays all of the scraped information

## Submission
This repository contains:
- Jupyter notebook script `Pymaceuticals.ipynb` with initial web scraping
- Python scripts `scrape_mars.py` and Flask app `app.py`
- `index.html` inside the directory `templates` that displays the scraped information
- `screenshots` directory containing screenshots of the final webpage displaying all scraped info
