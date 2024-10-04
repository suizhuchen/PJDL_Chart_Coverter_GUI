import os
import shutil
from zipfile import ZipFile
from PIL import Image
import subprocess
import threading
import sys

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
    {'Description': 'Osu! Mania Chart File', 'Filter': 'osz'},
]

temp_dir = os.path.join(os.path.dirname(__file__), "temp")
chart_list = []


def open_file_dialog(title, type_filter, allow_all_files=True, dialog_type='open', default_dir='') -> str:
    text_filter = ''
    if allow_all_files:
        text_filter += "All Supported Files ("
        for file_type in type_filter:
            text_filter += f"*.{file_type['Filter']} "
        text_filter = text_filter[:-1]
        text_filter += ");;"
    for file_type in type_filter:
        text_filter += f"{file_type['Description']} (*.{file_type['Filter']});;"

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


def clear_exit():
    shutil.rmtree(temp_dir, ignore_errors=True)


def try_get_ffmpeg_path(window):
    dir_ffmpeg_path = os.path.dirname(sys.argv[0]) + "/ffmpeg.exe"
    if os.path.exists(dir_ffmpeg_path):
        test_ffmpeg = AudioConvertAction(dir_ffmpeg_path, window)
        if test_ffmpeg.ffmpeg_check():
            window.lineEdit_3.setText(dir_ffmpeg_path)
            window.plainTextEdit.appendPlainText(f"成功读取ffmpeg！ffmpeg路径已设置为：{dir_ffmpeg_path}")


class ChartConvertAction:
    @staticmethod
    def ffmpeg_button_clicked(line_edit):
        ffmpeg_path = open_file_dialog("选择ffmpeg.exe路径：", [{'Description': 'ffmpeg.exe', 'Filter': 'exe'}],
                                       allow_all_files=False,
                                       dialog_type='open')
        if ffmpeg_path:
            line_edit.setText(ffmpeg_path)

    @staticmethod
    def input_button_clicked(window):
        file_path = open_file_dialog("选择你要转换的谱面文件：", ACCEPTABLE_INPUT_FILE_TYPES, dialog_type='open')
        if file_path:
            window.lineEdit.setText(file_path)
            shutil.rmtree(temp_dir, ignore_errors=True)
            os.makedirs(temp_dir, exist_ok=True)
            chart_list.clear()
            window.comboBox.clear()
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
                    full_path = os.path.join(temp_dir, chart_path)
                    with open(full_path, 'r', encoding='utf-8') as chart_file:
                        chart_content = chart_file.read()
                    chart_class = PJDLChart.generate_from_chart(chart_content, chart_type)
                    if isinstance(chart_class, PJDLChart):
                        chart_list.append([chart_class, chart_path, full_path])
                    else:
                        window.plainTextEdit.appendPlainText(f"已忽略{chart_path}，原因：{chart_class}")
                        continue
            for chart in chart_list:
                window.comboBox.addItem(f'{chart[0].version.strip()} ({chart[1]})', userData=chart[2])

    @staticmethod
    def output_button_clicked(line_edit, input_line_edit):
        file_name = ''
        if input_line_edit.text():
            file_name, file_ext = os.path.splitext(input_line_edit.text())

        file_path = open_file_dialog("选择你要保存谱面文件的位置：", ACCEPTABLE_OUTPUT_FILE_TYPES, dialog_type='save',
                                     default_dir=file_name if file_name else '', allow_all_files=False)
        if file_path:
            line_edit.setText(file_path)

    @staticmethod
    def convert_button_clicked(window):
        # 处理前检测
        chart_file_path = window.comboBox.itemData(window.comboBox.currentIndex())
        list_index = window.comboBox.currentIndex()
        if not chart_file_path:
            throw_error(window, "请选择要转换的谱面文件", log_text_edit=window.plainTextEdit)
            return
        if not os.path.exists(chart_file_path):
            throw_error(window, "选择的谱面文件不存在", log_text_edit=window.plainTextEdit)
            return
        output_package_path = window.lineEdit_2.text()
        if not output_package_path:
            throw_error(window, "请选择输出文件", log_text_edit=window.plainTextEdit)
            return
        if os.path.exists(output_package_path):
            os.remove(output_package_path)

        window.plainTextEdit.appendPlainText("--------------------------------")
        window.plainTextEdit.appendPlainText(f"开始转换：{chart_file_path}")
        chart_class = chart_list[list_index][0]
        chart_ext = os.path.splitext(output_package_path)[1]

        temp_chart_path = os.path.dirname(os.path.join(temp_dir, chart_list[list_index][1]))
        if chart_class.bg.startswith('"') and chart_class.bg.endswith('"'):
            chart_class.bg = chart_class.bg[1:-1]

        # 进行转换
        # 检测ffmpeg.exe是否存在
        audio_path = os.path.join(temp_chart_path, chart_class.song_path)
        if window.checkBox_2.isChecked():
            ffmpeg_path = window.lineEdit_3.text()
            ffmpeg = AudioConvertAction(ffmpeg_path, window)
            if not ffmpeg.ffmpeg_check():
                throw_error(window, "ffmpeg.exe不存在或不可用，请重新选择", log_text_edit=window.plainTextEdit)
                return
            output_path = audio_path + '.ogg'
            ffmpeg.convert(window, audio_path, output_path)
            # os.remove(audio_path)
            audio_path = os.path.join(os.path.dirname(audio_path), 'song.ogg')
            if os.path.exists(audio_path):
                os.remove(audio_path)
            os.rename(output_path, audio_path)
            chart_class.song_path = 'song.ogg'
        cover_path = os.path.join(temp_chart_path, chart_class.bg)
        if window.checkBox.isChecked():
            cover_output_path = cover_path + '.jpg'
            CoverConvertAction.convert(window, cover_path, cover_output_path)
            # os.remove(cover_path)
            cover_path = os.path.join(os.path.dirname(cover_path), 'cover.jpg')
            if os.path.exists(cover_path):
                os.remove(cover_path)
            os.rename(cover_output_path, cover_path)
            chart_class.bg = 'cover.jpg'

        if chart_ext == '.mcz':
            chart_content = chart_class.generate_to_chart('malody')
            file_name = 'chart.mc'
        elif chart_ext == '.pjdlc':
            chart_content = chart_class.generate_to_chart('pjdl')
            file_name = 'chart.json'
        elif chart_ext == '.osz':
            chart_content = chart_class.generate_to_chart('osu')
            file_name = 'chart.osu'
        else:
            throw_error(window, "不支持的输出文件类型", log_text_edit=window.plainTextEdit)
            return

        with ZipFile(output_package_path, 'w') as zip_file:
            zip_file.writestr(file_name, chart_content)
            zip_file.write(audio_path, arcname='song.ogg')
            zip_file.write(cover_path, arcname='cover.jpg')

        window.plainTextEdit.appendPlainText(f"转换完成：{output_package_path}")


