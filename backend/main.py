import requests # allows me to make TTP requests to APIS
# This file is for future use in case I want to make a bigger project from cat images . . .
import requests

# API key for The Cat API web application
API_KEY = "live_bPyP5VLWHhXSmKVlisI7c64350da9mSFKeIG9VlyhcoFltgxAfKLRAmYFZovPL0q"

# grabs a random cat image and ensures a valid request occurs
def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search" # request we're using to get random cat img
    
    headers = {
        "x-api-key": API_KEY
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            # The API returns a list of images, so we take the first one
            return data[0]["url"]
        else:
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    image_url = get_random_cat_image()
    if image_url:
        print(f"Random Cat Image URL: {image_url}")
    else:
        print("Failed to retrieve an image.")
