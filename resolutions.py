from itertools import islice, product

def parse_file(file):
    lines = iter(file)
    next(lines) # Discard the number of test cases T

    while lines:
        target = next(lines)
        food_count = int(next(lines))
        foods = islice(lines, food_count)
        yield format_testcase(target, foods)

def format_testcase(target, foods):
    return {
        'target': format_macronutrients(target),
        'foods': [format_macronutrients(food) for food in foods],
    }

def format_macronutrients(macronutrients):
    return tuple(int(nutrient) for nutrient in macronutrients.split(' '))

def evaluate_testcase(testcase):
    target = testcase['target']
    foods = testcase['foods']

    for combination in product((True, False), repeat=len(foods)):
        selected_foods = [food for index, food in enumerate(foods) if combination[index]]
        total = tuple(sum(nutrients) for nutrients in zip(*selected_foods))
    
        if total == target:
            return 'yes'

    return 'no'

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        for index, testcase in enumerate(parse_file(file)):
            print 'Case #{n}: {result}'.format(
                n=index+1,
                result=evaluate_testcase(testcase),
            )
