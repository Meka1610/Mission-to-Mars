import pandas as pd

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# set up executable path,
# set up the URL
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# set up HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Mars Facts

# creating new DataFrame from HTML table. Pandas function read_html()
# searching specifically for and returns a list of tables found 
# in the HTML. 
# specify an index of 0, telling Pandas pull ONLY the first table
# it encounters, or first item in the list. Then, it turns table 
# into a DataFrame
df = pd.read_html('https://galaxyfacts-mars.com')[0]

# Assign columns to new DataFrame for addionitional clarity
df.columns=['description', 'Mars', 'Earth']

# .set_index() function, turning Description column into the 
# DataFrame's index.
# inplace=True means the updated index will remain in place, without
# having to reassign the DataFrame to a new variable
df.set_index('description', inplace=True)
df


# converting DataFrame back into HTML-ready code using .to_html()
df.to_html()


# Quit the brower from running anymore
browser.quit()


# ## Mars News

def mars_news():

   # Visit the mars nasa news site
   url = 'https://redplanetscience.com/'
   browser.visit(url)

   # Optional delay for loading the page
   browser.is_element_present_by_css('div.list_text', wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')

   slide_elem = news_soup.select_one('div.list_text')
   slide_elem.find('div', class_='content_title')

   # Use the parent element to find the first <a> tag and save it as  `news_title`
   news_title = slide_elem.find('div', class_='content_title').get_text()
   news_title

   # Use the parent element to find the paragraph text
   news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
   news_p

   return news_title, news_p


def mars_news(browser):

# Scrape Mars News
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

# Add try/except for error handling
try:
    slide_elem = news_soup.select_one('div.list_text')
    # Use the parent element to find the first 'a' tag and save it as 'news_title'
    news_title = slide_elem.find('div', class_='content_title').get_text()
    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

except AttributeError:
    return None, None

return news_title, news_p
