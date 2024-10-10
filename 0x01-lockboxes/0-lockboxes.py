#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns: True if all boxes can be opened else False
    '''
    lent = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < lent:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < lent and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(lent):
        if i not in opened_boxes and i != 0:
            return False
    return True
