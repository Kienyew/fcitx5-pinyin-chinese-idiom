# fcitx5-pinyin-chinese-idiom
A dictionary of chinese idioms for fcitx5 pinyin

## Install
1. Install from AUR: https://aur.archlinux.org/packages/fcitx5-pinyin-chinese-idiom
2. Install Manually:  
    1. Clone this repository
    2. Fetch `idiom.json` file from https://github.com/pwxcoo/chinese-xinhua/blob/master/data/idiom.json
    3. Convert `idiom.json` to the format recognized by libime: `python ./convert.py idiom.json > idiom.raw`.
    4. Convert `idiom.raw` to the format recognized by fcitx5: `libime_pinyin_dict idiom.raw idiom.dict`
    5. Import dictionary in Fcitx5 config tool.

## Credit
Dictionary data will fetch from https://github.com/pwxcoo/chinese-xinhua
