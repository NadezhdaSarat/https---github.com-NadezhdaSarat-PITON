from operator import index

from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 4003030, "г. Волгоград", "ул. Родниковая", 130, 524
from_address = 560236, "г. Москва", "ул. Веселая", 524, 320
sending = Mailing
sending(to_address, from_address, "334455", "tr 16523456")

print("Отправление", sending.track, "из", from_address, "в", to_address, ".Стоимость", sending.cost, "рублей")

