# ssdlite_mobilenet_v2

## 数据集读取

### 1) voc格式

只需要给出voc数据集的路径，且路径下的文件格式如下：

```
├─JPEGImages
├─Annotations
├─ImageSets
		└─Main
			├─trainval.txt
			└─test.txt
└─labels.txt
```

文件说明：

- JPEGImages保存图片

- Annotations保存标注文件，文件格式为xml

- trainval.txt和test.txt保存图片名，如图

![image-20200808162742174](C:\Users\DanevenChin\AppData\Roaming\Typora\typora-user-images\image-20200808162742174.png)

- 如果训练非官方voc数据集，则需要手动生成labels.txt，其中保存数据集的类别，如图

![image-20200808164320537](C:\Users\DanevenChin\AppData\Roaming\Typora\typora-user-images\image-20200808164320537.png)

## 默认设置

- 输入图片尺寸：300*300

- 输入图片归一化：均值127 方差128

- iou阈值：0.45

- SSD输出特征图size：[19, 10, 5, 3, 2, 1]

- SSD对应的尺度大小：[(60, 105), (105, 150), (150, 195), (195, 240), (240, 285), (285, 330)]

- 坐标编码：x_scale=y_scale=10  w_scale=h_scale=5

- 纵横比：[[2], [2, 3], [2, 3], [2, 3], [2], [2]]

- 数据预处理：随机亮度、
  					   随机对比度、
  					   随机饱和度、
  					   随机色彩、
  					   随机亮度噪声、
  					   随机图片扩展、
  					   随机裁剪、 
  					   随机镜像

- batch_size：128

- 优化器：SGD

- scheduler：余弦退火，t_max=50

- 学习率：0.01

- momentum：0.9

- weight_decay：5e-4

- epoch：100

- 损失函数：分类loss使用log_softmax+cross_entropy

  ​				   定位loss使用smooth_l1

- 难例挖掘：选择分类loss大到小前3倍正样本数量的负样本参与到反向梯度中。

