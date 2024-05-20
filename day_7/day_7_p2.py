import sys
from collections import defaultdict,Counter


def FiveOfKind(hand):
    mp = defaultdict(lambda:0)
    for h in hand:
        mp[h] += 1
    keys = list(mp.keys()).copy()
    for i in keys:
        if i != 'K' and mp[i]+mp['K'] >=5:
            return True
    
    if mp['K'] == 5:
        return True
    return False
    
def FourOfKind(hand):
    mp = defaultdict(lambda:0)
    for h in hand:
        mp[h] += 1
        
    keys = list(mp.keys()).copy()
    for i in keys:
        if i != 'K' and mp[i]+mp['K'] >=4:
            return True
    
    # if mp['K'] == 4:
    #     return True
    return False

def FullHouse(hand):
    mp = defaultdict(lambda:0)
    for h in hand:
        mp[h] += 1

    if mp['K'] == 1 or mp['K'] == 2:
        lis = sorted(mp.values())
        if lis == [1,2,2]:
            return True

    lis = sorted(mp.values())
    if lis == [2,3]:
        return True
    return False

def ThreeOfKind(hand):
    mp = defaultdict(lambda:0)
    for h in hand:
        mp[h] += 1

    keys = list(mp.keys()).copy()
    for i in keys:
        if i != 'K' and mp[i]+mp['K'] >=3:
            return True

    return False

def TwoPair(hand):
    mp = defaultdict(lambda:0)
    for h in hand:
        mp[h] += 1
    
    # if mp['K'] == 2:
    #     lis = sorted(mp.values)
    #     if lis == [1,1,1,2]:
    #         return True
    
    lis = sorted(mp.values())
    if lis[1] == 2 and lis[2] == 2:
        return True
    return False

def OnePair(hand):
    mp = defaultdict(lambda:0)
    for h in hand:
        mp[h] += 1
    
    keys = list(mp.keys()).copy()
    for i in keys:
        if i != 'K' and mp[i]+mp['K'] >=2:
            return True
    return False
  
def type(hand):
  hand = hand.replace('T',chr(ord('9')+1))
  hand = hand.replace('J',chr(ord('9')+2))
  hand = hand.replace('Q',chr(ord('9')+3))
  hand = hand.replace('K',chr(ord('9')+4))
  hand = hand.replace('A',chr(ord('9')+5))

  mp = Counter(hand)

  if sorted(mp.values()) == [5]:
    return (6, hand)
  elif sorted(mp.values()) == [1,4]:
    return (5, hand)
  elif sorted(mp.values()) == [2,3]:
    return (4, hand)
  elif sorted(mp.values()) == [1,1,3]:
    return (3, hand)
  elif sorted(mp.values()) == [1,2,2]:
    return (2, hand)
  elif sorted(mp.values()) == [1,1,1,2]:
    return (1, hand)
  else:
    return (0, hand)


if __name__ == '__main__':
    
    inputs = sys.stdin.read().splitlines()
    
    #inputs = ['23569 12', '2364Q 23', '2365T 34', '23685 45', '23QJ9 56', '2457T 67']
    
    hands = [i.split(" ") for i in inputs]
    #print(hands)
    
    five = []
    four = []
    full = []
    three = []
    twoP = []
    oneP = []
    hc = []

    for hand in hands:
        
        if FiveOfKind(hand[0]):
            five.append(hand)
        elif FourOfKind(hand[0]):
            four.append(hand)
        elif FullHouse(hand[0]):
            full.append(hand)
        elif ThreeOfKind(hand[0]):
            three.append(hand)
        elif TwoPair(hand[0]):
            twoP.append(hand)
        elif OnePair(hand[0]):
            oneP.append(hand)
        else:
            hc.append(hand)

    five = sorted(five,key = lambda x:type(x[0]))
    four = sorted(four,key = lambda x:type(x[0]))
    full = sorted(full,key = lambda x:type(x[0]))
    three = sorted(three,key = lambda x:type(x[0]))
    twoP = sorted(twoP,key = lambda x:type(x[0]))
    oneP = sorted(oneP,key = lambda x:type(x[0]))
    hc = sorted(hc,key = lambda x:type(x[0]))
    
    final_lis = hc+oneP+twoP+three+full+four+five
    
    # print(five)
    # print(four)
    # print(full)
    # print(three)
    # print(twoP)
    # print(oneP)
    # print(hc)
    # print(final_lis)
    
    rank = 1
    res = 0
    
    for hand in final_lis:
        res += (int(hand[1])*rank)
        rank+=1
    print(res)
