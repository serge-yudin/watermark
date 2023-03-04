import io

import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

class WaterMarker:
    def __init__(self, img: bytes, watermark: str) -> None:
        '''
        Initializes a WaterMarker instance.

        Parameters:
        img (bytes): The image file opened in 'rb' mode.
        watermark (str): The text to be placed on the img.

        Returns:
        None
        '''
        self.image = img
        self.watermark = watermark
        self.color = (0, 0, 0)
        self.font = 'Arial.ttf'  # should be in the same directory

    def image_to_nparray(self, img: bytes):
        '''
        Converts image file to a numpy array.

        Parameters:
        img (bytes): The image file opened in 'rb' mode.

        Returns:
        numpy.ndarray: The numpy array representation of the image.
        '''
        return np.frombuffer(img.read(), np.uint8())

    def is_light(self, img: bytes, threshold=127) -> bool:
        '''
        Returns True if the given image is light, False otherwise.
        Image Value refers to lightness or darkness of an image.

        Parameters:
        img (bytes): The image file opened in 'rb' mode.
        threshold (int): The threshold value to determine the lightness or darkness of the image.

        Returns:
        bool: True if the given image is light, False otherwise.
        '''
        image = cv2.imdecode(self.image_to_nparray(img), cv2.IMREAD_GRAYSCALE)
        return cv2.mean(image)[0] > threshold

    def set_white_text_color(self):
        '''
        Sets the text color to white.
        
        Parameters:
        None

        Returns:
        None
        '''
        self.color = (255, 255, 255)

    def place_watermark(self):
        '''
        Adds the watermark to the image and returns the modified image as binary data.

        Parameters:
        None

        Returns:
        bytes: The binary data representation of the modified image with the watermark.
        '''
        if not self.is_light(self.image):
            self.set_white_text_color()
        img = Image.open(self.image).convert('RGBA')
        watermark = Image.new('RGBA', img.size, self.color + (0,))
        font = ImageFont.truetype(self.font, 30)
        draw = ImageDraw.Draw(watermark)
        textwidth, textheight = draw.textsize(self.watermark, font)
        x = img.size[0] - textwidth - 10
        y = img.size[1] - textheight - 10
        draw.text((x, y), self.watermark, font=font,
                fill=self.color + (80,))
        buffer = io.BytesIO()
        final_image = Image.alpha_composite(img, watermark)
        final_image.save(buffer, format='PNG')
        return buffer.getvalue()

