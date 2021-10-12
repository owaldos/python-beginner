def number_of_bottles():
    for index in range(99,0,-1):
        
        if index==1:
            print(f'{index} bottle of milk on the wall, {index} bottle of milk.')
            print('Take one down and pass it around, no more bottles of milk on the wall.')
        else:
            print(f'{index} bottles of milk on the wall, {index} bottles of milk.')
            print(f'Take one down and pass it around, {index-1} bottles of milk on the wall.')
          
    print('No more bottles of milk on the wall,no more bottles of milk.')
    print('Go to the store and some more, 99 bottles of milk on the wall.')

number_of_bottles()