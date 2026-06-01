# Week 1 Report（2026.5.30-2026.6.6）

## 本周主题

项目初始化与基础工具链熟悉。

本周主要目标不是训练复杂模型，而是熟悉一个研究项目从 0 开始的基本流程：

```text
项目结构搭建 -> 文档填写 -> Git/GitHub 管理 -> Python 环境测试 -> Notebook 基础使用 -> 数据加载
```

## 本周目标

- 搭建 `toy-world-model-lab` 项目框架
- 熟悉 Git/GitHub 的基础上传流程
- 理解项目中文档、配置、代码、实验记录各自的作用
- 在 VSCode 中使用 Jupyter Notebook
- 测试 PyTorch 环境是否可用
- 加载 Fashion MNIST 数据集，为 AutoEncoder 重建任务做准备

## 本周完成

- 创建项目目录结构
- 编写 `README.md` 第一版
- 编写 `requirements.txt`
- 编写 `.gitignore`
- 编写 `configs/default.yaml`
- 创建 `docs/concepts.md` 概念笔记
- 创建 `docs/paper_notes/lagernvs.md` 论文笔记模板
- 创建 `experiments/experiment_log.md` 实验记录模板
- 初始化 Git 仓库
- 连接 GitHub 远程仓库
- 完成第一次 `push`
- 学会修改文件后的基础上传流程
- 完成 PyTorch 环境测试
- 在 VSCode 中创建并运行 `.ipynb` 文件
- 加载 Fashion MNIST 数据集
- 查看单张图片和 batch 的 shape
- 显示 Fashion MNIST 图片样例
- 初步整理 AutoEncoder reconstruction notebook

## 项目结构理解

本周理解了一个研究项目不应该只有代码，还应该包括文档、配置、实验记录和输出结果管理。

当前项目结构中各部分的作用：

```text
README.md                 项目说明、目标、进度
requirements.txt          记录项目依赖，方便复现环境
.gitignore                控制哪些文件不上传 GitHub
configs/default.yaml      保存实验参数
docs/                     学习笔记、论文笔记、周报
notebooks/                探索实验、数据查看、可视化
src/                      正式代码
experiments/              实验记录
outputs/                  保存图片、视频、模型结果
```

这一步训练的是项目组织能力。以后做研究时，代码、实验记录和文档要分开放，方便自己回顾，也方便和老师、师兄沟通。

## Git/GitHub 学习记录

本周学会了基础的 Git/GitHub 流程。

常用命令：

```bash
git status
git add .
git commit -m "说明这次改了什么"
git push
```

每一步的作用：

```text
git status      查看当前有哪些修改
git add .       把修改加入暂存区
git commit      保存一个本地版本
git push        上传到 GitHub
```

理解了常见状态：

```text
U / Untracked                  新文件还没有被 Git 跟踪
Changes to be committed         文件已经加入暂存区，准备提交
working tree clean              当前没有新的修改
LF will be replaced by CRLF      Windows 下常见的换行符提醒，不是错误
```

这一步训练的是版本管理能力。以后每完成一个小功能或一次实验记录，都应该及时 commit 和 push。

## Notebook 学习记录

本周开始使用 VSCode 中的 Jupyter Notebook。

理解了 `.ipynb` 的基本特点：

```text
.py      适合正式代码，从上到下运行
.ipynb   适合探索实验，可以一格一格运行并显示结果
```

Notebook 中常见 cell：

```text
Markdown cell   写说明文字
Code cell       运行 Python 代码
```

Notebook 的运行结果通常显示在每个 cell 下方，而不是主要看终端。

这一步训练的是探索实验能力。以后可以用 notebook 来查看数据、画图、验证小想法，再把稳定代码整理到 `src/` 中。

## PyTorch 与数据加载

本周完成了 PyTorch 基础环境测试，并加载了 Fashion MNIST 数据集。

理解了单张图片和 batch 的 shape：

```text
single image shape: [1, 28, 28]
batch image shape: [batch_size, 1, 28, 28]
```

含义：

```text
1             灰度通道
28            图片高度
28            图片宽度
batch_size    一次送入模型的图片数量
```

这一步训练的是数据检查能力。任何模型训练之前，都应该先确认数据是否能正确读取、shape 是否符合预期、图片显示是否正常。

## AutoEncoder 任务理解

本周初步进入 AutoEncoder 图片重建任务。

AutoEncoder 的目标是：

```text
input image -> reconstructed image
```

它和分类任务的区别：

```text
分类任务：图片 -> 标签
重建任务：图片 -> 图片
```

AutoEncoder 的结构可以理解为：

```text
input image -> encoder -> latent feature -> decoder -> reconstructed image
```

当前阶段只需要理解基本流程，不追求重建质量。

这一步的地位是：从图像分类过渡到图像生成/预测任务。后续的小球世界模型会进一步变成：

```text
current observation + action -> next observation
```

## 代码进展

目前完成了项目基础框架和 notebook 数据加载部分。

已创建或更新的文件包括：

```text
README.md
requirements.txt
.gitignore
configs/default.yaml
docs/concepts.md
docs/paper_notes/lagernvs.md
docs/weekly_reports/week1.md
experiments/experiment_log.md
notebooks/01_autoencoder_reconstruction.ipynb
src/test_torch.py
```

当前还没有完成正式的小球 world model 训练代码。

## 问题排查与解决记录

### 问题 1：Typora 打开 README.md 是空的

现象：

```text
VSCode 中写了 README.md，但 Typora 打开后看不到内容。
```

原因：

```text
可能是 VSCode 中内容没有保存，或者 Typora 打开的不是同一个文件路径。
```

解决方法：

```text
1. 在 VSCode 中 Ctrl + S 保存
2. 确认 Typora 打开的是同一路径下的 README.md
3. 从 VSCode 中右键文件，选择在文件资源管理器中显示，再用 Typora 打开
```

