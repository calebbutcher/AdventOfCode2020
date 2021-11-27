# Part 1
import re

# Opening input file and cleaning things up.

# Turning this: 
# byr:1971
# iyr:2017 hgt:160cm
# eyr:2020 ecl:hzl
# pid:157096267

# Into this: 
# ['byr:1971', 'iyr:2017', 'hgt:160cm', 'eyr:2020', 'ecl:hzl', 'pid:157096267']
with open('input.txt', 'r') as file:
    input = file.read().split('\n\n')
    input = [x.replace('\n', ' ').split() for x in input]

    #print(input[0])

    passports = []

    # Looping through our input array and splitting the values/labels by looking for ":" characters. 
    for person in input:
        passports.append(dict(data.split(':') for data in person))

    # Each entry now looks like this
    # {'byr': '1971', 'iyr': '2017', 'hgt': '160cm', 'eyr': '2020', 'ecl': 'hzl', 'pid': '157096267'}

    #print(passports[0])

    # Sorts out entries that are not length 8 or length 7 with the cid value missing since we are cheating to allow those
    passports = [x for x in passports if len(x.keys()) == 8 or (len(x) == 7 and 'cid' not in x.keys())]

    print("Part 1")
    print("Number of Valid Passports:", len(passports))

    # Part 2
    # Need to use regex to pattern match and validate data
    valid_passports = []
    values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for person in passports:
        if (1920 <= int(person['byr']) <= 2002
        and 2010 <= int(person['iyr']) <= 2020
        and 2020 <= int(person['eyr']) <= 2030
        and ((person['hgt'][-2:] == 'cm' and 150 <= int(person['hgt'][:-2]) <= 193) or (person['hgt'][-2:] == 'in' and 59 <= int(person['hgt'][:-2]) <= 76))
        and (re.match(r'#[\da-f]{6}', person['hcl']))
        and (person['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        and (re.match(r'\d{9}', person['pid']))
        and len(person['pid'])) == 9:
            valid_passports.append(person)
            
    print("Part 2")
    print("Number of Valid Passports:", len(valid_passports))     