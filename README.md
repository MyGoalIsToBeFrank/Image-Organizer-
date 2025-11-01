# Image Organizer
（For English version, please scroll down）

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

一个强大的图片整理工具，可以自动检测、分析和整理目录中的所有图片文件。

## 功能特性

- 🔍 **智能图片检测**：递归扫描目录及子目录，支持多种图片格式
- 📊 **目录结构分析**：生成详细的目录结构报告
- 📅 **按日期整理**：根据文件修改日期自动重命名和整理图片
- 🛡️ **安全复制**：保留原始文件，只复制到整理目录
- 📝 **详细日志**：记录所有操作和重命名信息
- 🚀 **一键运行**：提供批处理脚本，支持管理员权限

## 支持的图片格式

- JPG/JPEG
- PNG
- GIF
- BMP
- TIFF
- WebP
- SVG

## 快速开始

### 环境要求

- Python 3.6+
- Windows 操作系统

### 安装步骤

1. 克隆或下载项目文件到本地目录
2. 确保Python已安装并在PATH中

### 使用方法

#### 方法一：使用批处理脚本（推荐）

双击运行 `run_image_organizer.bat`，脚本会自动请求管理员权限并执行整理操作。

#### 方法二：直接运行Python脚本

```bash
python image_organizer.py
```

## 输出文件

脚本运行后会在当前目录生成以下文件：

- `directory_structure.txt` - 目录结构分析报告
- `rename_log.txt` - 图片重命名详细日志
- `pics/` - 整理后的图片文件夹

## 整理规则

图片会按照修改日期重命名，格式为：`YYYYMMDD_XXX.ext`

- `YYYYMMDD`：文件修改日期
- `XXX`：三位数字编号（000-999）
- `ext`：原始文件扩展名

## 示例输出

```
20240821_000.jpg
20240821_001.jpg
20240822_000.png
20240822_001.png
20240822_002.png
```

## 安全特性

- ✅ **保留原始文件**：使用复制而非移动，确保数据安全
- ✅ **元数据完整**：保留文件的所有元数据信息
- ✅ **错误处理**：完善的异常处理机制
- ✅ **日志记录**：详细的操作日志便于追踪

## 项目结构

```
Image Organizer/
├── image_organizer.py      # 主程序文件
├── run_image_organizer.bat # Windows批处理启动器
├── README.md               # 项目说明文档
└── pics/                   # 整理后的图片目录（运行后生成）
```

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 贡献

欢迎提交 Issue 和 Pull Request！

---

# Image Organizer

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A powerful image organization tool that automatically detects, analyzes, and organizes all image files in a directory.

## Features

- 🔍 **Smart Image Detection**: Recursively scans directories and subdirectories, supports multiple image formats
- 📊 **Directory Structure Analysis**: Generates detailed directory structure reports
- 📅 **Date-based Organization**: Automatically renames and organizes images based on file modification dates
- 🛡️ **Safe Copy**: Preserves original files, only copies to organized directory
- 📝 **Detailed Logging**: Records all operations and renaming information
- 🚀 **One-click Execution**: Provides batch scripts with administrator privilege support

## Supported Image Formats

- JPG/JPEG
- PNG
- GIF
- BMP
- TIFF
- WebP
- SVG

## Quick Start

### System Requirements

- Python 3.6+
- Windows Operating System

### Installation

1. Clone or download project files to local directory
2. Ensure Python is installed and in PATH

### Usage

#### Method 1: Using Batch Script (Recommended)

Double-click `run_image_organizer.bat`, the script will automatically request administrator privileges and execute the organization process.

#### Method 2: Run Python Script Directly

```bash
python image_organizer.py
```

## Output Files

After running, the script will generate the following files in the current directory:

- `directory_structure.txt` - Directory structure analysis report
- `rename_log.txt` - Detailed image renaming log
- `pics/` - Organized images folder

## Organization Rules

Images are renamed according to modification date with format: `YYYYMMDD_XXX.ext`

- `YYYYMMDD`: File modification date
- `XXX`: Three-digit number (000-999)
- `ext`: Original file extension

## Example Output

```
20240821_000.jpg
20240821_001.jpg
20240822_000.png
20240822_001.png
20240822_002.png
```

## Safety Features

- ✅ **Preserves Original Files**: Uses copy instead of move to ensure data safety
- ✅ **Complete Metadata**: Preserves all file metadata
- ✅ **Error Handling**: Comprehensive exception handling
- ✅ **Logging**: Detailed operation logs for tracking

## Project Structure

```
Image Organizer/
├── image_organizer.py      # Main program file
├── run_image_organizer.bat # Windows batch launcher
├── README.md               # Project documentation
└── pics/                   # Organized images directory (generated after run)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Issues and Pull Requests are welcome!
