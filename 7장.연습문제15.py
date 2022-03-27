import turtle
import random

## 2021041039 이수민 ##

myTurtle, tX, tY, tColor, tSize, tShape= [None] * 6 
playerTurtles = []
swidth, sheight = 500, 500

## 메인 함수 부분 ##
if __name__ == "__main__" :
    turtle.title('리스트 활용해서 거북이 정렬')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    


    ## 랜덤으로 거북이 객체 5개를 생성 후 playerTurtles에 넣기 ##
    for i in range(0, 5) :
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random(); g = random.random(); b = random.random()
        tAngle = random.randrange(0,361)
        tSize = random.randrange(1,100)/10
        playerTurtles.append([myTurtle, tSize, r, g, b, tX, tY])
# 2차원 리스트 형태

## tSum을 key로 해서 playerTurtles를 오름차순 정렬한 다음 reverse ##
##playerTurtles의 각 원소를 반환하면 이를 turtles로 받아 turtles[1]인 tSize을 key로 사용 ##
    soredTurtles = sorted(playerTurtles, key=lambda turtles : turtles[1] ,reverse = True)

    for index, tList in enumerate(soredTurtles[0:]) : # enumerate는 index 값을 같이 반환해 줌 (튜플 형태)
        myTurtle = tList[0]
        myTurtle.color((tList[2], tList[3], tList[4]))
        myTurtle.pencolor((tList[2], tList[3], tList[4]))
        myTurtle.turtlesize(tList[1])
        myTurtle.penup()
        if index == 0 : # 첫 번째 거북이는 이전 거북이가 없기 때문에 해당 위치로만 이동
            myTurtle.goto(tList[5], tList[6])
            continue
        myTurtle.goto(soredTurtles[index-1][5], soredTurtles[index-1][6])
         # 선을 그을 거북이를 이 전의 거북이 위치로 이동
        myTurtle.pendown()
        myTurtle.goto(tList[5], tList[6])
         # 설정된 거북이의 좌표로 이동하면서 선 긋기

turtle.done()
