import tkinter as tk
import tkinter.font as tkfont
import time
# 定义画布是否有效
flag = False
# 确定画布大小
width = 400
height = 600
# 设置元素格子大小
cell_size = 50
# 定义动画展示时间
show_time = 0.2

# 创建容器与画布
def create_canvas(title):
    # 创建容器对象
    root = tk.Tk()
    # 确定标题
    root.title(title)
    # 创建画布
    canvas = tk.Canvas(root, width=width, height=height)
    # 添加画布对象至主容器并居中
    canvas.pack(side='top', fill='both', expand=True)
     
    return root,canvas

# 打印状态
def print_images(state,state_message,canvas,position_y):
    # 设置字体
    font = tkfont.Font(family="Arial", size=18)
    # 行列数
    rows = cols = int(len(state)**0.5)
    # 绘制状态信息
    title_text = canvas.create_text(width/2,position_y+height/16,text=state_message, fill='black', font=font)
    # 绘制数码状态
    for row in range(rows):
            for col in range(cols):
                # 获得某一行某一列的值
                value = state[row * rows + col]
                x_start = width/2-rows*cell_size/2 + col*cell_size
                y_start = position_y+height/8 + row*cell_size
                # 绘制矩形
                canvas.create_rectangle(x_start, y_start, x_start + cell_size, y_start + cell_size, outline='blue')
                # 填充矩形颜色
                if value != 0:
                    canvas.create_rectangle(x_start, y_start, x_start + cell_size, y_start + cell_size, fill='skyblue')
                if value == 0:
                    canvas.create_rectangle(x_start, y_start, x_start + cell_size, y_start + cell_size, fill='white')
                # 填值进表格
                canvas.create_text(x_start + cell_size // 2, y_start + cell_size // 2, text=str(value), fill='white', font=font)
    return title_text

def draw_images(state,state_message,canvas,position_y,root):
    if flag == False :
        return
    title_text = print_images(state,state_message,canvas,position_y)
    root.update()
    time.sleep(show_time)
    if state_message != "目标状态":
        canvas.delete(title_text)
