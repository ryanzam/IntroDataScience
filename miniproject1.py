
# coding: utf-8

# In[94]:


# Mini project 1 for Data Science course
# In this project top 5 restaurant had to be scrapped from yelp website based on some criteria with data plots.
# Code could be more optimized but I am fine because it is scapping data i wanted
import matplotlib
import matplotlib.pyplot as plt

import urllib2
import re
# python library for pulling data from HTML, XML
from bs4 import BeautifulSoup

#list of top 5 restaurant
top_restaurant = []

#review list of top 5 restaurant
review_list = []

#rating list of top 5 restaurant
rating_list = []

distance_list = []

# link used for scrapping data.
url = "https://www.yelp.com/search?find_desc=Breakfast+%26+Brunch&start=0&sortby=rating&cflt=breakfast_brunch&attrs=RestaurantsPriceRange2.2,BusinessAcceptsCreditCards&open_now=715&open_time=7969&l=p:FI-18:Helsinki::"

page_source = urllib2.urlopen(url).read()


soup = BeautifulSoup(page_source)

restaurant_data = soup.find_all("div", {"class": "media-story"})

for each_restaurant in restaurant_data:
    try:
        #top 5 pick 
        restaurant_name = each_restaurant.h3.span.span.text
        
        ratings = each_restaurant.div.div["title"]
        rating_list.append(ratings)
        
        distance = each_restaurant.ul.li.find_next_sibling().small.text.strip()        
        distance_list.append(distance)
        
        
    except:
        pass
    
    try:
        reviews = re.findall(r'\d+', (each_restaurant.div.span.text).strip())
        
        for review in reviews[:5]:
            review = int(review)
            if review>4:
                review_list.append(review)
                top_restaurant.append(restaurant_name)
            
        
    except:
        pass

#top 5 restaurant
top5_list = top_restaurant[:5] #returns encoded list
top5_list = [i.encode('ascii','ignore').strip() for i in top5_list]

print top5_list

# top pick based on review count
plt.plot(review_list[:5])
plt.title("Plot for top pick based on review count")
plt.xlabel('top 5 restaurant')
plt.ylabel('reviews')
plt.show()

#based on ratings
plt.plot(rating_list)
plt.title("Plot for top pick based on ratings")
plt.show()

#plot based on distance
plt.plot(distance_list[:5])
plt.title("Plot for top pick based on distance from helsinki city")
plt.xlabel('top 5 restaurant')
plt.ylabel('distance')
plt.show()

