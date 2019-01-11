import PIL
import sys
import numpy as np
import shutil
import os
import re
from PIL import ImageFont, ImageDraw, Image

if not os.path.exists('temp'): os.mkdir('temp')
if not os.path.exists('img'): os.mkdir('img')

text_eng="“Good design adds value faster than it adds cost.”"
text_kor="“좋은 디자인은 그 때문에 소모되는 비용보다 빠르게 가치가 쌓인다.”"

fout=open('Readme.md','w')

readme="""
# Free fonts
""";

fout.write(readme)
dir_root='fonts'
dirs = [f for f in os.listdir(dir_root) if os.path.isdir(os.path.join(dir_root,f))]
for dir in dirs:
    dir_a=os.path.join(dir_root,dir)
    
    fout.write("## "+dir+"\n")
    fin=open(os.path.join(dir_a,'link.txt'),'r')
    fout.write("[Offical link]("+fin.read()+")\n")
    fin.close()
    
    files = [f for f in os.listdir(dir_a) if re.match(r'.*\.(ttf|otf)', f)]
    width=640;
    height=len(files)*100;
    image=PIL.Image.new('RGB',(width,height),color='white')
    draw = ImageDraw.Draw(image)
    for i in range(0,len(files)):
        tmp="temp/font"+os.path.splitext(files[i])[1]
        shutil.copy(os.path.join(dir_a,files[i]),tmp)
        font = ImageFont.truetype(tmp, 20)
        draw.text((10, 100*i), os.path.splitext(files[i])[0], font=font,fill=(241,95,95))
        font = ImageFont.truetype(tmp, 18)
        draw.text((20, 100*i+33), text_eng, font=font,fill=(55,55,35))
        draw.text((20, 100*i+67), text_kor, font=font,fill=(35,55,55))
    image.save(os.path.join('img',dir+".png"))
    fout.write("![]("+os.path.join('img',dir+".png")+")")
    print(dir)
    