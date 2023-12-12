import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
import buttons
import password
# from ui.ui_main import Ui_MainWindow
from ui.generate import Ui_MainWindow


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Length counter
        self.connect_slider_to_spinbox()

        # create password
        self.set_password()

        for btn in buttons.GENERATE_PASSWORD:
            getattr(self.ui, btn).clicked.connect(self.set_password)

        # visibly password
        self.ui.btn_visibility.clicked.connect(self.visibility_password)

        # copy password
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

        # when write in line edit
        self.when_password_edit()

    def connect_slider_to_spinbox(self) -> None:
        self.ui.slider_len.valueChanged.connect(self.ui.spinBox_len.setValue)
        self.ui.spinBox_len.valueChanged.connect(self.ui.slider_len.setValue)
        self.ui.spinBox_len.valueChanged.connect(self.set_password)

    def get_characters(self) -> str:
        ch = ''
        for button in buttons.Characters:
            if getattr(self.ui, button.name).isChecked():
                ch += button.value
        return ch

    def set_password(self) -> None:
        try:
            self.ui.line_password.setText(
                password.create_new(length=self.ui.spinBox_len.value(), characters=self.get_characters())
            )
        except IndexError:
            self.ui.line_password.setText('Из чего...')

        self.get_entropy_and_strong()

    def get_number_char(self) -> int:
        num = 0
        for n in buttons.CHARACTER_NUMBER.items():
            if getattr(self.ui, n[0]).isChecked():
                num += n[1]
        return num

    def get_entropy_and_strong(self) -> None:
        length = len(self.ui.line_password.text())
        number_char = self.get_number_char()
        entropy = password.get_entropy(length, number_char)

        self.ui.entropy.setText(
            f'Entropy: {entropy} bit'
        )

        for strength in password.StrengthToEntropy:
            if entropy >= strength.value:
                self.ui.stronght.setText(f'Strength: {strength.name}')

    def visibility_password(self) -> None:
        if self.ui.btn_visibility.isChecked():
            self.ui.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.line_password.setEchoMode(QLineEdit.Password)

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.line_password.text())

    def when_password_edit(self) -> None:
        self.ui.line_password.textEdited.connect(self.get_entropy_and_strong)
        # print(self.ui.line_password.textEdited)
        # if self.ui.line_password.textEdited:
        #     print(self.ui.line_password.text())
        #     for char in self.ui.line_password.text():
        #         if char in ascii_lowercase:
        #             self.ui.btn_lower.setChecked(True)
        #         # else:
        #         #     self.ui.btn_lower.setChecked(False)
        #         if char in ascii_uppercase:
        #             self.ui.btn_upper.setChecked(True)
        #         # else:
        #         #     self.ui.btn_upper.setChecked(False)
        #         if char in digits:
        #             self.ui.btn_num.setChecked(True)
        #         # else:
        #         #     self.ui.btn_num.setChecked(False)
        #         if char in punctuation:
        #             self.ui.btn_special.setChecked(True)
        #         # else:
        #         #     self.ui.btn_special.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec())
