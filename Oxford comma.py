def oComma(anyList):
    try:
        for i in range(len(anyList) - 1):
            print(anyList[i], end=', ')
        print('and ' + anyList[-1])
    except IndexError:
        print('List is empty.')


spam = ['dogs', 'cats', 'purple', 'penguins']

oComma(spam)

empty = []

oComma(empty)