class AudioConvertAction:
    def __init__(self, ffmpeg_path, window):
        self.ffmpeg_path = ffmpeg_path
        self.window = window

    def read_output(self, pipe, prefix):
        for line in iter(pipe.readline, ''):
            self.window.plainTextEdit.appendPlainText(f"{prefix}: {line.strip()}")
        pipe.close()

    def convert(self, window, input_path, output_path):
        if not self.ffmpeg_check():
            throw_error(window, "ffmpeg.exe不存在，请将ffmpeg.exe放入程序目录", log_text_edit=window.plainTextEdit)
            return
        if not os.path.exists(input_path):
            throw_error(window, "选择的音频不存在", log_text_edit=window.plainTextEdit)
            return
        if os.path.exists(output_path):
            os.remove(output_path)
        window.plainTextEdit.appendPlainText(f"开始转换音频：{input_path}")
        try:
            ffmpeg_process = subprocess.Popen([self.ffmpeg_path, '-loglevel', 'error', '-i', input_path, output_path],
                                              shell=True,
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout_thread = threading.Thread(target=self.read_output, args=(ffmpeg_process.stdout, 'ffmpeg'))
            stderr_thread = threading.Thread(target=self.read_output, args=(ffmpeg_process.stderr, "ffmpeg"))
            stdout_thread.start()
            stderr_thread.start()

            stdout_thread.join()
            stderr_thread.join()

            return_code = ffmpeg_process.wait()
            if return_code is not None:
                window.plainTextEdit.appendPlainText(f"ffmpeg已退出，返回码：{return_code}")
                window.plainTextEdit.appendPlainText(f"音频转换完成：{output_path}")
        except Exception as e:
            throw_error(window, f"音频转换失败：{e}", log_text_edit=window.plainTextEdit)
            return

    def ffmpeg_check(self):
        if not os.path.exists(self.ffmpeg_path):
            return False
        # 检测ffmpeg版本
        try:
            ffmpeg_version = subprocess.check_output([self.ffmpeg_path, '-version'], shell=True, text=True)
            if 'ffmpeg version' not in ffmpeg_version:
                return False
        except Exception as e:
            return False
        return True


class CoverConvertAction:
    @staticmethod
    def convert(window, input_path, output_path):
        if not os.path.exists(input_path):
            throw_error(window, "选择的图片不存在", log_text_edit=window.plainTextEdit)
            return
        if os.path.exists(output_path):
            os.remove(output_path)
        window.plainTextEdit.appendPlainText(f"开始转换图片：{input_path}")
        try:
            img = Image.open(input_path)
            img.save(output_path)
            window.plainTextEdit.appendPlainText(f"图片转换完成：{output_path}")
        except Exception as e:
            throw_error(window, f"图片转换失败：{e}", log_text_edit=window.plainTextEdit)
            return
