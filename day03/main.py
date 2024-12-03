import re


def parse_mul_expr(expr: str) -> int:
    nums = re.findall(r"(\d+)+", expr)
    print(f"expr: {expr}, nums: {nums}")
    
    if (len(nums) != 2):
        print(expr)
        print(nums)
        raise ValueError(f"Invalid expression: {expr}")
    return int(nums[0]) * int(nums[1])



with open("input.txt", "r") as f:
    data = f.read()
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    total = 0
    enable = True
    for match in matches:
       if match == "don't()":
           enable = False
           continue
       elif match == "do()":
           enable = True
           continue
       elif enable:
           total += parse_mul_expr(match)
    print(total)




