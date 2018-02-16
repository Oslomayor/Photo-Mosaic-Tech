# Photo-Mosaic-Tech
制作马赛克图片，小图拼成大图

### 先上个示例图片，这是我在除夕那天做的

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/AB.png)

## 1. 食用目的

1. 把成百上千张图片，有序组合，淡化处理，拼成一张大图片的背景
2. 显得有技术有逼格，并且还有艺术感

## 2. 食用工具

### 1. Foto-Mosaic-Edda

- 这是一款制作马赛克图片的专用工具，选择系统合适版本[下载](http://www.fmedda.com/en/download) 
- 有专业版和普通版，普通版是免费的。专业版的排版效果多一些。

### 2. Python 3.6 && Pillow

- 图像处理，这里用到 Pyhton 3.6 环境和 Pillow 库。
- Foto-Mosaic-Edda 处理之后，就有马赛克的效果。它通过计算小图片的平均颜色，挑选出颜色匹配的小图片，来代替大图中的像素点。
- 透明的效果更好看，因此借用 Foto-Mosaic-Edda 获得马赛克图，再用Python 脚本进行透明融合处理。

## 3.食用步骤

### 1. 制作背景小图

- 选择一个包含成百上千张图片的文件夹，作为 Foto-Mosaic-Edda 的数据库
- 软件内部有向导，按照 Foto-Mosaic-Edda 的向导，选择一张纯白图片作为 theme 图片
- 选用之前生成的数据库，运行，制作完成背景小图  
  ![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/rawB.jpg)


### 2. 准备主题图片

- 选择一张图片，作为大图

  ![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/rawA.jpg)

- 用 PS 等图片处理工具，把**背景小图**和**主题大图**调整为**相同尺寸**

### 3. 运行 Python 脚本

- Python 3.6 ,  需要 Pillow 库
- 脚本代码 [在此](https://github.com/Oslomayor/Photo-Mosaic-Tech/blob/master/mergeAB.py)
- 注意图片的路径和图片名

## 4. 图片透明融合原理

- PNG 格式的图片，每个像素由4个通道的数据组成。
- 除了R,G,B, 还有1个A通道，即 Alpha 通道，控制不透明度。Alpha 为100代表不透明，Alpha为0代表完全透明，Alpha为 0 -100 则代表半透明。
- 用PNG方式读取图片，返回的数据类型是列表，每个像素对应一个列表元素，每个元素是一个存储R,G,B,A值的四元组。因此，只要把两张图片的像素乘比例因数，再相加得到一个新列表。以PNG图片的格式输出这个新列表即可。


