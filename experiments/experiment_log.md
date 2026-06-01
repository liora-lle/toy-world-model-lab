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

## exp002_ball_image_generation

日期：2026-06-01

目标：验证 generate_ball_image 是否能根据给定位置生成 32x32 小球图像。

配置：
- image_size: 32
- radius: 2
- positions: (8,8), (16,16), (24,24), (8,24), (24,8)

结果：
- 成功生成小球图像
- 成功显示不同位置的小球

观察：
- x 增大时，小球向右移动
- y 增大时，小球向下移动
- 图像像素值范围为 0 到 1

问题：
- 待补充

下一步：
- 增加 action 更新函数
- 实现 up/down/left/right 对小球位置的控制


## exp003_action_update

日期：2026-06-01

目标：验证 action 是否能正确更新小球位置。

配置：
- image_size: 32
- radius: 2
- step_size: 4
- actions: up / down / left / right
- start_position: (16, 16)

结果：
- 成功定义 `ACTION_TO_DELTA`
- 成功实现 `update_position`
- 成功根据 action 更新小球位置
- 成功生成 current_image 和 next_image
- 成功可视化动作前后的变化

观察：
- `right` 会让 x 增大
- `left` 会让 x 减小
- `up` 会让 y 减小
- `down` 会让 y 增大
- 图像坐标系的原点在左上角
- `step_size` 控制单步动作移动幅度
- 对 32x32 图像来说，`step_size=4` 比 `step_size=1` 更容易观察

问题：
- 如果 `step_size` 太小，视觉变化不明显
- 如果 `step_size` 太大，小球移动会太跳跃
- 需要边界处理，避免小球跑出图像

下一步：
- 生成连续 episode
- 将单步动作扩展为动作序列


## exp004_generate_episode

日期：2026-06-01

目标：生成一段连续的小球运动 episode，理解 trajectory / episode 的基本形式。

配置：
- image_size: 32
- sequence_length: 6
- radius: 2
- step_size: 4
- start_position: (16, 16)
- actions: random choice from up / down / left / right

结果：
- 成功实现 `generate_episode`
- 成功生成 6 帧小球图像
- 成功生成 5 个 action
- 成功记录每一帧的小球位置
- 成功可视化一段连续小球运动过程

观察：
- 一段 episode 中，frames 数量比 actions 数量多 1
- action 表示两个相邻 frame 之间发生的动作
- episode 可以拆成多个训练样本：


## exp005_pytorch_dataset

日期：2026-06-01

目标：将小球 episode 拆分成 PyTorch Dataset 样本。

配置：
- num_sequences: 10
- sequence_length: 6
- image_size: 32
- radius: 2
- step_size: 4
- batch_size: 8

结果：
- 成功构建 BallWorldModelDataset
- 成功返回 observation、action、next_observation
- 成功使用 DataLoader 读取 batch

观察：
- 每条 episode 有 sequence_length 帧和 sequence_length - 1 个 action
- Dataset 样本数量 = num_sequences * (sequence_length - 1)
- observation shape 为 [1, 32, 32]
- batch observation shape 为 [batch_size, 1, 32, 32]
- action 已经从字符串转换为数字编号

问题：
- 当前 action 只是整数编号，后续模型中可能需要 embedding 或 one-hot
- 当前数据全部在初始化时生成，数据量很大时需要考虑更高效的数据生成方式

下一步：
- 构建最小 world model
- 输入 observation 和 action
- 输出 next_observation