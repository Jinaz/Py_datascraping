import cv2 as cv
import imageFunctions.imagecomparison as ic

menuCoords = [118,155,304,405]
votemenuCoords = [108,155,308,615]
PrepareInGame = [1033,1064,772,1148]
MissionInGame = [1030,1069,797,1121]

def readimage(path, coords):
    image = cv.imread(path)
    return image[coords[0]:coords[1],coords[2]:coords[3],:]
menu = "DATA/menu.png"
enemy = "DATA/enemy.png"
prep = "DATA/prepare.png"
post = "DATA/postmatch.png"

menuimg = readimage(menu, menuCoords)
enemyimg = readimage(enemy, MissionInGame)
prepimg = readimage(prep, PrepareInGame)
postimg = readimage(post, votemenuCoords)

menuimg = ic.prefilter(menuimg, "opening")
enemyimg = ic.prefilter(enemyimg, "opening")
prepimg = ic.prefilter(prepimg, "opening")
postimg = ic.prefilter(postimg, "opening")

cv.imwrite("DATA/enemyFiltered.png", enemyimg)
cv.imwrite("DATA/prepFiltered.png", prepimg)
cv.imwrite("DATA/postFiltered.png", postimg)
cv.imwrite("DATA/menuFiltered.png", menuimg)

cv.imshow("",menuimg)
cv.waitKey()
cv.imshow("",enemyimg)
cv.waitKey()
cv.imshow("",prepimg)
cv.waitKey()
cv.imshow("",postimg)
cv.waitKey()