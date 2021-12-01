fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} #, 'cid'}


def solve_a(passports: list):
    """Check passports are valid"""
    valid_passports = 0
    for passport in passports:
        total_fields = 0
        l = []
        for x in passport.split():
            l.extend(x.split('\n'))
        for field in l:
            if field.split(":")[0] in fields:
                total_fields += 1
                if total_fields == len(fields):
                    valid_passports += 1

    return valid_passports


def solve_b(passports: list):
    """Check passports are more valid"""

    def field_valid(key, value) -> bool:
        if key == 'byr':
            return 1920 <= int(value) <= 2002
        elif key == 'iyr':
            return 2010 <= int(value) <= 2020
        elif key == 'eyr':
            return 2020 <= int(value) <= 2030
        elif key == 'hgt':
            if 'cm' in value:
                return 150 <= int(value.rstrip('cm')) <= 193
            elif 'in' in value:
                return 59 <= int(value.rstrip('in')) <= 76
        elif key == 'hcl':
            valid_chars = 'abcdef0123456789'
            for i, c in enumerate(value):
                if i == 0:
                    if c != "#":
                        return False
                elif c not in valid_chars:
                    return False
            return True
        elif key == 'ecl':
            return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        elif key == 'pid':
            return value.isnumeric() and len(value) == 9
        else:
            return False

    valid_passports = 0
    for passport in passports:
        valid_fields = 0
        l = []
        for x in passport.split():
            l.extend(x.split('\n'))
        for field in l:
            split = field.split(':')
            if field_valid(*split):
                valid_fields += 1
            else:
                print(field)
        if valid_fields == len(fields):
            valid_passports += 1

    return valid_passports


if __name__ == '__main__':
    passports = open("4.txt").read().split("\n\n")
    print(solve_a(passports))
    print(solve_b(passports))

