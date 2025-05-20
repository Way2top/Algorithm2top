import time
import random
import threading
import tkinter as tk
import pygame

# 总运行时间（秒）
TOTAL_TIME = 90 * 60

# 每次提示间隔的最小最大秒数
MIN_INTERVAL = 2 * 60
MAX_INTERVAL = 5 * 60

# 音频文件路径（和程序放同一目录）
FOCUS_SOUND_FILE = "专注声音.mp3"  # 2-5分钟时播放（支持mp3或wav）
REST_SOUND_FILE = "休息声音.wav"  # 90分钟结束时播放（支持mp3或wav）


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("提示音计时器")
        self.root.geometry("300x250")

        # 初始化pygame音频
        pygame.mixer.init()

        # 显示剩余时间的标签
        self.label = tk.Label(root, text="剩余时间：90:00", font=("Arial", 16))
        self.label.pack(pady=20)

        # 开始按钮
        self.start_button = tk.Button(root, text="开始", font=("Arial", 12), command=self.start_timer)
        self.start_button.pack(pady=5)

        # 暂停按钮
        self.pause_button = tk.Button(root, text="暂停", font=("Arial", 12), command=self.pause_timer, state="disabled")
        self.pause_button.pack(pady=5)

        # 结束（重置）按钮
        self.stop_button = tk.Button(root, text="结束(重置)", font=("Arial", 12), command=self.reset_timer)
        self.stop_button.pack(pady=5)

        # 初始化状态
        self.start_time = None  # 开始时间
        self.elapsed_pause = 0  # 暂停期间的累计时间
        self.running = False  # 当前是否在运行
        self.paused = False  # 当前是否暂停
        self.thread = None  # 后台线程
        self.remaining_time = TOTAL_TIME  # 剩余时间

        # 启动界面刷新
        self.update_label()

    def play_sound(self, file_path):
        """
        播放提示声音（mp3或wav）
        """
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"播放声音出错：{e}")

    def play_focus_sound(self):
        """
        播放专注提示音
        """
        threading.Thread(target=self.play_sound, args=(FOCUS_SOUND_FILE,)).start()

    def play_rest_sound(self):
        """
        播放休息提示音
        """
        threading.Thread(target=self.play_sound, args=(REST_SOUND_FILE,)).start()

    def start_timer(self):
        """
        开始计时器
        """
        if not self.running:
            self.running = True
            self.paused = False
            self.start_time = time.time()
            self.elapsed_pause = 0
            self.thread = threading.Thread(target=self.run_timer)
            self.thread.start()

            # 更新按钮状态
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")

    def pause_timer(self):
        """
        暂停/继续计时器
        """
        if self.running:
            if not self.paused:
                self.paused = True
                self.pause_start_time = time.time()
                self.pause_button.config(text="继续")
            else:
                self.paused = False
                self.elapsed_pause += time.time() - self.pause_start_time
                self.pause_button.config(text="暂停")

    def reset_timer(self):
        """
        重置计时器
        """
        self.running = False
        self.paused = False
        self.remaining_time = TOTAL_TIME
        self.start_time = None
        self.elapsed_pause = 0

        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled", text="暂停")
        self.label.config(text="剩余时间：90:00")

    def run_timer(self):
        """
        后台线程处理计时逻辑
        """
        next_interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)  # 第一个专注提示的间隔
        last_play_time = time.time()

        while self.running:
            if self.paused:
                time.sleep(0.1)
                continue

            elapsed = time.time() - self.start_time - self.elapsed_pause
            self.remaining_time = TOTAL_TIME - elapsed

            if self.remaining_time <= 0:
                break

            # 到了播放专注提示音的时候
            if time.time() - last_play_time >= next_interval:
                self.play_focus_sound()
                last_play_time = time.time()
                next_interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)

            time.sleep(0.1)

        # 如果是正常结束，播放休息提示音
        if self.running:
            self.play_rest_sound()

        self.running = False
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled", text="暂停")
        self.remaining_time = TOTAL_TIME

    def update_label(self):
        """
        更新剩余时间显示
        """
        if self.start_time and self.running:
            if not self.paused:
                elapsed = time.time() - self.start_time - self.elapsed_pause
            else:
                elapsed = self.pause_start_time - self.start_time - self.elapsed_pause
            remaining = TOTAL_TIME - elapsed
            if remaining < 0:
                remaining = 0
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            self.label.config(text=f"剩余时间：{minutes:02d}:{seconds:02d}")
        else:
            minutes = int(self.remaining_time // 60)
            seconds = int(self.remaining_time % 60)
            self.label.config(text=f"剩余时间：{minutes:02d}:{seconds:02d}")

        self.root.after(1000, self.update_label)


def main():
    root = tk.Tk()
    app = TimerApp(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        app.reset_timer()


if __name__ == "__main__":
    main()
