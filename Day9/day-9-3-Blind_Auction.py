BidLogo = '''
                __
               (_()  \
          \__/  ||    \  \__/
          (oo)  /)       (oo)
         //~~\\//       //~~\\
         \\__/\/   _____\\__//_____
          |/\|    |                |
    _____ |||| ___|                |______
   ______(_)(_)___|________________|____jro

'''

BidData = {}

FinishedBidding = False


def BidEntry(Name, Bid):
    BidData[Name] = Bid


def MaxBid(Dict):
    Name, Bid = None, None

    for i in Dict:
        for j in Dict:
            if Dict[i] > Dict[j]:
                Name = i
                Bid = Dict[i]
    return Name, Bid


print(BidLogo)
print("Welcome to Blind Bidding !!!")
while not FinishedBidding:
    BidderName = input("Enter your name : ")
    BidAmount = input("Enter your bid : $")
    BidData[BidderName] = BidAmount
    EndBid = input("Finished Bidding ? yes/no")
    if EndBid == "yes":
        FinishedBidding = True
    else:
        print(BidLogo, "\n\n")
MaxBidder = MaxBid(Dict=BidData)
print(f"Winner is {MaxBidder[0]}, with Max Bid of ${MaxBidder[1]}")
