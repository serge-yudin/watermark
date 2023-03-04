<h1>WaterMarker</h1>
<p>
WaterMarker is a Python class that adds watermarks to images. The watermark can be any text string, and the class automatically adjusts the text color based on the lightness or darkness of the image.
</p>
<h3>Requirements</h3>
<uL>
<li>Python 3.x
<li>OpenCV (cv2)
<li>Pillow (PIL)
</ul>
<h3>Installation</h3>
<p>
Install the required packages using pip:
</p>
<code>
pip install opencv-python Pillow
</code>
<h3>Usage</h3>
<p>
Create a WaterMarker instance by passing the image file opened in rb mode and the watermark text. Then call the place_watermark() method to add the watermark to the image and return the modified image as binary data.
</p>
<code>
from watermarker import WaterMarker

with open('path/to/image.png', 'rb') as f:
    img_data = f.read()

wm = WaterMarker(img_data, 'My Watermark Text')
modified_img_data = wm.place_watermark()
</code>
<p>
By default, the watermark text color is black. If the image is light, the text color is changed to white. You can also explicitly set the text color to white by calling the set_white_text_color() method before calling place_watermark().
</p>
<h3>Example</h3>
<code>
from watermarker import WaterMarker

with open('path/to/image.png', 'rb') as f:
    img_data = f.read()

wm = WaterMarker(img_data, 'My Watermark Text')
modified_img_data = wm.place_watermark()

with open('path/to/modified_image.png', 'wb') as f:
    f.write(modified_img_data)
</code>
<h3>License</h3>
<p>
This project is licensed under the MIT License - see the LICENSE file for details.</p>
