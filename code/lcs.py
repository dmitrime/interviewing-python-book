def lcs(A, B):
    table = [["" for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    res = ""
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                table[i][j] = table[i-1][j-1] + A[i-1]
                res = max(table[i][j], res, key=len)
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1], key=len)
    return res

def lcs_1d(A, B):
    current = ["" for _ in range(len(B)+1)]
    previous = list(current)
    res = ""
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                current[j] = previous[j-1] + A[i-1]
                res = max(current[j], res, key=len)
            else:
                current[j] = max(previous[j], current[j-1], key=len)
        # copy current row to previous
        previous = list(current)
    return res

def lcs_rec(A, B):
    if A == "" or B == "":
        return ""
    if A[0] == B[0]:
        return A[0] + lcs_rec(A[1:], B[1:]) 
    else:
        return max(lcs_rec(A[1:], B), lcs_rec(A, B[1:]), key=len)

if __name__ == '__main__':
    assert lcs("", "") == "" 
    assert lcs("a", "b") == "" 
    assert lcs("cat", "cut") == "ct"
    assert lcs("impossible", "possible") == "possible"
    assert lcs("ACGGTCGAGTGCGCGGAAGCCGGCCGA", "GTCGTCGGAATGCGTTGCTCTGTAAA")  == "GTCGTCGGAAGCGGCCGA"

    assert lcs_rec("", "") == "" 
    assert lcs_rec("a", "b") == "" 
    assert lcs_rec("cat", "cut") == "ct"
    assert lcs_rec("impossible", "possible") == "possible"
    #assert lcs_rec("ACGGTCGAGTGCGCGGAAGCCGGCCGA", "GTCGTCGGAATGCGTTGCTCTGTAAA") == "CGGAA"

    assert lcs_1d("", "") == "" 
    assert lcs_1d("a", "b") == "" 
    assert lcs_1d("cat", "cut") == "ct"
    assert lcs_1d("impossible", "possible") == "possible"
    assert lcs_1d("ACGGTCGAGTGCGCGGAAGCCGGCCGA", "GTCGTCGGAATGCGTTGCTCTGTAAA")  == "GTCGTCGGAAGCGGCCGA"
