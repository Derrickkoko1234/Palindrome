def reverse(num):
    str_num = str(num)
    numbers = []
    inverse_number = ''
    for i in str_num:
        numbers.append(i)

    no_of_items = len(numbers)

    stop = 0
    while no_of_items > 0:
        inverse_number = inverse_number + numbers[no_of_items - 1]
        no_of_items -= 1

    return inverse_number


def add_nums(num, num_reverse):
    answer = num + num_reverse
    return answer


start_number = 10
end_number = 1834
palindrone = open('palindrome.txt', 'a')
non_palindrone = open('non_palindrome.txt', 'a')

while start_number <= end_number:
    if int(start_number) != 196:
        pali_count = 0
        new_number = start_number
        while pali_count <= 20:
            if int(new_number) == int(reverse(new_number)):
                palindrone.write("{'Number': " + str(start_number) +
                                 ", 'Palindrone': 'Yes', 'Number of processes': " + str(pali_count) + "}\n")
                break
            elif pali_count > 20:
                palindrone.write("{'Number': " + str(start_number) +
                                 ", 'Palindrone': 'No', 'Number of processes': " + str(pali_count) + "}\n")
                # pali_count = "This number isn't a Palindrone"
                break
            else:
                new_number = add_nums(
                    int(new_number), int(reverse(new_number)))

            pali_count += 1
    else:
        pass
    start_number += 1

print(palindrone)
print(non_palindrone)
