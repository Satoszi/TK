import exifreader
path_name = "1.jpg"
f = open(path_name, 'rb')

# Return Exif tags
tags = exifreader.process_file(f)