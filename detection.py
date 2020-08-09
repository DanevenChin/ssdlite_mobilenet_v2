# -*- coding: utf-8 -*-
"""
@author  : 秦丹峰
@contact : daneven.jim@gmail.com
@time    : 2020/8/5 21:50
@file    : detection.py
@desc    : 
"""
# -*- coding: utf-8 -*-
"""
@author  : 秦丹峰
@contact : daneven.jim@gmail.com
@license : (C) Copyright, 广州海格星航信息科技有限公司
@time    : 2020/8/4 22:52
@file    : detection_demo.py
@desc    : 运行demo
"""
from net.mobilenet_v2_ssd_lite import create_mobilenetv2_ssd_lite, create_mobilenetv2_ssd_lite_predictor
from utils.misc import Timer
from utils.box_utils import plot_one_box
import cv2
import os
import sys

class predict(object):
    def __init__(self, net_type, model_path, label_path):
        super(predict, self).__init__()

        self.class_names = [name.strip() for name in open(label_path).readlines()]
        net = create_mobilenetv2_ssd_lite(len(self.class_names), is_test=True)
        net.load(model_path)
        self.predictor = create_mobilenetv2_ssd_lite_predictor(net, candidate_size=200, device="cuda:0")
        print("[INFO] 模型加载成功!")

    def __call__(self, orig_image, is_draw=False, img_name=None, save_path=None, is_show=False):
        image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
        boxes, labels, probs = self.predictor.predict(image, 10, 0.4)

        if is_draw:
            for i in range(boxes.size(0)):
                box = boxes[i, :]
                label = f"{self.class_names[labels[i]]}: {probs[i]:.2f}"
                plot_one_box(box, orig_image, (0,0,255),label,is_show)
        if save_path is not None:
            save_path = save_path + '/' + img_name
            cv2.imwrite(save_path, orig_image)
        print(f"Found {len(probs)} objects. The output image is {save_path}")

        return orig_image, boxes, labels, probs

def inference_img():
    net_type = "mb2-ssd-lite"
    model_path = "saved_model/mb2-ssd-lite-Epoch-10-Loss-1.9788172841072083.pth"
    label_path = "saved_model/voc-model-labels.txt"
    predictor = predict(net_type, model_path, label_path)

    image_path = "/home/qindanfeng/work/deep_learning/datasets/vehicle_datasets/ImageSets/Main/test.txt"
    root = "/home/qindanfeng/work/deep_learning/datasets/vehicle_datasets/JPEGImages"
    save_path = "saved_model/img_result"

    with open(image_path)as f:
        img_list = f.read().splitlines()

    for img in img_list:
        img_path = root + '/' + img + '.jpg'
        img_name = img + '.jpg'
        img = cv2.imread(img_path)
        predictor(img, True, img_name, save_path)


def inference_video(video_path, out_file):
    net_type = "mb2-ssd-lite"
    model_path = "saved_model/mb2-ssd-lite-Epoch-35-Loss-2.0251203179359436.pth"
    label_path = "saved_model/voc-model-labels.txt"
    predictor = predict(net_type, model_path, label_path)

    cap = cv2.VideoCapture(video_path)
    FrameNumber = cap.get(7)  # 视频文件的帧数
    vid_writer = cv2.VideoWriter(out_file, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30,
                                 (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                  int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    frame_interval = 1
    count = 1

    while True:
        print("{} | {}".format(count, FrameNumber))
        ret, frame = cap.read()
        if ret:
            h, w, c = frame.shape
        else:
            print("Done processing of %s" % video_path.split('/')[-1])
            print("Output file is stored as %s" % out_file)
            break
        if count % frame_interval == 0:
            frame, _, _, _ = predictor(frame, True)

        vid_writer.write(frame)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_path = "/home/qindanfeng/work/deep_learning/datasets/vehicle_test_video"
    out_file = "saved_model/video_result"
    video_list = os.listdir(video_path)
    for video_name in video_list:
        path = video_path+'/'+video_name
        save_path = out_file+'/result_'+video_name
        print("推断视频:", path)
        inference_video(path, save_path)
