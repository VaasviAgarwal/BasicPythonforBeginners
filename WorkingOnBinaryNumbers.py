N = input()
A = input()
B = input()
 
if not N.isnumeric():
    print('Invalid input')
 
else:
    N = int(N)
    if N < 3:
        print('Invalid input')
    
    else:
        A = A.split()
        B = B.split()
        if len(A)!=len(B) or len(A)!=N:
            print('Invalid input')
        
        else:
            f = 0
            fl = 0
            for i in range(N):
                if not (A[i].isnumeric() or B[i].isnumeric()):
                    fl = 1
                    break 
                else:
                    A[i] = int(A[i])
                    B[i] = int(B[i])
            if fl:
                print('Invalid entry')
            else:
                for i in A:
                    if not(i==0 or i==1):
                        f = 1
                for i in B:
                    if not(i==0 or i==1):
                        f = 1
                if f:
                    print('Invalid Input')
                else:
                    c = 0
                    i = 0
                    while i<N:
                        x = A[i]
                        y = B[i]
                        if A==B:
                            break
                        if x!=y:
                            for j in range(i, N, 2):
                                if A[j] == B[j]:
                                    break
                            if j == i or j == i+1:
                                j = i
                            elif j == N-1 and N == 3:
                                j = N-1
                            elif j == N-2:
                                j = N-2
                            else:
                                j = j-2
                            X = A[i:j+1]
                            for k in range(0, len(X)):
                                if k%2 == 0:
                                    m = k + i
                                    if A[m] == 0:
                                        A[m] = 1
                                    else:
                                        A[m] = 0
                            c = c+1
                            print(A)
                        i = i+1
                    print(c)
