def rigth_operator(problems):
    for problem in problems:
        if (problem.find('+') != -1) ^ (problem.find('-') != -1): 
            pass
        else:
            return False
    return True

def only_digits(problems):
    for problem in problems:
        digits = problem.replace('+','').replace('-','').replace(' ','')
        if not digits.isdigit():
            return False
    return True

def max_four_digits(problems):
    for problem in problems:
        digits = problem.replace(' ','')
        if problem.find('-') != -1:
            first_number = digits[:problem.find('-')-1:]
            second_number = digits[problem.find('-')::]
            if (len(first_number) > 4) or (len(second_number)>4):
                return False
        elif problem.find('+') != -1:
            first_number = digits[:problem.find('+')-1:]
            second_number = digits[problem.find('+')::]
            if (len(first_number) > 4) or (len(second_number)>4):
                return False
    return True

def solution_unanswered(problems, show_answers):
    # Start in Black each line of string to print and the separator counter
    first_addends = ''
    second_addends = ''
    addition_line = ''
    answers = ''
    count = 1
    # Iterate over each problem
    for problem in problems:
        # Remove blank spaces
        numbers_and_operator = problem.replace(' ','')
        # Determine the operator and its position
        if (numbers_and_operator.find('-')!=-1):
            pos_operator = numbers_and_operator.find('-')
            operator = '-'
        else:
            pos_operator = numbers_and_operator.find('+')
            operator = '+'
        # Get the numbers to be added or subtracted
        first_number = numbers_and_operator[:pos_operator:]
        second_number = numbers_and_operator[pos_operator+1::]
        # Process the case where the first number is longer
        if (len(first_number) > len(second_number)):
            # Creating the first line of addends with the first number
            first_addends += '  ' + first_number
            # Creating second line of addends
            # ---- adding the operator in the second line of addends
            second_addends += operator
            # ---- blank spaces in the second line of addends
            for _ in range((len(first_number)-len(second_number)+1)):
                second_addends += ' '
            # ---- adding the second number in the second line of addends
            second_addends += second_number
            # Create the dividing line
            for _ in range((len(first_number)+2)):
                addition_line += '-'
            # Calculate the answer
            if operator == '-':
                answer = str(int(first_number) - int(second_number))
            else:
                answer = str(int(first_number) + int(second_number))
            # blank spaces in the line of answers
            for _ in range((len(first_number)-len(answer)+2)):
                answers += ' '
            # Add the answer in the line of answers
            answers += answer
        elif (len(first_number) < len(second_number)):
            for _ in range((len(second_number)-len(first_number)+2)):
                first_addends += ' '
            first_addends += first_number
            second_addends += operator + ' ' + second_number
            for _ in range((len(second_number)+2)):
                addition_line += '-'     
            if operator == '-':
                answer = str(int(first_number) - int(second_number))
            else:
                answer = str(int(first_number) + int(second_number))
            for _ in range((len(second_number)-len(answer)+2)):
                answers += ' '
            answers += answer
        elif (len(first_number) == len(second_number)):
            first_addends += '  ' + first_number
            second_addends += operator + ' ' + second_number
            for _ in range((len(second_number)+2)):
                addition_line += '-'
            if operator == '-':
                answer = str(int(first_number) - int(second_number))
            else:
                answer = str(int(first_number) + int(second_number))
            for _ in range((len(first_number)-len(answer)+2)):
                answers += ' '
            answers += answer
        # Create 4 blank separators on each line of text
        if (len(problems) > count):
            first_addends += '    '
            second_addends += '    '
            addition_line += '    '
            answers += '    '
            count += 1
    # returning the response with or without a result
    if show_answers:
        return first_addends + '\n' + second_addends + '\n' + addition_line + '\n' + answers
    else:
        return first_addends + '\n' + second_addends + '\n' + addition_line

def arithmetic_arranger(problems, show_answers=False):
    if(len(problems)>5):
        return ('Error: Too many problems.')
    elif not rigth_operator(problems):
        return ("Error: Operator must be '+' or '-'.")
    elif not only_digits(problems):
        return ('Error: Numbers must only contain digits.')
    elif not max_four_digits(problems):
        return ('Error: Numbers cannot be more than four digits.')
    else:
        solution = solution_unanswered(problems, show_answers)
        return solution

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
