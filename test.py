from base import ReadObunachilars

# @dp.callback_query(F.d○ata, Xabarlar.finish)
# async def KinolarFinish(call: CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     kino_nomi = data.get('nomi')
#     kino_des = data.get('url')
#     kino_url = data.get('narxi')
#     xabar = call.data
#     if xabar == 'ha':
#         Taom_add(NOMI=kino_nomi, PHOTO_URL=kino_des, NARXI=kino_url)
#         await call.answer("Taom muafaqiyatli qo'shildi ")
#         await state.clear()
#         await call.message.delete()

#     else:
#         await call.answer("Taom qo'shilmadi")
#         await state.clear()
#         await call.message.delete()



# @dp.callback_query(F.data == "call")
# async def BoglanishBot(call: CallbackQuery):
#     user_phone = "+998997487611"
#     url = "@telfonlar_bozori_Bot"
#     user_url = "@madrimovjavohir"
#     await call.message.answer(f"📞 Telfon: {user_phone}\n📍 Telegram: {url}\n✉️ Admin: {user_url}\n\n💬 Novvi kamchilikla bolsa yozib qoldiriringlo ⤵️")
    
#     await call.message.delete()


# @dp.callback_query(F.data == "ortga")
# async def OrtgaBot(call: CallbackQuery):
#     await call.message.answer_photo(photo="https://media.licdn.com/dms/image/v2/D5612AQFaEcVPcxUT9w/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1693211333774?e=2147483647&v=beta&t=Z2wA6gMQ4AKNlp0JL8eguiE4k9fGFw61O75CN2FJqhI", caption="Bosh sahifaga qaytdingiz", reply_markup=menyu)
#     await call.message.delete()


# @dp.callback_query(F.data == "taom")
# async def TaomlarBot(call: CallbackQuery):
#     await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=221a8997b63b1e03d6b51584f7293f26_l-5315900-images-thumbs&n=13", caption="Bizda mavjud taomlar", reply_markup=yegulik.as_markup())
#     await call.message.delete()


# @dp.callback_query(F.data == "ichimlik")
# async def IchimlikBot(call: CallbackQuery):
#     await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSItESPNRbAW2y3L4jHwV0Pwo87gtfDRx7dvw&s", caption="Bizda mavjud ichimliklar", reply_markup=suv.as_markup())
#     await call.message.delete()


# @dp.callback_query(F.data == "zakus")
# async def ZakuzkaBot(call: CallbackQuery):
#     await call.message.answer_photo(photo="https://i.ytimg.com/vi/Ju8xb6zmZaY/maxresdefault.jpg", caption="Bizda mavjud zakuzkalar", reply_markup=zak.as_markup())
#     await call.message.delete()


# @dp.message(F.text == "admin")
# async def QoshishBot(message: types. Message):
#     telegram_id = message.from_user.id
#     if telegram_id == admin:
#         await message.answer(f"Nima qo'shamiz", reply_markup=taom)
#         await message.delete()


# @dp.callback_query(F.data=="taomm", F.from_user.id == admin)
# async def Taomlar_Add(call: CallbackQuery, state:FSMContext):
#     await call.message.answer("Taom nomini yuboring ⤵️")
#     await state.set_state(TaomADD.nomi)


# @dp.message(F.text, TaomADD.nomi)
# async def TaomNomi(message: Message, state: FSMContext):
#     taom_nomi = message.text
#     await state.update_data(
#         {"nomi":taom_nomi}
#     )
#     await message.answer("Taom rasmini url yuboring ⤵️")
#     await state.set_state(TaomADD.url)


# @dp.message(F.text, TaomADD.url)
# async def TaomNomi(message: Message, state: FSMContext):
#     url = message.text
#     await state.update_data(
#         {"url":url}
#     )
#     await message.answer("Taom narxini yuboring ⤵️")
#     await state.set_state(TaomADD.narxi)


# @dp.message(F.text, TaomADD.narxi)
# async def KinoNomi(message: Message, state: FSMContext):
#     taom_narxi = message.text
#     await state.update_data(
#         {"narxi":taom_narxi}
#     )
#     data = await state.get_data()
#     nomi = data.get('nomi')
#     url = data.get('url')
#     await message.answer_photo(photo=url, caption=f"Nomi: {nomi}\nNarxi: {taom_narxi}", reply_markup=tasdiqlash)
#     await state.set_state(TaomADD.finish)


