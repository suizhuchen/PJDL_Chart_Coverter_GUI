# PJDL Chart Converter GUI

基于PySide6与PyQt-Fluent-Widgets的啤酒道理(PJDL)转换器的GUI实现。

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## 目录

- [使用指南](#使用指南)
    - [使用前提示](#使用前提示)
    - [配置要求](#配置要求)
    - [安装步骤](#安装步骤)
    - [如何报告错误或自己进一步开发](#如何报告错误或自己进一步开发)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 使用指南

在GUI界面内，通过按钮选择谱面文件与要转换的格式，点击转换按钮即可。如果遇到不支持PJDL的歌曲文件与封面图片文件，若勾选选项，转换器会尝试帮你转换到正确的格式。

###### 使用前提示

如果想要使用转换音频到OGG功能，需要下载ffmpeg，下载之后可以放在转换器目录下，或通过按钮手动选择ffmpeg.exe。

ffmpeg下载地址：https://github.com/BtbN/FFmpeg-Builds/releases

###### 配置要求

1. Windows10以上系统（我只打包了windows版本，需要其他版本自行使用nuitka编译）
2. osz/mcz/pjdl谱面文件

###### **安装步骤**

1. 从Release下载软件
2. 运行exe文件

#### 如何报告错误或自己进一步开发

在本仓库内提出issue，包括你的运行截图，以及谱面文件，较为详细的描述你的问题，我尽力解决

群里at我也行（一群蓝色头发管理员）

当然，你也可以帮忙修改一些代码，fork仓库，改完pull request。毕竟我的代码真是一言难尽。

项目是main.py作为入口主程序，我通过下面的nuitka命令编译成exe文件：

```
python -m nuitka --mingw64 --onefile --disable-console --enable-plugin=pyside6 --windows-icon-from-ico=winicon.ico --remove-output --lto=yes main.py
```

chartConvert.py是根据.ui文件生成的，有关PyQt-Fluent-Widgets的其他代码可以搜一下文档。

### 作者

Suichen

suichen114514@outlook.com

### 鸣谢

PJDL作者：[会唱歌的花枝丸](https://github.com/hua-zhi-wan)

PySide6: [PySide6](https://www.qt.io/qt-for-python)

QFluentWidgets: [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)

README文件模板：[Best_README_template](https://github.com/shaojintian/Best_README_template)

<!-- links -->

[your-project-path]:suizhuchen/PJDL_Chart_Coverter_GUI

[contributors-shield]: https://img.shields.io/github/contributors/suizhuchen/PJDL_Chart_Coverter_GUI.svg?style=flat-square

[contributors-url]: https://github.com/suizhuchen/PJDL_Chart_Coverter_GUI/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/suizhuchen/PJDL_Chart_Coverter_GUI.svg?style=flat-square

[forks-url]: https://github.com/suizhuchen/PJDL_Chart_Coverter_GUI/network/members

[stars-shield]: https://img.shields.io/github/stars/suizhuchen/PJDL_Chart_Coverter_GUI.svg?style=flat-square

[stars-url]: https://github.com/suizhuchen/PJDL_Chart_Coverter_GUI/stargazers

[issues-shield]: https://img.shields.io/github/issues/suizhuchen/PJDL_Chart_Coverter_GUI.svg?style=flat-square

[issues-url]: https://img.shields.io/github/issues/suizhuchen/PJDL_Chart_Coverter_GUI.svg

[license-shield]: https://img.shields.io/github/license/suizhuchen/PJDL_Chart_Coverter_GUI.svg?style=flat-square

[license-url]: https://github.com/suizhuchen/PJDL_Chart_Coverter_GUI/blob/master/LICENSE.txt
