
Student: Nihad abdulla
  2- ci mesele
  
  integer = input()
while not (integer.isdigit()):
    print("only number are allowed")
    print("Type any number here")
    integer = input()

ones = {'0': '', '1': 'bir ', '2': 'iki ', '3': 'uc ', '4': 'dord ', '5': 'bes ', '6': 'alti ', '7': 'yeddi ', '8': 'sekkiz ',
        '9': 'doqquz '}

teens = {'0': 'on', '1': 'onbir ', '2': 'oniki ', '3': 'onuc ', '4': 'ondord ', '5': 'onbes ', '6': 'onalti ', '7': 'onyeddi ', '8': 'onsekkiz ',
        '9': 'ondoqquz '}

decades = {'0': '', '2': 'iyrimi ', '3': 'otuz ', '4': 'qirx ', '5': 'elli ', '6': 'altimis ', '7': 'yetmis ', '8': 'seksen ',
        '9': 'doxsan '}


hundreds = {'0': '', '1': 'yuz ', '2': 'iki yuz ', '3': 'uc yuz ', '4': 'dord yuz ', '5': 'bes yuz ', '6': 'alti yuz ', '7': 'yeddi yuz ', '8': 'sekkiz yuz ',
        '9': 'doqquz yuz '}


comma_word = {'3': 'min,', '6': 'milyon,', '9': 'milyard, ' }

word = ''
integer_side = integer
int_length = len(integer)
integer_change = len(integer)
change = 3
while integer_change > 0:
    if integer == '0':
        word = 'sifir'
        break
    if integer_side[integer_change - 2] == '1':
        for digit in teens:
            if integer_side[integer_change - 1] == digit:
                word = teens[digit] + word
    else:
        for digit_1 in ones:
            if integer_side[integer_change - 1] == digit_1:
                word = ones[digit_1] + word
        if integer_change > 1:
            for digit_2 in decades:
                if integer_side[integer_change - 2] == digit_2:
                    word = decades[digit_2] + word
    if integer_change > 2:
        for digit_3 in hundreds:
            if integer_side[integer_change - 3] == digit_3:
                word = hundreds[digit_3] + word
    if integer_change > 3:
        word = comma_word[str(change)] + word

    change = change + 3
    integer_change = integer_change - 3

print(word)
