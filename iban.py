

COUNTRIES = {
     'AL': ("Albania", 28),
     'AD': ("Andorra", 24),
     'AT': ("Austria", 20),
     'AZ': ("Azerbaijan", 28),
     'BH': ("Bahrain", 22),
     'BY': ("Belarus", 28),
     'BE': ("Belgium", 16),
     'BA': ("Bosnia and Herzegovina", 20),
     'BR': ("Brazil", 29),
     'BG': ("Bulgaria", 22),
     'CR': ("Costa Rica", 22),
     'HR': ("Croatia", 21),
     'CY': ("Cyprus", 28),
     'CZ': ("Czech Republic", 24),
     'DK': ("Denmark", 18),
     'DO': ("Dominican Republic", 28),
     'TL': ("East Timor", 23),
     'EG': ("Egypt", 29),
     'SV': ("El Salvador", 28),
     'EE': ("Estonia", 20),
     'FO': ("Faroe Islands", 18),
     'FI': ("Finland", 18),
     'FR': ("France", 27),
     'GE': ("Georgia", 22),
     'DE': ("Germany", 22),
     'GI': ("Gibraltar", 23),
     'GR': ("Greece", 27),
     'GL': ("Greenland", 18),
     'GT': ("Guatemala", 28),
     'HU': ("Hungary", 28),
     'IS': ("Iceland", 26),
     'IQ': ("Iraq", 23),
     'IE': ("Ireland", 22),
     'IL': ("Israel", 23),
     'IT': ("Italy", 27),
     'JO': ("Jordan", 30),
     'KZ': ("Kazakhstan", 20),
     'XK': ("Kosovo", 20),
     'KW': ("Kuwait", 30),
     'LV': ("Latvia", 21),
     'LB': ("Lebanon", 28),
     'LY': ("Libya", 25),
     'LI': ("Liechtenstein", 21),
     'LT': ("Lithuania", 20),
     'LU': ("Luxembourg", 20),
     'MK': ("North Macedonia", 19),
     'MT': ("Malta", 31),
     'MR': ("Mauritania", 27),
     'MU': ("Mauritius", 30),
     'MC': ("Monaco", 27),
     'MD': ("Moldova", 24),
     'ME': ("Montenegro", 22),
     'NL': ("Netherlands", 18),
     'NO': ("Norway", 15),
     'PK': ("Pakistan", 24),
     'PS': ("Palestinian territories", 29),
     'PL': ("Poland", 28),
     'PT': ("Portugal", 25),
     'QA': ("Qatar", 29),
     'RO': ("Romania", 24),
     'RU': ("Russia", 29),
     'LC': ("Saint Lucia", 32),
     'SM': ("San Marino", 27),
     'ST': ("São Tomé and Príncipe", 25),
     'SA': ("Saudi Arabia", 24),
     'RS': ("Serbia", 22),
     'SC': ("Seychelles", 31),
     'SK': ("Slovakia", 24),
     'SI': ("Slovenia", 19),
     'ES': ("Spain", 24),
     'SD': ("Sudan", 18),
     'SE': ("Sweden", 24),
     'CH': ("Switzerland", 21),
     'TN': ("Tunisia", 24),
     'TR': ("Turkey", 26),
     'UA': ("Ukraine", 29),
     'AE': ("United Arab Emirates", 23),
     'GB': ("United Kingdom", 22),
     'VA': ("Vatican City", 22),
     'VG': ("British Virgin Islands", 24)
}

LETTERS = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35
    }


def check_iban(iban):
    iban_list = []
    char = iban[0] + iban[1]
    key = char
    if key in COUNTRIES:
        for i in iban:
            if i != ' ':
                iban_list.append(i)
        length = COUNTRIES.get(char)[1]
        if len(iban_list) == length: 
            for j in range(4):
                iban_list.append(iban_list[j])
            del iban_list[0:4]
            for l, k in enumerate(iban_list):
                for letter, number in LETTERS.items():
                    if k == letter:
                        del iban_list[l]
                        iban_list.insert(l, str(number))
            iban_list = int("".join(iban_list))
            if iban_list % 97 == 1:
                return True
            else:
                return False
        else: 
            return False
    else:
        return False
