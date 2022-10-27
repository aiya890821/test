import tkinter as tk

'''
创建一个GUI程序

1、导入 Tkinter 模块
2、创建控件
3、指定这个控件的 master， 即这个控件属于哪一个
4、告诉 GM(geometry manager) 有一个控件产生了。
'''
root=tk.Tk()  # 建立主窗口
root.title("简易计算器")
root.geometry("295x280")
# root.attributes("-alpha",0.9)
'''
说明

1、mainloop()方法允许程序循环执行，并进入等待和处理事件。

窗口中的组件可以理解为一个连环画.

2、mainloop()方法的作用是监控每个组件，当组件发生变化或触发事件时，会立即更新窗口。
'''
font=('宋体',20)
font_16=('宋体',16)

result_num=tk.StringVar()
result_num.set(" ")

tk.Label(root,
         textvariable=result_num,font=font,height=2,
         width=20,justify=tk.LEFT,anchor=tk.SE
        ).grid(row=1,column=1,columnspan=4)

button_clear=tk.Button(root,text='C',width=5,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_back=tk.Button(root,text='←',width=5,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_division=tk.Button(root,text='/',width=5,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_multiplication=tk.Button(root,text='x',width=5,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_clear.grid(row=2,column=1,padx=4,pady=2)
button_back.grid(row=2,column=2,padx=4,pady=2)
button_division.grid(row=2,column=3,padx=4,pady=2)
button_multiplication.grid(row=2,column=4,padx=4,pady=2)


button_seven=tk.Button(root,text='7',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_eight=tk.Button(root,text='8',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_nine=tk.Button(root,text='9',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_substaction=tk.Button(root,text='_',width=5,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_seven.grid(row=3,column=1,padx=4,pady=2)
button_eight.grid(row=3,column=2,padx=4,pady=2)
button_nine.grid(row=3,column=3,padx=4,pady=2)
button_substaction.grid(row=3,column=4,padx=4,pady=2)

button_four=tk.Button(root,text='4',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_five=tk.Button(root,text='5',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_six=tk.Button(root,text='6',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_add=tk.Button(root,text='+',width=5,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_four.grid(row=4,column=1,padx=4,pady=2)
button_five.grid(row=4,column=2,padx=4,pady=2)
button_six.grid(row=4,column=3,padx=4,pady=2)
button_add.grid(row=4,column=4,padx=4,pady=2)

button_one=tk.Button(root,text='1',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_two=tk.Button(root,text='2',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_three=tk.Button(root,text='3',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
button_equal=tk.Button(root,text='=',width=5,height=3,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_one.grid(row=5,column=1,padx=4,pady=2)
button_two.grid(row=5,column=2,padx=4,pady=2)
button_three.grid(row=5,column=3,padx=4,pady=2)
button_equal.grid(row=5,column=4,padx=4,pady=2,rowspan=2)

button_zero=tk.Button(root,text='0',width=12,font=font_16,relief=tk.FLAT,bg='#eacda1')
# button_zero1=tk.Button(root,text='0',width=5,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_dot=tk.Button(root,text='.',width=5,font=font_16,relief=tk.FLAT,bg='#eacda1')
# button_equal=tk.Button(root,text='=',width=5,font=font_16,relief=tk.FLAT,bg='#b1b2b2')
button_zero.grid(row=6,column=1,padx=4,pady=2,columnspan=2)
# button_zero1.grid(row=6,column=2,padx=4,pady=2)
button_dot.grid(row=6,column=3,padx=4,pady=2)
# button_equal.grid(row=6,column=4,padx=4,pady=2)




#点击事件
def click_button(x):
    print('x',x)
    result_num.set(result_num.get()+x)
#计算结果
def calculation():
    opt_str=result_num.get()
    result=eval(opt_str)
    result_num.set(str(result))

def clear():
    result_num.set(" ")
def backspace():
    res=str(result_num.get())
    # print(res[:-1])  #删除输入的最后一个字符
    result_num.set(res[:-1])

button_zero.config(command=lambda: click_button('0'))
button_one.config(command=lambda: click_button('1'))
button_two.config(command=lambda: click_button('2'))
button_three.config(command=lambda: click_button('3'))
button_four.config(command=lambda: click_button('4'))
button_five.config(command=lambda: click_button('5'))
button_six.config(command=lambda: click_button('6'))
button_seven.config(command=lambda: click_button('7'))
button_eight.config(command=lambda: click_button('8'))
button_nine.config(command=lambda: click_button('9'))
button_add.config(command=lambda: click_button('+'))
button_substaction.config(command=lambda: click_button('-'))
button_multiplication.config(command=lambda: click_button('*'))
button_division.config(command=lambda: click_button('/'))
button_dot.config(command=lambda: click_button('.'))
button_equal.config(command=calculation)
button_clear.config(command=clear)
button_back.config(command=backspace)

root.mainloop() # 进入等待与处理窗口事件
