# Week 1 Report

## 本周目标

搭建 toy-world-model-lab 项目框架，熟悉 Git/GitHub 基础流程，并完成 VSCode 中 Jupyter Notebook 的基础使用。

## 本周完成

- 创建 toy-world-model-lab 项目目录结构
- 编写 README.md 第一版
- 编写 requirements.txt
- 编写 .gitignore
- 编写 configs/default.yaml
- 创建 concepts.md 概念笔记
- 创建 experiment_log.md 实验记录模板
- 初始化 Git 仓库，并连接到 GitHub
- 完成第一次 GitHub push
- 学会修改文件后的基础上传流程
- 完成 PyTorch 环境测试
- 在 VSCode 中创建并运行 .ipynb 文件
- 加载 Fashion MNIST 数据集
- 查看单张图片和 batch 的 shape
- 显示 Fashion MNIST 图片样例

## 学到的概念

### 项目结构

一个研究项目不只是代码，还需要文档、配置、实验记录和输出结果管理。

- README.md：说明项目目标、结构和当前进度
- requirements.txt：记录项目依赖，方便复现环境
- .gitignore：控制哪些文件不上传到 GitHub
- configs/default.yaml：统一管理实验参数
- docs/：保存概念笔记、论文笔记和周报
- notebooks/：用于探索实验和可视化
- src/：用于保存正式代码
- experiments/：用于记录实验过程
- outputs/：用于保存图片、视频和模型结果

### Git/GitHub

Git 用于本地版本管理，GitHub 用于远程备份和协作。

常用流程：

```bash
git status
git add .
git commit -m "说明这次改了什么"
git push
```

理解了常见状态：

- U / Untracked：新文件还没有被 Git 跟踪
- Changes to be committed：文件已经加入暂存区，准备提交
- working tree clean：当前没有新的修改
- LF will be replaced by CRLF：Windows 下常见的换行符提醒，不是错误

### Jupyter Notebook

.ipynb 文件适合做探索实验，可以一段一段运行代码，并直接在 cell 下方查看输出、图片和报错。

当前理解：

- Markdown cell 用于写说明文字
- Code cell 用于运行 Python 代码
- Notebook 适合看数据、画图、验证想法
- 正式训练代码后续应该逐步整理到 src/*.py 中

### PyTorch 和 Fashion MNIST

完成了 PyTorch 基础环境测试，并加载了 Fashion MNIST 数据集。

理解了：

```text
单张图片 shape: [1, 28, 28]
batch 图片 shape: [batch_size, 1, 28, 28]
```

其中：

- 1 表示灰度通道
- 28 表示图片高度
- 28 表示图片宽度
- batch_size 表示一次送入模型的图片数量

## 代码进展

目前已完成项目基础框架和 notebook 数据加载部分，还没有开始正式训练 AutoEncoder 模型。

已完成的代码/文件包括：

- README.md
- requirements.txt
- .gitignore
- configs/default.yaml
- docs/concepts.md
- docs/paper_notes/lagernvs.md
- experiments/experiment_log.md
- notebooks/01_autoencoder_reconstruction.ipynb
- src/test_torch.py

## 遇到的问题
- 使用 git add . 时出现 LF/CRLF warning，后来理解这是 Windows 换行符提示，不是错误。
- 第一次 git commit 时命令写成了错误格式，后来理解正确写法是：

```bash
git commit -m "commit message"
```

- 刚开始不清楚 notebook 的运行结果在哪里查看，后来理解输出会显示在每个 cell 下方，终端主要用于命令行操作。

## 当前收获

本周主要熟悉了一个研究项目从 0 开始的基础流程：

```text
项目结构搭建 -> 文档填写 -> Git 管理 -> GitHub 上传 -> 环境测试 -> Notebook 数据加载
```

现在已经能完成最基础的项目初始化、版本提交、远程上传和 notebook 数据查看。

## 下周计划

- 在 notebook 中实现 AutoEncoder 模型
- 完成 Fashion MNIST 图片重建实验
- 理解 encoder、decoder、latent representation 和 reconstruction loss
- 保存原图与重建图对比结果到 outputs/figures/
- 在 experiment_log.md 中记录第一次模型实验

## 想请教师兄/老师的问题

- 当前 toy world model 项目的学习路线是否符合组里的入门要求？
- 后续应该优先学习 world model 数据流程，还是先补 diffusion / transformer 概念？
- 对于 CPU-only 笔记本，是否还有推荐的小型实验任务？
