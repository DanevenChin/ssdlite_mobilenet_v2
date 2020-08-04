# 训练代码
python train.py \
--datasets ~/work/YOLOv3/datasets/VOC/VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007 ~/work/YOLOv3/datasets/VOC/VOCtrainval_11-May-2012/VOCdevkit/VOC2012 \
--validation_dataset ~/work/YOLOv3/datasets/VOC/VOCtest_06-Nov-2007/VOCdevkit/VOC2007 \
--net mb2-ssd-lite \
--base_net models/mb2-imagenet-71_8.pth  \
--scheduler cosine \
--lr 0.01 \
--t_max 200 \
--validation_epochs 5 \
--num_epochs 200

# 运行demo
python detection_demo.py \
mb2-ssd-lite \
saved_model/mb2-ssd-lite-Epoch-150-Loss-2.8759542611929088.pth \
models/voc-model-labels.txt \
/home/qindanfeng/work/YOLOv3/datasets/coco2014/val2014/COCO_val2014_000000000042.jpg

# 性能评估
python eval.py \
--net mb2-ssd-lite  \
--dataset ~/work/YOLOv3/datasets/VOC/VOCtest_06-Nov-2007/VOCdevkit/VOC2007 \
--trained_model saved_model/mb2-ssd-lite-Epoch-150-Loss-2.8759542611929088.pth \
--label_file models/voc-model-labels.txt


# 训练车辆检测模型，by20.08.04
python train.py \
--datasets /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--validation_dataset /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--net mb2-ssd-lite \
--base_net models/mb2-imagenet-71_8.pth  \
--scheduler cosine \
--lr 0.01 \
--t_max 200 \
--validation_epochs 5 \
--num_epochs 200