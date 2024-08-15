import re

pattern = r'\b\d'

number_guests = int(input())
regular_guests = set()
vip_guests = set()

for _ in range(number_guests):
    reservation_code = input()

    if reservation_code:
        vip_guests.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

    # if reservation_code.startswith(chr(48), chr(57)):
    #     vip_guests.add(reservation_code)
    # else:
    #     regular_guests.add(reservation_code)