# @dp.callback_query(F.data, TaomADD.finish)
# async def KinolarFinish(call: CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     kino_nomi = data.get('nomi')
#     kino_des = data.get('url')
#     kino_url = data.get('narxi')
#     xabar = call.data
#     if xabar == 'ha':
#         Taom_add(NOMI=kino_nomi, PHOTO_URL=kino_des, NARXI=kino_url)
#         await call.answer("Taom muafaqiyatli qo'shildi ")
#         await state.clear()
#         await call.message.delete()
#     else:
#         await call.answer("Taom qo'shilmadi")
#         await state.clear()
#         await call.message.delete()


# @dp.callback_query(F.data)
# async def TaomlarBot(call: CallbackQuery):
#     xabar = call.data
#     # print(xabar)
#     builder = InlineKeyboardBuilder()
#     for i in range(1, 13):
#         builder.add(types.InlineKeyboardButton(text=str(i), callback_data=str(i)))
#     builder.add(types.InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga"))
#     builder.adjust(4)
#     for taom in ReadTaomlar():
#         if taom[0] == xabar:
            # await call.message.answer_photo(photo=f"{taom[1]}", caption=f"Maxsulot: {taom[0]}\nNarxi: {taom[2]}", reply_markup=builder.as_markup())
#             await call.message.delete()

#     builderr = InlineKeyboardBuilder()
#     for a in range(1, 13):
#         builderr.add(types.InlineKeyboardButton(text=str(a), callback_data=str(a)))
#     builderr.add(types.InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga"))
#     builderr.adjust(4)
#     for taomm in ReadIchimlik():
#         if taomm[0] == xabar:
#             await call.message.answer_photo(photo=f"{taomm[1]}", caption=f"Maxsulot: {taomm[0]}\nNarxi: {taomm[2]}", reply_markup=builderr.as_markup())
#             await call.message.delete()

#         builderrr = InlineKeyboardBuilder()
#     for b in range(1, 13):
#         builderrr.add(types.InlineKeyboardButton(text=str(b), callback_data=str(b)))
#     builderrr.add(types.InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga"))
#     builderrr.adjust(4)
#     for taommm in ReadZakuska():
#         if taommm[0] == xabar:
#             await call.message.answer_photo(photo=f"{taommm[1]}", caption=f"Maxsulot: {taommm[0]}\nNarxi: {taommm[2]}", reply_markup=builderrr.as_markup())
#             await call.message.delete()





# Xodim kerak:

# 🏢 Idora: Webcoder
# 📚 Texnologiya: React, React-native, Javascript 
# 🇺🇿 Telegram: @Anvar_developer 
# 📞 Aloqa: +998 88 135 31 30 
# 🌐 Hudud: Toshkent sh
# ✍️ Mas'ul: Anvar
# 🕰 Murojaat vaqti: 9:00 - 18:00 
# 🕰 Ish vaqti: 9:00 - 18:00 
# 💰 Maosh: amaliyot
# ‼️ Qo`shimcha: Kim o'z ustida ishlamoqchi bo'lsa va portfoliyoga ega bo'lmoqchi bo'lsa amaliyotga taklif qilamiz





# @dp.message(Form.phone)
# async def TelRaqam(message: Message, state: FSMContext):
#     if message.contact:
#         phone_number = message.contact.phone_number
#         if phone_number.startswith("998") or phone_number.startswith("+998"):
#             await state.update_data(phone_number=phone_number)
#             await message.answer("▫️ Yoshingizni tanlang.", reply_markup=yosh)
#             await state.set_state(Form.age)
#         else:
#             await message.answer(
#                 text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
#                 reply_markup=ReplyKeyboardRemove(),
#             )
#             await state.clear()
    # elif message.text:
    #     r = message.text.replace("+", "")
    #     if len(message.text) == 12 or len(message.text) == 13:
    #         if (str(r).startswith("998")) or str(r).startswith("+998"):
    #             await state.update_data(phone_number=message.text)
    #             await message.answer("▫️ Yoshingizni tanlang.", reply_markup=yosh)
    #             await state.set_state(Form.age)
    #         else:
    #             await message.answer(
    #                 text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
    #                 reply_markup=ReplyKeyboardRemove(),
    #             )
    #             await state.clear()
    #     else:
    #         await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yuboring.</b>")

    # else:
    #     await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yubioring</b>")


