'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
'''

def char2int(char):
    return ord(char) - ord('a')

str = input()

alphabet_check = []

for i in range(ord('z')-ord('a') + 1):
    alphabet_check.append(-1)

#print(len(alphabet_check))

for i, char in enumerate(str):
    if alphabet_check[char2int(char)] == -1:
        alphabet_check[char2int(char)] = i

for i in alphabet_check:
    print(i, end=' ')




