from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


tasdiqlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data='ha'), InlineKeyboardButton(text="❌ Bekor qilish", callback_data='yoq')]
    ]
)


tasdiq = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha", callback_data='ha'), InlineKeyboardButton(text="Yoq", callback_data='yoq')]
    ]
)


tasdiqla = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha", callback_data='ha'), InlineKeyboardButton(text="Yoq", callback_data='yoq')]
    ]
)


habarlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Sherik kerak", callback_data='sherik'), InlineKeyboardButton(text="Ish joyi kerak", callback_data='ish')],
        [InlineKeyboardButton(text="Hodim kerak", callback_data='hodim'), InlineKeyboardButton(text="Ustoz kerak", callback_data='ustoz')],
        [InlineKeyboardButton(text="Shogirt garak",callback_data='shoggi')]
    ]
)

# taom = InlineKeyboardMarkup(

#     inline_keyboard=[
#         [InlineKeyboardButton(text="Taomlar", callback_data='taomm'), InlineKeyboardButton(text="Ichimliklar", callback_data='ichimlikk'), InlineKeyboardButton(text="Zakuska", callback_data='zakuss')],
#         [InlineKeyboardButton(text="Ortga", callback_data='ortga')]
#     ]
# )


# taomlars = ReadTaomlar()
# yegulik = InlineKeyboardBuilder()
# for i in taomlars:
#     yegulik.button(text=f"{i[0]}", callback_data=f"{i[0]}")
# yegulik.button(text="🔙 Ortga", callback_data="ortga")
# yegulik.adjust(2)
# # print(yegulik)


# ichimlik = ReadIchimlik()
# suv = InlineKeyboardBuilder()
# for suvv in ichimlik:
#     suv.button(text=f"{suvv[0]}", callback_data=f"{suvv[0]}")
# suv.button(text="🔙 Ortga", callback_data="ortga")
# suv.adjust(2)
# # print(suvv)


# zakuzka = ReadZakuska()
# zak = InlineKeyboardBuilder()
# for zakk in zakuzka:
#     zak.button(text=f"{zakk[0]}", callback_data=f"{zakk[0]}")
# zak.button(text="🔙 Ortga", callback_data="ortga")
# zak.adjust(2)


# from base import ReadTaomlar
# taomlars = len(ReadTaomlar())
# keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

# for taom in taomlars:
    # button = KeyboardButton(taom[0])
    # keyboard.add(button)
# print(keyboard)