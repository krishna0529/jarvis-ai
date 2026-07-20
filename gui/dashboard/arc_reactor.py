import math
# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import QWidget
# pyrefly: ignore [missing-import]
from PySide6.QtCore import QTimer, Qt, QRectF
# pyrefly: ignore [missing-import]
from PySide6.QtGui import QPainter, QColor, QPen, QRadialGradient, QFont

class ArcReactorWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(280, 280)
        self.angle = 0
        self.pulse = 0
        self.pulse_growing = True
        self.is_active = True
        
        # 60 FPS animation timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(16)

    def update_animation(self):
        self.angle = (self.angle + 2) % 360
        if self.pulse_growing:
            self.pulse += 0.02
            if self.pulse >= 1.0:
                self.pulse_growing = False
        else:
            self.pulse -= 0.02
            if self.pulse <= 0.2:
                self.pulse_growing = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()
        center_x = width / 2
        center_y = height / 2
        radius = min(width, height) / 2 - 20

        # Background Dark Glass
        painter.fillRect(self.rect(), QColor(10, 15, 25))

        # Core Radial Gradient (Iron Man Cyan Glow)
        glow_radius = radius * (0.8 + 0.2 * self.pulse)
        gradient = QRadialGradient(center_x, center_y, glow_radius)
        gradient.setColorAt(0.0, QColor(0, 240, 255, 220))
        gradient.setColorAt(0.4, QColor(0, 180, 255, 120))
        gradient.setColorAt(0.8, QColor(0, 80, 150, 40))
        gradient.setColorAt(1.0, QColor(10, 15, 25, 0))
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QRectF(center_x - glow_radius, center_y - glow_radius, glow_radius * 2, glow_radius * 2))

        # Outer Holographic Ring (Rotating)
        painter.save()
        painter.translate(center_x, center_y)
        painter.rotate(self.angle)

        pen = QPen(QColor(0, 240, 255, 200), 3, Qt.DashLine)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QRectF(-radius, -radius, radius * 2, radius * 2))

        # Arc Segments (10 segments)
        num_segments = 10
        for i in range(num_segments):
            seg_angle = (360 / num_segments) * i
            painter.save()
            painter.rotate(seg_angle)
            seg_pen = QPen(QColor(0, 255, 230, 240), 4)
            painter.setPen(seg_pen)
            painter.drawLine(int(radius * 0.65), 0, int(radius * 0.85), 0)
            painter.restore()

        painter.restore()

        # Inner Reverse Rotating Ring
        painter.save()
        painter.translate(center_x, center_y)
        painter.rotate(-self.angle * 1.5)

        inner_radius = radius * 0.55
        pen_inner = QPen(QColor(0, 190, 255, 180), 2, Qt.DotLine)
        painter.setPen(pen_inner)
        painter.drawEllipse(QRectF(-inner_radius, -inner_radius, inner_radius * 2, inner_radius * 2))
        painter.restore()

        # Central Glowing Core
        core_radius = radius * 0.35
        core_grad = QRadialGradient(center_x, center_y, core_radius)
        core_grad.setColorAt(0.0, QColor(255, 255, 255, 255))
        core_grad.setColorAt(0.5, QColor(0, 240, 255, 220))
        core_grad.setColorAt(1.0, QColor(0, 120, 200, 150))
        painter.setBrush(core_grad)
        painter.setPen(QPen(QColor(0, 240, 255), 2))
        painter.drawEllipse(QRectF(center_x - core_radius, center_y - core_radius, core_radius * 2, core_radius * 2))

        # Center Text label "JARVIS"
        painter.setPen(QColor(10, 25, 40))
        font = QFont("Consolas", 12, QFont.Bold)
        painter.setFont(font)
        painter.drawText(QRectF(center_x - core_radius, center_y - 12, core_radius * 2, 24), Qt.AlignCenter, "JARVIS")
