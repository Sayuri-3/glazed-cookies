# Glazed Cookies 🍪🥛
## An e-hentai.org gallery downloader

> The provided code is released "as is", with no guarantees or warranties. Although the creator has endeavored to deliver high-quality content, the accuracy, reliability, or completeness of this software and its components is not guaranteed. The code should be utilized at your own risk. <br>
The creator does not intend to contravene any laws or regulations of the user's country of residence with this disclaimer. The user is responsible for ensuring that the use of this code is in compliance with all local, national, and international law. <br>
By choosing to use this code, you are agreeing to fully accept this disclaimer. If any part of this disclaimer is not agreed with, please do not use this code.

## Pre-requisites

Before utilization, the main application referred to as `cookie-sauce.py`, requires the installation of 2 libraries unless they are already installed.

To install the requirements:
`pip3 install bs4 img2pdf`

## Usage 🔖

1. Clone the repository via Git and navigate into the directory.
2. Choose your preferred gallery on E.H.
3. Execute the script : `python3 cookie-sauce.py`
4. `Title for the PDF ->` Enter a suitable title for the final PDF. It is suggested to use the doujin/comic title.
5. `Enter the first image URL ->` Provide the first gallery image URL by right-clicking on the first image and selecting "copy link to". Paste this URL into the script.
6. `Number of images ->` Refer to the number of images in the gallery and provide this information.
7. PATIENTLY wait for the script to download each image. This may take some time. The script will generate a folder named `/tool-cache` where it stores the images before assembling them into a PDF.
8. Next, the script will compile all the images into a PDF and clear the `/tool-cache` directory. The PDF will be created in the same folder from which the script was executed.

### Additional Information

BS4 is utilized by this script to navigate the site and scrape every image from the selected gallery. In order to circumvent anti-bot measures and to not overload the EH servers, a moderate delay of 1.5 seconds between each download has been incorporated into the script. It is strongly advised not to modify this setting.

### Changelog
- Inclusion of the script into the repository
- Functional as of 04/01/2024.

