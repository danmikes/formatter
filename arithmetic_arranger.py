import re

def arithmetic_arranger(problems, solve = False):

  first = ""
  second = ""
  lines = ""
  result = ""
  string = ""

  for problem in problems:
    if len(problems) > 4:
      return "Error: Too many problems."
    if re.search("[^\s0-9.+-]", problem):
      if re.search("[*/]", problem):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    operand1 = problem.split(' ')[0]
    operator = problem.split(' ')[1]
    operand2 = problem.split(' ')[2]

    if (len(operand2) > 4 or len(operand2) > 4):
      return "Error: Numbers cannot be more than four digits."

    if operator == '+':
      sum = str(int(operand1) + int(operand2))
    elif operator == '-':
      sum = str(int(operand1) - int(operand2))

    length = max(int(operand1), int(string))
    top = str(operand1).rjust(length)
    bottom = operator + str(operand2).rjust(length - 1)
    line = ""
    sum = str(sum).rjust(length)
    for s in range(length):
      line = line + ' '

    if problem != problems[-1]:
      first = first + top + ' '
      second = second + bottom + ' '
      lines = line + line + ' '
      result = result + sum + ' '
    else:
      first = first + top + ' '
      second = second + bottom + ' '
      lines = lines + line + ' '
      result = result + ' '

    if solve:
      string = first + '\n' + second + '\n' + lines + '\n' + result
    else:
      string = first + '\n' + second + '\n' + lines
    return string
