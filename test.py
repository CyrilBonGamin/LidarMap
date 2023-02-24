import math
from matplotlib import pyplot as plt
from PIL import Image

def mapfunc():
    f = open('examp9.txt')

    removed_chars = [',', ';']
    chars = set(removed_chars)

    lt = []

    for line in f.readlines():
        res = ''.join(filter(lambda x: x not in chars, line))
        nums = list(map(float, res.split()))
        lt.append(nums)

    x1 = []
    y1 = []

    for i in range(len(lt)):
        x1.append(lt[i][0] + 0.3*math.cos(lt[i][2]))
        y1.append(lt[i][1] + 0.3*math.sin(lt[i][2]))

    xx = []
    yy = []

    pov = [(-120 + 0.35*i)*0.0174 for i in range(len(lt[0]))]

    for i in range(len(lt)):
        for j in range(len(lt[0][3:])):
            if lt[i][j] < 5.6 and lt[i][j] > 0.5:
                xx.append(x1[i] + lt[i][j]*math.cos(lt[i][2] - pov[j]))
                yy.append(y1[i] + lt[i][j]*math.sin(lt[i][2] - pov[j]))

    plt.figure(figsize=(14, 10))
    plt.scatter(xx, yy, color = 'g', s = 2)
    plt.savefig('maps.png', bbox_inches='tight')
    plt.scatter(x1, y1, color = 'b', s = 2)
    plt.grid(linestyle = '--')
    plt.show()
    picture = Image.open('maps.png')
    cord = (50, 50, 1100, 770) # лево, верх, право, низ
    new_picture = picture.crop(cord)
    new_picture.save('maps.png')

if __name__ == '__main__':
    mapfunc()