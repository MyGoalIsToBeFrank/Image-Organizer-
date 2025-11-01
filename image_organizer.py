#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片整理脚本
功能：
1. 检测当前目录及所有子目录中的图片文件
2. 生成目录结构报告并保存为txt文件
3. 按照修改日期重命名并复制所有图片到pics文件夹（保留原始文件）
"""

import os
import shutil
import time
from datetime import datetime
from pathlib import Path
import sys

# 支持的图片文件扩展名
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'}

def get_image_files(root_dir):
    """
    递归获取目录中所有图片文件
    返回：图片文件路径列表
    """
    image_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if Path(file).suffix.lower() in IMAGE_EXTENSIONS:
                image_files.append(os.path.join(root, file))
    return image_files

def generate_directory_structure(root_dir, output_file):
    """
    生成目录结构报告
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("图片目录结构报告\n")
        f.write("=" * 50 + "\n")
        f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"根目录: {os.path.abspath(root_dir)}\n\n")

        # 统计信息
        total_dirs = 0
        total_images = 0

        for root, dirs, files in os.walk(root_dir):
            level = root.replace(root_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            f.write(f"{indent}{os.path.basename(root)}/\n")

            total_dirs += 1

            subindent = ' ' * 2 * (level + 1)
            image_count = 0
            for file in files:
                if Path(file).suffix.lower() in IMAGE_EXTENSIONS:
                    f.write(f"{subindent}{file}\n")
                    image_count += 1
                    total_images += 1

            if image_count > 0:
                f.write(f"{subindent}({image_count} 张图片)\n")

        f.write("\n" + "=" * 50 + "\n")
        f.write(f"总文件夹数: {total_dirs}\n")
        f.write(f"总图片数: {total_images}\n")

def get_file_modification_date(file_path):
    """
    获取文件的修改日期
    返回：YYYYMMDD格式的日期字符串
    """
    timestamp = os.path.getmtime(file_path)
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime('%Y%m%d')

def organize_images(image_files, target_dir):
    """
    按照修改日期重命名并复制图片到目标文件夹（保留原始文件）
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 按日期分组图片
    date_groups = {}
    for img_path in image_files:
        date_str = get_file_modification_date(img_path)
        if date_str not in date_groups:
            date_groups[date_str] = []
        date_groups[date_str].append(img_path)

    # 为每组图片分配编号并重命名
    renamed_files = []
    for date_str, files in date_groups.items():
        # 按原文件名排序，确保重命名的一致性
        files.sort()

        for i, img_path in enumerate(files):
            # 生成新文件名：YYYYMMDD_XXX.ext
            ext = Path(img_path).suffix.lower()
            new_name = f"{date_str}_{i:03d}{ext}"
            new_path = os.path.join(target_dir, new_name)

            # 处理文件名冲突（虽然理论上不应该发生）
            counter = 1
            while os.path.exists(new_path):
                name_without_ext = f"{date_str}_{i:03d}_{counter}"
                new_name = f"{name_without_ext}{ext}"
                new_path = os.path.join(target_dir, new_name)
                counter += 1

            # 复制文件（保留原始文件以确保安全性）
            try:
                shutil.copy2(img_path, new_path)
                renamed_files.append((os.path.basename(img_path), new_name))
                print(f"已复制: {os.path.basename(img_path)} -> {new_name}")
            except Exception as e:
                print(f"复制失败 {img_path}: {e}")

    return renamed_files

def main():
    """
    主函数
    """
    current_dir = os.getcwd()

    print("图片整理脚本启动...")
    print(f"工作目录: {current_dir}")

    # 1. 检测图片文件
    print("\n1. 检测图片文件...")
    image_files = get_image_files(current_dir)
    print(f"找到 {len(image_files)} 张图片")

    if not image_files:
        print("未找到任何图片文件，程序退出。")
        return

    # 2. 生成目录结构报告
    print("\n2. 生成目录结构报告...")
    structure_file = "directory_structure.txt"
    generate_directory_structure(current_dir, structure_file)
    print(f"目录结构报告已保存到: {structure_file}")

    # 3. 整理图片
    print("\n3. 整理图片...")
    pics_dir = "pics"
    renamed_files = organize_images(image_files, pics_dir)

    print("\n整理完成！")
    print(f"共处理 {len(renamed_files)} 张图片")
    print(f"图片已复制到: {pics_dir} 文件夹（原始文件已保留）")

    # 生成重命名日志
    log_file = "rename_log.txt"
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write("图片重命名日志\n")
        f.write("=" * 50 + "\n")
        f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for old_name, new_name in renamed_files:
            f.write(f"{old_name} -> {new_name}\n")

    print(f"重命名日志已保存到: {log_file}")

if __name__ == "__main__":
    main()