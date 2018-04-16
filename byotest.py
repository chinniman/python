def number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    assert expected == actual, "expected {0}, got{1}".format(expected,actual)

def test_not_equal(a,b):
    assert a!=b, "did not expect {0} but got {1}".format(a,b)

def test_is_in(collection,item):
    assert item in collection, "{0} does not cotain {1}".format(collection,item)

def test_not_in(collection,item):
    assert item not in collection, "{0} contains {1} but shouldn't".format(collection,item)

def test_not_enough(val,val1):
    assert val == val1, "expected {0}, got {1}".format(val, val1)
    
    
# test_are_equal(number_of_evens([1,2,3,4,5]), 2)

# test_not_equal(3, 3)

# test_is_in([1,2,3,4,5],0)

# test_not_in([1,2,3,4,5], 1)