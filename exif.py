from exif import Image

with open('1.jpg', 'rb') as image_file:
    my_image = Image(image_file)
    
my_image.has_exif