# for ii in ReadObunachilars():
#     obunachilar = ii[2]
#     print(obunachilar)


    # telegram = call.from_user.url
    # name = call.from_user.username
    # xabar = call.data
    # builder = InlineKeyboardBuilder()
    # for i in range(1, 13):
    #     builder.add(types.InlineKeyboardButton(text=str(i), callback_data=str(i)))
    # builder.add(types.InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga"))
    # builder.adjust(4)
    # for taom in ReadTaomlar():
    #     if taom[0] == xabar:
    #         await call.message.answer_photo(photo=f"{taom[1]}", caption=f"Maxsulot: {taom[0]}\nNarxi: {taom[2]}", reply_markup=builder.as_markup())
    #         call.message.delete()



# from telegram import ParseMode
# from telegram.ext import Updater, CommandHandler

# def mention_user(update, context):
#  user_id = 6004741215  # Replace with the actual user ID
#  mention_string = f'<a href="tg://user?id={user_id}">User</a>'

#  context.bot.send_message(chat_id=update.message.chat_id, text=mention_string, parse_mode=ParseMode.HTML)

# def main():
#  updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
#  dp = updater.dispatcher

#  dp.add_handler(CommandHandler('mention', mention_user))

#  updater.start_polling()
#  updater.idle()

# if __name__ == '__main__':
#  main()



# import re

# pattern = '[0-9]'
# test_string = '100'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	















# @dp.message(F.contact, Xabarlar.aloqa)
# async def TaomNomi(message: Message, state: FSMContext):
#     if message.contact:
#         phone_number = message.contact.phone_number
#         if phone_number.startswith("998") or phone_number.startswith("+998"):
#             await state.update_data(
#                 {"aloqa":phone_number}
#             )
#             await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️", reply_markup=ReplyKeyboardRemove())
#             await state.set_state(Xabarlar.hudud)
#         else:
#             await message.answer(
#                 text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
#                 reply_markup=ReplyKeyboardRemove(),
#             )
#             await state.clear()

#     elif message.text:
#         r = message.text.replace("+", "")
#         if len(message.text) == 12 or len(message.text) == 13:
#             if (str(r).startswith("998")) or str(r).startswith("+998"):
#                 await state.update_data(
#                     {"aloqa":message.text}
#                 )
#                 await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
#                 await state.set_state(Xabarlar.hudud)
#             else:
#                 await message.answer(
#                     text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
#                     reply_markup=ReplyKeyboardRemove(),
#                 )
#                 await state.clear()
#         else:
#             await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yuboring.</b>")

#     else:
#         await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yubioring</b>")




# @dp.message(F.contact, Xabar.aloqa)
# async def TaomNomi(message: Message, state: FSMContext):
#     if message.contact:
#         phone_number = message.contact.phone_number
#         if phone_number.startswith("998") or phone_number.startswith("+998"):
#             await state.update_data(
#                 {"aloqa":phone_number}
#             )
#             await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
#             await state.set_state(Xabar.hudud)
#         else:
#             await message.answer(
#                 text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
#                 reply_markup=ReplyKeyboardRemove(),
#             )
#             await state.clear()

#     elif message.text:
#         r = message.text.replace("+", "")
#         if len(message.text) == 12 or len(message.text) == 13:
#             if (str(r).startswith("998")) or str(r).startswith("+998"):
#                 await state.update_data(
#                     {"aloqa":message.text}
#                 )
#                 await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
#                 await state.set_state(Xabar.hudud)
#             else:
#                 await message.answer(
#                     text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
#                     reply_markup=ReplyKeyboardRemove(),
#                 )
#                 await state.clear()
#         else:
#             await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yuboring.</b>")

#     else:
#         await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yubioring</b>")
