import os
import subprocess
import requests

data = [
    {
        "url": "https://huggingface.co/TMElyralab/MusePose/resolve/main/MusePose/denoising_unet.pth",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/MusePose"
    }, {
        "url": "https://huggingface.co/TMElyralab/MusePose/resolve/main/MusePose/motion_module.pth",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/MusePose"
    }, {
        "url": "https://huggingface.co/TMElyralab/MusePose/resolve/main/MusePose/pose_guider.pth",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/MusePose"
    }, {
        "url": "https://huggingface.co/TMElyralab/MusePose/resolve/main/MusePose/reference_unet.pth",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/MusePose"
    }, {
        "url": "https://huggingface.co/lambdalabs/sd-image-variations-diffusers/resolve/main/unet/diffusion_pytorch_model.bin",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/sd-image-variations-diffusers/unet"
    }, {
        "url": "https://huggingface.co/lambdalabs/sd-image-variations-diffusers/resolve/main/unet/config.json",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/sd-image-variations-diffusers/unet"
    }, {
        "url": "https://huggingface.co/stabilityai/sd-vae-ft-mse/resolve/main/diffusion_pytorch_model.bin",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/sd-vae-ft-mse"
    }, {
        "url": "https://huggingface.co/stabilityai/sd-vae-ft-mse/resolve/main/config.json",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/sd-vae-ft-mse"
    }, {
        "url": "https://huggingface.co/yzd-v/DWPose/resolve/main/dw-ll_ucoco_384.pth",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/dwpose"
    }, {
        "url": "https://download.openmmlab.com/mmdetection/v2.0/yolox/yolox_l_8x8_300e_coco/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/dwpose"
    }, {
        "url": "https://huggingface.co/lambdalabs/sd-image-variations-diffusers/resolve/main/image_encoder/pytorch_model.bin",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/image_encoder"
    }, {
        "url": "https://huggingface.co/lambdalabs/sd-image-variations-diffusers/resolve/main/image_encoder/config.json",
        "path": "custom_nodes/Comfyui-MusePose/pretrained_weights/image_encoder"
    }, {
        "url": "https://huggingface.co/datasets/Gourieff/ReActor/resolve/main/models/detection/bbox/face_yolov8m.pt",
        "path": "models/ultralytics/bbox" 
    }, {
        "url": "https://huggingface.co/datasets/Gourieff/ReActor/blob/main/models/sams/sam_vit_b_01ec64.pth",
        "path": "models/sams" 
    }
]

clone_projects = [
    "https://github.com/Gourieff/comfyui-reactor-node.git",
    "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git",
    "https://github.com/TemryL/ComfyS3.git"
]

# 下载文件并保存到指定路径
for item in data:
    url = item['url']
    path = item['path']
    
    # 创建目录
    os.makedirs(path, exist_ok=True)
    
    # 确定文件名
    filename = os.path.basename(url)
    
    # 特殊情况重命名文件
    if url == "https://download.openmmlab.com/mmdetection/v2.0/yolox/yolox_l_8x8_300e_coco/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth":
        filename = "yolox_l_8x8_300e_coco.pth"
    
    # 完整文件路径
    filepath = os.path.join(path, filename)
    
    # 下载文件
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename} to {filepath}")
    else:
        print(f"Failed to download {url}")
    

# 克隆项目
for url in clone_projects:
    # 完整路径
    path = os.path.join("custom_nodes", os.path.basename(url).replace(".git", ""))

    # 克隆项目
    subprocess.run(["git", "clone", url, path])
