# DB-Front

<div style="text-align:right"><font style="font-size:20px;">周䶮 王治同 2021.6.1</font></div>

## 一、运行方法

### 1. 打开mysql服务

windows 操作系统中，用管理员身份打开命令提示符（command prompt），执行：

```bash
net start mysql
```

### 2. 运行 django 后端

进入根目录下的 football 文件夹。

请 **务必先切换到合适的 python 环境上** 。在此用命令行：

```bash
python manage.py runserver
```

打开 django 后端，默认端口：`localhost:8000`

### 3. 运行vue前端

进入根目录下的 PRE 文件夹。

初次运行时，先在命令行输入：

```bash
npm install
```

安装依赖库。然后执行：

```bash
npm run dev
```

以在本地打开 vue 前端页面，默认端口：`localhost:8081`

## 二、环境要求

### python环境：

| 名称       | 版本       | 备注                                 |
| ---------- | ---------- | ------------------------------------ |
| python     | 3.7.0      |                                      |
| django     | 3.1.5      |                                      |
| matplotlib | 3.3.2      | **其他版本可能出错！**最好采用该版本 |
| PyQt5-Qt5  | 5.15.2     |                                      |
| numpy      | **1.19.1** | **其他版本可能出错！**最好采用该版本 |

若绘图部分出错，则可能是上面提到的 `matplotlib` 或者 `numpy` 的版本与代码不匹配导致的。

可采用以下方法解决：

```bash
pip uninstall matplotlib
pip install matplotlib==3.3.2
```

或者

```bash
pip uninstall numpy
pip install numpy==1.19.1
```

尤其是 `numpy` 的版本，绘制图片的 python 脚本对 `numpy` 版本比较敏感，该部分不太 robust，因此 **建议采用这个numpy版本！** 

### node.js 环境

| 名称 | 版本     |
| ---- | -------- |
| node | v14.15.4 |
| npm  | 7.11.2   |

## 三、具体功能

### visualization page

对一支队伍在特定时段内积分的变化进行可视化处理。

### Competitions

对数据库的 `all_event` 表进行增删查改，管理所有的比赛。

### Search Team

关于 `all_country`，`world_country` 和 `league_country` 查询，未能来得及完成功能，静待花开。

### Rankings

查看不同排名榜单的具体排名。

