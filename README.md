# pairwise-gpu-skinning-morph

角色做表情时嘴角的 morph target 把口型覆盖掉，导出时顶点骨骼权重超过 4 个却没归一化，双四元数蒙皮在缩放骨骼下未重新正交化，关节处膨胀；morph 叠加按数组顺序执行，表情和口型互相清零；切线空间只变换了位置没变换切线，法线贴图方向随表情翻转；GPU 蒙皮缓冲每帧重建，异步 compute 写顶点与绘制之间没有 barrier；多相机分屏共用一份蒙皮结果，左右眼姿态差一帧；蒙皮在裁剪空间做，透视除法后再插值导致近处肢体扭曲；LOD 切换时 morph 权重没跟着插值，表情突然跳变；根运动被蒙皮矩阵重复应用，角色滑步；远距离骨骼矩阵浮点精度漂移，手指抖动。render/gpu_skinning_morph.py 是核心，tests/test_gpu_skinning_morph.py 15个红。要修的是：权重 Top4 归一；morph 按通道权重叠加；双四元数正交化；切线一起变换；蒙皮 compute 后插 barrier；多相机独立姿态；蒙皮在世界空间做；LOD 同步插值 morph；根运动单独剥离；骨骼矩阵局部化计算。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：见平台；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
