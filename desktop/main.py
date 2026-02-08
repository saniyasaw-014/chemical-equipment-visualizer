import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QFileDialog, QLabel, QLineEdit
)
from api_client import login, upload_csv
from charts import show_chart

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")

        layout = QVBoxLayout()

        self.user = QLineEdit()
        self.user.setPlaceholderText("Username")

        self.pwd = QLineEdit()
        self.pwd.setPlaceholderText("Password")
        self.pwd.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.handle_login)

        upload_btn = QPushButton("Upload CSV")
        upload_btn.clicked.connect(self.handle_upload)

        self.status = QLabel("Status: Not logged in")

        layout.addWidget(self.user)
        layout.addWidget(self.pwd)
        layout.addWidget(login_btn)
        layout.addWidget(upload_btn)
        layout.addWidget(self.status)

        self.setLayout(layout)

    def handle_login(self):
        try:
            login(self.user.text(), self.pwd.text())
            self.status.setText("Status: Logged in")
        except Exception as e:
            self.status.setText("Login failed")

    def handle_upload(self):
        try:
            path, _ = QFileDialog.getOpenFileName(self, "Select CSV", "", "*.csv")
            if path:
                data = upload_csv(path)
                self.status.setText(
                f"""
                Total: {data['total_equipment']}
                Avg Flow: {data['average_flowrate']}
                Avg Pressure: {data['average_pressure']}
                Avg Temp: {data['average_temperature']}
                """
                )
                show_chart(data["type_distribution"])
        except Exception as e:
            self.status.setText("Upload failed")


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())
