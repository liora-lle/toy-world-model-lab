# Concepts

这个文件用于记录学习过程中遇到的核心概念。要求是用自己的话写清楚，不追求复杂公式。

## World Model

World model 可以理解为：根据当前观测和动作，预测未来会发生什么。

```text
observation + action -> next observation
```

在本项目中，对应的是：

```text
当前小球画面 + 动作 -> 下一帧小球画面
```

## VLA

VLA 是 Vision-Language-Action 的缩写。

它研究的是：模型如何根据视觉输入和语言指令，输出动作。

```text
image + language instruction -> action
```

在真实机器人任务中，可能是：

```text
看到桌面画面 + “把杯子拿起来” -> 机械臂动作
```

在本项目中，可以简化成：

```text
小球画面 + “move left” -> left
```

## Novel View Synthesis

Novel view synthesis 是新视角生成。

它的目标是：根据已有视角的图像，生成另一个视角下的图像。

```text
source view + target view -> target image
```

在本项目中，可以先简化成：

```text
正常视角小球图像 + 目标 view_id -> 翻转或旋转后的图像
```

## Diffusion Model

Diffusion model 是一种生成模型。

可以用大白话理解为：先把图片逐步加噪声，再训练模型学习如何把噪声去掉。

```text
training: image -> noisy image -> denoise
generation: noise -> denoise step by step -> image
```

当前阶段只需要理解基本流程，不需要深入数学公式。

## Transformer

Transformer 是一种适合处理序列的模型结构。

序列可以是：

```text
文字 token
图像 patch
视频帧
动作序列
```

当前阶段只需要理解：transformer 常用于处理多模态信息，比如图像、语言和动作。

## LeRobot-style Data

机器人学习数据通常包含 observation、action 和 episode。

```text
observation: 机器人看到的画面或自身状态
action: 机器人执行的动作
episode: 一整段连续操作过程
```

在本项目中，可以对应成：

```text
observation: 当前小球图像
action: up / down / left / right
next_observation: 下一帧小球图像
episode: 一段小球运动轨迹
```


## Action Scale

Action scale 表示一个动作的幅度。
在本项目中，`step_size` 控制小球每次移动多少像素。
```text
step_size = 1: movement is small
step_size = 4: movement is easier to observe
动作太小：状态变化不明显
动作太大：容易不稳定或越界
```