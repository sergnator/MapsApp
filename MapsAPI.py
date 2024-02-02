import requests
from Constants import *
from PIL import Image
from io import BytesIO


def create_map_image(params):
    response = requests.get(API_SERVER_MAP, params=params)
    image = Image.open(BytesIO(response.content))
    return image
