import requests


def get_nasa_apod(api_key: str):
    """
    Fetch the NASA Astronomy Picture of the Day (APOD) data.
    """
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "hd": True}
    response = requests.get(url, params=params)
    response.raise_for_status()
    result = response.json()

    title = result["title"]
    date = result["date"]
    explanation = result["explanation"]
    media_type = result["media_type"]
    hd_url = result["hdurl"]  # HD image if available
    url = result["url"]  # Fallback image or video link

    if media_type == "image":
        # Download the image content
        image_url = hd_url if hd_url else url  # prefer HD if available
        img_response = requests.get(image_url)
        img_response.raise_for_status()
        # Get image
        img_data_uri = img_response.content
    else:
        # Typically a YouTube or Vimeo link
        img_data_uri = f"See here: {url}"

    return f"{title} ({date}) \n {explanation} \n", img_data_uri
