# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.font
import tkinter.filedialog
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


window=tk.Tk()
window.title("HMD Deeplearning Camp: Python Program")
window.geometry("640x400+100+100")
window.resizable(False, False)

count=0

#%%
def example():
    example=tk.Tk()
    example.title("Example")
    example.geometry("640x400+100+100")
    example.resizable(False, False)
    label = tk.Label(example, text="버튼을 누르면 1씩 증가된 값을 출력하는 카운터를 만드시오.")
    label.pack()
    
    def countUP():
        global count
        
        
    font=tk.font.Font(family="맑은 고딕", size=30, slant="italic")
    
    label1 = tk.Label(example, text="0", font=font)
    label1.place(x=310, y=150) 
    button = tk.Button(example, overrelief="solid", width=50, height=5, command=countUP, repeatdelay=1000, repeatinterval=100, text='카운터')
    button.pack()
    
button = tk.Button(window, overrelief="solid", width=70, height=3, command=example, repeatdelay=1000, repeatinterval=100, text='예제')
button.pack()
    


#%% For문과 numpy를 이용하여 1부터 10까지의 list를 만들고 list의 곱을 계산 계산
def Mission1():        
    Mission1=tk.Tk()
    Mission1.title("Mission1")
    Mission1.geometry("640x400+100+100")
    Mission1.resizable(False, False)    
    label1_Mission1 = tk.Label(Mission1, text="1. 1부터 10까지의 값을 갖는 list를 만들고 출력")
    label1_Mission1.pack()
    label2_Mission1 = tk.Label(Mission1, text="2. For문을 활용하여 위에서 만든 list가 갖고있는 값들을 곱한 결과 출력")
    label2_Mission1.pack()
    label3_Mission1 = tk.Label(Mission1, text="3. numpy를 활용하여 위에서 만든 list가 갖고있는 값들을 곱한 결과 출력")
    label3_Mission1.pack()
    
    def forandnumpy():
        global a
        
        # Mission1_1

        
        # Mission1_2

        
        # Mission1_3

    
    
    btnMission1 = tk.Button(Mission1, overrelief="solid", width=70, height=3, command=forandnumpy, repeatdelay=1000, repeatinterval=100, text='결과보기') # 버튼을 올릴 장소, 버튼에 들어갈 내용
    btnMission1.pack() # auto 위치 지정 
btn1 = tk.Button(window, overrelief="solid", width=70, height=3, command=Mission1, repeatdelay=1000, repeatinterval=100, text='미션1') # 버튼을 올릴 장소, 버튼에 들어갈 내용
btn1.pack()

#%% 조건문을 이용하여 1을 입력받으면 10 2를 입력받으면 20 3을 입력받으면 30으로 출력
def Mission2():
    Mission2=tk.Tk()
    Mission2.title("Mission2")
    Mission2.geometry("640x400+100+100")
    Mission2.resizable(False, False)    
    label1_Mission2 = tk.Label(Mission2, text="조건문을 활용하여 1을 입력받으면 10, 2를 입력받으면 20, 3을 입력받으면 30으로 출력")
    label1_Mission2.pack()
    label2_Mission2 = tk.Label(Mission2, text="1. Tkinter를 활용해서 데이터 입력받아서 출력")
    label2_Mission2.pack()
    label3_Mission2 = tk.Label(Mission2, text="2. 조건문을 활용하여 알고리즘 구성")
    label3_Mission2.pack()
    
    def ifelse():
        global b
        
        # Mission2_1
        
        
        def output():
            global c
            #입력받은 내용을 저장 후 출력

            
        # Mission2_2
 

            
        button1_ifelse = tk.Button(Mission2, text="1,2,3 중 하나의 값을 입력하시오.", command=output)
        button1_ifelse.pack()
        
        

    btnMission2 = tk.Button(Mission2, overrelief="solid", width=70, height=3, command=ifelse, repeatdelay=1000, repeatinterval=100, text='결과보기')
    btnMission2.pack()
    
btn2 = tk.Button(window, overrelief="solid", width=70, height=3, command=Mission2, repeatdelay=1000, repeatinterval=100, text='미션2')
btn2.pack()

#%% Pandas를 이용하여 excel 파일 입력 받아서 데이터프레임으로 저장
df={}
def Mission3():
    Mission3=tk.Tk()
    Mission3.title("Mission3")
    Mission3.geometry("640x400+100+100")
    Mission3.resizable(False, False)    
    label1_Mission3 = tk.Label(Mission3, text="Pandas를 활용하여 Data.xlsx 파일의 데이터를 Dataframe으로 저장 후 출력")
    label1_Mission3.pack()
    label2_Mission3 = tk.Label(Mission3, text="1. Tkinter를 활용해서 GUI를 통한 파일 입력받기은 후 파일명 출력")
    label2_Mission3.pack()
    label3_Mission3 = tk.Label(Mission3, text="2. 입력받은 파일을 Pandas를 활용하여 Dataframe 형태로 저장 후 출력")
    label3_Mission3.pack()
    def pandasandexcel():
        global d
        
        # Mission3_1
        def file_input():
            global e
            
            # Mission3_2

            
        btnMission3_1 = tk.Button(Mission3, overrelief="solid", width=70, height=3, command=file_input, repeatdelay=1000, repeatinterval=100, text='파일입력')
        btnMission3_1.pack()
        
        
    btnMission3 = tk.Button(Mission3, overrelief="solid", width=70, height=3, command=pandasandexcel, repeatdelay=1000, repeatinterval=100, text='결과보기')
    btnMission3.pack()
    
