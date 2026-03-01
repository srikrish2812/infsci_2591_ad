def get_signs_strings(num1,num2):
    is_negative = (num1<0) ^ (num2<0)
    s1, s2 = str(abs(num1)), str(abs(num2))
    return is_negative, s1, s2

def rectangle_multiply(num1,num2):
    if num1 == 0 or num2 == 0:
        return 0
    
    is_negative, s1, s2 = get_signs_strings(num1,num2)
    len1, len2 = len(s1), len(s2)
    total=0
    
    # i am creating a grid and summing based on the positions of the digits
    for i in range(len1):
        for j in range(len2):
            product = int(s1[i])*int(s2[j])
            power = (len1 - 1 - i) + (len2 - 1 - j)
            total += product * (10 ** power)
    
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
    print("--- Problem 2 Rectangle Results ---")
    for idx, (num1, num2) in enumerate(test_cases_p2):
        result = rectangle_multiply(num1, num2)
        print(f"Test Case {idx+1}: \n  Num1: {num1}\n  Num2: {num2}\n  Product: {result}\n")