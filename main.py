import requests
import json


# Function to get channel ID from username
def get_channel_id(username, api_key):
    search_url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={username}&key={api_key}'
    response = requests.get(search_url)
    data = response.json()

    # Print the full response for debugging
    print(json.dumps(data, indent=2))

    # Extract the channel ID
    if 'items' in data and len(data['items']) > 0:
        return data['items'][0]['snippet']['channelId']
    else:
        raise Exception("No channel found for the given username.")


# Function to get subscriber count from channel ID
def get_subscriber_count(channel_id, api_key):
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&fields=items/statistics/subscriberCount&key={api_key}'
    response = requests.get(url)
    data = response.json()

    # Print the full response for debugging
    print(json.dumps(data, indent=2))

    # Extract the subscriber count
    if 'items' in data and len(data['items']) > 0:
        return data['items'][0]['statistics']['subscriberCount']
    else:
        raise Exception("No subscriber count found for the given channel ID.")


# Main function
def main():
    api_key = "AIzaSyDh4oll0iHesYzmMnGx_xjntUKe1clilJI"
    youtube_url = "https://www.youtube.com/@tendofficial"

    # Extract username from URL
    username = youtube_url.split('@')[1]

    try:
        # Get channel ID from username
        channel_id = get_channel_id(username, api_key)
        print(f'Channel ID: {channel_id}')

        # Get subscriber count from channel ID
        subscriber_count = get_subscriber_count(channel_id, api_key)
        print(f'Subscriber Count: {subscriber_count}')
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
