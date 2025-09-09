
from address import Address
from mailing import Mailing

to_address = Address(4003030, "г. Волгоград", "ул. Родниковая", 130, 524)
from_address = Address(560236, "г. Москва", "ул. Веселая", 524, 320)
cost = "3344,55"
track = "tr 16523456"

mailing = Mailing(to_address, from_address, "334455", "tr 16523456")

print("Отправление", mailing.track, "из", from_address.index, from_address.city, from_address.street, from_address.house, from_address.flat, "в", to_address.index, to_address.city, to_address.street, to_address.house, to_address.flat, ".Стоимость", mailing.cost, "рублей")

