from PIL import Image
import numpy as np
import math as mt
from colorama import Back
N6 = open('../../onDevice/bmps/N7A.bmp', "rb")

BOARD_WIDTH = 14
BOARD_HEIGHT = 42

def checkPosition(imgMapList, position, numbers):
        if len(imgMapList) > position:
              if any([imgMapList[position] == number for number in numbers]):
                     return True
        return False

def checkForShape(colorNumbers ,imgMapList, startPoint, shapeList, checkPoints):
    if all([checkPosition(imgMapList, startPoint + point, colorNumbers) for point in checkPoints]):
        shapeList.append((colorNumbers[0] , [startPoint + shapePoint for shapePoint in checkPoints]))    
        

def findSShape(imgMapList, startPoint, shapeList):
        if checkPosition(imgMapList, startPoint, [5]):
            checkForShape([5], imgMapList, startPoint, shapeList, [0, 1, 13, 14])
            checkForShape([5], imgMapList, startPoint, shapeList, [0, 14, 15, 29])

def findJShape(imgMapList, startPoint, shapeList):
        if checkPosition(imgMapList, startPoint, [8,1]):
            checkForShape([8,1], imgMapList, startPoint, shapeList, [0, 1, 14, 28])
            checkForShape([8,1], imgMapList, startPoint, shapeList, [0, 14, 27, 28])
            checkForShape([8,1], imgMapList, startPoint, shapeList, [0, 1, 2, 16])
            checkForShape([8,1], imgMapList, startPoint, shapeList, [0, 14, 15, 16])

def findLShape(imgMapList, startPoint, shapeList):
        if checkPosition(imgMapList, startPoint, [3]):
            checkForShape([3], imgMapList, startPoint, shapeList, [0, 14, 28, 29])
            checkForShape([3], imgMapList, startPoint, shapeList, [0, 14, 13, 12])
            checkForShape([3], imgMapList, startPoint, shapeList, [0, 1, 2, 14])
            checkForShape([3], imgMapList, startPoint, shapeList, [0, 1, 15, 29])
            
def findZShape(imgMapList, startPoint, shapeList):
        if checkPosition(imgMapList, startPoint, [4]):
            checkForShape([4], imgMapList, startPoint, shapeList, [0, 1, 15, 16])
            checkForShape([4], imgMapList, startPoint, shapeList, [0, 14, 13, 27])

def findIShape(imgMapList, startPoint, shapeList):
        if checkPosition(imgMapList, startPoint, [2]):
            checkForShape([2], imgMapList, startPoint, shapeList, [0, 1, 2, 3])
            checkForShape([2], imgMapList, startPoint, shapeList, [0, 14, 28, 42])

def findOShape(imgMapList, startPoint, shapeList):
        if checkPosition(imgMapList, startPoint, [7]):
            checkForShape([7], imgMapList, startPoint, shapeList, [0, 1, 14, 15])     

def findTShape(imgMapList, startPoint, shapeList):
        if checkPosition(imgMapList, startPoint, [6]):
            checkForShape([6], imgMapList, startPoint, shapeList, [0, 1, 2, 15])
            checkForShape([6], imgMapList, startPoint, shapeList, [0, 14, 15, 28])   
            checkForShape([6], imgMapList, startPoint, shapeList, [0, 14, 13, 15])   
            checkForShape([6], imgMapList, startPoint, shapeList, [0, 14, 13, 28])

def getColor(number):
      match number:
            case 5:
                return Back.GREEN
            case 8:
                return Back.BLUE
            case 3:
                return Back.WHITE
            case 4:
                return Back.RED
            case 2:
                return Back.CYAN
            case 7:
                return Back.YELLOW
            case 6:
                return Back.MAGENTA
            case 0:
                return Back.BLACK            

def buildStartingGrid(shapeList):
        workingArr = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
        for [color, shape] in shapeList:
                for point in shape:
                      x = mt.trunc(point / BOARD_WIDTH)
                      y = point - (x * BOARD_WIDTH)
                      workingArr[x][y] = color
        return workingArr

def printTetris(arr2d):
      for line in arr2d:
                str = f'{Back.BLACK}|'
                for block in line:
                        str += f'{getColor(block)}_|'
                print(str)  

im = Image.open(N6)
SShape = 5
JShape = [8, 1]
RedShape = 4
LShape = 3
IShape = 2
TShape = 6
OShape = 7

imList = list(im.getdata())
shapeList = []
print(len(imList))
for index, imagePixel in enumerate(imList):
        if imagePixel != 0:
            findSShape(imList, index, shapeList)
            findJShape(imList, index, shapeList)
            findZShape(imList, index, shapeList)
            findLShape(imList, index, shapeList)
            findIShape(imList, index, shapeList)
            findOShape(imList, index, shapeList)
            findTShape(imList, index, shapeList)

arr2d = buildStartingGrid(shapeList)
printTetris(arr2d)