import os

print("Amend start:")

font_list = os.listdir('output_font') 
for font in font_list:
    # print(os.path.join('output_font/' + font))
    font_dir = os.path.join('output_font/' + font)
    with open(font_dir, 'r', encoding= 'utf-8') as f:
        lines = f.readlines()
        inc = '''#ifdef __has_include
        #if __has_include("lvgl.h")
            #ifndef LV_LVGL_H_INCLUDE_SIMPLE
                #define LV_LVGL_H_INCLUDE_SIMPLE
            #endif
        #endif
#endif\n'''
        lines.insert(5, inc)
    with open(font_dir, 'w', encoding= 'utf-8') as f:
        f.writelines(lines)
print("Amend finish.")