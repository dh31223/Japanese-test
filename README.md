# 环境配置方式

## 前提

必须安装了python。

## 如何安装

### 克隆仓库到本地

```bash
git clone https://github.com/dh31223/Japanese-test.git
```

### 更换软件下载来源

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 创建python虚拟环境

```bash
python -m venv .venv
```

### 下载相应的包

```bash
pip install -r requirements.txt
```

### 运行程序

```bash
python main.py
```
