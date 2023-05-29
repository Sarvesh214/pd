import requests
import bs4

request1 = requests.get('https://www.flipkart.com/poco-c31-royal-blue-64-gb/p/itm19effae969b86')
print(request1)
print(request1.text)

soup = bs4.BeautifulSoup(request1.text)
print(soup)


print("Here is print reviews:==\n")
reviews = soup.findAll('div',{'class':'t-ZTKy'});
for review in reviews:
    print(review.get_text()+"\n\n")

print("ratings print below here")
ratings = soup.find('div',{'class':'_2d4LTz'});
print(ratings)

print("individual rating goes here \n")
individual_ratings = soup.findAll('div',{'class' : '_3LWZlK _1BLPMq'});
for indi_rating in individual_ratings:
    print(indi_rating.get_text() + "\n")
    print(individual_ratings)



print("\nfetching the tags")
tags = soup.find('span' , {'class':'yhBlnd GXgmTe'});
print(tags)

print("\n \n Fetching the customer names")
customer_name = soup.findAll('p',{'class':'_2sc7ZR _2V5EHH'});
for cust_name in customer_name:
    print(cust_name.get_text() + "\n")

