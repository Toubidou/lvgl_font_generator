import json
import subprocess

with open('config.json', 'r', encoding= 'utf-8') as f:
    try: 
        fonts_config = json.loads(f.read())['Font']
    except json.JSONDecodeError:
        pass


for font_cfg in fonts_config:
    if 'range' in font_cfg:
        r = subprocess.run([
            'lv_font_conv.cmd',
            '--font', font_cfg["font_path"],
            '--size', f'{font_cfg["size_pixel"]}',
            '--format', 'lvgl',
            '--bpp', f'{font_cfg["bpp"]}',
            '--symbols', font_cfg["symbols"],
            '--range', font_cfg["range"],
            '-o', font_cfg["output"] 
        ])
    else:
        r = subprocess.run([
            'lv_font_conv.cmd',
            '--font', font_cfg["font_path"],
            '--size', f'{font_cfg["size_pixel"]}',
            '--format', 'lvgl',
            '--bpp', f'{font_cfg["bpp"]}',
            '--symbols', font_cfg["symbols"],
            '-o', font_cfg["output"] 
        ])
    # print(r)