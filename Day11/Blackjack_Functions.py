from random import choice

Card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def DrawCard():
    Num = choice(Card)
    return Num

def Score(Num):
    score = sum(Num)
    if score == 21:
        score = 0
    if (score > 21) and (11 in Num):
        Num.remove(11)
        Num.append(1)
        score = sum(Num)
    return score



def ManipulateCards(NumList,IsDrawer=True):
    Total = SumNum(NumList)
    if Total > 21 and 11 in NumList:
        NumIndex = NumList.index(11)
        NumList[NumIndex] = 1
        Total = SumNum(NumList)
    if IsDrawer:
        MaskList = []
        MaskList.extend(NumList)
        MaskList[-1] = 'X'
        return {'total': Total, 'list': MaskList,'actual_list': NumList }
    return {'total': Total, 'list': NumList}
