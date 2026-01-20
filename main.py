import LvFontGenerator
import LvFontAmend

def main():
    print("Start generate lvgl fonts:")

    lfg = LvFontGenerator.LvFontGenerator()
    if lfg.start_generate() == 0:
        print("Lvgl generator success.")

        lfa = LvFontAmend.LvFontAmend()
        print("Start amend lvgl font:")
        lfa.amend()
    else:
        print("Generate error!!!")

if __name__ == "__main__":
    main()