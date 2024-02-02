import requests
from Constants import *
from PIL import Image
from io import BytesIO


def create_map_image(params):
    response = requests.get(API_SERVER_MAP, params=params)
    image_ = Image.open(BytesIO(response.content))
    image = Image.new('RGB', image_.size, (255, 255, 255))
    image.paste(image_)
    return image
