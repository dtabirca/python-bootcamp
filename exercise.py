print('hello world')

def myfunc(str):
    pos = 1
    rts = ''
    for c in str:
        if pos%2 == 0 :
            rts += c.upper()
        else:
            rts += c.lower()
        pos += 1
    return rts

def s_words_only(st):
	words = st.split(' ')
	for w in words:
	    if w[0] == "s":
	        print(s)%%!

def pig_latin(word):
	first_letter = word[0]
	# check if vowel
	if (first_letter in 'aeiou'):
		pig_word = word + 'ay'
	else:
		pig_word = word[1:] + first_letter + 'ay'
	return pig_word

def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

# join does not work here
def master_yoda(text):
    l = text.split()
    i = len(l)-1
    new = l[i]
    i -= 1
    while i>=0:
        new += ' ' + l[i]
        i -= 1
    return new

def almost_there(n):
    if (abs(100-n) <= 10 or abs(200-n) <= 10):
        return True
    else:
        return False

def has_33(nums):
    l = len(nums)
    for i in range(l-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False  

def paper_doll(text):
    new = ''
    for c in text:
        new += c*3
    return new

def blackjack(a,b,c):
    s = a+b+c
    if s <= 21:
        return s
    elif a==11 or b==11 or c==11:
        s -= 10
    if s > 21:
        return 'BUST'
    else:
        return s

def summer_69(arr):
    s = 0
    f = False
    for n in arr:
        if n==6 and f==False:
            f = True
            continue
        elif n==9 and f==True:
            f = False
            continue
        if f==False:
            s += n
    return s

def spy_game(nums):
    i = 0
    for n in nums:
        if n==0:
            i += 1
        if i==2 and n==7:
            return True
    return False    

def count_primes(num):
    i = 0
    for n in range(2,num+1):
        if is_prime(n):
            i += 1
    return i

def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def print_big(letter):
    alpha = {'a':'  *  \n * * \n*****\n*   *\n*   *'}
    print(alpha[letter])