import asyncio
import logging
from states import Xabarlar, Xabar
from aiogram import types
from aiogram import Bot, Dispatcher, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command, CommandStart
from config import tokenn , a
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from battons import habarlar, tasdiq, tasdiqla


logging.basicConfig(level=logging.INFO)
bot = Bot(token=tokenn,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Assalomu aleykum {message.from_user.first_name}\n\nUstoz shoggi botiga hush kelibsiz?", reply_markup=habarlar)
    await message.delete()


@dp.callback_query(F.data=="ish")
async def Taomlar_Add(call: CallbackQuery, state:FSMContext):
    await call.message.answer("Ish joyi topish uchun ariza berish:\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await call.message.answer("Ism, familyangizni yuboring ⤵️")
    await state.set_state(Xabarlar.xodim)


@dp.message(F.text, Xabarlar.xodim)
async def TaomNomi(message: Message, state: FSMContext):
    xodim = message.text
    await state.update_data(
        {"xodim":xodim}
    )
    await message.answer("🕑 Yosh:\n\nYoshingizni kiriting ? ⤵️")
    await state.set_state(Xabarlar.yosh)


@dp.message(F.text, Xabarlar.yosh)
async def TaomNomi(message: Message, state: FSMContext):
    yosh = message.text
    await state.update_data(
        {"yosh":yosh}
    )
    await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?Texnologiya nomlarini vergul bilan ajrating. Masalan:\n\nJava, C++, C# ⤵️")
    await state.set_state(Xabarlar.texnologiya)


@dp.message(F.text, Xabarlar.texnologiya)
async def TaomNomi(message: Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya":texnologiya}
    )
    await message.answer("📞 Aloqa:\n\nBog`lanish uchun raqamingizni kiriting?\nMasalan: +998 90 123 45 67 ⤵️")
    await state.set_state(Xabarlar.aloqa)


@dp.message(F.text, Xabarlar.aloqa)
async def TaomNomi(message: Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(
        {"aloqa":aloqa}
    )
    await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
    await state.set_state(Xabarlar.hudud)


@dp.message(F.text, Xabarlar.hudud)
async def TaomNomi(message: Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud":hudud}
    )
    await message.answer("💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting? ⤵️")
    await state.set_state(Xabarlar.narxi)


@dp.message(F.text, Xabarlar.narxi)
async def TaomNomi(message: Message, state: FSMContext):
    narxi = message.text
    await state.update_data(
        {"narxi":narxi}
    )
    await message.answer("👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan: Talaba ⤵️")
    await state.set_state(Xabarlar.kasbi)


@dp.message(F.text, Xabarlar.kasbi)
async def TaomNomi(message: Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi":kasbi}
    )
    await message.answer("🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan: 9:00 - 18:00 ⤵️")
    await state.set_state(Xabarlar.murojat)


@dp.message(F.text, Xabarlar.murojat)
async def TaomNomi(message: Message, state: FSMContext):
    murojat = message.text
    await state.update_data(
        {"murojat":murojat}
    )
    await message.answer("🔎 Maqsad: Maqsadingizni qisqacha yozib bering. ⤵️")
    await state.set_state(Xabarlar.maqsad)


@dp.message(F.text, Xabarlar.maqsad)
async def KinoNomiiiii(message: Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {"maqsad":maqsad}
    )
    data = await state.get_data()
    telegram = message.from_user.url
    name = message.from_user.username
    xodim = data.get('xodim')
    yosh = data.get('yosh')
    texnologiya = data.get('texnologiya')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    narxi = data.get('narxi')
    kasbi = data.get('kasbi')
    murojat = data.get('murojat')
    maqsad = data.get('maqsad')
    await message.answer(f"Ish joyi kerak:\n\n👨‍💼 Xodim: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML")
    await message.answer("Barcha ma'lumtlar to'g'rimi", reply_markup=tasdiq)
    await state.set_state(Xabarlar.finish)


@dp.callback_query(F.data, Xabarlar.finish)
async def Finish(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    data = await state.get_data()
    telegram = call.from_user.url
    name = call.from_user.username
    xodim = data.get('xodim')
    yosh = data.get('yosh')
    texnologiya = data.get('texnologiya')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    narxi = data.get('narxi')
    kasbi = data.get('kasbi')
    murojat = data.get('murojat')
    maqsad = data.get('maqsad')
    if xabar == 'ha':
        await call.message.answer("Adminga yuborildi...")
        await bot.send_message(chat_id=a[0], text=f"Ish joyi kerak:\n\n👨‍💼 Xodim: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML", reply_markup=tasdiqla)
    else:
        await call.message.answer("Yuborilmadi!")
    await state.clear


@dp.callback_query(F.data)
async def Finishsh(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    if xabar == 'ha':
        await call.message.answer("Gruppaga yuborildi")
        await call.message.send_copy(chat_id=-1002467871625, reply_markup=ReplyKeyboardRemove())
    else:
        await call.message.answer("Yuborilmadi!")




@dp.callback_query(F.data=="sherik")
async def Taomlar_Add(call: CallbackQuery, state:FSMContext):
    await call.message.answer("Sherik topish uchun ariza berish:\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await call.message.answer("Ism, familyangizni yuboring?")
    await state.set_state(Xabar.xodim)


@dp.message(F.text, Xabar.xodim)
async def TaomNomi(message: Message, state: FSMContext):
    xodim = message.text
    await state.update_data(
        {"yosh":xodim}
    )
    await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?Texnologiya nomlarini vergul bilan ajrating. Masalan:\n\nJava, C++, C# ⤵️")
    await state.set_state(Xabar.texnologiya)


@dp.message(F.text, Xabar.texnologiya)
async def TaomNomi(message: Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya":texnologiya}
    )
    await message.answer("📞 Aloqa:\n\nBog`lanish uchun raqamingizni kiriting?\nMasalan: +998 90 123 45 67 ⤵️")
    await state.set_state(Xabar.aloqa)


@dp.message(F.text, Xabar.aloqa)
async def TaomNomi(message: Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(
        {"aloqa":aloqa}
    )
    await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
    await state.set_state(Xabar.hudud)


@dp.message(F.text, Xabar.hudud)
async def TaomNomi(message: Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud":hudud}
    )
    await message.answer("💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting? ⤵️")
    await state.set_state(Xabar.narxi)


@dp.message(F.text, Xabar.narxi)
async def TaomNomi(message: Message, state: FSMContext):
    narxi = message.text
    await state.update_data(
        {"narxi":narxi}
    )
    await message.answer("👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan: Talaba ⤵️")
    await state.set_state(Xabar.kasbi)


@dp.message(F.text, Xabar.kasbi)
async def TaomNomi(message: Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi":kasbi}
    )
    await message.answer("🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan: 9:00 - 18:00 ⤵️")
    await state.set_state(Xabar.murojat)


@dp.message(F.text, Xabar.murojat)
async def TaomNomi(message: Message, state: FSMContext):
    murojat = message.text
    await state.update_data(
        {"murojat":murojat}
    )
    await message.answer("🔎 Maqsad: Maqsadingizni qisqacha yozib bering. ⤵️")
    await state.set_state(Xabar.maqsad)


@dp.message(F.text, Xabar.maqsad)
async def KinoNomiiiii(message: Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {"maqsad":maqsad}
    )
    data = await state.get_data()
    telegram = message.from_user.url
    name = message.from_user.username
    xodim = data.get('xodim')
    texnologiya = data.get('texnologiya')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    narxi = data.get('narxi')
    kasbi = data.get('kasbi')
    murojat = data.get('murojat')
    maqsad = data.get('maqsad')
    await message.answer(f"Ish joyi kerak:\n\n🏅 Sherik:{xodim}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML")
    await message.answer("Barcha ma'lumtlar to'g'rimi", reply_markup=tasdiq)
    await state.set_state(Xabar.finish)


@dp.callback_query(F.data, Xabar.finish)
async def Finish(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    data = await state.get_data()
    telegram = call.from_user.url
    name = call.from_user.username
    xodim = data.get('xodim')
    texnologiya = data.get('texnologiya')
    aloqa = data.get('aloqa')
    hudud = data.get('hudud')
    narxi = data.get('narxi')
    kasbi = data.get('kasbi')
    murojat = data.get('murojat')
    maqsad = data.get('maqsad')
    if xabar == 'ha':
        await call.message.answer("Adminga yuborildi...")
        await bot.send_message(chat_id=a[0], text=f"Ish joyi kerak:\n\n👨‍💼 Xodim: {xodim}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML", reply_markup=tasdiqla)
    else:
        await call.message.answer("Yuborilmadi!")
    await state.clear


@dp.callback_query(F.data)
async def Finishsh(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    if xabar == 'ha':
        await call.message.answer("Gruppaga yuborildi")
        await call.message.send_copy(chat_id=-1002467871625, reply_markup=ReplyKeyboardRemove())
    else:
        await call.message.answer("Yuborilmadi!")





# @dp.callback_query(F.data, Xabarlar.finish)
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


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Tugadi")