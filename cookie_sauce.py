import requests
from bs4 import BeautifulSoup
import os
import time
from PIL import Image
from reportlab.pdfgen import canvas

new_dir_name = "tool_cache"
pdf_title = input("Title for the PDF -> ")
first_image_url = input("Enter first image URL -> ")
number_of_images = int(input("Number of images -> "))

accepted_formats = ["jpg", "jpeg", "png", "webp"]

current_dir = os.path.dirname(os.path.abspath(__file__))
new_dir_path = os.path.join(current_dir, new_dir_name)
os.makedirs(new_dir_path, exist_ok=True)

# Header User-Agent
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

r = requests.get(first_image_url, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

img_counter = 0
image_files = []

for i in range(0, number_of_images):
    if i != 0:
        r = requests.get(loop_url, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')

    div = soup.find("div", id="i3")
    img_url = div.find("img")["src"]
    extension = os.path.splitext(img_url)[-1].lstrip(".").lower()

    if extension in accepted_formats:
        response = requests.get(img_url, headers=headers, stream=True)
        if response.status_code == 200:
            img_path = os.path.join(new_dir_path, f"{img_counter}.{extension}")
            with open(img_path, 'wb') as out_file:
                out_file.write(response.content)

            if extension != "jpg":
                img = Image.open(img_path).convert("RGB")
                img_path_jpg = os.path.join(new_dir_path, f"{img_counter}.jpg")
                img.save(img_path_jpg, "JPEG")
                os.remove(img_path)
                img_path = img_path_jpg

            image_files.append(img_path)
            img_counter += 1

    next_link = soup.find("a", id="next")
    loop_url = next_link["href"]

    print(f"[Info] - Page {i+1}/{number_of_images} downloaded")
    time.sleep(1.5)

print("[Info] - Generating PDF, please wait...")
pdf_path = os.path.join(current_dir, f"{pdf_title}.pdf")
c = canvas.Canvas(pdf_path)

for img_path in image_files:
    img = Image.open(img_path)
    width, height = img.size
    c.setPageSize((width, height))
    c.drawImage(img_path, 0, 0, width, height)
    c.showPage()

c.save()

for img_path in image_files:
    os.remove(img_path)
os.rmdir(new_dir_path)

print(f"[Info] - PDF '{pdf_title}.pdf' successfully generated, enjoy !")
