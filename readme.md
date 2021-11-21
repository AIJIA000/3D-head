# 					3D-head-reconstruct

## Getting Started

Clone the repo:

```
git https://github.com/tootoolscn/tootools-3D-face.git
```

### Requirements

* Python 3.7 (numpy, skimage, scipy, opencv)  

* PyTorch >= 1.6 (pytorch3d)  

* face-alignment (Optional for detecting face)

  You can run

  ```
  conda create -n 3d-head python==3.7
  source/conda activate 3d-head
  pip install -r requirements.txt
  pip install pytorch==0.6.0
  ```
  
  For visualization, we use our rasterizer that uses pytorch JIT Compiling Extensions. If there occurs a compiling error, you can install [pytorch3d](https://github.com/facebookresearch/pytorch3d/blob/master/INSTALL.md) instead and set --rasterizer_type=pytorch3d when running the demos.

### Usage

​		Prepare profile:

								链接: https://pan.baidu.com/s/1MhD20EG_zMEEHbBCuaMypg  密码: 6rmg

```
cd tmp_data
mv/cp * ../data
```

​		reconstruction

```
python demos/demo_reconstruct.py
```

​		The file will save in the saveFlie. 