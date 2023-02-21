# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> lab1.py
@Author : yge
@Date : 2023/2/21 12:15
@Desc :

==============================================================
'''
import matplotlib.pyplot as plt
def person_heoght(name:str,height:int):
    x_short = [0, 170, 250]
    y_short = [1, 0, 0]

    x_average = [0, 170, 175, 250]
    y_average = [0, 1, 1, 0]

    x_tall = [0, 175, 250]
    y_tall = [0, 1, 1]

    y1,y2,y3 = 0,0,0
    if height>=0 and height<=170:
        x_short = [0, height,170, 250]
        y1 = (170-height)/170
        y_short = [1,y1 ,0, 0]

        x_average = [0, height,170, 175, 250]
        y2 = height/170
        y_average = [0, y2,1, 1, 0]

        x_tall = [0, height,175, 250]
        y3 = height/175
        y_tall = [0, y3,1, 1]
    elif height>170 and height<175:
        x_short = [0,170,height, 250]
        y1 = 0
        y_short = [1, 0,y1, 0]

        x_average = [0,  170, height,175, 250]
        y2 = 1
        y_average = [0,  1, y2,1, 0]

        x_tall = [0, height, 175, 250]
        y3 = height / 175
        y_tall = [0, y3, 1, 1]
    elif height>175 and height<=250:
        x_short = [0, 170,height,250]
        y1 = 0
        y_short = [1, 0, y1,0]

        x_average = [0, 170,175, height,250]
        y2 = (250-height)/75
        y_average = [0, 1, 1, y2,0]

        x_tall = [0, 175,  height,250]
        y3 = 1
        y_tall = [0, 1, y3,1]




    plt.title("Person Height")
    plt.plot(x_short,y_short,color='r', label='Short')
    plt.plot(x_average, y_average, color='g', label='Average')
    plt.plot(x_tall, y_tall, color='b', label='Tall')
    plt.xlabel("height(cm)")
    if height>=0 and height<=250:
         plt.annotate(name+"("+str(height)+","+str(y1)+")",xy=(height,y1),color='r')
         plt.annotate(name+"("+str(height)+","+str(y2)+")", xy=(height, y2),color='g')
         plt.annotate(name+"("+str(height)+","+str(y3)+")", xy=(height, y3),color='b')

         plt.scatter([height, ], [y1, ], 20, color='r')
         plt.scatter([height, ], [y2, ], 20, color='g')
         plt.scatter([height, ], [y3, ], 20, color='b')
    plt.legend()
    plt.show()



if __name__ == "__main__":
    person_heoght("Ruth Bader Ginsburg", 160)
    person_heoght("Rishi Sunak", 176)
    person_heoght("Ming Yao",226)





