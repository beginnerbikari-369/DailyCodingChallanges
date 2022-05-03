def check(string):
    round = 0
    curly = 0
    square = 0
    for i in range(len(string)):
        if string[i] == '(':
            round += 1
        elif string[i] == ')':
            round -= 1
        elif string[i] == '{':
            curly += 1
        elif string[i] == '}':
            curly -= 1
        elif string[i] == '[':
            square += 1
        elif string[i] == ']':
            square -= 1
    if round ==0 and curly == 0 and square == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    string = input()
    print(check(string))