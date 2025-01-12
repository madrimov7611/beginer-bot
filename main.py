import asyncio
import logging
import re
from base import InsertUserlar, ReadObunachilar, ReadObunachilars
from states import Xabarlar, Xabar, Xabar1, Xabar2, Xabar3, Rekla
from aiogram import types
from aiogram import Bot, Dispatcher, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command, CommandStart
from config import tokenn , admins
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from battons import habarlar, tasdiq, tasdiqlash, ortgaaaa, tell, adminlar



logging.basicConfig(level=logging.INFO)
bot = Bot(token=tokenn,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()



@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    first_name = message.from_user.first_name
    username = message.from_user.username
    user_url = message.from_user.url
    if message.from_user.id == admins[0]:
        await message.answer("Qanday eee 👋\n\nNima qilamiz ich qisib getdi qu ♠", reply_markup=adminlar)
        await state.set_state(Rekla.abc1)
    else:
        a = []
        for i in ReadObunachilars():
            a.append(i[1])
        if first_name in a:
            pass
        else:
            InsertUserlar(first_name=first_name, username=username, user_url=user_url)
        await message.answer(f"Assalomu aleykum {message.from_user.first_name}👋\n\nUstoz shoggi botiga hush kelibsiz?", reply_markup=habarlar)
        await message.delete()



# @dp.callback_query(F.data == "rek", Rekla.abc1)
# async def Obunachilar(call: CallbackQuery):
#     await call.message.answer("yuboring: ")

# @dp.message(F.text)
# async def Obunachilar(mess: Message):
#     for ii in ReadObunachilars():
#         await mess.send_copy(chat_id=admins)
#     await mess.answer("yuborildi")



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
    if yosh.isdigit():
        await state.update_data(
            {"yosh":yosh}
        )
        await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?Texnologiya nomlarini vergul bilan ajrating. Masalan:\n\nJava, C++, C# ⤵️")
        await state.set_state(Xabarlar.texnologiya)
    else:
        await message.answer("Text yubormang ❌\nYoshingizni yuboring !")
        await state.set_state(Xabarlar.yosh)


@dp.message(F.text, Xabarlar.texnologiya)
async def TaomNomi(message: Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya":texnologiya}
    )
    await message.answer("📞 Aloqa:\n\nBog`lanish uchun raqamni ulashishni bosing", reply_markup=tell)
    await message.answer(f"Agar telegramdagi no'merda muammo bo'sa\nyozib yuborishingiz mumkin\n\nMasalan: +998 90 123 45 67 ")
    await state.set_state(Xabarlar.aloqa)


@dp.message(F.contact, Xabarlar.aloqa)
async def TaomNomi(message: Message, state: FSMContext):
    if message.contact:
        phone_number = message.contact.phone_number
        if phone_number.startswith("998") or phone_number.startswith("+998"):
            await state.update_data(
                {"aloqa":phone_number}
            )
            await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️", reply_markup=ReplyKeyboardRemove())
            await state.set_state(Xabarlar.hudud)
        else:
            await message.answer(
                text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                reply_markup=ReplyKeyboardRemove(),
            )
            await state.clear()

    elif message.text:
        r = message.text.replace("+", "")
        if len(message.text) == 12 or len(message.text) == 13:
            if (str(r).startswith("998")) or str(r).startswith("+998"):
                await state.update_data(
                    {"aloqa":message.text}
                )
                await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
                await state.set_state(Xabarlar.hudud)
            else:
                await message.answer(
                    text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await state.clear()
        else:
            await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yuboring.</b>")

    else:
        await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yubioring</b>")



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
    # if narxi.isdigit():
    await state.update_data(
        {"narxi":narxi}
    )
    await message.answer("👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan: Talaba ⤵️")
    await state.set_state(Xabarlar.kasbi)
    # else:
    #     await message.answer("Son ko'rinishida yuboring !")
    #     await state.set_state(Xabarlar.narxi)


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
    await message.answer("🔎 Maqsad:\n\nMaqsadingizni qisqacha yozib bering. ⤵️")
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
    if xabar == 'haa':
        await call.message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!", reply_markup=ortgaaaa)
        await bot.send_message(chat_id=admins[0], text=f"Ish joyi kerak:\n\n👨‍💼 Xodim: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML", reply_markup=tasdiqlash)
    else:
        await state.clear()
        await call.message.answer("Yuborilmadi!", reply_markup=ortgaaaa)
        await call.message.delete()        


@dp.callback_query(F.data == "ha")
async def Finishsh(call: CallbackQuery):
    xabar = call.data
    if xabar == 'ha':
        await call.message.answer("Gruppaga yuborildi")
        await call.message.send_copy(chat_id= -1002467871625, reply_markup=ReplyKeyboardRemove())
        await call.message.delete()
    else:
        await call.message.answer("Yuborilmadi!")



@dp.callback_query(F.data == "sherik")
async def Taomlar_Add(call: CallbackQuery, state:FSMContext):
    await call.message.answer("Sherik topish uchun ariza berish:\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await call.message.answer("Ism, familyangizni yuboring?")
    await state.set_state(Xabar.xodim)


@dp.message(F.text, Xabar.xodim)
async def TaomNomi(message: Message, state: FSMContext):
    xodim = message.text
    await state.update_data(
        {"xodim":xodim}
    )
    await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?Texnologiya nomlarini vergul bilan ajrating. Masalan:\n\nJava, C++, C# ⤵️")
    await state.set_state(Xabar.texnologiya)


@dp.message(F.text, Xabar.texnologiya)
async def TaomNomi(message: Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya":texnologiya}
    )
    await message.answer("📞 Aloqa:\n\nBog`lanish uchun raqamni ulashishni bosing", reply_markup=tell)
    await message.answer(f"Agar telegramdagi no'merda muammo bo'sa\nyozib yuborishingiz mumkin\n\nMasalan: +998 90 123 45 67 ")
    await state.set_state(Xabar.aloqa)


@dp.message(F.contact, Xabar.aloqa)
async def TaomNomi(message: Message, state: FSMContext):
    if message.contact:
        phone_number = message.contact.phone_number
        if phone_number.startswith("998") or phone_number.startswith("+998"):
            await state.update_data(
                {"aloqa":phone_number}
            )
            await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
            await state.set_state(Xabar.hudud)
        else:
            await message.answer(
                text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                reply_markup=ReplyKeyboardRemove(),
            )
            await state.clear()

    elif message.text:
        r = message.text.replace("+", "")
        if len(message.text) == 12 or len(message.text) == 13:
            if (str(r).startswith("998")) or str(r).startswith("+998"):
                await state.update_data(
                    {"aloqa":message.text}
                )
                await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
                await state.set_state(Xabar.hudud)
            else:
                await message.answer(
                    text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await state.clear()
        else:
            await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yuboring.</b>")

    else:
        await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yubioring</b>")


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
    # if narxi.isdigit():
    await state.update_data(
        {"narxi":narxi}
    )
    await message.answer("👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan: Talaba ⤵️")
    await state.set_state(Xabar.kasbi)
    # else:
    #     await message.answer("Son ko'rinishida yuboring !")
    #     await state.set_state(Xabarlar.narxi)


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
    await message.answer("🔎 Maqsad:\n\nMaqsadingizni qisqacha yozib bering. ⤵️")
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
    await message.answer(f"Sherik kerak:\n\n🏅 Sherik: {xodim}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML")
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
    if xabar == 'haa':
        await call.message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!")
        await bot.send_message(chat_id=admins[0], text=f"Sherik kerak:\n\n🏅 Sherik: {xodim}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML", reply_markup=tasdiqlash)
    else:
        await state.clear()
        await call.message.answer("Yuborilmadi!", reply_markup=ortgaaaa)
        await call.message.delete()


@dp.callback_query(F.data == "ha")
async def Finishsh(call: CallbackQuery):
    xabar = call.data
    if xabar == 'ha':
        await call.message.answer("Gruppaga yuborildi")
        await call.message.send_copy(chat_id=-1002467871625, reply_markup=ReplyKeyboardRemove())
    else:
        await call.message.answer("Yuborilmadi!")



@dp.callback_query(F.data == "hodim")
async def Taomlar_Add(call: CallbackQuery, state:FSMContext):
    await call.message.answer("Xodim topish uchun ariza berish:\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa,\nHA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await call.message.answer("🎓 Idora nomi?")
    await state.set_state(Xabar1.xodim)


@dp.message(F.text, Xabar1.xodim)
async def TaomNomi(message: Message, state: FSMContext):
    xodim = message.text
    await state.update_data(
        {"xodim":xodim}
    )
    await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?Texnologiya nomlarini vergul bilan ajrating. Masalan:\n\nJava, C++, C# ⤵️")
    await state.set_state(Xabar1.texnologiya)


@dp.message(F.text, Xabar1.texnologiya)
async def TaomNomi(message: Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya":texnologiya}
    )
    await message.answer("📞 Aloqa:\n\nBog`lanish uchun raqamni ulashishni bosing", reply_markup=tell)
    await message.answer(f"Agar telegramdagi no'merda muammo bo'sa\nyozib yuborishingiz mumkin\n\nMasalan: +998 90 123 45 67 ")
    await state.set_state(Xabar1.aloqa)


@dp.message(F.contact, Xabar1.aloqa)
async def TaomNomi(message: Message, state: FSMContext):
    if message.contact:
        phone_number = message.contact.phone_number
        if phone_number.startswith("998") or phone_number.startswith("+998"):
            await state.update_data(
                {"aloqa":phone_number}
            )
            await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
            await state.set_state(Xabar1.hudud)
        else:
            await message.answer(
                text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                reply_markup=ReplyKeyboardRemove(),
            )
            await state.clear()

    elif message.text:
        r = message.text.replace("+", "")
        if len(message.text) == 12 or len(message.text) == 13:
            if (str(r).startswith("998")) or str(r).startswith("+998"):
                await state.update_data(
                    {"aloqa":message.text}
                )
                await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
                await state.set_state(Xabar1.hudud)
            else:
                await message.answer(
                    text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await state.clear()
        else:
            await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yuboring.</b>")

    else:
        await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yubioring</b>")


@dp.message(F.text, Xabar1.hudud)
async def TaomNomi(message: Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud":hudud}
    )
    await message.answer("✍️Mas'ul ism sharifi?")
    await state.set_state(Xabar1.narxi)


@dp.message(F.text, Xabar1.narxi)
async def TaomNomi(message: Message, state: FSMContext):
    maqsad = message.text
    await state.update_data(
        {"qoshimcha":maqsad}
    )
    await message.answer("🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await state.set_state(Xabar1.kasbi)


@dp.message(F.text, Xabar1.kasbi)
async def TaomNomi(message: Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi":kasbi}
    )
    await message.answer("🕰 Ish vaqtini kiriting?")
    await state.set_state(Xabar1.murojat)


@dp.message(F.text, Xabar1.murojat)
async def TaomNomi(message: Message, state: FSMContext):
    murojat = message.text
    await state.update_data(
        {"murojat":murojat}
    )
    await message.answer("💰 Maoshni kiriting?")
    await state.set_state(Xabar1.maqsad)


@dp.message(F.text, Xabar1.maqsad)
async def KinoNomiiiii(message: Message, state: FSMContext):
    narxi = message.text
    # if narxi.isdigit():
    await state.update_data(
        {"narxi":narxi}
    )
    await message.answer("‼️ Qo`shimcha ma`lumotlar?")
    await state.set_state(Xabar1.finish)
    # else:
    #     await message.answer("Son ko'rinishida yuboring !")
    #     await state.set_state(Xabar1.maqsad)



@dp.message(F.text, Xabar1.finish)
async def KinoNomiiiii(message: Message, state: FSMContext):
    maqsadd = message.text
    await state.update_data(
        {"maqsad":maqsadd}
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
    qoshim = data.get('qoshimcha')
    await message.answer(f"Xodim kerak:\n\n🏢 Idora: {xodim}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n✍️ Mas'ul: {narxi}\n🕰 Murojaat vaqti: {kasbi}\n🕰 Ish vaqti: {murojat}\n💰 Maosh: {maqsad}\n‼️ Qo`shimcha: {qoshim}", parse_mode="HTML")
    await message.answer("Barcha ma'lumtlar to'g'rimi", reply_markup=tasdiq)
    await state.set_state(Xabar1.finish1)


@dp.callback_query(F.data, Xabar1.finish1)
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
    qoshim = data.get('qoshimcha')
    if xabar == 'haa':
        await call.message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!")
        await bot.send_message(chat_id=admins[0], text=f"Xodim kerak:\n\n🏢 Idora: {xodim}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n✍️ Mas'ul: {narxi}\n🕰 Murojaat vaqti: {kasbi}\n🕰 Ish vaqti: {murojat}\n💰 Maosh: {maqsad}\n‼️ Qo`shimcha: {qoshim}", parse_mode="HTML", reply_markup=tasdiqlash)
    else:
        await state.clear()
        await call.message.answer("Yuborilmadi!", reply_markup=ortgaaaa)
        await call.message.delete()


@dp.callback_query(F.data == "ha")
async def Finishsh(call: CallbackQuery):
    xabar = call.data
    if xabar == 'ha':
        await call.message.answer("Gruppaga yuborildi")
        await call.message.send_copy(chat_id=-1002467871625, reply_markup=ReplyKeyboardRemove())
    else:
        await call.message.answer("Yuborilmadi!")



@dp.callback_query(F.data=="ustoz")
async def Taomlar_Add(call: CallbackQuery, state:FSMContext):
    await call.message.answer("Ustoz topish uchun ariza berish:\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa,\nHA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await call.message.answer("Ism, familyangizni kiriting?")
    await state.set_state(Xabar2.xodim)


@dp.message(F.text, Xabar2.xodim)
async def TaomNomi(message: Message, state: FSMContext):
    xodim = message.text
    await state.update_data(
        {"xodim":xodim}
    )
    await message.answer("🕑 Yosh:\n\nYoshingizni kiriting ? ⤵️")
    await state.set_state(Xabar2.yosh)


@dp.message(F.text, Xabar2.yosh)
async def TaomNomi(message: Message, state: FSMContext):
    yosh = message.text
    if yosh.isdigit():
        await state.update_data(
            {"yosh":yosh}
        )
        await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?Texnologiya nomlarini vergul bilan ajrating. Masalan:\n\nJava, C++, C# ⤵️")
        await state.set_state(Xabar2.texnologiya)
    else:
        await message.answer("Text yubormang ❌\nYoshingizni yuboring !")
        await state.set_state(Xabar2.yosh)


@dp.message(F.text, Xabar2.texnologiya)
async def TaomNomi(message: Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya":texnologiya}
    )
    await message.answer("📞 Aloqa:\n\nBog`lanish uchun raqamni ulashishni bosing", reply_markup=tell)
    await message.answer(f"Agar telegramdagi no'merda muammo bo'sa\nyozib yuborishingiz mumkin\n\nMasalan: +998 90 123 45 67 ")
    await state.set_state(Xabar2.aloqa)


@dp.message(F.text, Xabar2.aloqa)
async def TaomNomi(message: Message, state: FSMContext):
    if message.contact:
        phone_number = message.contact.phone_number
        if phone_number.startswith("998") or phone_number.startswith("+998"):
            await state.update_data(
                {"aloqa":phone_number}
            )
            await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
            await state.set_state(Xabar2.hudud)
        else:
            await message.answer(
                text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                reply_markup=ReplyKeyboardRemove(),
            )
            await state.clear()

    elif message.text:
        r = message.text.replace("+", "")
        if len(message.text) == 12 or len(message.text) == 13:
            if (str(r).startswith("998")) or str(r).startswith("+998"):
                await state.update_data(
                    {"aloqa":message.text}
                )
                await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
                await state.set_state(Xabar2.hudud)
            else:
                await message.answer(
                    text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await state.clear()
        else:
            await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yuboring.</b>")

    else:
        await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yubioring</b>")


@dp.message(F.text, Xabar2.hudud)
async def TaomNomi(message: Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud":hudud}
    )
    await message.answer("💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting? ⤵️")
    await state.set_state(Xabar2.narxi)


@dp.message(F.text, Xabar2.narxi)
async def TaomNomi(message: Message, state: FSMContext):
    narxi = message.text
    # if narxi.isdigit():
    await state.update_data(
        {"narxi":narxi}
    )
    await message.answer("👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan: Talaba ⤵️")
    await state.set_state(Xabar2.kasbi)
    # else:
    #     await message.answer("Son ko'rinishida yuboring !")
    #     await state.set_state(Xabar2.narxi)


@dp.message(F.text, Xabar2.kasbi)
async def TaomNomi(message: Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi":kasbi}
    )
    await message.answer("🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan: 9:00 - 18:00 ⤵️")
    await state.set_state(Xabar2.murojat)


@dp.message(F.text, Xabar2.murojat)
async def TaomNomi(message: Message, state: FSMContext):
    murojat = message.text
    await state.update_data(
        {"murojat":murojat}
    )
    await message.answer("🔎 Maqsad: Maqsadingizni qisqacha yozib bering. ⤵️")
    await state.set_state(Xabar2.maqsad)


@dp.message(F.text, Xabar2.maqsad)
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
    await message.answer(f"Ustoz kerak:\n\n🎓 Shogird: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML")
    await message.answer("Barcha ma'lumtlar to'g'rimi", reply_markup=tasdiq)
    await state.set_state(Xabar2.finish)


@dp.callback_query(F.data, Xabar2.finish)
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
    if xabar == 'haa':
        await call.message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!")
        await bot.send_message(chat_id=admins[0], text=f"Ustoz kerak:\n\n🎓 Shogird: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML", reply_markup=tasdiqlash)
    else:
        await state.clear()
        await call.message.answer("Yuborilmadi!", reply_markup=ortgaaaa)
        await call.message.delete()


@dp.callback_query(F.data == "ha")
async def Finishsh(call: CallbackQuery):
    xabar = call.data
    if xabar == 'ha':
        await call.message.answer("Gruppaga yuborildi")
        await call.message.send_copy(chat_id= -1002467871625, reply_markup=ReplyKeyboardRemove())
    else:
        await call.message.answer("Yuborilmadi!")



@dp.callback_query(F.data=="shoggi")
async def Taomlar_Add(call: CallbackQuery, state:FSMContext):
    await call.message.answer("Shogird topish uchun ariza berish:\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa,\nHA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await call.message.answer("Ism, familyangizni kiriting?")
    await state.set_state(Xabar3.xodim)


@dp.message(F.text, Xabar3.xodim)
async def TaomNomi(message: Message, state: FSMContext):
    xodim = message.text
    await state.update_data(
        {"xodim":xodim}
    )
    await message.answer("🕑 Yosh:\n\nYoshingizni kiriting ? ⤵️")
    await state.set_state(Xabar3.yosh)


@dp.message(F.text, Xabar3.yosh)
async def TaomNomi(message: Message, state: FSMContext):
    yosh = message.text
    if yosh.isdigit():
        await state.update_data(
            {"yosh":yosh}
        )
        await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?Texnologiya nomlarini vergul bilan ajrating. Masalan:\n\nJava, C++, C# ⤵️")
        await state.set_state(Xabarlar.texnologiya)
    else:
        await message.answer("Text yubormang ❌\nYoshingizni yuboring !")
        await state.set_state(Xabar3.yosh)


@dp.message(F.text, Xabar3.texnologiya)
async def TaomNomi(message: Message, state: FSMContext):
    texnologiya = message.text
    await state.update_data(
        {"texnologiya":texnologiya}
    )


    if message.contact:
        phone_number = message.contact.phone_number
        if phone_number.startswith("998") or phone_number.startswith("+998"):
            await state.update_data(
                {"aloqa":phone_number}
            )
            await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
            await state.set_state(Xabar3.hudud)
        else:
            await message.answer(
                text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                reply_markup=ReplyKeyboardRemove(),
            )
            await state.clear()

    elif message.text:
        r = message.text.replace("+", "")
        if len(message.text) == 12 or len(message.text) == 13:
            if (str(r).startswith("998")) or str(r).startswith("+998"):
                await state.update_data(
                    {"aloqa":message.text}
                )
                await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
                await state.set_state(Xabar3.hudud)
            else:
                await message.answer(
                    text="<b>🙅‍♂️ Bot faqat O'zbekiston fuqarolari uchun ishlaydi.</b>",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await state.clear()
        else:
            await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yuboring.</b>")

    else:
        await message.answer(text="<b>⚠️ Faqat telefon raqamingizni yubioring</b>")


@dp.message(F.text, Xabar3.aloqa)
async def TaomNomi(message: Message, state: FSMContext):
    aloqa = message.text
    await state.update_data(
        {"aloqa":aloqa}
    )
    await message.answer("🌐 Hudud:\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting. ⤵️")
    await state.set_state(Xabar3.hudud)


@dp.message(F.text, Xabar3.hudud)
async def TaomNomi(message: Message, state: FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud":hudud}
    )
    await message.answer("💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting? ⤵️")
    await state.set_state(Xabar3.narxi)


@dp.message(F.text, Xabar3.narxi)
async def TaomNomi(message: Message, state: FSMContext):
    narxi = message.text
    # if narxi.isdigit():
    await state.update_data(
        {"narxi":narxi}
    )
    await message.answer("👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan: Talaba ⤵️")
    await state.set_state(Xabar3.kasbi)
    # else:
    #     await message.answer("Son ko'rinishida yuboring !")
    #     await state.set_state(Xabar3.narxi)


@dp.message(F.text, Xabar3.kasbi)
async def TaomNomi(message: Message, state: FSMContext):
    kasbi = message.text
    await state.update_data(
        {"kasbi":kasbi}
    )
    await message.answer("🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan: 9:00 - 18:00 ⤵️")
    await state.set_state(Xabar3.murojat)


@dp.message(F.text, Xabar3.murojat)
async def TaomNomi(message: Message, state: FSMContext):
    murojat = message.text
    await state.update_data(
        {"murojat":murojat}
    )
    await message.answer("🔎 Maqsad: Maqsadingizni qisqacha yozib bering. ⤵️")
    await state.set_state(Xabar3.maqsad)


@dp.message(F.text, Xabar3.maqsad)
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
    await message.answer(f"Shogird kerak:\n\n🎓 Ustoz: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML")
    await message.answer("Barcha ma'lumtlar to'g'rimi", reply_markup=tasdiq)
    await state.set_state(Xabar3.finish)


@dp.callback_query(F.data, Xabar3.finish)
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
    if xabar == 'haa':
        await call.message.answer("📪 So`rovingiz tekshirish uchun adminga jo`natildi!")
        await bot.send_message(chat_id=admins[0], text=f"Ustoz kerak:\n\n🎓 Shogird: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML", reply_markup=tasdiqlash)
    else:
        await state.clear()
        await call.message.answer("Yuborilmadi!", reply_markup=ortgaaaa)
        await call.message.delete()


@dp.callback_query(F.data == "ha")
async def Finishsh(call: CallbackQuery):
    xabar = call.data
    if xabar == 'ha':
        await call.message.answer("Gruppaga yuborildi")
        await call.message.send_copy(chat_id= -1002467871625, reply_markup=ReplyKeyboardRemove())
    else:
        await call.message.answer("Yuborilmadi!")


@dp.callback_query(F.data == "reklama")
async def Obunachilar(call: CallbackQuery):
    ii = []
    for i in ReadObunachilars():
        ii.append(i[3])
        await bot.send_photo(chat_id=ii, photo="https://pbs.twimg.com/media/FzjzGjWXsAEn7kb.jpg")
        # await call.message.answer(f"Obunachilaringiz soni: {obunachilar}")



@dp.callback_query(F.data == "obuna")
async def Obunachilar(call: CallbackQuery):
    for ii in ReadObunachilar():
        obunachilar = ii[0]
        await call.message.answer(f"Obunachilaringiz soni: {obunachilar}")


@dp.callback_query(F.data == "username")
async def Obunachilar(call: CallbackQuery):
    for ii in ReadObunachilars():
        await call.message.answer(f"Obunachilarning ismi: <a href='{ii[3]}'> {ii[1]}</a>")


@dp.message(F.text == "ortga")
async def ortga_start(message: Message):
    await message.answer(f"Bosh sahifaga qaytdingiz", reply_markup=habarlar)
    await message.delete()


@dp.callback_query(F.data == "ortga")
async def ortga_start(call: CallbackQuery):
    if call.message.from_user.id != admins[0]:
        await call.message.answer(f"Bosh sahifaga qaytdingiz", reply_markup=habarlar)
        await call.message.delete()
    else:
        await call.message.answer_photo(photo="https://st2.depositphotos.com/1002277/10073/i/450/depositphotos_100732302-stock-photo-word-admin-on-wood-planks.jpg")



async def main():
    # await bot.send_message(chat_id=admins[0],text="Salom Javohir men yana ishga tushdim")
    await dp.start_polling(bot)

async def error():
    # await bot.send_message(chat_id=admins[0],text="Men ishimni tugatdim🤣")
    await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        asyncio.run(error())
        print("Tugadi")