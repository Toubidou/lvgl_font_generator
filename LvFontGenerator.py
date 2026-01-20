import json
import subprocess

class LvFontGenerator:
    def __init__(self):
        with open('config.json', 'r', encoding= 'utf-8') as f:
            try: 
                self.fonts_config = json.loads(f.read())['Font']
            except json.JSONDecodeError:
                pass
    def start_generate(self):
        for font_cfg in self.fonts_config:
            if 'range' in font_cfg:
                r = subprocess.run([
                    'lv_font_conv.cmd',
                    '--no-compress', 
                    '--no-prefilter',
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
                    '--no-compress', 
                    '--no-prefilter',
                    '--font', font_cfg["font_path"],
                    '--size', f'{font_cfg["size_pixel"]}',
                    '--format', 'lvgl',
                    '--bpp', f'{font_cfg["bpp"]}',
                    '--symbols', font_cfg["symbols"],
                    '-o', font_cfg["output"] 
                ])
        return r.returncode