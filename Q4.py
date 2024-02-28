import requests
url = input("Enter the URL of the website: ")
try:
    response = requests.get(url)
    response.raise_for_status() 
except requests.exceptions.RequestException as e:
    print(f"Error connecting to the website: {e}")
else:
    print("Connection successful. HTML content:")
    print(response.text)
