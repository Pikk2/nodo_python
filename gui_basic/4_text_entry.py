from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("480x360+1050+400") 
# //////////////////////////////////////////

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")


# 엔터 안되고 한줄로 입력 받음 ㅎㅎ
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력 하세요 : ")



def btncmd():
    print(txt.get("1.0", END)) # 1 : 첫번째라인, 0 : 0번째 column 위치
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()





root.mainloop()
