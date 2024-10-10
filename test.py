# 👨‍💼 Xodim: Doston
# 🕑 Yosh: 19
# 📚 Texnologiya: Html, Css, Bootstrap, Tailwind, Javascript, React. Js, Node. Js, Firebase 
# 🇺🇿 Telegram: @Mc_dose 
# 📞 Aloqa: +998 93 094 78 79 
# 🌐 Hudud: Toshkent sh 
# 💰 Narxi: Amaliyot uchun  
# 🕰 Murojaat qilish vaqti: 8:00 - 13:00 
# 🔎 Maqsad: Maqsadim 1oy tekin amaliyotga ishlab keyingi oydan oyliklo ishga otisg 



# @dp.message(F.text, Xabarlar.maqsad)
# async def KinoNomi(message: Message, state: FSMContext, call: CallbackQuery):
#     maqsad = message.text
#     print(xabar)
#     await state.update_data(
#         {"maqsad":maqsad}
#     )
#     data = await state.get_data()
#     telegram = message.from_user.url
#     name = message.from_user.username
#     xodim = data.get('xodim')
#     yosh = data.get('yosh')
#     texnologiya = data.get('texnologiya')
#     aloqa = data.get('aloqa')
#     hudud = data.get('hudud')
#     narxi = data.get('narxi')
#     kasbi = data.get('kasbi')
#     murojat = data.get('murojat')
#     maqsad = data.get('maqsad')
#     await message.answer(f"Ish joyi kerak:\n\n👨‍💼 Xodim: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML")
#     await message.answer("Barcha ma'lumtlar to'g'rimi", reply_markup=tasdiq)
#     xabar = call.data
#     if xabar == 'ha':
#         await call.message.answer("Adminga yuborildi...")
#         await bot.send_message(chat_id=admin, text=f"Ish joyi kerak:\n\n👨‍💼 Xodim: {xodim}\n🕑 Yosh: {yosh}\n📚 Texnologiya: {texnologiya}\n🇺🇿 Telegram: <a href='{telegram}'>@{name}</a>\n📞 Aloqa: {aloqa}\n🌐 Hudud: {hudud}\n💰 Narxi: {narxi}\n👨🏻‍💻 Kasbi: {kasbi}\n🕰 Murojaat qilish vaqti: {murojat}\n🔎 Maqsad: {maqsad}", parse_mode="HTML")
#         await state.clear()
#     else:
#         await call.message.answer("Yuborilmadi!")
#         await state.clear()
#     await state.set_state(Xabarlar.finish)


