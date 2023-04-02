#Username in codewars.com: markindTCD
#At this point, I have 5th Kyu

#Codewars style ranking system (4kyu)
class User ():    
    def __init__ (self):
        self.RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.rank_index = 0
        self.progress = 0
        
    def inc_progress (self, rank):
        rank_index = self.RANKS.index(rank)
        
        if rank_index == self.rank_index:
            self.progress += 3
        elif rank_index == self.rank_index - 1:
            self.progress += 1
        elif rank_index > self.rank_index:
            difference = rank_index - self.rank_index
            self.progress += 10 * difference * difference
            
        while self.progress >= 100:
            self.rank_index += 1
            self.rank = self.RANKS[self.rank_index]
            self.progress -= 100    
        
        if self.rank == 8:
            self.progress = 0
            return


##Recover a secret string from random triples (4Kyu)
#There is a secret string which is unknown to you. 
#Given a collection of random triplets from the string, recover the original string.
def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)
  
def fix(l, a, b):
   """let l.index(a) < l.index(b)"""
   if l.index(a) > l.index(b):
       l.remove(a)
       l.insert(l.index(b), a)


#Weight for weight (5kyu): The weight of a number will be from now on the sum 
#of its digits and then the original one will be sorted
def order_weight(string):
    string = list(string.split(" "))
    weights = list(map(sum_,string))
    new_weights, new_string = zip(*sorted(zip(weights, string)))
    return ' '.join(new_string)
 
def sum_(string):
    sum_i = 0
    for i in list(string):
        sum_i+=int(i)
    return sum_i


#Codewars style ranking system (4kyu)
#Convert a string into an integer. The strings simply represent the numbers in words.

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def parse_int(string):
    print(string)
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)

#Codewars style ranking system (4kyu)
#Write a function that computes the nth smallest Hamming number.

def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

#Codewars style ranking system (4kyu)
#Write a function for coin problem

def count_change2(money, coins, i=0):
    if money < 0:
        return 0
    if money == 0:
        return 1
    if i == len(coins) and money > 0:
        return 0
    return count_change2(money - coins[i], coins, i) + count_change2(money, coins, i + 1)
