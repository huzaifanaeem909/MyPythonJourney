"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
.
.
.
upto value of n
"""

n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, 6):
        print(i, end=" ")
    print()

"""
1          |   1
1 2        |   2 2
1 2 3      |   3 3 3
1 2 3 4    |   4 4 4 4
1 2 3 4 5  |   5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

"""
1          |   5           |   5
2 1        |   5 4         |   4 4 
3 2 1      |   5 4 3       |   3 3 3
4 3 2 1    |   5 4 3 2     |   2 2 2 2
5 4 3 2 1  |   5 4 3 2 1   |   1 1 1 1 1
"""
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(i, end=" ")
    print()

"""
*          |  * * * * * | 5 4 3 2 1  | 5 5 5 5 5  
* *        |  * * * *   | 5 4 3 2    | 4 4 4 4     
* * *      |  * * *     | 5 4 3      | 3 3 3       
* * * *    |  * *       | 5 4        | 2 2        
* * * * *  |  *         | 5          | 1          
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

"""
5 4 3 2 1  |  1
4 3 2 1    |  2  3
3 2 1      |  4  5  6
2 1        |  7  8  9  10
1          |  11 12 13 14 15
"""

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

count = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(count, end=" ")
        count += 1
    print()

"""
         *  |          1  |         1  |         *          | * * * * * * * * *
       * *  |        1 2  |       2 2  |       * * *        |   * * * * * * *
     * * *  |      1 2 3  |     3 3 3  |     * * * * *      |     * * * * * 
   * * * *  |    1 2 3 4  |   4 4 4 4  |   * * * * * * *    |       * * *
 * * * * *  |  1 2 3 4 5  | 5 5 5 5 5  | * * * * * * * * *  |         *
"""
for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(i, end=" ")
    print()

for a in range(1, 6):
    for b in range(a, 5):
        print(" ", end=" ")
    for c in range(1, (a * 2)):
        print("*", end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, (i * 2)):
        print("*", end=" ")
    print()

"""
         *          |  * * * * * * * * *
       * * *        |    * * * * * * *
     * * * * *      |      * * * * * 
   * * * * * * *    |        * * *
 * * * * * * * * *  |          *
   * * * * * * *    |        * * *
     * * * * *      |      * * * * *
       * * *        |    * * * * * * *
         *          |  * * * * * * * * *
 """

for a in range(1, 6):
    for b in range(a, 5):
        print(" ", end=" ")
    for c in range(1, (a * 2)):
        print("*", end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, (i * 2)):
        print("*", end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, (i * 2)):
        print("*", end=" ")
    print()
for a in range(1, 5):
    for b in range(a, 4):
        print(" ", end=" ")
    for c in range(1, (a * 2) + 2):
        print("*", end=" ")
    print()
