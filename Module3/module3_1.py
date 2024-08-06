calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    string = (len(string), string.upper(), string.lower())
    count_calls()
    return string

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)