E = "1 2 3"
digits = E.split()

def verificare_palindrom(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


palindromes = set(digits)
queue = digits[:]

for _ in range(4):
    new_queue = []
    for num in queue:
        for digit in digits:
            new_num = num + digit
            if verificare_palindrom(new_num):
                palindromes.add(new_num)
            new_queue.append(new_num)
    queue = new_queue

palindromes = list(palindromes)
for i in range(len(palindromes) - 1):
    for j in range(i + 1, len(palindromes)):
        if int(palindromes[i]) > int(palindromes[j]):
            palindromes[i], palindromes[j] = palindromes[j], palindromes[i]

print(palindromes)
