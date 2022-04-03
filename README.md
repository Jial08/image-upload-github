# Alfred Workflow 一键上传图片到github

参考：https://github.com/sunshinev/markdown-image-upload-github

有没有在写markdown时，因为想上传一张图片而苦恼？

现在可以直接截图后将图片上传到github，并且返回markdown格式的图片语法

- 旧版本 https://github.com/sunshinev/remote_pics/xxx.jpg
- 新版本(CDN加速) https://cdn.jsdelivr.net/gh/sunshinev/remote_pics/xxx.jpg


**注意**：Pillow模块不支持从剪贴板获取gif图片，所以目前不支持gif上传

![image](https://cdn.jsdelivr.net/gh/sunshinev/remote_pics/kapture-alfred.gif)

## 运行环境

Alfred + Mac  

## 支持图片类型
- JPG
- PNG

## 工作原理
1. 使用Alfred热键功能触发Workflow工作流程，执行Python脚本。
2. 使用Pillow模块从剪贴板Clipboard中获取`jpg/png`图片文件，并通过 GitHub api 上传
3. 将打印的加速路径直接复制到粘贴板并粘贴

## 安装

安装python的Pillow模块
```
pip install pillow
# 或
conda install pillow
```
