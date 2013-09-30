from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
import datetime

now = datetime.datetime.now()

base_url = ("http://www.expedia.com/Orange-County-Hotels-Disneyland-Hotel-On-Disneyland-Resort-Property.h15276.Hotel-Information?chkin=10/11/2013&chkout=10/14/2013&rm1=a2:c3:c3")

soup = BeautifulSoup(urlopen(base_url).read())
rooms = soup.find_all("div", "room-info")

print "Pricing data scraped on: " + str(now)
print "For trip Oct 11 - Oct 14, prices quoted are nightly"
print " "

for room in rooms:
	room_type = room.find("h3", class_="room-name")
	room_price = room.find("span", class_="room-price")
	print room_type, room_price
