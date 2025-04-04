import requests  # Import APIs


def get_nasa_apod(api_key: str):
    """
    Fetch the NASA Astronomy Picture of the Day (APOD) data.
    """

    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "hd": True}
    response = requests.get(url, params=params)

    # Check response (logs)
    if response.status_code != 200:
        print("[INFO] NASA API request failed.")

    result = response.json()

    title = result["title"]
    date = result["date"]
    explanation = result["explanation"]
    media_type = result["media_type"]
    url = result["url"]  # Fallback image or video link

    if media_type == "image":
        # Download the image content
        img_response = requests.get(url)
        img_response.raise_for_status()
        # Get image
        img_data_uri = img_response.content
    else:
        # Typically a YouTube or Vimeo link
        img_data_uri = f"See here: {url}"

    return (
        f"{title} ({date}) - {media_type} \n {explanation} \n",
        media_type,
        img_data_uri,
    )


if __name__ == "__main__":
    import os

    NASA_API_KEY = os.getenv("NASA_API_KEY")
    apod_text, media_type, apod = get_nasa_apod(api_key=NASA_API_KEY)
    print(apod_text)
    print(media_type)
    # print(apod)
