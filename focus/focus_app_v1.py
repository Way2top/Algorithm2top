import sys
import time
import random
import threading
import pygame
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QWidget, QFrame)
from PyQt5.QtCore import Qt, QTimer, QPoint, QRectF
from PyQt5.QtGui import QFont, QIcon, QColor, QPalette, QPainter, QPen, QBrush, QPixmap

# 总运行时间（秒）
TOTAL_TIME = 90 * 60

# 每次提示间隔的最小最大秒数
MIN_INTERVAL = 2 * 60
MAX_INTERVAL = 5 * 60

# 音频文件路径（和程序放同一目录）
FOCUS_SOUND_FILE = "专注声音.mp3"  # 2-5分钟时播放（支持mp3或wav）
REST_SOUND_FILE = "休息声音.wav"  # 90分钟结束时播放（支持mp3或wav）


class CircularProgressBar(QFrame):
    """圆形进度条"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 100
        self.setFixedSize(200, 200)
        
    def setValue(self, value):
        """设置进度值"""
        self.value = max(0, min(100, value))
        self.update()
        
    def paintEvent(self, event):
        """绘制进度条"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制背景圆环
        rect = QRectF(self.rect().adjusted(10, 10, -10, -10))
        pen = QPen(QColor(240, 240, 240), 10)
        painter.setPen(pen)
        painter.drawEllipse(rect)
        
        # 绘制进度圆环
        pen = QPen(QColor(76, 175, 80), 10)  # 绿色进度条
        painter.setPen(pen)
        angle = 360 * (self.value / 100)
        # 确保角度是整数
        start_angle = 90 * 16
        span_angle = int(-angle * 16)
        painter.drawArc(rect, start_angle, span_angle)
        
        # 绘制中心文本 - 分钟数和MIN
        painter.setPen(QPen(QColor(50, 50, 50)))
        
        # 设置较大的字体用于分钟数
        font = painter.font()
        font.setPointSize(24)
        painter.setFont(font)
        
        minutes = int((self.value / 100) * (TOTAL_TIME // 60))
        time_text = f"{minutes:02d} MIN"  # 将分钟数和MIN组合在一起
        
        # 绘制组合文本
        painter.drawText(rect, Qt.AlignCenter, time_text)


class TimerApp(QMainWindow):
    """计时器应用主窗口"""
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # 初始化pygame音频
        pygame.mixer.init()
        
        # 初始化状态
        self.start_time = None  # 开始时间
        self.elapsed_pause = 0  # 暂停期间的累计时间
        self.running = False  # 当前是否在运行
        self.paused = False  # 当前是否暂停
        self.thread = None  # 后台线程
        self.remaining_time = TOTAL_TIME  # 剩余时间
        
        # 界面更新计时器
        self.ui_timer = QTimer(self)
        self.ui_timer.timeout.connect(self.update_ui)
        self.ui_timer.start(1000)  # 每秒更新一次
        
    def initUI(self):
        """初始化UI界面"""
        # 设置窗口标题和大小
        self.setWindowTitle("专注计时器")
        self.setGeometry(100, 100, 400, 500)
        self.setMinimumSize(400, 500)
        
        # 设置窗口样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f7fa;
            }
            QLabel {
                color: #333333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 15px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # 创建标题标签
        title_label = QLabel("专注计时器")
        title_font = QFont("Arial", 24, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50;")
        main_layout.addWidget(title_label)
        
        # 创建圆形进度条
        self.progress_bar = CircularProgressBar()
        main_layout.addWidget(self.progress_bar, alignment=Qt.AlignCenter)
        
        # 创建时间显示标签
        self.time_label = QLabel("剩余时间：90:00")
        time_font = QFont("Arial", 18)
        self.time_label.setFont(time_font)
        self.time_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.time_label)
        
        # 创建按钮布局
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        
        # 创建开始按钮
        self.start_button = QPushButton("开始")
        self.start_button.setFont(QFont("Arial", 12))
        self.start_button.clicked.connect(self.start_timer)
        button_layout.addWidget(self.start_button)
        
        # 创建暂停按钮
        self.pause_button = QPushButton("暂停")
        self.pause_button.setFont(QFont("Arial", 12))
        self.pause_button.clicked.connect(self.pause_timer)
        self.pause_button.setEnabled(False)
        button_layout.addWidget(self.pause_button)
        
        # 创建重置按钮
        self.reset_button = QPushButton("重置")
        self.reset_button.setFont(QFont("Arial", 12))
        self.reset_button.clicked.connect(self.reset_timer)
        button_layout.addWidget(self.reset_button)
        
        main_layout.addLayout(button_layout)
        
        # 创建信息标签
        self.info_label = QLabel("专注模式：每2-5分钟提醒一次")
        self.info_label.setFont(QFont("Arial", 10))
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("color: #7f8c8d;")
        main_layout.addWidget(self.info_label)
        
        # 添加底部版权信息
        footer_label = QLabel("© 2025 专注计时器")
        footer_label.setFont(QFont("Arial", 9))
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet("color: #95a5a6;")
        main_layout.addWidget(footer_label)
    
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
            self.thread.daemon = True
            self.thread.start()
            
            # 更新按钮状态
            self.start_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.pause_button.setText("暂停")
    
    def pause_timer(self):
        """
        暂停/继续计时器
        """
        if self.running:
            if not self.paused:
                self.paused = True
                self.pause_start_time = time.time()
                self.pause_button.setText("继续")
            else:
                self.paused = False
                self.elapsed_pause += time.time() - self.pause_start_time
                self.pause_button.setText("暂停")
    
    def reset_timer(self):
        """
        重置计时器
        """
        self.running = False
        self.paused = False
        self.remaining_time = TOTAL_TIME
        self.start_time = None
        self.elapsed_pause = 0
        
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.pause_button.setText("暂停")
        
        self.update_ui()
    
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
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.pause_button.setText("暂停")
        self.remaining_time = TOTAL_TIME
    
    def update_ui(self):
        """
        更新UI界面
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
            self.time_label.setText(f"剩余时间：{minutes:02d}:{seconds:02d}")
            
            # 更新进度条
            progress = (remaining / TOTAL_TIME) * 100
            self.progress_bar.setValue(progress)
        else:
            minutes = int(self.remaining_time // 60)
            seconds = int(self.remaining_time % 60)
            self.time_label.setText(f"剩余时间：{minutes:02d}:{seconds:02d}")
            
            # 更新进度条
            self.progress_bar.setValue(100)


def main():
    """主函数"""
    app = QApplication(sys.argv)
    
    # 确保中文显示正常
    font = QFont("SimHei")
    app.setFont(font)
    
    window = TimerApp()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()    