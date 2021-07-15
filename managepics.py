import glob
from PIL import Image
from PIL.ExifTags import TAGS
import re

def get_image_datetime (filename):
    image = Image.open(filename)
    exifdata = image.getexif()
    
    datetime = ''

    #tag 306 is Datetime
    if 306 in exifdata.keys():
        datetime = exifdata.get(306)
        # if isinstance(datetime, bytes):
        #     datetime = datetime.decode()

    return datetime

def get_filename(image_datetime):
    output_filename = re.sub(':', '', image_datetime)
    output_filename = re.sub(' ', '_', output_filename)
    return output_filename

for filename in glob.iglob('pics\**\*.jpg', recursive=True):
    image_datetime = get_image_datetime(filename)
   
    if image_datetime:
        output_filename = get_filename(image_datetime)
     
    print(f'{filename}: {output_filename}')




# from PIL import Image
# from PIL.ExifTags import TAGS
# # path to the image or video
# imagename = r"C:\Users\14706\Documents\picsproject\pics\EP-1gb\100NCD40\Kiddies\lw.jpg"
# # read the image data using PIL
# image= Image.open(imagename)
# # extract EXIF data
# exifdata= image.getexif()
# # iterating over all EXIF data fields
# for tag_id in exifdata:
#     # get the tag name, instead of human unreadable tag id
#     tag= TAGS.get(tag_id, tag_id)
#     data = exifdata.get(tag_id)
#     # decode bytes 
#     if isinstance(data, bytes):
#         data= data.decode()
#     print(f"{tag:25}: {data}')")