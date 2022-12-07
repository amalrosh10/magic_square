def creatingSquare(n):
    # 2-D array with all slots set to 0
    mgsqr = [[0 for x in range(n)]
             for y in range(n)]

    # initialize position of 1
    r = n // 2
    c = n - 1
    # Fill the magic square by placing values
    num = 1
    while num <= (n * n):
        if r == -1 and c == n:  # 3rd condition
            c = n - 2
            r = 0
        else:
            # next number goes out of right side of square
            if c == n:
                c = 0
            # next number goes out of upper side
            if r < 0:
                r = n - 1

        if mgsqr[int(r)][int(c)]:  # 2nd condition
            c = c - 2
            r = r + 1
            continue
        else:
            mgsqr[int(r)][int(c)] = num
            num = num + 1

        c = c + 1
        r = r - 1  # 1st condition

    # Printing magic square
    print("Magic Square for n =", n)
    print("Sum of each row or column",
          n * (n * n + 1) // 2, "\n")

    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (mgsqr[i][j]),
                  end='')

            if j == n - 1:
                print()


n = 7
creatingSquare(n)