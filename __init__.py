import sys
import subprocess
import os
import importlib.util
import warnings

# 静音 numpy 2.0 的 deprecation 警告
warnings.filterwarnings('ignore', category=DeprecationWarning, module='numpy')

def check_and_install_dependencies():
    """检查并安装依赖，支持新版 numpy 和 opencv"""
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    requirements_path = os.path.join(current_dir, "requirements.txt")
    
    if not os.path.exists(requirements_path):
        return

    try:
        with open(requirements_path, 'r') as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        for req in requirements:
            # 解析包名（去掉版本限制，只安装包名）
            pkg_name = req.split('>=')[0].split('==')[0].split('<')[0].strip()
            
            # 特殊处理包名映射
            if pkg_name == "opencv-python":
                import_name = "cv2"
            elif pkg_name == "Pillow":
                import_name = "PIL"
            else:
                import_name = pkg_name
            
            # 检查是否已安装
            spec = importlib.util.find_spec(import_name)
            if spec is None:
                try:
                    print(f"[OpenPose] 安装依赖: {req}")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", req])
                    print(f"[OpenPose] {req} 安装成功")
                except Exception as e:
                    print(f"[OpenPose] 安装 {req} 失败: {e}")
            else:
                print(f"[OpenPose] 依赖已存在: {import_name}")
                
    except Exception as e:
        print(f"[OpenPose] 依赖检查失败: {e}")

# 执行依赖检查
check_and_install_dependencies()

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
import time

WEB_DIRECTORY = "./js"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']

# 添加时间戳强制刷新缓存
JS_FILE_TIMESTAMP = str(int(time.time()))