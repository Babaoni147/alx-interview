#!/usr/bin/python3
"""
Pascal Trangle
"""


def pascal_triangle(n):
    '''
    Pascal's triangle
    '''
    if n <= 0:
        return []
    else:
        respt = []
        for i in range(n):
            if len(respt) == 0:
                respt.append([1])
            else:
                row = [1]
                for j in range(1, len(respt[-1])):
                    row.append(respt[-1][j] + respt[-1][j - 1])
                row.append(1)
                respt.append(row)
        return respt
