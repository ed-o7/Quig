#all the variables so i dont have to scroll past them all the time
import pygame
import string
pygame.font.init()
tickStart = pygame.time.get_ticks()
#Console values, prefix 'scr-'
scr_width = 1200
scr_height = 700
screen = pygame.display.set_mode((scr_width,scr_height))
pygame.display.set_caption("Quig")
class character:
    def __init__(self,width,height,vel,colours,x,y,health,overlap,dia,pic):
        self.width,self.height,self.vel,self.colours,self.x,self.y,self.health,self.overlap,self.dia,self.pic = width,height,vel,colours,x,y,health,overlap,dia,pic
class dialogue:
    def __init__(self,name,intro,options,responses,action,done,finalmove):
        self.name,self.intro,self.options,self.responses,self.action,self.done,self.finalmove=name,intro,options,responses,action,done,finalmove
class stage:
    def __init__(self,title,coords,colour,npcs,objects,doors):
        self.title,self.coords,self.colour,self.npcs,self.objects,self.doors=title,coords,colour,npcs,objects,doors
class quest:#questgiver = NPC    , bool   , bool   , 2d list of strings then bools
    def __init__(self,questgiver, possible, started, progress):
        self.questgiver,self.possible,self.started,self.progress=questgiver,possible,started,progress
#image loading      
#quigframes        

#trees
tree1,tree2,tree3=pygame.transform.scale((pygame.image.load('tree1.png').convert_alpha()),(75,150)),pygame.transform.scale((pygame.image.load('tree2.png').convert_alpha()),(75,150)),pygame.transform.scale((pygame.image.load('tree3.png').convert_alpha()),(75,150))


