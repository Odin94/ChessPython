def point_in_rect(point, rect):
    px = point[0]
    py = point[1]

    rx = rect[0]
    ry = rect[1]
    rw = rect[2]
    rh = rect[3]

    if px > rx + rw or px < rx:
        return False
    if py > ry + rh or py < ry:
        return False
    else:
        return True