import time
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

# 深度优先搜索
def dfs(initial_state, goal_state, max_steps):
    start_time = time.time()
    start_memory = psutil.Process().memory_info().rss / 1024

    # 创建集合,记录已经搜索过的状态
    visited = set()
    stack = [(initial_state, [])]
    nodes_searched = 0

    # 创建画布
    root,canvas = paint.create_canvas("深度搜索优先")
    # 打印最终状态
    paint.draw_images(goal_state,"目标状态",canvas,0,root)

    while stack and nodes_searched <= max_steps:
        current_state, path = stack.pop()
        # 搜索节点数加1
        nodes_searched += 1

        if current_state == goal_state:
            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss / 1024
            print(f"深度优先搜索：")
            print(f"搜索节点数：{nodes_searched}")
            print(f"搜索时间：{end_time - start_time} 秒")
            print(f"内存占用：{end_memory - start_memory} KB")
            paint.draw_images(goal_state,"搜索成功",canvas,paint.height/2,root)
            root.destroy()
            return path
        
        if tuple(current_state) not in visited:
            # 添加此次搜索的状态
            visited.add(tuple(current_state))
            size = int(len(current_state) ** 0.5)
            blank_index = current_state.index(0)
            # 确定状态信息
            state_message = "不存在,继续向下一层搜索"
            
            # 若0的位置不在最左侧,则可以向左移动一格
            if blank_index % size > 0:
                stack.append((move(current_state, blank_index - 1), path + [current_state]))                
            # 若0的位置不在最右侧,则可以向右移动一格
            if blank_index % size < size - 1:
                stack.append((move(current_state, blank_index + 1), path + [current_state]))
            # 若0的位置不在最顶侧,则可以向上移动一格
            if blank_index >= size:
                stack.append((move(current_state, blank_index - size), path + [current_state]))
            # 若0的位置不在最底侧,则可以向下移动一格
            if blank_index < len(current_state) - size:
                stack.append((move(current_state, blank_index + size), path + [current_state]))
            
        else:
            if blank_index % size > 0:
                state_message = "已存在非最左子树,向左邻结点搜索"
            else:
                state_message = "已存在是最左子树,向上回溯一层"

        paint.draw_images(current_state,state_message,canvas,paint.height/2,root)
    
    # 结束时间,内存计数变量
    end_time = time.time()
    end_memory = psutil.Process().memory_info().rss / 1024
    print(f"深度优先搜索：")
    print("本次搜索已达最大步数,搜索失败")
    print(f"搜索节点数：{nodes_searched}")
    print(f"搜索时间：{end_time - start_time} 秒")
    print(f"内存占用：{end_memory - start_memory} KB")
    root.destroy()
    root.mainloop()
    return path