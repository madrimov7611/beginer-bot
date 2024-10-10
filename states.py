from aiogram.fsm.state import State, StatesGroup

class Xabarlar(StatesGroup):
    xodim = State()
    yosh = State()
    texnologiya = State()
    telegram = State()
    aloqa = State()
    hudud = State()
    narxi = State()
    kasbi = State()
    murojat = State()
    maqsad = State()
    finish = State()
    finish1 = State()
    
class Xabar(StatesGroup):
    xodim = State()
    # yosh = State()
    texnologiya = State()
    telegram = State()
    aloqa = State()
    hudud = State()
    narxi = State()
    kasbi = State()
    murojat = State()
    maqsad = State()
    finish = State()
    finish1 = State()

# class ZakuskaADD(StatesGroup):
    # nomi = State()
    # url = State()
    # narxi = State()
    # finish = State()