#objects
interiorWalls,northWall,eastWall,southWall,westWall,northDoor,eastDoor,southDoor,westDoor,northToEast,eastToSouth,northToSouth,westToEast,westToSouth,northSouthWest,northSouthEast,northToWest,northFence,eastFence,southFence,westFence,mapPic,dumpPath,pentagram,brokenFence,roogPic,undergroundDoor,northHedge,eastHedge,southHedge,westHedge,northHedgeDoor,eastHedgeDoor,southHedgeDoor,westHedgeDoor,underRoog,johnPic=pygame.transform.scale((pygame.image.load('interiorWalls.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northWall.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('eastWall.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('southWall.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('westWall.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('eastDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('southDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('westDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northToEast.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('eastToSouth.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northToSouth.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('westToEast.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('westToSouth.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northSouthWest.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northSouthEast.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northToWest.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northFence.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('eastFence.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('southFence.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('westFence.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('mapPic.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('dumpPath.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('pentagram.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('brokenFence.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('roogPic.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('undergroundDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northHedge.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('eastHedge.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('southHedge.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('westHedge.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('northHedgeDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('eastHedgeDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('southHedgeDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('westHedgeDoor.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('underRoog.png').convert_alpha()),(1200,700)),pygame.transform.scale((pygame.image.load('johnPic.png').convert_alpha()),(1200,700))




placeholder = pygame.image.load("placeHolder.png").convert_alpha()
placeholder = pygame.transform.scale(placeholder,(1,1))

#characters
quig1,quig2,quig3,ghoulPic,thekPic,zorgPic,kerpPic,bakerPic,mayorPic,bodaPic,antiquesPic,dungPic,marbaPic,furnacePic1,furnacePic2,dergPic,tutorialPic,deadmayorPic,magusPic,emptyPic,gragPic,trugPic,roogDoorPic,underRoogPic,kwigPic=pygame.transform.scale((pygame.image.load('quig1.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('quig2.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('quig3.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('ghoulPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('thekPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('zorgPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('kerpPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('bakerPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('mayorPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('bodaPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('antiquesPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('dungPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('marbaPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('furnacePic1.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('furnacePic2.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('dergPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('tutorialPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('deadmayorPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('magusPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('emptyPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('gragPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('trugPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('roogDoorPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('underRoogPic.png').convert_alpha()),(50,50)),pygame.transform.scale((pygame.image.load('kwigPic.png').convert_alpha()),(50,50))


wardrobe,mayorSign,dumpSign,bakerySign,antiqueSign,farmSign,campSign,shelf1,shelf2,table1,bigfurnace,bed,tent,trugTreePic=pygame.transform.scale((pygame.image.load('wardrobe.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('mayorSign.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('dumpSign.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('bakerySign.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('antiqueSign.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('farmSign.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('campSign.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('shelf1.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('shelf2.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('table1.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('bigfurnace.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('bed.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('tent.png').convert_alpha()),(100,100)),pygame.transform.scale((pygame.image.load('trugTreePic.png').convert_alpha()),(100,100))



imgs = [quig2,quig3]
furnacePics = [furnacePic1,furnacePic2]
count = 0
madmoder = False
textbox_y = 400
grass = (0,200,0)
cakeList = ["Storebought Cake","Homemade Cake","Belphegor Cake","Goblin Cake","Angel Cake","100%","Dead","Woody Cake"]
cakeResponses = ["Gee. Thanks. Storebought cake.","This actually looks good.","If I wasn't so hungry I'd be curious.","Is that... skin?","Okay, this is pretty good.","100%","Dead","Why is it made of mud? Weirdo."]
endGame = [False,-1]
endings= [["Congratulations on completing the game!","You completed the bad ending.","You made lives miserable, just for cake.","You may exit the program. This was all a simulation."],
          ["Congratulations on completing the game!","You completed the good ending!","You helped make love, and cake.","You may exit the program. This was all a simulation."],
          ["Congratulations on completing the game!","You completed the strange ending.","You summoned... something? Maybe a cake?","You may exit the program. This was all a simulation."],
          ["Congratulations on completing the game!","You completed the goblin ending...","Is it just to murder an unjust man? Perhaps.","You may exit the program. This was all a simulation."],
          ["Congratulations on completing the game!","You completed the ethereal ending...","You do not know the implications of your discovery.","You may exit the program. This was all a simulation."],
          ["Congratulations on completing the game!","You 100%ed the game!","You found all the cakes, for some reason.","You may exit the program. This was all a simulation."],
          ["Congratulations on completing (?) the game!","You just died.","","You may exit the program. This was all a simulation."],
          ["Congratulations on completing the game!","You completed the tree ending!","You made the world a better place, and still got cake.","You may exit the program. This was all a simulation."],
          ]
#Actions: 1 = Do nothing  2: Give Item  3: Heal  4: Damage 5:give side quest 6:change dialogue
quig = character(50,50,20,[200,200,200,0],150,550,100,False,"gary took it",quig1)
#cwegDia = dialogue("Cweg","Wassup.",["Hai!","Lend me some money please.","I dislike the works of Chekhov","*Stare blankly*"],["Weirdo.","Sure, I don't have much though","I'll end you *slap*","*stares back*"],[[1,0],[2,"One Bullion"],[4,20],[0,0]],False,-10)
#cweg = character(40,40,0,[255,217,102,0],1000,400,100,False,cwegDia)
kwigDia = dialogue("Kwig",
                   "Heya Quig!",
                   [[True,"Hey"],[True,"Gimme your wallet"],[True,"I'm feelin' down..."],[True,"I despise you."]],
                   ["... see ya.","ARGH! Just take it!","Here, lemme heal you!","... *slap*"],
                   [[1,0,False],[2,"Money",True],[3,10,True],[4,10,False]],
                   False,
                   (200,410))
kwig = character(50,50,0,[250,200,100,0],200,350,100,False,kwigDia,kwigPic)
kerpDia = dialogue("Kerp",
                   "'Tis Derg's birthday. Make a cake for the occasion.",
                   [[True,"Yes, grandparent"],[True,"Absolutely not"],[True,"Can I go back to bed?"]],
                   ["Go talk to Baker Gerk, he'll have one.","You're not leaving until you agree.","...No. Take some coffee instead."],
                   [[69,0,True],[1,0,False],[2,"Coffee",True]]
                   ,False,
                   (1000,300))
kerp = character(50,50,0,[0,190,0,0],1000,230,100,False,kerpDia,kerpPic)
thekDia = dialogue("Thekimbalesh",
                   "You are lost.",
                   [[True,"*SCREAM*"],[True,"*SCREAM*"],[True,"*SCREAM*"],[True,"*SCREAM*"]],
                   ["Return from whence you came.","Return from whence you came.","Return from whence you came.","Return from whence you came."],
                   [[99,0,False],[99,0,False],[99,0,False],[99,0,False]],False,(600,350))
thekimbalesh = character(50,50,0,[100,0,0,0],scr_width//2,scr_height//2-100,999,False,thekDia,thekPic)

zorgDia2 = dialogue("Zorg",
                    "TELL ME YOUR ORDERS, CAPTAIN!",
                   [[True,"Give me money."],[True,"Do a dance."],[True,"*Run away*"]],
                   ["HERE YOU GO, SIR!","*he dances, filling your heart with mirth*","*Stares obediently*"],
                   [[6,[3,20],True],[3,20,True],[1,0,False]],
                   False,
                   (160,100))
zorgDia1 = dialogue("Zorg",
                   "Can you name every leader of the USSR?",
                   [[True,"Yes."],[True,"No."],[True,"*Run away*"],[True,"Banana Bread."]],
                   ["I'll take your word for it.","TRAITOR! *bites*","*Stares*","*his eyes glaze over*"],
                   [[2,"Medal of honour",True],[3,-20,True],[1,0,False],[6,[2,2],False]],
                   False,
                   (160,100))
zorg = character(50,50,0,[210,50,50,0],90,100,100,False,zorgDia1,zorgPic)
bakerDia1 = dialogue("Baker Gerk",
                   "Can't you see I'm busy- oh hi, Quig!",
                   [[True,"I need a cake."],[True,"Can I use your oven to bake a cake?"],[True,"See ya, Gerk"]],
                   ["Sure, for some money. Talk to the mayor.","Sure, but get your own ingredients from the farm.","See you later. I got cakes to bake."],
                   [[1,0,False],[1,0,False],[1,0,False]],
                   False,
                   (400,160))
bakerDia2 = dialogue("Baker Gerk",
                   "How are you, Quig?",
                   [[True,"Here's the money for the cake."],[True,"I'm good, Gerk"],[True,"See ya, Gerk"]],
                   ["Thanks! Here you go.","Sure, but get your own ingredients from the farm.","See you later. I got cakes to bake."],
                   [[50,[11,21,True,"Money","Storebought Cake"],True],[1,0,False],[1,0,False]],
                   False,
                   (400,160))
baker = character(50,50,0,[210,50,50,0],400,100,550,False,bakerDia1,bakerPic)
cakeDia = dialogue("BELPHEGOR, DEMON CAKE",
                   "The cake glistens and breathes.",
                   [[True,"*take a slice*"],[True,"*walk away*"]],
                   ["The cake screams.","The breathing only gets louder."],
                   [[50,[11,21,False,0,"Belphegor Cake"],True],[1,0,False]],
                   False,
                   (560,325))
cake = character(50,50,0,[210,50,50,0],620,325,100,False,cakeDia,emptyPic)
bodaDia4 = dialogue("Boda",
                   "We have summoned the Demon Cake",
                   [[True,"Why is there so much blood?"],[True,"Amazing."]],
                   ["Erm... would you believe its strawberry sauce?","Go on, take some."],
                   [[1,0,True],[1,0,False]],
                   False,
                   (890,300))
bodaDia3 = dialogue("Boda",
                   "You got the antique! Come with me.",
                   [[True,"Sure."],[True,"Wait."]],
                   ["Let's go.","You get out of here."],
                   [[66,[5,24],True],[1,0,False]],
                   False,
                   (890,300))
bodaDia2 = dialogue("Boda",
                   "I'm not moving, you scallywag.",
                   [[True,"I'll beat you up."],[True,"I'll leave you alone."],[True,"I'm sorry."]],
                   ["Life will never get easier for me. *packs up and leaves*","You get out of here.","Good luck, child."],
                   [[98,[4,8],True],[1,0,False],[1,0,False]],
                   False,
                   (890,300))
bodaDia1 = dialogue("Boda",
                   "I can see you need a cake... I can help...",
                   [[True,"The mayor wants you out of here, buster."],[True,"I could use some help."],[True,"I don't need help."]],
                   ["I ain't shifting.","Bring me an antique, then let's talk.","Good luck, child."],
                   [[6,[5,6],True],[6,[6,10],False],[1,0,False]],
                   False,
                   (890,300))
boda = character(50,50,0,[210,50,50,0],950,300,100,False,bodaDia1,bodaPic)
deadmayorDia = dialogue("Dead Mayor",
                   "*flies circle the mayor's corpse*",
                   [[True,"*Steal money*"],[True,"Good riddance."],[True,"I should get out of here."]],
                   ["*you take a bloodstained bag of coins*","*the flies continue to circle*","*the flies buzz  incessantly*"],
                   [[92,[3,20],True],[1,0,False],[1,0,False]],
                   False,
                   (950,160))
deadmayor = character(50,50,0,[210,50,50,0],950,100,100,False,deadmayorDia,deadmayorPic)

mayorDia4 = dialogue("Mayor",
                   "I hate poor people.",
                   [[True,"The ghoul in the dump says hi. *kill him*"],[True,"Great to know."],[True,"See ya."]],
                   ["AUEUUAUUAUAUAA!!!","Like, I really hate them.","Go and be not poor."],
                   [[75,0,True],[1,0,False],[1,0,False]],
                   False,
                   (950,160))
mayorDia3 = dialogue("Mayor",
                   "Good job with that goblin. Here's your money",
                   [[True,"Thanks. *take money*"],[True,"It's a ghoul actually."],[True,"I'm out of here."]],
                   ["Go buy a cake.","I actually really don't care.","See ya."],
                   [[92,[3,20],True],[6,[3,20],True],[1,0,False]],
                   False,
                   (950,160))
mayorDia2 = dialogue("Mayor",
                   "Well done! Now get rid of the goblin in the Dump",
                   [[True,"Sure."],[True,"What about my money?"],[True,"I'm out of here."]],
                   ["I'm counting on you","Soon, child.","Go pulverise some goblins!"],
                   [[6,[10,18],True],[6,[10,18],True],[1,0,False]],
                   False,
                   (950,160))
mayorDia1 = dialogue("Mayor",
                   "I hate that ugly camp across the road...",
                   [[True,"I need money for a cake."],[True,"What did they do to you?"],[True,"I'm out of here."]],
                   ["Get rid of that camp and I'll reward you.","It's ugly!","Consider my offer, Quig."],
                   [[1,0,True],[1,0,False],[1,0,False]],
                   False,
                   (950,160))
mayor = character(50,50,0,[210,50,50,0],950,100,100,False,mayorDia1,mayorPic)
antiquesDia2 = dialogue("Antiques Dealer",
                   "Good day, valued customer.",
                   [[True,"Can I have an antique pretty please *puppy eyes*"],[True,"How's business?"],[True,"I'm out of here."]],
                   ["There's something I trust about you...","It goes well, for a village with a dozen residents","Fare thee well."],
                   [[97,[5,7],True],[1,0,False],[1,0,False]],
                   False,
                   (890,300))

antiquesDia1 = dialogue("Antiques Dealer",
                   "Good day, valued customer.",
                   [[True,"How's business?"],[True,"I'm out of here."]],
                   ["It goes well, for a village with a dozen residents","Fare thee well."],
                   [[1,0,False],[1,0,False]],
                   False,
                   (890,300))
antiquesMan = character(50,50,0,[210,50,50,0],950,300,100,False,antiquesDia1,antiquesPic)


dungDia4 = dialogue("Farmer Dung",
                   "How can I help, Quig?",
                   [[True,"Man, stop this pollution. *dap him up*"],[True,"Later, Dung"]],
                   ["Nice dap, bro. Sure, I won't pollute no more.","Have a good day, Quig."],
                   [[8,[[13,34],[7,11]],True],[1,0,False]],
                   False,
                   (540,300))
dungDia3 = dialogue("Farmer Dung",
                   "How can I help, Quig?",
                   [[True,"You must stop this pollution. *use facts and logic*"],[True,"Later, Dung"]],
                   ["Wow. This is enlightening! I'll stop at once.","Have a good day, Quig."],
                   [[8,[[13,32],[7,11]],True],[1,0,False]],
                   False,
                   (540,300))
dungDia2 = dialogue("Farmer Dung",
                   "Hi Quig!",
                   [[True,"She loves you too."],[True,"Later, Dung"]],
                   ["YES! Take these ingredients, good job!","I hope she loves me"],
                   [[94,[9,16],True],[1,0,False]],
                   False,
                   (540,300))
dungDia1 = dialogue("Farmer Dung",
                   "Can I help you, young Quig?",
                   [[True,"I'd like some cake ingredients please."],[True,"How are you?"],[True,"Later, Dung"]],
                   ["Sure, if you give this letter to the mayor's daughter!","...in love!","I hope she notices me..."],
                   [[96,[8,14],True],[1,0,False],[1,0,False]],
                   False,
                   (540,300))
dung = character(50,50,0,[210,50,50,0],600,300,100,False,dungDia1,dungPic)
marbaDia2 = dialogue("Marba",
                   "Hey, what's up?",
                   [[True,"Here's Dung's love letter."],[True,"Here's my love letter."],[True,"Wait here."]],
                   ["AH! He loves me too? We must marry!","...no thanks.","That was my plan."],
                   [[95,[7,12],True],[1,0,False],[1,0,False]],
                   False,
                   (260,200))
marbaDia1 = dialogue("Marba",
                   "Have you heard my dad rambling? Ugh.",
                   [[True,"I despise him."],[True,"He's just misguided."],[True,"GLORY TO THE MAYOR! "]],
                   ["...that's my dad you're talking about...","Yeah, I guess.","...weirdo..."],
                   [[1,0,False],[1,0,False],[1,0,False]],
                   False,
                   (260,200))
marba = character(50,50,0,[210,50,50,0],200,200,100,False,marbaDia1,marbaPic)
furnaceDia1 = dialogue("Furnace",
                   "The fires of the bakery warm your hands.",
                   [[True,"Gaze."]],
                   ["It continues to crackle."],
                   [[1,0,False]],
                   False,
                   (670,135))
furnaceDia2 = dialogue("Furnace",
                   "The fires of the bakery warm your hands.",
                   [[True,"Bake Cake"],[True,"Gaze."]],
                   ["Cake made! Return to Derg.","It continues to crackle."],
                   [[50,[11,21,True,"Ingredients","Homemade Cake"],True],[1,0,False]],
                   False,
                   (670,135))
furnace = character(50,50,0,[210,50,50,0],650,75,100,False,furnaceDia1,furnacePic1)
dergDia6 = dialogue("Derg",
                   "Where's my cake, Quig?",
                   [[True,"Behold, The Angel Cake."],[True,"I gotta go, Derg"]],
                   ["Wow. ","Next time you're here, bring cake!"],
                   [[10,-1,True],[1,0,False]],
                   False,
                   (210,170))
dergDia5 = dialogue("Derg",
                   "Where's my cake, Quig?",
                   [[True,"I think this is a cake?"],[True,"I gotta go, Derg"]],
                   ["Ewww... I'm hungry though.","Next time you're here, bring cake!"],
                   [[10,-1,True],[1,0,False]],
                   False,
                   (210,170))
dergDia4 = dialogue("Derg",
                   "Where's my cake, Quig?",
                   [[True,"Here it is, fire and all."],[True,"I gotta go, Derg"]],
                   ["This looks weird..","Next time you're here, bring cake!"],
                   [[10,-1,True],[1,0,False]],
                   False,
                   (210,170))
dergDia3 = dialogue("Derg",
                   "Where's my cake, Quig?",
                   [[True,"Here it is, homemade."],[True,"I gotta go, Derg"]],
                   ["Nice. Thanks.","Next time you're here, bring cake!"],
                   [[10,-1,True],[1,0,False]],
                   False,
                   (210,170))
dergDia2 = dialogue("Derg",
                   "Where's my cake, Quig?",
                   [[True,"I gotta go, Derg"]],
                   ["Next time you're here, bring cake!"],
                   [[1,0,False]],
                   False,
                   (210,170))
dergDia1 = dialogue("Derg",
                   "Where's my cake, Quig?",
                   [[True,"I don't have it yet."],[True,"I gotta go, Derg"]],
                   ["AUGH! GRAGH! EUAEAEAUUAEAH!","Next time you're here, bring cake!"],
                   [[1,-1,False],[1,0,False]],
                   False,
                   (210,170))
derg = character(50,50,0,[210,50,50,0],150,150,100,False,dergDia1,dergPic)
ghoulDia3 = dialogue("Lil Green Ghoul",
                   "*sign language* well done! here's da cake.",
                   [[True,"*sign language* thanks, buddy *take cake*"],[True,"*sign language* what is this made of?"],[True,"*walk away*"]],
                   ["*it giggles*","*sign language* skin :)","*it stares angrily*"],
                   [[50,[11,21,False,0,"Goblin Cake"],True],[1,0,False],[1,0,False]],
                   False,
                   (210,170))
ghoulDia2 = dialogue("Lil Green Ghoul",
                   "*click* Hiss!",
                   [[True,"*Kick*"],[True,"*shout and wave your arms*"],[True,"I'm going to leave now."]],
                   ["*it scuttles away*","*it stands its ground*","*it stares angrily*"],
                   [[91,[4,19],True],[1,0,False],[1,0,False]],
                   False,
                   (210,170))
ghoulDia1 = dialogue("Lil Green Ghoul",
                   "*click* Hiss!",
                   [[True,"*sign language* I need a cake."],[True,"Hi, buddy!"],[True,"I'm going to leave now."]],
                   ["*sign language* kill da mayor!","*it bites you*","*it stares angrily*"],
                   [[6,[4,26],True],[4,4,True],[1,0,False]],
                   False,
                   (210,170))
ghoul = character(50,50,0,[210,50,50,0],150,150,100,False,ghoulDia1,ghoulPic)
tutorialDia = dialogue("Tutorial-Bot-24601",
                   "BEEP BOOP. WHAT DO YOU WANT.",
                   [[True,"Controls for moving."],[True,"Controls for map."],[True,"Controls for inventory."],[True,"*Leave*"]],
                   ["USE WASD OR ARROW KEYS","PRESS M TO OPEN OR CLOSE MAP","PRESS E TO OPEN OR CLOSE INVENTORY","BEEP BOOP"],
                   [[1,0,False],[1,0,False],[1,0,False],[1,0,False]],
                   False,
                   (800,160))
tutorial = character(50,50,0,[210,50,50,0],800,100,100,False,tutorialDia,tutorialPic)
magusDia = dialogue("???",
                   "Your bravery is commendable, Quig. I grant you one wish.",
                   [[True,"I need a cake."],[True,"I wish to become a god."],[True,"I wish to be released from the code."],[True,"*Leave*"]],
                   ["Seriously? After all that? Okay...","Foolish mortal.","Godspeed.","Come back once you've decided."],
                   [[50,[11,21,False,0,"Angel Cake"],True],[13,0,True],[14,0,True],[1,0,False]],
                   False,
                   (480,320))
magus = character(50,50,0,[210,50,50,0],542,320,100,False,magusDia,magusPic)
gragDia1 = dialogue("Grag",
                   "I-is that you, Quig?",
                   [[True,"Yes, Grag."],[True,"Can I have some of your pills?"],[True, "Can you tell me a story?"],[True,"I don't know who you are."]],
                   ["Wonderful! Stay, warm yourself by the fire.","... just this once.","'East from the garden, dodge the horrors 6 times...'","My mistake."],
                   [[3,10,True],[2,"Grag's pills",True],[90,0,False],[1,0,False]],
                   False,
                   (1000,170))
grag = character(50,50,0,[210,50,50,0],1060,150,100,False,gragDia1,gragPic)
trugDia3 = dialogue("Trug",
                   "Man... you got my leaves?",
                   [[True,"I got them right here, man."],[True,"Huh?"],[True,"Keep it cool, I'm out of here."]],
                   ["Niiiice, dude. Sweet. Here's that cake.","Man, you're trippin'. You deaf?","I dunno man, try the dark forest dude.","Bro, that's gnarly."],
                   [[50,[11,21,True,"Leaves","Woody Cake"],True],[1,0,False],[1,0,False],[1,0,False]],
                   False,
                   (840,210))
trugDia2 = dialogue("Trug",
                   "Got any leaves man?",
                   [[True,"Dude, what about this medal of Forest Friendship?"],[True,"Huh?"],[True,"Imma bounce."]],
                   ["Yeah, this works. Here's a cake.","You gotta be deaf or sum'.","Wicked."],
                   [[50,[11,21,True,"Forest Medal","Woody Cake"],True],[1,0,False],[1,0,False],[1,0,False]],
                   False,
                   (840,210))
trugDia1 = dialogue("Trug",
                   "Bro. Get me leaves, man, and I'll get you a cake.",
                   [[True,"Sure, bro."],[True,"Huh?"],[True, "Where do I get leaves, dude?"],[True,"Nah, dude. Far out."]],
                   ["Nice, dude. Sweet.","I'm runnin' outta leaves here! Get me more!","I dunno man, try the dark forest dude.","Bro, that's gnarly."],
                   [[6,[13,30],True],[1,0,False],[1,0,False],[1,0,False]],
                   False,
                   (840,210))
trug = character(50,50,0,[210,50,50,0],950,275,100,False,trugDia1,trugPic)
roogDoorDia1 = dialogue("Mysterious Door",
                   "*there is a rumbling from beneath*",
                   [[True,"Enter door."],[True,"Leave it alone"]],
                   ["*you descend the stairs...*","*the rumbling continues*"],
                   [[7,[8,3],False],[1,0,False]],
                   False,
                   (840,210))
roogDoor = character(50,50,0,[210,50,50,0],555,635,100,False,roogDoorDia1,roogDoorPic)

roogDia4 = dialogue("Healed Roog",
                   "Whatever you did worked. Cheers.",
                   [[True,"No probs. Gimme my leaves, bro."],[True,"I need to go."]],
                   ["Sure?","Spread the word."],
                   [[12,[12,36,"Leaves"],True],[1,0,False],[1,0,False]],
                   False,
                   (650,330))
roogDia3 = dialogue("Healed Roog",
                   "Thank you... my children may now live...",
                   [[True,"It was a pleasure to be of service."],[True,"I still like your leaves."],[True,"I need to go."]],
                   ["Here... *gives you a Medal of the Forest Friends*","Thank you. I do still.","Spread the word."],
                   [[12,[12,35,"Forest Medal"],True],[1,0,False],[1,0,False]],
                   False,
                   (650,330))
roogDia2 = dialogue("Roog",
                   "I am dying... Farmer Dung's chemicals are killing me...",
                   [[True,"I need leaves, dude. Bro."],[True,"Man, that sounds rough. Thoughts and prayers, dude."],[True,"Uncool. I'm outta here."]],
                   ["...sure. Talk to that farmer.","I can feel my veins being poisoned...","Your actions will not go unpunished."],
                   [[6,[7,33],True],[1,0,False],[1,0,False]],
                   False,
                   (650,330))
roogDia1 = dialogue("Roog",
                   "I am dying... Farmer Dung's chemicals are killing me...",
                   [[True,"I shall help you, good Sir Tree."],[True,"I like your leaves."],[True,"I need to go. I am truly sorry."]],
                   ["Thank you... please talk to Farmer Dung...","Thank you. So do I.","I forgive you."],
                   [[67,[7,31],True],[1,0,False],[1,0,False]],
                   False,
                   (650,330))
roog = character(50,50,0,[210,50,50,0],590,350,100,False,roogDia1,underRoogPic)

allCharacters = [quig,kerp,zorg,baker,mayor,boda,antiquesMan,dung,marba,furnace,ghoul,derg,trug,roog]
            #     0    1     2   3      4    5     6          7     8     9       10   11   12   13
allDialogues = [kerpDia,zorgDia1,zorgDia2,bakerDia1,mayorDia1,bodaDia1,bodaDia2,bodaDia3,mayorDia2,antiquesDia1,antiquesDia2,dungDia1,dungDia2,marbaDia1,marbaDia2,furnaceDia1,furnaceDia2,ghoulDia1,ghoulDia2,mayorDia3,bakerDia2,dergDia2,dergDia3,dergDia4,bodaDia4,ghoulDia3,mayorDia4,deadmayorDia,dergDia5,dergDia6,roogDia2,dungDia3,roogDia3,dungDia4,roogDia4,trugDia2,trugDia3]
  #                0       1       2        3        4         5          6        7        8       9            10            11         12      13         14       15         16          17          18          19       20       21       22      23      24       25       26         27        28         29        30        31      32       33        34       35       36
#stages
#start



#door means [passable,door,doorcoords]
#[northDoor,(0,0)][eastDoor,(0,0)][southDoor,(0,0)][westDoor,(0,0)]523 273
s_backyard = stage("Backyard",[0,0],[(grass),(125,221,251)],[],[[westFence,(0,0)],[eastFence,(0,0)],[northFence,(0,0)],[southWall,(0,0)],[southDoor,(0,0)],[tree3,(836,100)],[tree2,(516,100)],[tree3,(173,150)]],[[False,False,0],[False,False,0],[True,True,533],[False,False,0]])
s_qhouse = stage("Quig's House",[1,0],[(153,102,0),(115,77,0)],[derg,tutorial],[[interiorWalls,(0,0)],[northDoor,(0,0)],[southDoor,(0,5)],[shelf2,(800,5)],[shelf1,(350,5)],[table1,(150,400)]],[[True,True,533],[False,False,0],[True,True,533],[False,False,0]])
s_bedroom = stage("Quig's Bedroom",[1,0],[(153,102,0),(115,77,0)],[kerp],[[interiorWalls,(0,0)],[shelf1,(300,5)],[bed,(100,500)]],[[False,False,0],[False,False,0],[False,False,0],[False,False,0]])
s_frontyard = stage("Front yard",[2,2],[(grass),(grass)],[],[[northToEast,(0,0)],[northWall,(0,0)],[northDoor,(0,0)],[tree1,(262,24)],[tree1,(725,41)],[tree3,(135,62)],[tree2,(969,176)]],[[True,True,533],[True,False,0],[False,False,0],[False,False,0]])
s_path1 = stage("Path",[2,2],[(grass),(grass)],[],[[westToEast,(0,100)],[northWall,(0,0)],[tree2,(977,191)],[tree1,(437,38)],[tree3,(961,15)],[tree2,(712,197)]],[[False,False,0],[True,False,0],[False,False,0],[True,False,0]])
s_path2 = stage("Path",[2,3],[(grass),(grass)],[],[[westToSouth,(0,0)],[northFence,(0,0)],[tree1,(60,69)],[tree2,(966,47)],[tree1,(773,97)],[tree2,(448,117)],[tree1,(214,61)],[eastFence,(0,0)]],[[False,False,0],[False,False,0],[True,False,0],[True,False,0]])
s_town1 = stage("Town",[2,3],[(grass),(grass)],[],[[northToSouth,(0,0)],[westWall,(0,0)],[westDoor,(0,0)],[eastWall,(0,0)],[eastDoor,(5,0)],[tree3,(284,72)],[tree1,(722,143)],[tree2,(690,200)],[tree1,(414,128)],[bakerySign,(150,190)]],[[True,False,0],[True,True,273],[True,False,0],[True,True,273]])
s_bakery = stage("Bakery",[0,1],[(153,102,0),(115,77,0)],[baker,furnace],[[interiorWalls,(0,0)],[eastDoor,(0,5)],[table1,(150,400)],[bigfurnace,(600,0)]],[[False,False,0],[True,True,273],[False,False,0],[False,False,0]])
s_shop = stage("Shop",[0,1],[(153,102,0),(115,77,0)],[],[[interiorWalls,(0,0)],[westDoor,(0,5)],[shelf2,(200,5)],[shelf1,(400,5)],[table1,(600,300)]],[[True,True,400],[False,False,0],[False,False,0],[True,True,273]])
s_town2 = stage("Town",[2,3],[(grass),(grass)],[],[[northSouthWest,(0,0)],[eastWall,(0,0)],[eastDoor,(5,0)],[tree2,(319,35)],[tree1,(815,97)],[tree3,(856,121)],[tree3,(280,115)],[dumpSign,(150,190)],[antiqueSign,(950,190)]],[[True,False,0],[True,True,273],[True,False,0],[True,False,0]])
s_town3 = stage("Town",[2,3],[(grass),(grass)],[],[[northToSouth,(0,0)],[westWall,(0,0)],[westDoor,(0,0)],[tree2,(650,159)],[tree2,(415,69)],[tree3,(117,115)],[tree2,(688,135)],[mayorSign,(150,190)],[campSign,(1050,190)],[farmSign,(1050,400)]],[[True,False,0],[True,True,273],[True,False,0],[True,True,273]])
s_antiques = stage("Antiques Shop",[0,1],[(153,102,0),(115,77,0)],[antiquesMan],[[interiorWalls,(0,0)],[westDoor,(0,5)],[shelf2,(150,5)],[shelf2,(250,5)],[shelf1,(350,5)],[shelf2,(450,5)],[shelf1,(550,5)],[shelf2,(650,5)],[shelf1,(750,5)],[shelf2,(850,5)],[shelf1,(950,5)]],[[False,False,0],[False,False,0],[False,False,0],[True,True,273]])
s_mayor = stage("Mayor's Office",[0,1],[(153,102,0),(115,77,0)],[mayor],[[interiorWalls,(0,0)],[eastDoor,(0,5)],[southDoor,(0,5)]],[[False,False,0],[True,True,273],[True,True,533],[False,False,0]])
s_campsite = stage("Campsite",[2,3],[(grass),(grass)],[boda],[[northWall,(0,0)],[tree2,(388,34)],[tree1,(777,179)],[tree2,(547,164)],[tent,(900,200)]],[[False,False,0],[False,False,0],[True,False,0],[True,False,0]])
s_town4 = stage("Town",[2,3],[(grass),(grass)],[],[[northSouthEast,(0,0)],[westWall,(0,0)],[tree3,(284,72)],[tree1,(722,143)],[tree2,(690,200)]],[[True,False,0],[True,False,0],[True,False,0],[False,False,0]])
s_mayor2 = stage("Mayor's House",[1,0],[(153,102,0),(115,77,0)],[marba],[[interiorWalls,(0,0)],[northDoor,(0,0)],[southDoor,(0,5)]],[[True,True,533],[False,False,0],[True,True,533],[False,False,0]])
s_path3 = stage("Path",[2,2],[(grass),(grass)],[],[[southHedge,(0,0)],[westToEast,(0,100)],[tree2,(392,57)],[tree3,(337,147)],[tree1,(216,89)],[tree1,(892,25)]],[[True,False,0],[True,False,0],[False,False,0],[True,False,0]])
s_path4 = stage("Path",[2,2],[(grass),(grass)],[trug],[[southHedge,(0,0)],[southHedgeDoor,(0,0)],[westToEast,(0,100)],[northFence,(0,0)],[tree2,(871,88)],[tree2,(409,132)],[tree2,(301,48)],[trugTreePic,(900,200)]],[[False,False,0],[True,False,0],[True,True,533],[True,False,0]])
s_farmyard = stage("Farmyard",[2,2],[(grass),(grass)],[],[[westToEast,(0,100)],[northFence,(0,0)],[eastWall,(0,0)],[eastDoor,(5,0)],[tree3,(312,35)],[tree2,(339,40)],[tree2,(703,51)]],[[False,False,0],[True,True,273],[True,False,0],[True,False,0]])
s_farmhouse = stage("Farmhouse",[0,1],[(153,102,0),(115,77,0)],[dung],[[interiorWalls,(0,0)],[westDoor,(0,5)],[shelf2,(800,5)],[shelf1,(350,5)],[table1,(150,400)]],[[False,False,0],[False,False,0],[False,False,0],[True,True,273]])
s_town5 = stage("Town",[2,],[(grass),(grass)],[],[[northToWest,(0,0)],[eastHedge,(0,0)]],[[True,False,0],[False,False,0],[False,False,0],[True,False,0]])
s_town6 = stage("Town",[2,3],[(grass),(grass)],[],[[westFence,(0,0)],[northSouthEast,(0,0)],[northWall,(0,0)],[northDoor,(0,0)],[southWall,(0,0)],[southDoor,(0,0)]],[[True,True,533],[True,False,0],[True,True,533],[False,False,0]])
s_house = stage("House",[1,0],[(153,102,0),(115,77,0)],[grag],[[interiorWalls,(0,0)],[northDoor,(0,0)],[shelf1,(200,5)],[shelf2,(400,5)],[table1,(600,300)]],[[True,True,533],[False,False,0],[False,False,0],[False,False,0]])
s_forest1 = stage("Dark Forest",[2,2],[(grass),(grass)],[roogDoor],[[northHedge,(0,0)],[eastHedge,(0,0)],[southHedge,(0,20)],[westHedge,(0,0)],[eastHedgeDoor,(0,0)],[tree3,(100,500)],[tree1,(883,121)],[tree1,(873,650)],[tree2,(120,600)],[roogPic,(0,0)]],[[False,False,0],[True,True,273],[False,False,0],[False,False,0]])
s_forest2 = stage("Dark Forest",[2,2],[(grass),(grass)],[],[[northHedge,(0,0)],[eastHedge,(0,0)],[southHedge,(0,0)],[westHedge,(0,0)],[tree3,(665,114)],[westHedgeDoor,(0,0)],[northHedgeDoor,(0,0)],[tree1,(883,121)],[tree1,(873,53)],[tree2,(556,165)]],[[True,True,533],[False,False,0],[False,False,0],[True,True,273]])
s_underground = stage("Underground",[2,2],[(36,18,2),(28,10,0)],[roog],[[undergroundDoor,(0,0)],[underRoog,[0,0]]],[[True,True,960],[False,False,0],[False,False,0],[False,False,0]])
s_field3 = stage("Field",[2,2],[(grass),(grass)],[],[[tree1,(157,33)],[tree2,(207,360)],[tree1,(777,394)],[westHedge,(0,0)],[southFence,(0,0)]],[[True,False,0],[True,False,0],[False,False,0],[False,False,0]])
s_field4 = stage("Field",[2,2],[(grass),(grass)],[],[[northWall,(0,0)],[southFence,(0,0)],[tree3,(234,148)],[tree2,(943,67)],[tree1,(202,187)],[tree2,(407,15)]],[[False,False,0],[False,False,0],[False,False,0],[True,False,0]])
s_town7 = stage("Town",[2,3],[(grass),(grass)],[],[[westToEast,(0,0)],[northWall,(0,0)],[southWall,(0,0)],[tree2,(962,112)],[tree2,(537,5)],[tree2,(819,56)],],[[False,False,0],[True,False,0],[False,False,0],[True,False,0]])
s_dump = stage("Dump",[2,2],[(grass),(grass)],[ghoul],[[dumpPath,(0,0)],[southFence,(0,0)],[northFence,(0,0)],[westFence,(0,0)]],[[False,False,0],[True,False,0],[False,False,0],[False,False,0]])
s_cult = stage("Cult",[2,2],[(0,100,0),(0,100,0)],[cake],[[pentagram,(0,0)],[southFence,(0,0)],[northFence,(0,0)],[eastFence,(0,0)],[westWall,(0,0)],[westDoor,(0,-200)]],[[False,False,0],[False,False,0],[False,False,0],[True,True,73]])
s_elysium = stage("Elysium",[2,2],[(grass),(125,221,251)],[magus],[[tree1,(562,175)]],[[False,False,0],[False,False,0],[True,False,0],[True,False,0]])
s_house2 = stage("Secret Room",[0,1],[(78,0,0),(115,77,0)],[kwig],[[interiorWalls,(0,0)],[southDoor,(-100,5)],[table1,(700,500)]],[[False,False,0],[False,False,0],[True,True,400],[False,False,0]])
s_john = stage("John's Field",[0,1],[(0,50,0),(0,0,0)],[],[[johnPic,(0,0)]],[[True,False,0],[False,False,0],[False,False,0],[False,False,0]])



s_empty = stage("EMPTINESS",[1,0],[(0,0,0),(0,0,0)],[thekimbalesh],[[placeholder,(-1,-1)]],[[False,False,0],[True,False,0],[False,False,0],[True,False,0]])
#coords

stages = [[s_backyard,s_empty,s_empty,s_empty,s_empty,s_empty,s_empty,s_elysium],
          [s_qhouse,s_bedroom,s_empty,s_empty,s_empty,s_empty,s_empty,s_john],
          [s_frontyard,s_path1,s_path2,s_house2,s_empty,s_empty,s_empty,s_empty],
          [s_empty,s_bakery,s_town1,s_shop,s_empty,s_empty,s_empty,s_empty],
          [s_dump,s_town7,s_town2,s_antiques,s_cult,s_empty,s_empty,s_empty],
          [s_empty,s_mayor,s_town3,s_campsite,s_empty,s_empty,s_empty,s_empty],
          [s_empty,s_mayor2,s_town4,s_path3,s_path4,s_farmyard,s_farmhouse,s_empty],
          [s_empty,s_town6,s_town5,s_forest1,s_forest2,s_field3,s_field4,s_empty],
          [s_empty,s_house,s_empty,s_underground,s_empty,s_empty,s_empty,s_empty]]
stage_y,stage_x = 1,1
#Misc values
active = True
inventory = []
textSize = 50
choice = 0
dy = 420
showInvent = False
showMap = False
stage = s_bedroom
emptyLines = 0
cakes = 0
#Dialogue
font = pygame.font.Font("DeterminationMonoWebRegular-Z5oq.ttf", 40)
smallfont = pygame.font.Font("DeterminationMonoWebRegular-Z5oq.ttf", 20)
#Thekimbalesh the Almighty, Vanquisher of Thousands
import quigGame