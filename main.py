import math
import numpy as np
import cv2
import test
import os

def Houghfunc():
    img = cv2.imread('maps.png', cv2.IMREAD_COLOR)
    # Convert the image to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cdstP = np.copy(gray)
    # Find the edges in the image using canny detector
    edges = cv2.Canny(gray, 50, 200, None, 3)
    edges2 = cv2.GaussianBlur(edges, (5, 5), 0)
    # Detect points that form a line
    lines = cv2.HoughLinesP(edges2, 1, np.pi/180, 100, 0, 0)
    # Draw lines on the image
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(gray, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

    linesP = cv2.HoughLinesP(edges, 2, np.pi / 180, 50, None, 20, 8)

#    cdstP = cv2.cvtColor(cdstP, cv2.COLOR_GRAY2BGR)
    canv = np.zeros((1024, 1480, 3), np.uint8)
    canv.fill(255)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2 .line(canv, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 3, cv2.LINE_AA)


    #cv2.imshow("Source", img)
    #cv2.imshow("Detected Lines - Standard Hough Line Transform", gray)
    cv2.imshow("After Hough transform", canv)

    cv2.waitKey()

if __name__ == '__main__':
    test.mapfunc()
    Houghfunc()
    path = 'maps.png'
    try:
        os.remove(path)
    except:
        print('Files do not exist')