学到的内容：

```text
不同软件编辑的是同一个本地文件，关键是路径一致并且已经保存。
```

### 问题 2：Git 中出现 U / Untracked

现象：

```text
VSCode 文件名旁边显示 U，文件变绿。
```

原因：

```text
Git 发现了新文件，但还没有开始跟踪它。
```

解决方法：

```bash
git add .
```

学到的内容：

```text
新文件需要先 git add，之后才能 commit。
```

### 问题 3：git add 后出现 LF will be replaced by CRLF

现象：

```text
warning: LF will be replaced by CRLF
```

原因：

```text
Windows 和 Linux/Mac 的换行符格式不同，Git 在提醒换行符可能会被转换。
```

解决方法：

```text
这只是 warning，不是 error。当前阶段可以继续 commit。
```

学到的内容：

```text
warning 不一定代表代码出错，要学会区分 warning 和 error。
```

### 问题 4：git commit 命令写错

现象：

```text
error: pathspec ... did not match any file(s) known to git
```

原因：

```text
把 git commit -m 写成了错误格式，少了 - 或空格位置不对。
```

正确写法：

```bash
git commit -m "commit message"
```

学到的内容：

```text
-m 是 commit message 的参数，前面必须有短横线。
```

### 问题 5：Notebook 运行很慢

现象：

```text
运行 notebook cell 后很久没有输出。
```

可能原因：

```text
第一次启动 Python kernel
第一次 import torch / torchvision
正在下载 Fashion MNIST
VSCode notebook kernel 选择不正确
```

排查方法：

```text
1. 中断当前 cell
2. 重启 kernel
3. 先运行 print("hello notebook")
4. 在终端中测试 python -c "import torch; print(torch.__version__)"
5. 检查 notebook 右上角 Python 环境是否正确
```

学到的内容：

```text
遇到运行慢时，要区分是代码慢、环境问题，还是 notebook kernel 问题。
```

### 问题 6：VSCode 打开 notebook 报 Webview / Service Worker 错误

现象：

```text
Could not initialize webview
Could not register service worker
InvalidStateError
```

原因：

```text
这是 VSCode Webview 显示层或 Service Worker 缓存异常，不是 Python 代码错误。
```

解决方法：

```text
1. 保存当前文件
2. 完全关闭 VSCode
3. 清理 VSCode Service Worker 缓存
4. 重新打开 VSCode 和项目
```

学到的内容：

```text
不是所有报错都来自代码。这个问题属于工具缓存问题。
```

注意事项：

```text
如果再次看到 Webview / Service Worker 相关报错，优先考虑 VSCode 缓存或插件状态，而不是立刻修改代码。
```

### 问题 7：GitHub 预览 notebook 显示 An error occurred / 0 Bytes

现象：

```text
GitHub 打开 .ipynb 文件时显示 An error occurred，并且文件大小是 0 Bytes。
```

原因：

```text
上传到 GitHub 的 .ipynb 文件是空文件，不是合法 notebook。
```

解决方法：

```text
重新创建合法的 .ipynb 文件，确保里面至少有一个 cell，并保存后再 commit / push。
```

学到的内容：

```text
.ipynb 本质上是 JSON 格式的结构化文件，不能只是空文件改后缀。
```

### 问题 8：VSCode 中 notebook 显示旧内容或空白

现象：

```text
磁盘上的 notebook 已经被更新，但 VSCode 中打开后仍然显示旧内容或空白 cell。
```

原因：

```text
VSCode 中可能打开的是未保存的旧缓冲区，而不是磁盘上的最新文件。
```

解决方法：

```text
1. 关闭当前 notebook 标签页
2. 如果提示保存，选择不保存
3. 从左侧文件树重新打开 notebook
```

注意事项：

```text
不要在旧的空白页面直接 Ctrl + S，否则可能会把磁盘上的正确内容覆盖掉。
```

学到的内容：

```text
VSCode 中的未保存内容和磁盘上的真实文件可能不一致。
```

### 问题 9：Notebook 中中文显示成问号

现象：

```text
Markdown 中的中文显示成 ?????
```

原因：

```text
中文内容没有按 UTF-8 正确写入或保存，导致编码损坏。
```

解决方法：

```text
使用 UTF-8 编码重新写入 notebook，并检查文件中是否还包含 ????。
```

注意事项：

```text
如果中文已经变成问号，不要继续保存旧页面，应该重新用 UTF-8 写入。
```

学到的内容：

```text
中文文档、Markdown、notebook 都应该统一使用 UTF-8 编码。
```

## 本周总结

本周完成了从零搭建项目的基础流程，也遇到并解决了一些真实的新手常见问题。

当前已经初步掌握：

```text
项目结构组织
基础文档编写
Git/GitHub 上传流程
VSCode Notebook 使用
PyTorch 环境测试
Fashion MNIST 数据加载
工具问题排查
```

本周最重要的收获是：研究项目不只是写模型，还包括环境、工具、版本管理、文档记录和问题排查。

## 下周计划

- 继续运行并理解 `01_autoencoder_reconstruction.ipynb`
- 完成 AutoEncoder 图片重建实验
- 保存原图与重建图对比结果到 `outputs/figures/`
- 在 `experiments/experiment_log.md` 中补充 AutoEncoder 实验结果
- 开始进入小球数据集生成任务
- 理解 `observation + action -> next_observation` 的数据结构

## 想请教师兄/老师的问题

- 当前 toy world model 的学习路线是否符合组里的入门要求？
- 后续应该优先学习 world model 数据流程，还是先补 diffusion / transformer 概念？
- 对于 CPU-only 笔记本，是否还有推荐的小型实验任务？
