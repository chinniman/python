def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case(" ") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One Lower case"
assert count_upper_case("&^%") == 0, "Special characters"
assert count_upper_case("1") == 0, "number"
assert count_upper_case("Hi423People") == 2, "remix"

print("all the test passed")