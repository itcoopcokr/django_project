from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image

import os, glob

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def _add_thumb(s):
    parts = s.split(".")  # abc.jpg
    parts.insert(-1, "thumb")  # abc.thumb.jpg
    if parts[-1].lower() not in ['jpg','jpeg']:
        parts[-1]=  "jpg"
    return ".".join(parts) # thumb_nail 파일명 만들기

class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thum_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thum_path)  # thumb_path 만들어준다

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save) # 원본이미지 저장
        img = Image.open(self.path)

        size = (100, 100)
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGB', size, (255, 255,255,0)) # 흰색 백그라운드 이미지
        background.paste(img, (int(  (size[0]-img.size[0])/2 ), int((size[1]-img.size[1])/2) ))
        background.save(self.thumb_path,'JPEG') # 썸네일 이미지를 thumb_path 경로에 저장

    def delete(self, save=True):
        '''원본 파일뿐만 아니라, 쎔네일도 삭제'''
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)

class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=100, thumb_height=100, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)
