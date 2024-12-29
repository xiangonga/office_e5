import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("时间到！休息一下吧！")

def pomodoro_timer(work_duration=25, break_duration=5):
    print("开始专注工作！")
    countdown(work_duration * 60)  # 转换为秒
    print("开始休息！")
    countdown(break_duration * 60)  # 转换为秒

if __name__ == "__main__":
    pomodoro_timer()
    import time

def focus_clock(work_time=25, rest_time=5):
    print("开始专注时钟")
    while True:
        # 工作时间段
        print("工作时间开始了！")
        time.sleep(work_time * 60)  # 转换为秒
        print("工作时间结束，请休息一下！")

        # 休息时间段
        time.sleep(rest_time * 60)
        print("休息时间结束了，准备进入下一个工作周期！")

if __name__ == "__main__":
    focus_clock()
