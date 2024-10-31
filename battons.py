from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


tasdiqlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data='ha'), InlineKeyboardButton(text="❌ Bekor qilish", callback_data='yoq')]
    ]
)


tasdiq = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha", callback_data='haa'), InlineKeyboardButton(text="Yoq", callback_data='yoqq')]
    ]
)

# ortgaaa = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Ortga", callback_data="ortga")]
#     ]
# )


ortgaaaa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ortga")]
    ],
    resize_keyboard=True
)


tell = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Raqamni ulashish", request_contact=True)]
    ],
    resize_keyboard=True
)


habarlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Sherik kerak", callback_data='sherik'), InlineKeyboardButton(text="Ish joyi kerak", callback_data='ish')],
        [InlineKeyboardButton(text="Hodim kerak", callback_data='hodim'), InlineKeyboardButton(text="Ustoz kerak", callback_data='ustoz')],
        [InlineKeyboardButton(text="Shogirt garak",callback_data='shoggi')]
    ]
)


adminlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Username", callback_data='userr'), InlineKeyboardButton(text="Obuna soni", callback_data='obuna')],
    ]
)
