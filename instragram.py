import requests
from bs4 import BeautifulSoup
import instaloader


def main():
    URL = "https://www.instagram.com/{}/"
    username = input(f"\033[1;37mEnter username target: \033[1;32m")
    print(f"\033[1;32m\nSHOW INFORMATION IG USER\n")

    try:
        # Fetching the Instagram profile page
        r = requests.get(URL.format(username))
        r.raise_for_status()  # Raise an exception for bad response status codes

        # Parsing the HTML content
        soup = BeautifulSoup(r.text, "html.parser")

        # Finding meta tag with property="og:description" for user information
        meta = soup.find("meta", property="og:description")
        if meta:
            content = meta.attrs['content']
            parts = content.split("-")[0].strip().split()
            if len(parts) >= 4:
                followers = parts[0]
                following = parts[2]
                posts = parts[4]
                print(f" Followers: {followers}")
                print(f" Following: {following}")
                print(f" Posts: {posts}\n")
            else:
                print("Could not extract user information.")

        # Using instaloader to download profile picture
        ig = instaloader.Instaloader()
        ig.download_profile(username, profile_pic=True)

    except requests.RequestException as e:
        print(f"Error fetching Instagram profile page: {e}")
    except instaloader.ProfileNotExistsException:
        print(f"Profile '{username}' does not exist or is private.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
