import requests
from bs4 import BeautifulSoup

# URL of the website to scrap
url = "https://devsinc.com/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the specific anchor tag with the class "menu-block-btn" and href containing "company"
    about_us_link = soup.find('a', class_='menu-block-btn', href=lambda x: x and 'company' in x)

    # Extract the URL from the anchor tag
    if about_us_link:
        company_url = about_us_link['href']

        # Send a GET request to the company URL
        company_response = requests.get(company_url)

        # Check if the request to the company URL was successful (status code 200)
        if company_response.status_code == 200:
            # Parse the HTML content of the company webpage
            company_soup = BeautifulSoup(company_response.text, 'html.parser')

            # Now you can continue scraping or processing the content of the company webpage
            # print(company_soup)
            div_with_details = company_soup.findAll('div', class_='image-block-info')
            # Check if the div is found
            if div_with_details:
                # Extract details from the div
                title = div_with_details.find('span', class_='imbi-title').text.strip()
                desc = div_with_details.find('span', class_='imbi-desc').text.strip()

                # Print the details
                print("Title:", title)
                print("Description:", desc)
            else:
                print("No div with class 'image-block-info' found on the page.")
        else:
            print("Failed to retrieve the company webpage. Status code:", company_response.status_code)
    else:
        print("About us link not found on the initial page.")
else:
    print("Failed to retrieve the initial webpage. Status code:", response.status_code)
