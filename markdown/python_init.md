# Python Scripts 初始化：初始指令

## venv
### 建立
```sh
python3 -m venv venv
```
### 啟動
```sh
.\venv\Scripts\activate
```
### 查看當前 package list
```sh
pip list
```

## Package 安裝
### requests
```sh
pip install requests
```
### .env 用這個讀取
```sh
pip install python-dotenv
```


## 將 venv 中的 Package 寫進 requirements.txt
```sh
.\venv\Scripts\activate
pip freeze > requirements.txt
```