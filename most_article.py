from bs4 import BeautifulSoup
import urllib.request
import os

def handler(choice):
    if(choice) == "food & travel":
        return "food-dan-travel", True
    elif (choice) == "tekno & sains" or choice == "tekno" or choice == "sains":
        return "tekn-dan-sains", True
    elif (choice) ==  "Bola & Sport" or choice == "bola" or choice == "sport":
        return "bola-dan-sport", True
    elif (choice) == "Opini & Cerita" or choice == "opini" or choice == "cerita":
        return "opini-dan-cerita", True
    elif choice == "news" or choice == "mom" or choice == "otomotif" or choice == "woman" or choice == "bisnis":
        return choice, True
    return "", False

print("1. News")
print("2. Entertaiment")
print("3. Mom")
print("4. Food & Travel")
print("5. Tekno & Sains")
print("6. Otomotif")
print("7. Woman")
print("8. Bola & Sport")
print("9. Bisnis")
print("10. Opini & Cerita")

handle = input ("Type Your Choice example(News): ")
resHandler, boolHandler = handler(handle.lower())
url = "https://kumparan.com/trending/"+ resHandler
r = urllib.request.urlopen(url)


soup = BeautifulSoup(r, "html.parser")
result = soup.find_all(attrs={"data-qa-id": "title"})

if not boolHandler:
    print("\nNot Found Your Choice!!!")
    print("Search For Top 5 All Article")
    print("\nTop 5 Article in Kumparan: ")
else:
    print(f"\nTop 5 Article about {handle} in Kumparan: ")

for i in range(5) :
    theParent = result[i].find_parent('a').get("href")
    print(f'{i+1}. {result[i].get_text()}')
    print(f"https://kumparan.com/{theParent}")


