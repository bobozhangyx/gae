# gae
项目目的：使用免费的gae平台作爬虫代理

参见：https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env

1.其中
pip install -t lib -r requirements.txt #主要用于安装项目所需要的相关依赖库。

2.最简单的配置需要以下4个文件
appengine_config.py app.yaml main.py requirements.txt

3.app.yaml中的
script: main.app是程序的运行入口
