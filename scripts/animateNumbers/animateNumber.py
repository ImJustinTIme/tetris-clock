from PIL import Image
N6 = open('../../onDevice/bmps/N6A.bmp', "rb")

def checkPosition(imgMapList, position, numbers):
        if len(imgMapList) > position:
              if any([imgMapList[position] == number for number in numbers]):
                     return True
        return False

def checkForShape(colorNumbers ,imgMapList, startPoint, shapeList, checkPoints):
    if all([checkPosition(imgMapList, startPoint + point, colorNumbers) for point in checkPoints]):
        shapeList.append((colorNumbers ,[startPoint + shapePoint for shapePoint in checkPoints]))    
        

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
            checkForShape([8,1], imgMapList, startPoint, shapeList, [0, 1, 15, 16])
            checkForShape([8,1], imgMapList, startPoint, shapeList, [0, 14, 13, 27])

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


print(shapeList)
print(len(shapeList))
im.show()