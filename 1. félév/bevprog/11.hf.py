#1. hf
from collections import namedtuple

Airport = namedtuple('Airport', 'name city runways time')

def line_to_airport(line):
    line = line.split(';')
    Airport = namedtuple('Airport', 'name city runways time')
    return Airport(line[0],line[1],line[2],line[3])
    
def airport_to_line(airport):
    return f"{airport.name} ({airport.city}): {airport.time}"

szamok = []
def distinct_runways(airport):
    if(airport.runways not in szamok):
        szamok.append(airport.runways)

def read_airports_from_file():
    with open('alma.txt') as file:
        for line in file:
            elso = line_to_airport(line.strip('\n'))
            airport_to_line(elso)
            distinct_runways(elso)
    szamok.sort()
    print(*szamok, sep='\n')

def main():
    read_airports_from_file()
    
if __name__ == '__main__':
    main()

#2.hf
from collections import namedtuple

LegoSet = namedtuple('LegoSet', 'number name theme pieces')

def line_to_lego_set(line):
    number, name, theme, pieces = line.split(';')
    return LegoSet(number, name, theme, pieces)

def lego_set_to_line(lego_set):
    return f"{lego_set.name} ({lego_set.number}): {lego_set.pieces} - {lego_set.theme}"

themes = {}
def count_by_themes(lego_sets):
    if lego_sets.theme in themes:
            themes[lego_sets.theme] += 1
    else:
        themes[lego_sets.theme] = 1

def read_lego_sets_from_file():
    with open('alma.txt') as file:
        for line in file:
            lego_set = line_to_lego_set(line.strip('\n'))
            lego_set_to_line(lego_set)
            count_by_themes(lego_set)
    for(key, value) in themes.items():
        print(f"{key}: {value}")

def main():
    read_lego_sets_from_file()
    
if __name__ == '__main__':
    main()

#3. hf
from collections import namedtuple

Coupon = namedtuple('Coupon', 'store product discount')

def line_to_coupon(line):
    store, product, discount = line.split(';')
    return Coupon(store, product, discount)

def coupon_to_line(coupon):
    return f'{coupon.product} ({coupon.store}): {coupon.discount}%'

discounts = {}
def group_by_discounts(coupons):
    if coupons.discount not in discounts:
        discounts[coupons.discount] = [coupons]
    else:
        discounts[coupons.discount].append(coupons)

def read_coupons_from_file():
    with open('alma.txt') as file:
        for line in file:
            coupon = line_to_coupon(line.strip('\n'))
            coupon_to_line(coupon)
            group_by_discounts(coupon)
    for (key, value) in discounts.items():
        print(f"{key}")
        for coupon in value:
            print(f"{coupon.product} ({coupon.store}): {coupon.discount}%")
            
def main():
    read_coupons_from_file()
    
if __name__ == '__main__':
    main()
