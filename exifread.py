import exifread
# Open image file for reading (binary mode)
path_name = "1.jpg"
f = open(path_name, 'rb')

# Return Exif tags
tags = exifread.process_file(f)