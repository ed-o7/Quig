trees = ["tree1","tree2","tree3"]
names = ["interiorWalls","northWall","eastWall","southWall","westWall","northDoor","eastDoor","southDoor","westDoor","northToEast","eastToSouth","northToSouth","westToEast","westToSouth","northSouthWest","northSouthEast","northToWest","northFence","eastFence","southFence","westFence","mapPic","dumpPath","pentagram","brokenFence","roogPic","undergroundDoor","northHedge","eastHedge","southHedge","westHedge","northHedgeDoor","eastHedgeDoor","southHedgeDoor","westHedgeDoor","underRoog","johnPic"]
chars = ["quig1","quig2","quig3","ghoulPic","thekPic","zorgPic","kerpPic","bakerPic","mayorPic","bodaPic","antiquesPic","dungPic","marbaPic","furnacePic1","furnacePic2","dergPic","tutorialPic","deadmayorPic","magusPic","emptyPic","gragPic","trugPic","roogDoorPic","underRoogPic","kwigPic"]
obstacles = ["wardrobe","mayorSign","dumpSign","bakerySign","antiqueSign","farmSign","campSign","shelf1","shelf2","table1","bigfurnace","bed","tent","trugTreePic"]
prev = ""
after = ""
use = 4
if use == 1:
    for i in range(0,len(trees)):
        prev = prev + (trees[i]+",")
        after = after + "pygame.transform.scale((pygame.image.load('"+trees[i]+".png"+"').convert_alpha()),(75,150)),"
elif use == 2:
    for i in range(0,len(names)):
        prev = prev + (names[i]+",")
        after = after + "pygame.transform.scale((pygame.image.load('"+names[i]+".png"+"').convert_alpha()),(1200,700)),"
elif use == 3:
    for i in range(0,len(chars)):
        prev = prev + (chars[i]+",")
        after = after + "pygame.transform.scale((pygame.image.load('"+chars[i]+".png"+"').convert_alpha()),(50,50)),"
elif use == 4:
    for i in range(0,len(obstacles)):
        prev = prev + (obstacles[i]+",")
        after = after + "pygame.transform.scale((pygame.image.load('"+obstacles[i]+".png"+"').convert_alpha()),(100,100)),"
print(prev[:-1]+"="+after[:-1])

