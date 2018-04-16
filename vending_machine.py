from byotest import *

euro_coins = [100, 50, 20, 10, 5, 2, 1]
usd_coins =  [100, 50, 25, 10, 5, 2, 1]
coin_dict = {100: 20, 50:20, 20:20, 10:20, 5:20, 2:20, 1:20}

def get_change(amount, coins = euro_coins):
    change = []
    status = True
    
    # if type(coins) is dict:
    #     for coin,numb in coins.items():
    #         while coin <= amount and numb >= 0:
    #             change.append(coin)
    #             amount -= coin
    # else:
    for coin in coins:
        coin_counter = 0
        while coin <= amount and coin_counter <20:
            change.append(coin)
            amount -= coin
            coin_counter +=1
            if coin == 1 and coin_counter == 20 and amount >0:
                # print ("change not possibl")
                status = False
    
    if status == True:
        return change
    else:
        return False

test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(3),[2,1])
test_are_equal(get_change(7),[5,2])
test_are_equal(get_change(9),[5,2,2])
test_are_equal(get_change(35, usd_coins),[25,10])
test_are_equal(get_change(9),[5,2,2])
test_are_equal(get_change(2100),[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,50,50])
test_not_enough(get_change(3761),False)

print(get_change(3761))
print("all test good")