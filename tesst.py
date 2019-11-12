import base64
import requests
import json

PHOTO_REFERENCE = 'CmRaAAAAVrHLYUujgVVXoq5wL8ChXh_is8H_EbiKjVRA8Mp1L7399mhLNOGmFVP0qjr1aPhpuUM5zrkkoY0koqQZwJapvyDcmP_F9ippNyEDuUm50Sqak53SiBS - \
    GDMdypVzwEoMEhA2srKsb2uAB3zIngCMqQDIGhTL6Cqf-sTZFdIbyRg1YHWf3SH81A'
API_KEY = 'AIzaSyBu5GK0P_4ojVWTyOjaXHBbUiY75M4abSw'
CLIENT_ID = "f80fa92a3bfe9b0"

def get_photo():
    url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&photoreference={}&key={}".format(
        PHOTO_REFERENCE, API_KEY)
    response = requests.get(url)
    
    return upload_imgur(response.content)

def upload_imgur(imagefile):
    url = 'https://api.imgur.com/3/image'

    payload = {
        'image': base64.standard_b64encode(imagefile)}
    files = {}
    headers = {
        'Authorization': 'Client-ID {}'.format(CLIENT_ID)
    }
    response = requests.request(
        'POST', url, headers=headers, data=payload, files=files, allow_redirects=False)

    return json.loads(response.text)['data']['link']

if __name__ == "__main__":
    print(get_photo())