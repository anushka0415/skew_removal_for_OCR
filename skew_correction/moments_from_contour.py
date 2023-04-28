



def moments_from_contour(xypoints):

    '''Create shape moments from points sampled from the outline of an
ellipse (note this is numerically inaccurate even for arrays of 1000s
of points). Included in this project primarily for testing purposes.

    '''

    assert len(xypoints.shape) == 3
    assert xypoints.shape[1:] == (1, 2)

    xypoints = xypoints.reshape((-1, 2))

    a00 = 0
    a10 = 0
    a01 = 0
    a20 = 0
    a11 = 0
    a02 = 0

    xi_1, yi_1 = xypoints[-1]

    for xy in xypoints:

        xi, yi = xy
        xi2 = xi * xi
        yi2 = yi * yi
        dxy = xi_1 * yi - xi * yi_1
        xii_1 = xi_1 + xi
        yii_1 = yi_1 + yi

        a00 += dxy
        a10 += dxy * xii_1
        a01 += dxy * yii_1
        a20 += dxy * (xi_1 * xii_1 + xi2)
        a11 += dxy * (xi_1 * (yii_1 + yi_1) + xi * (yii_1 + yi))
        a02 += dxy * (yi_1 * yii_1 + yi2)

        xi_1 = xi
        yi_1 = yi

    if a00 > 0:
        db1_2 = 0.5
        db1_6 = 0.16666666666666666666666666666667
        db1_12 = 0.083333333333333333333333333333333
        db1_24 = 0.041666666666666666666666666666667
    else:
        db1_2 = -0.5
        db1_6 = -0.16666666666666666666666666666667
        db1_12 = -0.083333333333333333333333333333333
        db1_24 = -0.041666666666666666666666666666667

    m00 = a00 * db1_2
    m10 = a10 * db1_6
    m01 = a01 * db1_6
    m20 = a20 * db1_12
    m11 = a11 * db1_24
    m02 = a02 * db1_12

    inv_m00 = 1. / m00
    cx = m10 * inv_m00
    cy = m01 * inv_m00

    mu20 = m20 - m10 * cx
    mu11 = m11 - m10 * cy
    mu02 = m02 - m01 * cy

    return m00, m10, m01, mu20, mu11, mu02