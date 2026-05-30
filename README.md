# Toy World Model Lab

这是一个面向初学者的研究入门项目，用来学习 world model、VLA、novel view synthesis 以及基础的科研项目流程。

This project is designed for a CPU-only laptop. The goal is to understand the research workflow and model pipeline, not to train a large model.

## Goal

构建一个小型 toy world model，让模型根据当前小球画面和动作，预测下一帧画面。

```text
current observation + action -> next observation
```

## Learning Topics

- PyTorch training pipeline
- Basic image generation
- World model
- VLA
- Novel view synthesis
- LeRobot-style data format
- Git/GitHub workflow
- Research notes and weekly reports

## Project Structure

```text
toy-world-model-lab/
├── README.md
├── requirements.txt
├── .gitignore
├── configs/
├── data/
├── docs/
├── notebooks/
├── src/
├── experiments/
└── outputs/
```

## Current Progress

- [x] Project structure
- [ ] Environment setup
- [ ] AutoEncoder reconstruction demo
- [ ] Ball dataset
- [ ] Toy world model
- [ ] Simple VLA extension
- [ ] Simple novel view extension
