from tkinter import*
from tkinter import ttk

## 2021041039 이수민 ##
## 탭 화면 만들기 ##

window = Tk()


baseTab=ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text='강아지')
tabCat= ttk.Frame(baseTab)
baseTab.add(tabCat, text='고양이')

baseTab.pack(expand=1, fill="both")

photoDog = PhotoImage(file = "강아지.gif")
labelDog=Label(tabDog, image= photoDog)
labelDog.pack()

photoCat = PhotoImage(file = "고양이.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()
