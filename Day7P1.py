puzzle_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


#Operators used are only + and *, 
#from a set of numbers and a target value, find the operators that would make the target value
#e.g; 190: 10 19 --> 10 * 19, 3267: 81 40 27 --> 81 * 40 + 27
#It can also not work for some of the numbers and the target values
#Sum the target values that work.



puzzle_input = puzzle_input.splitlines()


# print(puzzle_input[1])

hashmap={}

for equation in puzzle_input:
    target_number, test_values = equation.split(":")  # Unpack the split result
    target_number = int(target_number)
    test_values = test_values.lstrip()
    test_values = test_values.split(" ")
    test_values_int = list(map(int, test_values))
    hashmap[target_number] = test_values_int

def check_if_correct(target, values):
    if sum(values) == target:
        return target

    



correct_numbers=[]
for key,values in hashmap.items():
    correct_number = check_if_correct(key,values)
    correct_numbers.append(correct_number)

sum(correct_numbers)