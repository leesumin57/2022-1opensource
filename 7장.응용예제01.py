## 16진수 정렬하기 ##
import random

data =[]
i,j=0,0

## 2021041039 이수민 ##

if __name__ == "__main__" :
    for i in range(0,5) :
        tmp = hex(random.randrange(0,100000))
        data.append(tmp)

        print('\n정렬 전 데이터 :', end ='')
        [print(num, end = ' ') for num in data]

        for i in range(0, len(data) -1) : # 선택정렬
            for j in range(i+1, len(data)) :
                if int(data[i],16) > int(data[j],16) :
                    tmp = data[i]
                    data[i] = data[j]
                    data[j] = tmp

        print('\n정렬 후 데이터 : ', end = '')
        [print(num, end = ' ') for num in data]
            
