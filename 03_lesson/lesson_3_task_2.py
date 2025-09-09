from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Huawei nova 10 Pro", "GLA-LX1", "+79033717545")
phone2 = Smartphone("Nokia", "106 DS", "+79033717777")
phone3 = Smartphone("OPPO", "A5x", "+79063828545")
phone4 = Smartphone("Redmi", "14C", "+79098546363")
phone5 = Smartphone("Meizu", "Mblu 21", "+79196542365")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog: print(f"{phone.brand} {phone.model} - {phone.phone_number}")
