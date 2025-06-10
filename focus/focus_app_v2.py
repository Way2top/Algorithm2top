import sys
import time
import random
import threading
import pygame
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QWidget, QFrame, QDialog, 
                            QSpinBox, QFormLayout, QMessageBox, QStyle, 
                            QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, QTimer, QRectF, QSize
from PyQt5.QtGui import QFont, QColor, QPainter, QPen, QIcon

# 默认配置
DEFAULT_TOTAL_TIME = 90 * 60
DEFAULT_MIN_INTERVAL = 2 * 60
DEFAULT_MAX_INTERVAL = 5 * 60

# 音频文件路径
FOCUS_SOUND_FILE = "专注声音.mp3"
REST_SOUND_FILE = "休息声音.wav"


class CircularProgressBar(QFrame):
    """圆形进度条 (美化版)"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 100
        self.setFixedSize(220, 220)
        self.parent = parent
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 5)
        self.setGraphicsEffect(shadow)
        
    def setValue(self, value):
        self.value = max(0, min(100, value))
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        rect = QRectF(self.rect().adjusted(15, 15, -15, -15))
        
        pen_bg = QPen(QColor(230, 230, 230), 12, cap=Qt.RoundCap)
        painter.setPen(pen_bg)
        painter.drawEllipse(rect)
        
        pen_progress = QPen(QColor("#00a896"), 12, cap=Qt.RoundCap)
        painter.setPen(pen_progress)
        
        angle = 360 * (self.value / 100)
        start_angle = 90 * 16
        span_angle = int(-angle * 16)
        painter.drawArc(rect, start_angle, span_angle)
        
        painter.setPen(QPen(QColor("#333333")))
        font = QFont("Segoe UI", 28, QFont.Bold)
        painter.setFont(font)
        
        if self.parent and hasattr(self.parent, 'total_time'):
            total_minutes = self.parent.total_time // 60
            minutes = int((self.value / 100) * total_minutes)
        else:
            total_minutes = DEFAULT_TOTAL_TIME // 60
            minutes = int((self.value / 100) * total_minutes)
            
        time_text = f"{minutes:02d}"
        painter.drawText(rect, Qt.AlignCenter, time_text)

        min_font = QFont("Segoe UI", 10)
        painter.setFont(min_font)
        min_rect = rect.translated(0, 45)
        painter.drawText(min_rect, Qt.AlignCenter, "MIN")


class SettingsDialog(QDialog):
    """设置对话框 (美化版 + 修复光标问题)"""
    def __init__(self, parent=None, total_time=DEFAULT_TOTAL_TIME, 
                 min_interval=DEFAULT_MIN_INTERVAL, max_interval=DEFAULT_MAX_INTERVAL):
        super().__init__(parent)
        self.setWindowTitle("设置")
        self.setModal(True)
        self.setMinimumWidth(320)

        # <<< 全新的样式表，与主窗口风格统一
        self.setStyleSheet("""
            QDialog {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
                color: #333333;
            }
            QPushButton {
                background-color: #00a896;
                color: white;
                border: none;
                border-radius: 18px; /* 稍小的圆角以适应对话框 */
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                font-family: 'Segoe UI';
            }
            QPushButton:hover {
                background-color: #009182;
            }
            QPushButton:pressed {
                background-color: #007a6e;
            }
            QSpinBox {
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                background-color: white;
                font-size: 14px;
            }
            QSpinBox:focus {
                border: 1px solid #00a896; /* 聚焦时显示主题色边框 */
            }
            /* 样式化SpinBox的上下箭头 */
            QSpinBox::up-button, QSpinBox::down-button {
                subcontrol-origin: border;
                width: 16px;
                border-left: 1px solid #cccccc;
            }
            QSpinBox::up-arrow {
                image: url(./up_arrow.png); /* 需要在同目录下准备一个up_arrow.png图片 */
                width: 10px; height: 10px;
            }
            QSpinBox::down-arrow {
                image: url(./down_arrow.png); /* 需要在同目录下准备一个down_arrow.png图片 */
                width: 10px; height: 10px;
            }
        """)

        # 使用QFormLayout来对齐标签和输入控件
        form_layout = QFormLayout(self)
        form_layout.setSpacing(15)
        form_layout.setContentsMargins(20, 20, 20, 20)

        # --- 总时长 ---
        self.total_time_spinbox = QSpinBox()
        self.total_time_spinbox.setRange(1, 120)
        self.total_time_spinbox.setValue(total_time // 60)
        # <<< 修复：使用HBox将SpinBox和Label组合
        total_time_layout = self.create_spinbox_with_label(self.total_time_spinbox, "分钟")
        form_layout.addRow("总时长:", total_time_layout)

        # --- 最小提示间隔 ---
        self.min_interval_spinbox = QSpinBox()
        self.min_interval_spinbox.setRange(1, 60)
        self.min_interval_spinbox.setValue(min_interval // 60)
        min_interval_layout = self.create_spinbox_with_label(self.min_interval_spinbox, "分钟")
        form_layout.addRow("最小提示间隔:", min_interval_layout)

        # --- 最大提示间隔 ---
        self.max_interval_spinbox = QSpinBox()
        self.max_interval_spinbox.setRange(1, 60)
        self.max_interval_spinbox.setValue(max_interval // 60)
        max_interval_layout = self.create_spinbox_with_label(self.max_interval_spinbox, "分钟")
        form_layout.addRow("最大提示间隔:", max_interval_layout)

        # --- 按钮布局 ---
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        button_layout.addStretch() # 将按钮推向右侧
        ok_button = QPushButton("确定")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("取消")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        form_layout.addRow("", button_layout) # 添加按钮行

        # 连接验证逻辑
        self.min_interval_spinbox.valueChanged.connect(self.validate_intervals)
        self.max_interval_spinbox.valueChanged.connect(self.validate_intervals)
        self.validate_intervals()

    def create_spinbox_with_label(self, spinbox, label_text):
        """一个辅助函数，用于创建带标签的SpinBox布局"""
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        spinbox.setButtonSymbols(QSpinBox.NoButtons) # <<< 隐藏默认按钮，美化
        spinbox.setFixedWidth(80) # 固定宽度，更好看
        layout.addWidget(spinbox)
        layout.addWidget(QLabel(label_text))
        layout.addStretch() # 确保标签紧跟在spinbox后面
        return layout

    def accept(self):
        min_val = self.min_interval_spinbox.value()
        max_val = self.max_interval_spinbox.value()
        if min_val == max_val:
            QMessageBox.warning(self, "无效设置", "最小和最大提示间隔不能相同，请设置一个范围。")
            return
        super().accept()

    def validate_intervals(self):
        min_val = self.min_interval_spinbox.value()
        max_val = self.max_interval_spinbox.value()
        self.max_interval_spinbox.setMinimum(min_val)
        self.min_interval_spinbox.setMaximum(max_val)
        
    def get_settings(self):
        return (self.total_time_spinbox.value() * 60,
                self.min_interval_spinbox.value() * 60,
                self.max_interval_spinbox.value() * 60)

class TimerApp(QMainWindow):
    """计时器应用主窗口 (美化版)"""
    def __init__(self):
        super().__init__()
        self.total_time = DEFAULT_TOTAL_TIME
        self.min_interval = DEFAULT_MIN_INTERVAL
        self.max_interval = DEFAULT_MAX_INTERVAL
        
        self.initUI()
        
        try:
            pygame.mixer.init()
        except pygame.error as e:
            QMessageBox.critical(self, "音频初始化失败", f"Pygame音频模块初始化失败: {e}\n程序将无法播放声音。")

        self.start_time = None
        self.elapsed_pause = 0
        self.running = False
        self.paused = False
        self.thread = None
        self.remaining_time = self.total_time
        
        self.ui_timer = QTimer(self)
        self.ui_timer.timeout.connect(self.update_ui)
        self.ui_timer.start(500)
        
    def initUI(self):
        self.setWindowTitle("专注计时器")
        self.setGeometry(100, 100, 400, 550)
        self.setMinimumSize(380, 500)
        
        self.setStyleSheet("""
            QMainWindow { background-color: #f0f0f0; }
            QLabel { color: #333333; }
            QPushButton {
                background-color: #00a896; color: white; border: none;
                border-radius: 20px; padding: 12px 24px;
                font-size: 15px; font-weight: bold; font-family: 'Segoe UI';
            }
            QPushButton:hover { background-color: #009182; }
            QPushButton:pressed { background-color: #007a6e; }
            QPushButton:disabled { background-color: #c0c0c0; color: #666666; }
        """)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 15, 20, 15)
        main_layout.setSpacing(15)

        header_layout = QHBoxLayout()
        header_layout.addStretch()
        self.settings_button = QPushButton()
        
        # <<< FIX: 使用一个保证存在的标准图标
        icon = self.style().standardIcon(QStyle.SP_FileDialogDetailedView)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QSize(24, 24))
        
        self.settings_button.setFixedSize(40, 40)
        self.settings_button.setStyleSheet("""
            QPushButton {
                background-color: transparent; border-radius: 20px;
            }
            QPushButton:hover { background-color: #dcdcdc; }
        """)
        self.settings_button.clicked.connect(self.open_settings)
        header_layout.addWidget(self.settings_button)
        main_layout.addLayout(header_layout)

        title_label = QLabel("专注计时器")
        title_font = QFont("Segoe UI Black", 26)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50;")
        main_layout.addWidget(title_label)

        main_layout.addStretch(1)
        
        self.progress_bar = CircularProgressBar(self)
        main_layout.addWidget(self.progress_bar, alignment=Qt.AlignCenter)
        
        self.time_label = QLabel()
        time_font = QFont("Segoe UI", 20, QFont.Light)
        self.time_label.setFont(time_font)
        self.time_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.time_label)

        main_layout.addStretch(2)
        
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        
        self.start_button = QPushButton("开始")
        self.pause_button = QPushButton("暂停")
        self.reset_button = QPushButton("重置")
        self.pause_button.setEnabled(False)
        
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.reset_button)
        
        self.start_button.clicked.connect(self.start_timer)
        self.pause_button.clicked.connect(self.pause_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        
        main_layout.addLayout(button_layout)
        
        self.info_label = QLabel()
        self.info_label.setFont(QFont("Segoe UI", 10))
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("color: #888888;")
        main_layout.addWidget(self.info_label)

        main_layout.addStretch(1)
        
        footer_label = QLabel("© 2025 专注计时器\n技术支持：3066689820@qq.com")
        footer_label.setFont(QFont("Arial", 9))
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet("color: #b0b0b0;")
        main_layout.addWidget(footer_label)
        
        self._update_display()

    def _update_display(self):
        self.remaining_time = self.total_time
        minutes = int(self.remaining_time // 60)
        seconds = int(self.remaining_time % 60)
        self.time_label.setText(f"剩余时间: {minutes:02d}:{seconds:02d}")
        
        self.progress_bar.setValue(100)
        
        min_minutes = self.min_interval // 60
        max_minutes = self.max_interval // 60
        self.info_label.setText(f"每 {min_minutes} - {max_minutes} 分钟提醒一次")
    
    def open_settings(self):
        if self.running and not self.paused:
            QMessageBox.warning(self, "警告", "请先暂停计时器再进行设置。")
            return
        
        dialog = SettingsDialog(
            self, 
            self.total_time,
            self.min_interval,
            self.max_interval
        )
        
        if dialog.exec_():
            self.total_time, self.min_interval, self.max_interval = dialog.get_settings()
            self._update_display()
            if self.running and self.paused:
                self.reset_timer()
    
    def play_sound(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        except Exception as e:
            QTimer.singleShot(0, lambda: QMessageBox.warning(self, "播放错误", f"无法播放声音文件 {file_path}。\n错误: {e}"))
            print(f"播放声音出错：{e}")
    
    def play_focus_sound(self):
        threading.Thread(target=self.play_sound, args=(FOCUS_SOUND_FILE,)).start()
    
    def play_rest_sound(self):
        threading.Thread(target=self.play_sound, args=(REST_SOUND_FILE,)).start()
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.start_time = time.time()
            self.elapsed_pause = 0
            self.thread = threading.Thread(target=self.run_timer)
            self.thread.daemon = True
            self.thread.start()
            
            self.start_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.pause_button.setText("暂停")
    
    def pause_timer(self):
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
        self.running = False
        self.paused = False
        self.start_time = None
        self.elapsed_pause = 0
        
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.pause_button.setText("暂停")
        
        self._update_display()
    
    def run_timer(self):
        if self.min_interval >= self.max_interval:
            self.max_interval = self.min_interval + 60
        
        next_interval = random.randint(self.min_interval, self.max_interval)
        last_play_time = time.time()
        
        while self.running:
            if self.paused:
                time.sleep(0.1)
                continue
            
            elapsed = time.time() - self.start_time - self.elapsed_pause
            current_remaining = self.total_time - elapsed
            
            if current_remaining <= 0:
                self.remaining_time = 0
                break
            
            self.remaining_time = current_remaining
            
            if time.time() - last_play_time >= next_interval:
                self.play_focus_sound()
                last_play_time = time.time()
                next_interval = random.randint(self.min_interval, self.max_interval)
            
            time.sleep(0.05)
        
        if self.running:
            self.play_rest_sound()
            QTimer.singleShot(0, self.reset_timer)
    
    def update_ui(self):
        if self.running and not self.paused:
            remaining = self.remaining_time
            if remaining < 0:
                remaining = 0
                
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            self.time_label.setText(f"剩余时间: {minutes:02d}:{seconds:02d}")
            
            progress = (remaining / self.total_time) * 100
            self.progress_bar.setValue(progress)
        elif not self.running:
            minutes = int(self.total_time // 60)
            if self.time_label.text() != f"剩余时间: {minutes:02d}:00":
                 self._update_display()


def main():
    app = QApplication(sys.argv)
    
    try:
        font = QFont("Segoe UI")
        app.setFont(font)
    except Exception as e:
        print(f"设置默认字体失败: {e}")

    window = TimerApp()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()