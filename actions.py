import os
import shutil
from zipfile import ZipFile

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog

from qfluentwidgets import InfoBar, InfoBarPosition

from chart.main import PJDLChart

ACCEPTABLE_INPUT_FILE_TYPES = [
    {'Description': 'Malody Chart File', 'Filter': 'mcz'},
    {'Description': 'Osu! Mania Chart File', 'Filter': 'osz'},
    {'Description': 'PJDL Chart File', 'Filter': 'pjdlc'},
]

ACCEPTABLE_OUTPUT_FILE_TYPES = [
    {'Description': 'PJDL Chart File', 'Filter': 'pjdlc'},
    {'Description': 'Malody Chart File', 'Filter': 'mcz'},
]

temp_dir = os.path.join(os.path.dirname(__file__), "temp")
chart_list = []


def open_file_dialog(title, type_filter, allow_all_files=False, dialog_type='open', default_dir='') -> str:
    text_filter = ''
    for file_type in type_filter:
        text_filter += f"{file_type['Description']} (*.{file_type['Filter']});;"
    if allow_all_files:
        text_filter += "All Files (*)"
    else:
        text_filter = text_filter[:-2]
    if dialog_type == 'open':
        file_path, _ = QFileDialog.getOpenFileName(None, title, default_dir, text_filter)
    elif dialog_type == 'save':
        file_path, _ = QFileDialog.getSaveFileName(None, title, default_dir, text_filter)
    else:
        raise ValueError("Invalid dialog type")
    return file_path


def throw_error(window, message, log_text_edit=None):
    if log_text_edit:
        log_text_edit.appendPlainText(f'错误：{message}')
    InfoBar.error(
        title="错误",
        content=message,
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP_RIGHT,
        duration=-1,  # won't disappear automatically
        parent=window

    )


class ChartConvertAction:
    @staticmethod
    def input_button_clicked(window):
        file_path = open_file_dialog("选择你要转换的谱面文件：", ACCEPTABLE_INPUT_FILE_TYPES, dialog_type='open')
        if file_path:
            window.lineEdit.setText(file_path)
            shutil.rmtree(temp_dir, ignore_errors=True)
            os.makedirs(temp_dir, exist_ok=True)
            chart_list.clear()
            with ZipFile(file_path, 'r', metadata_encoding='utf-8') as zip_file:
                zip_file.extractall(temp_dir)
            window.plainTextEdit.appendPlainText("解压谱面完成")
            chart_path_list = []
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    chart_path_list.append(os.path.join(os.path.relpath(root, temp_dir), file))
            chart_ext = os.path.splitext(file_path)[1]
            if chart_ext == '.mcz':
                chart_filter = '.mc'
                chart_type = 'malody'
            elif chart_ext == '.osz':
                chart_filter = '.osu'
                chart_type = 'osu'
            elif chart_ext == '.pjdlc':
                chart_filter = '.json'
                chart_type = 'pjdl'
            else:
                throw_error(window, "不支持的谱面文件类型", log_text_edit=window.log_text_edit)
                return
            for chart_path in chart_path_list:
                if chart_path.endswith(chart_filter):
                    with open(os.path.join(temp_dir, chart_path), 'r', encoding='utf-8') as chart_file:
                        chart_content = chart_file.read()
                    chart_class = PJDLChart.generate_from_chart(chart_content, chart_type)
                    if chart_class is PJDLChart:
                        chart_list.append([chart_class, chart_path])
                    else:
                        window.plainTextEdit.appendPlainText(f"已忽略{chart_path}，原因：{chart_class}")
                        continue
            for chart in chart_list:
                window.comboBox.addItem(f'{chart[0].info} ({chart[1]})')

    @staticmethod
    def output_button_clicked(line_edit, input_line_edit):
        file_name = ''
        if input_line_edit.text():
            file_name, file_ext = os.path.splitext(input_line_edit.text())

        file_path = open_file_dialog("选择你要保存谱面文件的位置：", ACCEPTABLE_OUTPUT_FILE_TYPES, dialog_type='save',
                                     default_dir=file_name if file_name else '')
        if file_path:
            line_edit.setText(file_path)

    # @staticmethod
    # def convert_button_clicked(window, input_line_edit, output_line_edit, jpg_checkbox, ogg_checkbox, log_text_edit):
    #     input_file_path = input_line_edit.text()
    #     output_file_path = output_line_edit.text()
    #     jpg_enabled = jpg_checkbox.isChecked()
    #     ogg_enabled = ogg_checkbox.isChecked()
    #     if not input_file_path or not output_file_path:
    #         throw_error(window, "请选择输入文件和输出文件", log_text_edit)
    #         return
    #     if not os.path.exists(input_file_path):
    #         throw_error(window, "输入文件不存在", log_text_edit)
    #         return
    #     if os.path.exists(output_file_path):
    #         os.remove(output_file_path)
    #     # 正式处理
    #     # 解压缩输入文件
    @staticmethod
    def convert_button_clicked(window, input_line_edit, output_line_edit, jpg_checkbox, ogg_checkbox, log_text_edit):
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                print(os.path.join(os.path.relpath(root, temp_dir), file))
