import time
from collections import deque
import psutil
import paint

# 移动状态函数
def move(state, move_index):
    # 确定当前状态0的位置
    blank_index = state.index(0)
    # 复制当前的状态
    new_state = state.copy()
    # 交换0与移动位置的目标
    new_state[blank_index], new_state[move_index] = new_state[move_index], new_state[blank_index]
    return new_state

# 宽度优先搜索
def bfs(initial_state, goal_state, max_steps):
    start_time = time.time()
    start_memory = psutil.Process().memory_info().rss / 1024
    
    # 创建画布
    root,canvas = paint.create_canvas("宽度搜索优先")
    # 打印最终状态
    paint.draw_images(goal_state,"目标状态",canvas,0,root)

    # 创建集合,记录已经搜索过的状态
    visited = set()
    queue = deque([(initial_state, [])])
    nodes_searched = 0

    while queue and nodes_searched <= max_steps:
        # 弹出队列第一个元素
        current_state, path = queue.popleft()
        nodes_searched += 1

        if current_state == goal_state:
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024
            print(f"宽度优先搜索：")
            print(f"搜索节点数：{nodes_searched}")
            print(f"搜索时间：{end_time - start_time} 秒")
            print(f"内存占用：{end_memory - start_memory} KB")
            paint.draw_images(goal_state,"搜索成功",canvas,paint.height/2,root)
            root.destroy()
            return path

        if tuple(current_state) not in visited:
            visited.add(tuple(current_state))
            size = int(len(current_state) ** 0.5)
            blank_index = current_state.index(0)

            # 若0的位置不在最左侧,则可以向左移动一格
            if blank_index % size > 0:
                queue.append((move(current_state, blank_index - 1), path + [current_state]))
            # 若0的位置不在最右侧,则可以向右移动一格
            if blank_index % size < size - 1:
                queue.append((move(current_state, blank_index + 1), path + [current_state]))
            # 若0的位置不在最顶侧,则可以向上移动一格
            if blank_index >= size:
                queue.append((move(current_state, blank_index - size), path + [current_state]))
            # 若0的位置不在最顶侧,则可以向下移动一格
            if blank_index < len(current_state) - size:
                queue.append((move(current_state, blank_index + size), path + [current_state]))

        # 确定状态信息
        if blank_index < len(current_state) - size:
            state_message = "向右邻结点搜索"
        else:
            state_message = "向下一层搜索"

        paint.draw_images(current_state,state_message,canvas,paint.height/2,root)
    
    # 结束时间,内存计数变量
    end_time = time.time()
    end_memory = psutil.Process().memory_info().rss / 1024
    print(f"宽度优先搜索：")
    print("本次搜索已达最大步数,搜索失败")
    print(f"搜索节点数：{nodes_searched}")
    print(f"搜索时间：{end_time - start_time} 秒")
    print(f"内存占用：{end_memory - start_memory} KB")
    root.destroy()
    root.mainloop()
    return path
