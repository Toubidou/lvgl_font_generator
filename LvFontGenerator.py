import json
import os

with open('config.json', 'r', encoding= 'utf-8') as f:
    try: 
        fonts_config = json.loads(f.read())['Font']
    except json.JSONDecodeError:
        pass

for font_cfg in fonts_config:
    symbols = "".join(font_cfg["symbols"].split())
    command = "lv_font_conv.cmd --no-compress --no-prefilter " + "--font " + font_cfg["font_path"] +\
        " --size " + f'{font_cfg["size_pixel"]}' + " --format lvgl " + "--bpp " + f'{font_cfg["bpp"]}' +\
        " --symbols " + symbols + " -o " + font_cfg["output"]
    os.system(command)
    # print(command)