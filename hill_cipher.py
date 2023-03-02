import numpy as np
from numpy.linalg import inv,det
import utils
import math
from numpy import matrix
from numpy import linalg


def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=np.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=np.array(A)
  minor=np.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def __split2len(s, n):
    """Split string s to chunks of size n."""
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))
    


__mod = 127


def __char2Val(s):
    """Convert char s to ASCII value - 32."""
    return ord(s)


def __val2Char(n):
    """Convert int value +32 to ASCII."""
    return chr(n)


def hill_encryption(message: str, mat: list):
    assert len(mat) == 4 and len(mat[0]) == 4, "Key Matrix must be of 4x4 dim."
    messageInChunks = __split2len(message, 4)
    print(messageInChunks)
    cipherText = ""
    for plaintextChunk in messageInChunks:
        for i in range(4):
            val = 0
            for j in range(len(plaintextChunk)):
                val += mat[i][j]*__char2Val(plaintextChunk[j])
            val = val % __mod
            print(int(val))
            cipherText += __val2Char(int(val))
    return cipherText


def printMatrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table) + '\n')




def hill_decryption(ciphertext: str, mat: list):
    assert len(mat) == 4 and len(mat[0]) == 4, "Key Matrix must be of 4x4 dim."
    return hill_encryption(ciphertext, mat)


if __name__ == '__main__':
    # mat = [ [ 1,18,0,73],
    #         [13,9 , 88 ,103],
    #         [43,6 ,126,109],
    #         [89,88 ,114 ,118]
    # ]
    mat=[[15, 11, 1, 18],
        [48, 78, 0, 8],
        [1, 1, 0, 1],
        [79, 83, 93, 76]]
    # mat=[[2  ,     3 ,      124 ,    118],
    #   [1    , 18  , 124   ,76],
    #   [1     , 1   ,  125  ,   124],
    #   [85,      91 ,     126,     109]
    # ]
    invmat=modMatInv(mat,__mod)
    printMatrix(mat)
    printMatrix(invmat)
    message = input("enter the message to be encrypted: ")
    print(message)
    ciphertext = hill_encryption(message, mat)
    print(ciphertext)
    plaintext = hill_decryption(ciphertext, invmat)
    print(plaintext)
