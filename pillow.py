from PIL import Image
from PIL.ExifTags import TAGS

# path to the image or video
imagename = "4.mp4"

# read the image data using PIL
image = Image.open(imagename)


exifdata = image.getexif()


for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")