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
saved_model/mb2-ssd-lite-Epoch-15-Loss-2.1904499530792236.pth \
saved_model/voc-model-labels.txt \
/home/qindanfeng/work/deep_learning/datasets/vehicle_datasets/JPEGImages/0000f77c-6257be58.jpg

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

# resume
python train.py \
--datasets /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--validation_dataset /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--net mb2-ssd-lite \
--resume saved_model/mb2-ssd-lite-Epoch-35-Loss-2.0251203179359436.pth  \
--scheduler cosine \
--lr 0.01 \
--t_max 200 \
--validation_epochs 5 \
--num_epochs 200

# 性能测试
python eval.py \
--net mb2-ssd-lite  \
--dataset /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--trained_model saved_model/mb2-ssd-lite-Epoch-30-Loss-2.0793707370758057.pth \
--label_file saved_model/voc-model-labels.txt

----------- 0808代码优化，新的训练脚本如下 ----------------
python train.py \
--datasets /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--validation_dataset /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--net_name mb2_ssd_lite \
--base_net models/mb2-imagenet-71_8.pth  \
--scheduler cosine \
--lr 0.01 \
--t_max 100 \
--validation_epochs 5 \
--num_epochs 100

# resume
python train.py \
--datasets /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--validation_dataset /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--net mb2-ssd-lite \
--resume saved_model/mb2_ssd_lite/last.pth  \
--scheduler cosine \
--lr 0.01 \
--t_max 100 \
--validation_epochs 5 \
--num_epochs 100

# 性能测试
python eval.py \
--dataset /home/qindanfeng/work/deep_learning/datasets/vehicle_datasets \
--trained_model saved_model/mb2_ssd_lite/best.pth \
--label_file saved_model/voc-model-labels.txt