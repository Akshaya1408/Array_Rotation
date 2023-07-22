def rotate_array(A, B):
    N = len(A)
    B = B % N  

    A[:N-B] = reversed(A[:N-B])
    A[N-B:] = reversed(A[N-B:])
    A[:] = reversed(A[:])

    return A

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = int(input())
    print(rotate_array(A, B))
