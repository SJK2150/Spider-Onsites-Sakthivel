import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"{url} is up"
        else:
            return f"{url} is down (Status code: {response.status_code})"
    except requests.RequestException as e:
        return f"{url} is down (Error: {str(e)})"

def main():
    websites = [
        "http://esfjsujfple.com",
        "http://google.com",
        "http://njsjvojso.xyz"
    ]

    print("Website Monitoring Results:")
    for website in websites:
        result = check_website(website)
        print(result)

if __name__ == "__main__":
    main()
