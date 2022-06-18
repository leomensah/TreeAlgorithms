
def permuTation2(array):
    res = []
    perm = []
    count = {n:0 for n in array}
    for n in array:
        count[n] +=1

    def dfs():
        if len(perm) == len(array):
            res.append(perm.copy())
            return

        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -= 1
                
                dfs()

                count[n] += 1
                perm.pop()

print(permuTation2([1,1,2]))