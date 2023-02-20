# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1]. char, next):
                return i+1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    check = input()
    if "F" in check:
        text = input()
        with open(text, "r", encoding="ISO-8859-1") as file:
            module = file.read()
        mismatch = find_mismatch(module)
        if mismatch == "Success" :
            print("Success")
        else:
            print(mismatch)
    elif "I" in check:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Success" :
            print("Success")
        else:
            print(mismatch)
    else:
        mismatch = find_mismatch(check)
        print(mismatch)

main()
