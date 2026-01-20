import os

class LvFontAmend:
    def __init__(self):
        self.font_list = os.listdir('output_font')
    def amend(self):
        try:
            for font in self.font_list:
                font_dir = os.path.join('output_font/' + font)
                with open(font_dir, 'r', encoding= 'utf-8') as f:
                    lines = f.readlines()
                    inc = '''#ifdef __has_include   
    #if __has_include("lvgl.h")
        #ifndef LV_LVGL_H_INCLUDE_SIMPLE
            #define LV_LVGL_H_INCLUDE_SIMPLE
        #endif
    #endif\n#endif\n'''
                    lines.insert(5, inc)
                with open(font_dir, 'w', encoding= 'utf-8') as f:
                    f.writelines(lines)
        except FileNotFoundError:
            print("文件不存在！！！")
            return False
        except Exception as e:
            print("Error!!!")
            return False
        print("Amend finish.")