i, k, heartNum = 0, 0, 0
numstr, ch, heartstr = "", "", ""

## 2021041039 이수민 ##

if __name__ == "__main__" :
   numstr = input("숫자를 여러개 입력하세요 : ")
   print("")
   i = 0
   ch = numstr[i]
   while True :
       heartNum = int(ch)

       heartstr = ""
       for k in range(0,heartNum) :
           heartstr += "\u2665"
           k += 1

       print(heartstr)

       i += 1
       if(i > len(numstr) -1) :
            break

       ch = numstr[i]

 # NameError: name 'heartNume' is not defined. Did you mean: 'heartNum'?
 #  heartNume -> heartNum 변경 
