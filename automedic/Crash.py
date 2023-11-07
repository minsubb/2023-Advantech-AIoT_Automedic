import numpy as np
from itertools import combinations
from Car_Manager import Car, Overlap

cars = []
overlaps = []


def crash(boxes, shape, previous):
    cordi = boxes.xywh
    ids = boxes.id
    white = np.zeros(shape, dtype=np.uint8)
    n = len(cordi)
    current = []
    is_accident = False
    plag = 0

    if ids == None:
        return white, current, is_accident, plag

    # Generate Car object
    global cars
    if len(cars) < int(ids.max().item()):
        for i in range(len(cars) + 1, int(ids.max().item()) + 1):
            cars.append(Car(i))

    # Add car's cordinate
    for i in range(n):
        id = int(ids[i].item()) - 1
        cars[id].add(int(cordi[i][0].item()), int(cordi[i][1].item()))

    # Update frame & Calculate alpha
    global overlaps
    for ovl in overlaps:
        if ovl.is_on:
            ovl.frame += 1
            white = ovl.trace(white)
            if ovl.frame == 10:
                print("\n")
                ovl.speed()
                ovl.angle()
                is_accident, plag = ovl.prediction()
            elif ovl.frame > 10:
                ovl.is_on = False

    if n <= 1:
        return white, current, is_accident, plag

    # Crash checking
    arr = [i for i in range(n)]
    arr = list(combinations(arr, 2))
    for n1, n2 in arr:

        p1 = (int(cordi[n1][0].item()), int(cordi[n1][1].item()))
        p2 = (int(cordi[n2][0].item()), int(cordi[n2][1].item()))
        id1 = int(ids[n1].item()) - 1
        id2 = int(ids[n2].item()) - 1

        # Overlap checking
        th_w = cordi[n1][2] / 2 + cordi[n2][2] / 2
        th_h = cordi[n1][3] / 2 + cordi[n2][3] / 2
        if np.abs(p1[0] - p2[0]) < th_w and np.abs(p1[1] - p2[1]) < th_h:
            current.append((ids[n1], ids[n2]))

            # Skip previous overlap
            exist = False
            for a, b in previous:
                if a == ids[n1] and b == ids[n2]:
                    exist = True
                    break
            # Append overlaps
            if exist == False:
                overlaps.append(Overlap(cars[id1], cars[id2]))
                overlaps[-1].speed()
                overlaps[-1].angle()

    return white, current, is_accident, plag