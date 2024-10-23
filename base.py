from sqlite3 import Error, connect


def InsertUserlar(first_name):# first_name, telegram_id, url='None', username='None'
    try:
        c = connect('test.db')
        cursor = c.cursor()
        cursor.execute("""insert into userlar(first_name) values(?)""", (first_name,))
        c.commit()
        cursor.close()
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if c:
            c.close()
# InsertUserlar("Javohir")



def ReadObunachilar():
    try:
        c = connect('test.db')
        cursor = c.cursor()
        cursor.execute("select count(*) from userlar;")
        a = cursor.fetchall()
        cursor.close()
        return a
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if c:
            c.close()
# print(ReadObunachilar())


def ReadObunachilars():
    try:
        c = connect('test.db')
        cursor = c.cursor()
        cursor.execute("select * from userlar;")
        a = cursor.fetchall()
        cursor.close()
        return a
    except (Error, Exception) as eror:
        print("Eror", eror)
    finally:
        if c:
            c.close()



# try:
#     con = connect('test.db')
#     cursor = con.cursor()
#     cursor.execute("""
#             create table userlar(
#                 ID INTEGER PRIMARY KEY NOT NULL,           
#                 first_name text not null
#                 ); """)
#     con.commit()
#     cursor.close()
# except (Error, Exception) as eror:
#     print("Eror", eror)
# finally:
#     if con:
#         con.close()
#         print("Tugadi")






# def InsertSuv(nomi, photo_url, narxi):
    # try:
        # c = connect('mahsulot.db')
        # cursor = c.cursor()
        # cursor.execute("""insert into suv(nomi, photo_url, narxi) values(?, ?, ?)""", (nomi, photo_url, narxi))
        # c.commit()
        # cursor.close()
    # except (Error, Exception) as eror:
        # print("Eror", eror)
    # finally:
        # if c:
            # c.close()
# 
# InsertSuv('Hod dok','https://avatars.mds.yandex.net/i?id=d4a84fa33c77b74290c90e9c9446b5d2_l-9225598-images-thumbs&n=13',17000)


# def InsertTaomlar(nomi, photo_url, narxi):
#     try:
#         c = connect('mahsulot.db')
#         cursor = c.cursor()
#         cursor.execute("""insert into vodka(nomi, photo_url, narxi) values(?, ?, ?)""", (nomi, photo_url, narxi))
#         c.commit()
#         cursor.close()
#     except (Error, Exception) as eror:
#         print("Eror", eror)
#     finally:
#         if c:
#             c.close()

# InsertTaomlar("Fanta", 'https://media.istockphoto.com/id/477562540/photo/orange-fanta-can.jpg?s=612x612&w=0&k=20&c=NsviZAIWCuFeQ_eE-7BXXnAgIQf8FqlmLFv0ZTiaa50=', 12000)




# def ReadIchimlik():
    # try:
        # c = connect('drink.db')
        # cursor = c.cursor()
        # cursor.execute("select * from suv;")
        # a = cursor.fetchall()
        # cursor.close()
        # return a
    # except (Error, Exception) as eror:
        # print("Eror", eror)
    # finally:
        # if c:
            # c.close()
# print(ReadIchimlik())



# def ReadZakuzkalar():
    # try:
        # c = connect('zakuskalar.db')
        # cursor = c.cursor()
        # cursor.execute("select * from zakuskaa;")
        # a = cursor.fetchall()
        # cursor.close()
        # return a
    # except (Error, Exception) as eror:
        # print("Eror", eror)
    # finally:
        # if c:
            # c.close()

# qwerty = []
# for i in ReadZakuzkalar():
    # if i:
        # print(i[0])


# def Taom_Delete(nomi):
    # try:
        # con = connect("mahsulot.db")
        # cursor = con.cursor()
        # cursor.execute(f"delete from suv where nomi = {nomi};")
        # con.commit()
        # cursor.close()
    # except (Error, Exception) as eror:
        # print("Eror", eror)
    # finally:
        # if con:
            # con.close()
# print(Taom_Delete(nomi=""))


# def Zakuska_add(NOMI, PHOTO_URL, NARXI):
#     try:
#         con = connect("mahsulot.db")
#         cursor = con.cursor()
#         cursor.execute("INSERT INTO ZAKUSKA(NOMI, PHOTO_URL, NARXI) VALUES(?, ?, ?)", (NOMI, PHOTO_URL, NARXI))
#         con.commit()
#         cursor.close()
#     except (Error, Exception) as eror:
#         print("Eror", eror)
#     finally:
#         if con:
#             con.close()


# def Ichimlik_add(NOMI, PHOTO_URL, NARXI):
#     try:
#         con = connect("mahsulot.db")
#         cursor = con.cursor()
#         cursor.execute("INSERT INTO VODKA(NOMI, PHOTO_URL, NARXI) VALUES(?, ?, ?)", (NOMI, PHOTO_URL, NARXI))
#         con.commit()
#         cursor.close()
#     except (Error, Exception) as eror:
#         print("Eror", eror)
#     finally:
#         if con:
#             con.close()



# def Taom_add(NOMI, PHOTO_URL, NARXI):
#     try:
#         con = connect("mahsulot.db")
#         cursor = con.cursor()
#         cursor.execute("INSERT INTO SUV(NOMI, PHOTO_URL, NARXI) VALUES(?, ?, ?)", (NOMI, PHOTO_URL, NARXI))
#         con.commit()
#         cursor.close()
#     except (Error, Exception) as eror:
#         print("Eror", eror)
#     finally:
#         if con:
#             con.close()
        


# def ReadZakuska():
#     try:
#         c = connect('mahsulot.db')
#         cursor = c.cursor()
#         cursor.execute("select * from zakuska;")
#         a = cursor.fetchall()
#         cursor.close()
#         return a
#     except (Error, Exception) as eror:
#         print("Eror", eror)
#     finally:
#         if c:
#             c.close()
# # print(ReadZakuska())

# def ReadIchimlik():
#     try:
#         c = connect('mahsulot.db')
#         cursor = c.cursor()
#         cursor.execute("select * from vodka;")
#         a = cursor.fetchall()
#         cursor.close()
#         return a
#     except (Error, Exception) as eror:
#         print("Eror", eror)
#     finally:
#         if c:
#             c.close()
# # print(ReadIchimlik())

# def ReadTaomlar():
#     try:
#         c = connect('mahsulot.db')
#         cursor = c.cursor()
#         cursor.execute("select * from suv;")
#         a = cursor.fetchall()
#         cursor.close()
#         return a
#     except (Error, Exception) as eror:
#         print("Eror", eror)
#     finally:
#         if c:
#             c.close()
# print(ReadTaomlar())

# qwerty = []
# for taom in ReadTaomlar():
    # if taom:
        # qwerty = taom[0]
        # print(qwerty)


# def Suvv():
    # try:
        # con = connect('mahsulot.db')
        # cursor = con.cursor()
        # cursor.execute("""
            # CREATE TABLE vodka (
                # nomi TEXT NOT NULL,
                # photo_url TEXT NOT NULL,
                # narxi INTEGER NOT NULL
            # );
        # """)
        # con.commit()
        # cursor.close()
    # except (Error, Exception) as error:
        # print("Error:", error)
    # finally:
        # if con:
            # con.close()
            # print("Tugadi")
# Suvv()