# Experiment Log

这个文件用于记录每一次实验的配置、结果、观察和问题。

## setup001_project_setup

日期：2026-05-30

目标：搭建 toy-world-model-lab 项目结构，并完成 Git/GitHub 基础流程。

配置：
- device: CPU-only laptop
- editor: VSCode
- version control: Git + GitHub

结果：
- 完成项目目录结构搭建
- 完成 README.md、requirements.txt、.gitignore、default.yaml 等基础文件
- 成功初始化 Git 仓库
- 成功连接 GitHub 并完成第一次 push

观察：
- 项目结构比单个 notebook 更清晰
- Git 可以帮助记录每次修改
- GitHub 可以作为远程备份和展示入口

问题：
- 一开始不熟悉 git commit 的命令格式
- 对 Git 文件状态标记不熟悉，比如 U / Untracked

下一步：
- 使用 notebook 加载 Fashion MNIST
- 开始 AutoEncoder 图片重建练习

## exp001_autoencoder

日期：2026-05-30

目标：训练一个简单 AutoEncoder，理解 image -> image 的图片重建任务。

配置：
- dataset: Fashion MNIST
- model: SimpleAutoEncoder
- epochs: 1
- device: CPU
- loss: MSELoss
- optimizer: Adam
- learning_rate: 0.001

结果：
- 成功在 VSCode 中运行 Jupyter Notebook
- 成功加载 Fashion MNIST 数据集
- 成功查看单张图片和 batch 的 shape
- 成功训练 AutoEncoder 基础流程
- 成功显示原图和重建图对比

观察：
- AutoEncoder 的输入和输出都是图片
- encoder 负责把图片压缩成 latent feature
- decoder 负责根据 latent feature 重建图片
- 只训练 1 个 epoch 时，重建结果可能比较模糊，这是正常现象
- CPU 环境下应该优先使用小模型、小 batch 和少量 epoch

问题：
- Notebook 第一次运行时可能会因为 kernel 或环境选择问题变慢
- 需要确认 VSCode notebook 使用的是正确的 Python 环境

下一步：
- 理解 encoder、decoder 和 latent representation 的作用
- 保存 autoencoder_reconstruction.png 到 outputs/figures/
- 后续从图片重建过渡到小球下一帧预测任务
