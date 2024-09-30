calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return((len(string), string.upper(), string.lower()))


def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    list_to_search = [s.upper() for s in list_to_search]
    return string in list_to_search


print(string_info('Gladiator'))
print(string_info('Paradigma'))
print(string_info('Ironman'))

print(is_contains('Manhattan', ['hattan', 'Man', 'ManHaTTaN']))
print(is_contains('Oppengeimer', ['open', 'OpeNGeimeR', 'gamer']))
print(is_contains('Palindrom', ['palmir', 'PalinDROM', 'linda']))

print(calls)
