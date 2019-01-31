import requests					# reads html page into a variable	
from bs4 import BeautifulSoup	# parsing the read in data

URL = "https://en.wikipedia.org/wiki/Main_Page"	#Associate the target page 
r=requests.get(URL)				# creates the class variable of requests 

c = r.content					# grabs the contents of the page
#print(c)						

soup = BeautifulSoup(c,"html.parser")			# creates a class variable of BeautifulSoup		
#print(soup.prettify())			# helps to format the data for display purposes

# One way is to fetch all the "a" tags as they contain the "img" tags
#all_a_tags=soup.find_all("a",{"class":"image"})	
#print(all_a_tags)

#Another way as on this page is to directly fetch the "img" tag
all_img = soup.find_all("img")

imgList = []
#Browse through each entity of "img" and extract the information stored in its property "src"
for image in all_img:
	imgList.append(image['src'])

#Print the results
print(imgList)