btn3 = tk.Button(window, overrelief="solid", width=70, height=3, command=Mission3, repeatdelay=1000, repeatinterval=100, text='미션3')
btn3.pack()

#%% Mission3에서 저장한 데이터를 가지고  Matplotlib을 활용하여 그래프 생성
def Mission4():
    Mission4=tk.Tk()
    Mission4.title("Mission4")
    Mission4.geometry("640x400+100+100")
    Mission4.resizable(False, False)    
    label1_Mission4 = tk.Label(Mission4, text="Mission3에서 저장한 데이터를 가지고  Matplotlib을 활용하여 막대그래프 생성")
    label1_Mission4.pack()
    label2_Mission4 = tk.Label(Mission4, text="1. Matplotlib에서 한글폰트 추가하는 방법 찾기")
    label2_Mission4.pack()
    label3_Mission4 = tk.Label(Mission4, text="2. Dataframe으로 그래프 그리는 방법 찾기")
    label3_Mission4.pack()

    def graph():
        global f       
        # Mission4_1


        # Mission4_2
        
    
    btnMission4 = tk.Button(Mission4, overrelief="solid", width=70, height=3, command=graph, repeatdelay=1000, repeatinterval=100, text='결과보기')
    btnMission4.pack()
    
btn4 = tk.Button(window, overrelief="solid", width=70, height=3, command=Mission4, repeatdelay=1000, repeatinterval=100, text='미션4')
btn4.pack()


#%% Final Mission

def Final_Mission():
    Final_Mission=tk.Tk()
    Final_Mission.title("Final Mission")
    Final_Mission.geometry("640x400+100+100")
    Final_Mission.resizable(False, False)
    label_Final_Mission = tk.Label(Final_Mission, text="데이터 분석을 통해서 아래 문제들을 해결하여 얻은 하나의 문자열을 결과로 표시하시오.")
    label_Final_Mission.pack()
    label1_Final_Mission = tk.Label(Final_Mission, text="1-1. Pandas를 활용하여 Data_Final.xlsx의 'Sheet1' 데이터를 읽어오기")
    label1_Final_Mission.pack()
    label1_1_Final_Mission = tk.Label(Final_Mission, text="1-2. 'Sheet1'의 데이터 중 최소값을 찾고 3자리 2진수로 바꿔서 문자열 변수 Str1에 저장")
    label1_1_Final_Mission.pack()
    label2_Final_Mission = tk.Label(Final_Mission, text="2-1. Pandas를 활용하여 Data_Final.xlsx의 'Sheet2' 데이터를 읽어오기")
    label2_Final_Mission.pack()
    label2_2_Final_Mission = tk.Label(Final_Mission, text="2-2. 'Sheet2' 데이터 중 최빈값을 찾고 문자열 변수 Str2에 저장")
    label2_2_Final_Mission.pack()
    label3_Final_Mission = tk.Label(Final_Mission, text="3-1. Pandas를 활용하여 Data_Final.xlsx의 'Sheet3' 데이터를 읽어오기")
    label3_Final_Mission.pack()
    label3_3_Final_Mission = tk.Label(Final_Mission, text="3-2. 'Sheet3' 데이터 중 5이상은 0으로로 5미만는 1로 바꾼 후 3차원 그래프로 그려보고 보이는 내용을 문자열 변수 Str3에 GUI로 입력 받기")
    label3_3_Final_Mission.pack()
    label4_Final_Mission = tk.Label(Final_Mission, text="4. 문자열 변수 Str1, Str2, Str3를 하나의 문자열 변수 Str4에 저장하여 Str4를 화면에 표시")
    label4_Final_Mission.pack()

    def Final():
        global g
        # 1_1
        
        # 1_2

        # 2_1
        
        # 2_2
        
        # 3_1
        
        # 3_2 아래 HINT 참고
        
        ##https://python-graph-gallery.com/371-surface-plot/
        ## Transform it to a long format
        #df_plot=df['DataName'].unstack().reset_index()
        #df_plot.columns=["X","Y","Z"]
        
        ## Make the plot
        #fig = plt.figure()
        #ax = fig.gca(projection='3d')
        #ax.plot_trisurf(df_plot['Y'], df_plot['X'], df_plot['Z'], cmap=plt.cm.viridis, linewidth=0.2)
        #plt.show()
        
        # 4
    
    btn_Final_Mission = tk.Button(Final_Mission, overrelief="solid", width=70, height=3, command=Final, repeatdelay=1000, repeatinterval=100, text='결과보기')
    btn_Final_Mission.pack()
    
btn_Final = tk.Button(window, overrelief="solid", width=70, height=3, command=Final_Mission, repeatdelay=1000, repeatinterval=100, text='Final Mission')
btn_Final.pack()

window.mainloop()

