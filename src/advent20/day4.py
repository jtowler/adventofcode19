import re
from typing import List


def create_ppt(ppt: List[str]):
    d = {}
    for s in ppt:
        s = s.split(':')
        d[s[0]] = s[1]
    return d


def get_ppts(data: List[str]):
    ppts = []
    ppt = []
    for ln in data:
        if ln == '\n':
            ppts.append(create_ppt(ppt))
            ppt = []
        else:
            ppt += ln.rstrip('\n').split(' ')
    ppts.append(create_ppt(ppt))
    return ppts


def check_valid(d: dict, should_validate=False):
    for vk in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if vk not in d.keys():
            return False
    if should_validate:
        return validate(d)
    return True


def check_int_between(d, val, min_val, max_val):
    int_val = int(d[val])
    return (int_val < min_val) or (int_val > max_val)


def validate(d: dict):
    if check_int_between(d, 'byr', 1920, 2002):
        return False
    if check_int_between(d, 'iyr', 2010, 2020):
        return False
    if check_int_between(d, 'eyr', 2020, 2030):
        return False
    if 'cm' in d['hgt']:
        hgt = int(d['hgt'].rstrip('cm'))
        if (hgt < 150) or (hgt > 193):
            return False
    elif 'in' in d['hgt']:
        hgt = int(d['hgt'].rstrip('in'))
        if (hgt < 59) or (hgt > 76):
            return False
    else:
        return False
    if re.match('#[0-9a-f]{6}', d['hcl']) is None:
        return False
    if not d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if re.match('[0-9]{9}', d['pid']) is None:
        return False
    return True


if __name__ == '__main__':
    ppt_data = open("../../resources/advent20/input4.txt")
    ppts = get_ppts(ppt_data.readlines())
    print(sum([check_valid(ppt) for ppt in ppts]))
    print(sum([check_valid(ppt, True) for ppt in ppts]))
