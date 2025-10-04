import requests
import os
from urllib.parse import urlparse
from datetime import datetime as dt

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    urls_str = input("Please enter the images URLs separated by comma: ")
    urls = urls_str.split()

    for url in urls:
        try:
            # Create directory if it doesn't exist
            os.makedirs("Fetched_Images", exist_ok=True)
            
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes
            
            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            
            if not filename:
                today = dt.now().strftime("%d-%m-%Y %H:%M:%S")
                filename = f"downloaded_image_{today}.jpg"

            # Save the image
            filepath = os.path.join("Fetched_Images", filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("\nConnection strengthened. Community enriched.")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()