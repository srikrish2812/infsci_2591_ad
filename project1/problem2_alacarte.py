def get_sign_strings(num1,num2):
    is_negative = (num1<0) ^ (num2<0)
    s1, s2 = str(abs(num1)), str(abs(num2))
    return is_negative, s1, s2

def alacarte_multiply(num1,num2):
    if num1 == 0 or num2 == 0:
        return 0
    
    is_negative, s1, s2 = get_sign_strings(num1,num2)
    total=0
    # i am multiplying each digit of num2 with num1 and adding the results together
    # i am iterating through multiplier digits from right to lft
    for i, digit2 in enumerate(reversed(s2)):
        carry=0
        curr_part = 0
        d2 = int(digit2)
        # i am multiplying multiplicand by the single digit
        for j, digit1 in enumerate(reversed(s1)):
            d1 = int(digit1)
            product = d1 * d2 + carry
            carry = product // 10
            curr_part += (product % 10) * (10 ** j)
        
        if carry > 0:
            curr_part += carry * (10 ** len(s1))
            
        total += curr_part * (10 ** i)
    
    if is_negative:
        return -total
    return total

if __name__ == "__main__":
    test_cases_p2 = [
        (7000, 7294),
        (25, 5038385),
        (-59724, 783),
        (8516, -82147953548159344),
        (45952456856498465985, 98654651986546519856),
        (-45952456856498465985, -98654651986546519856)
    ]
    print("--- Problem 2 Alacarte Results ---")
    for idx, (num1, num2) in enumerate(test_cases_p2):
        result = alacarte_multiply(num1, num2)
        print(f"Test Case {idx+1}: \n  Num1: {num1}\n  Num2: {num2}\n  Product: {result}\n")