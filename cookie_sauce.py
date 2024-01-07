import requests
from bs4 import BeautifulSoup
import os
import time
import img2pdf

#Ask info for gallery download
new_dir_name = "tool_cache"
pdf_title = input("Title for the PDF -> ")
first_image_url = input("Enter the first image URL -> ")
number_of_images = int(input("Number of images -> "))

# Accepted formats // DO NOT MODIFY //
accepted_formats = ["jpg", "png"]

#Create folder to download images
current_dir = os.path.dirname(os.path.abspath(__file__))
new_dir_path = os.path.join(current_dir, new_dir_name)
os.makedirs(new_dir_path, exist_ok=True)

# User-Agent header
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

#Get the first image of the gallery
r = requests.get(first_image_url, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

# Counter for downloaded images
img_counter = 0

#Loop through the gallery
for i in range(0, number_of_images):
    if(i != 0):
        r = requests.get(loop_url, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')

    #Search current image, download and save it.
    div = soup.find("div", id="i3")
    img_url = div.find("img")["src"]

    # Extract extension from file
    extension = os.path.splitext(img_url)[-1].lstrip(".")

    # Verify if file format is allowed. 
    if extension.lower() in accepted_formats:
        response = requests.get(img_url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(os.path.join(new_dir_path, str(img_counter) + "."+extension), 'wb') as out_file:
                out_file.write(response.content)
            img_counter += 1

    #Extract next URL
    next_link = soup.find("a", id="next")
    loop_url = next_link["href"]
    
    print("[Info] - Done with page "+str(i+1)+" out of "+str(number_of_images))
    time.sleep(1.5)

#Convert to PDF
print("[Info] - Building PDF, please wait")
with open(os.path.join(current_dir, pdf_title+".pdf"), "wb") as f:
    imgs = []
    for i in range(img_counter):
        try:
            imgs.append(open(os.path.join(new_dir_path, str(i)+".jpg"),"rb"))
        except:
            imgs.append(open(os.path.join(new_dir_path, str(i)+".png"),"rb")) 
    f.write(img2pdf.convert(imgs))
#Clear cache
for filename in os.listdir(new_dir_path):
    file_path = os.path.join(new_dir_path, filename)
    os.remove(file_path)
