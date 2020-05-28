#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .. import loader, utils
from ..loader import ModuleConfig as mc

import logging
import random

logger = logging.getLogger(__name__)


@loader.tds
class MiscMod(loader.Module):
    """Press F to pay Respect"""
    strings = {"name": "Press F to pay Respect"}

    def __init__(self):
        self.config = mc("VOLTE_TEXT", "Каждый человек выбирает себе в жизни ту систему отсчёта, в которой он занимает наивысшую позицию.  "
                         + "(Дура, 🏳️‍🌈🏳️‍🌈🏳️‍🌈 красивая), (пьяные и оборванные, зато духовные). Ислам - это такая штука, в которой очень много говорится о том, как хорошо быть "
                         + "праведным муслимом и как хуёво быть кяфиром, кото🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈рому и голову-то отрезать не грех. Это мировосприятие очень хорошо "
                         + "приживается в низших слоях общества, которые вроде и хотят отрезать головы тем, кто поумнее да побогаче, но как-то не за что. А "
                         + "ислам решае🏳️‍🌈🏳️‍🌈🏳️‍🌈т две их🏳️‍🌈 проблемы: новая система координат, в которой они - прав🏳️‍🌈оверные, прочие же - кяфиры и дегуманизирует "
                         + "этих самых кяфиров, ставя их рангом ни🏳️‍🌈же животных. Что, конечно же очень импонирует таджику-дворнику, считать животными "
                         + "всех нас вокруг, кто богаче и умнее, но, увы, неправеднее. Находясь у себя на цивилизованной родине эти ебалаи осознают, что "
                         + "находятся в меньшинстве🏳️‍🌈🏳️‍🌈v и не рыпаются. Но их обида на весь мир требует выхода, и да, в коране же написано - убей кяфира, "
                         + "соверши джихад. Поэтому эти дворники, продавцы, ассенизаторы, съезжаются в сирию, чтобы почувствовать себя великими.  "
                         + "отрезание голов величия лишь добавляет. Не было бы ислама, был бы коммунизм - проблема не в тоталитарном"
                         + "человеконенавистническом учении, а в спросе на него. "
                         + "Тут в ответ на открытое письмо в ответ на открытое письмо, народ зашевелился и вяло поддерживает Андрея Вадимовича - надо начинать с себя и типа царь не несёт ответственности за всех."
                         + "Охуенно. Я за !!!!! "
                         + "Но есть одно маленькое (но), постараюсь объяснить...."
                         + "Это так. Не спорю. Император не ссыт в подъездах. Так и я не ссу. Но ведь кто-то ссыт, раз тема поднята? Нахуя ко мне обращаться? Пусть обращаются к тем кто ссыт. Логично? "
                         + "Давайте разбираться, а кто ссыт-то?"
                         + "Вот я начал с себя, давным давно. Не ворую, не сру в подъездах, не жульничаю и всё делаю по совести. Но вагоны в Министерстве "
                         + "О как пиздили так и пиздят.🏳️‍🌈 Я начал с себя блядь и давным давно закончил."
                         + "Я теперь вроде правильный и живу по совести. Дальше что? Вагоны то пиздят? Их то не я спиздил, почему Андрей Вадимович ко "
                         + "мне обратился, а не взял и не написал прямым текстом - гос🏳️‍🌈🏳️‍🌈🏳️‍🌈подин, например Табур🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈еткин, не пизди вагоны....Люби людей и начни с себя, Табуреткин.... "
                         + "Вот и мой друг - не ворует, не пьёт, не давит людей на переходах, не режет национальные меньшинства, работает только на"
                         + "зарплату, а миллионы в Приморье как пиздили - так🏳️‍🌈 и пиздят. Ну исправил он себя, мой друг-то, а дорогу спиздили..."
                         + "Вот моя подруга - не ворует, не пьёт, не давит людей на переходах, не режет национальные меньшинства, работает только на "
                         + "зарплату, а некоторые как ездили на Лексусах с сиренами, так и ездят. Как давили людей на зебре - так и давят и не несут ответственности. Исправили мы себя, а Лексусы всё носятся с сиренами."
                         + "Но той гниде кто сбила детей приговор должен вынести судья, а он не выносит. Он отпускает. Плохой судья, взял денег? Плохой."
                         + "Давайте уберём и назначим другого, справедливого. Но не назначают. Почему? А ещё большая шишка его покрыла. Давайте уберём"
                         + "Император конечно же 🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈тут вроде ни при чём. "
                         + "большую шишку, чтобы можно было исправить малую. Но нет. Ещё большая шишка его покрыла. И рано или поздно мы утыкаемся"
                         + "угадайте куда. И тогда естественно мы бьём челом и просим того, кто последний в цепи. А нам говорят - Император ни при чём, НАЧНИ С СЕБЯ. И сбрасывают с вершины опять в засанный подъезд.... "
                         + "А когда мы немного возмущаемся, нам кидают злобное: - не раскачивай лодку...."
                         + "Вот стоит зассаный подъезд. Почему зассан? А потому что пьяное быдло его зассало, а участковый вместо того, чтобы вхуярить ему, этому быдлу, 15 суток и заставить вылизать и научить культуре, если этого не делает дебилоид, школа и семья - делает вид",
                         "", "F_LENGTHS", [5, 1, 1, 4, 1, 1, 1], "что подъезд в идеальной чистоте.", "BLUE_TEXT",
                         "/ХУЙ /ПИЗДА\n/ЯГЕЙЙ /ФИСТИНГ\n/ЯПИДОР /ЯХУЙ /Я /ХОЧУКАКАТЬ /ЯСАРАНЧА /ЯТУБЛИТУРАТОР /ЯАНИМЕ /МОЯВОЙФУ /БЛЯДЬ /РАДУЖНЫЕЦВЕТА",
                         "Залупа Заулпа !!!🏳️‍🌈!11!!1!1", "TEST", 
                         "──────────────────────────────\n──────█████───█████──█████────\n──────█──███──█──────█───█────\n──────████────████───█████────\n──────████────█──────█────────\n──────█──██───█──────█────────\n──────█───██──█████──█────────",  )

    def config_complete(self):
        self.name = self.strings["name"]

    @loader.unrestricted
    async def twrpcmd(self, message):
        """Отлетел вайфай и блютуз и все пизда Рулю"""
        await utils.answer(message, self.config["VOLTE_TEXT"])

    @loader.unrestricted
    async def fcmd(self, message):
        """Pays respects"""
        args = utils.get_args_raw(message)
        if not args:
            r = random.randint(0, 3)
            logger.debug(r)
            if r == 0:
                await utils.answer(message, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
            elif r == 1:
                await utils.answer(message, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
            else:
                args = "F"
        if args:
            out = ""
            for line in self.config["F_LENGTHS"]:
                c = max(round(line / len(args)), 1)
                out += (args * c) + "\n"
            await utils.answer(message, "<code>" + utils.escape_html(out) + "</code>")
    
    @loader.unrestricted
    async def fuckcmd(self, message):
        """Fuck"""
         await event.reply('┏━┳┳┳━┳┳┓\n┃━┫┃┃┏┫━┫┏┓\n┃┏┫┃┃┗┫┃┃┃┃\n┗┛┗━┻━┻┻┛┃┃\n┏┳┳━┳┳┳┓┏┫┣┳┓\n┃┃┃┃┃┃┃┃┣┻┫┃┃\n┣┓┃┃┃┃┣┫┃┏┻┻┫\n┗━┻━┻━┻┛┗━━━┛')
    
    @loader.unrestricted
    async def respectcmd(self, message):
        """Respect"""
        await utils.answer(message, self.config["TEST"])                                            
    @loader.unrestricted
    async def kashtomcmd(self, message):
        """Прошей свой анал даун"""
        await utils.answer(message, self.config["BLUE_TEXT"])
