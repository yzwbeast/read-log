# ReadLog  

[English README available here](README.md)

一个简单高效的读书记录程序，用于记录和管理您的阅读记录。

## 功能  
- 添加书籍时支持填写中文名和英文名。  
- 跟踪阅读进度（未读、正在阅读、已读）。  
- 自动记录开始和完成时间。  
- 支持按书名、作者或关键词搜索。  
- 使用方向键进行直观导航。  

## 安装  
1. 克隆此仓库：
    ```bash
    git clone https://github.com/yzwbeast/BookLog.git
    cd BookLog
    ```
2.	安装 Python 3.6 或更高版本。
3.	安装所需依赖：
    ```bash
    pip install keyboard readchar
    ```
4. 运行程序：
    ```bash
    python3 book.py
    ```
## 使用方法
1.	添加书籍：输入中文名、英文名、作者，程序会自动记录开始时间。
2.	查看记录：列出所有书籍，包括阅读状态和时间戳。
3.	更新状态：将书籍标记为“正在阅读”或“已读”，并自动记录完成时间。
4.	搜索：通过书名、作者或关键词进行搜索。

## 示例
添加书籍：
   ```bash
   请输入书的中文名: 小王子  
请输入书的英文名（如果没有可留空）: The Little Prince  
请输入作者: 安东尼·德·圣-埃克苏佩里  
   ```
查看记录：
   ```bash
   1. 中文名: 小王子  
   英文名: The Little Prince  
   作者: 安东尼·德·圣-埃克苏佩里, 状态: 未读  
   开始时间: 2024-12-23 10:00:00, 完成时间: 未完成  
   ```
## License
本项目基于 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。

[English README available here](README.md)