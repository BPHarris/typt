# Presentation example showing loop scopes

def int_list_to_string(my_list):
    return_value = '['

    for i in my_list:
        return_value += str(i) + ', '

    return_value += ']'

    # Uncomment to show error
    # print(i)

    return return_value


# Uncomment to show example
def second_example(s):
    if s == 'True':
        result = True
    return result


# Print list to show program execution
print(int_list_to_string(range(0, 5)))
# print(second_example('True'))
# print(second_example('False'))
