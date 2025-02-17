def genereaza(max_length=5):

    results = []

    for i in range(max_length + 1):

        for j in range(max_length + 1):
            results.append('a'*i+'b'*j)

    return results

print(genereaza(4))