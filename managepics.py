import configparser
import glob
import re
import os

from PIL import Image
from PIL.ExifTags import TAGS


def check_output_directories(output_dirs): 

    for dir in output_dirs:
        if not os.path.exists(output_dirs[dir]): 
            os.makedirs(output_dirs[dir])
    


DATETIME_TAG = 306

def get_filename(image_datetime, extension = 'jpg'):
    output_filename = re.sub(':', '', image_datetime)
    output_filename = re.sub(' ', '_', output_filename)
    return f'{output_filename}.{extension}'

def get_image_datetime (filename, datetime_tag=306) :
    image = Image.open(filename)
    exifdata = image.getexif()
    
    datetime = ''

    #tag 306 is Datetime
    if datetime_tag in exifdata.keys():
        datetime = exifdata.get(datetime_tag)
        
    return datetime

# def get_image_filesize(filename, filesize_tag=514):
#     # 514 is number of bytes of jpeg data
#     image = Image.open(filename)
#     exifdata = image.getexif()
#     filesize = ''

#     if filesize_tag in exifdata.keys():
#         filesize = exifdata.get(filesize_tag)
        
    

def main():
    
    configs = configparser.ConfigParser()
    configs.read('configs.ini')


    input_files_pattern = f"{configs['INPUT']['pics.directory']}\**\*.jpg"

    #check if output directories exist, if not, create them.
    check_output_directories(configs['OUTPUT'])

    for filename in glob.iglob(input_files_pattern, recursive=True):
        image_datetime = get_image_datetime(filename)
        output_filename = ''
        if image_datetime:
            output_filename = get_filename(image_datetime)
        
        print(f'{filename}: {output_filename}')


    # organized = {}
    # duplicates = {}
    # scanned = {}
    
    # if output_filename == '':
    #     scanned.add(output_filename)
    # else:
    #     organized.add(output_filename)
    #     if output_filename in organized and filesize :



if __name__ == '__main__':
     main()
    


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