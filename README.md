# ReadLog  

[中文版本 README available here](README.zh.md)

A simple and efficient book tracking program to log and manage your reading records.  

## Features  
- Add books with Chinese and English titles.  
- Track reading progress (Not Started, Reading, Finished).  
- Automatically record start and finish times.  
- Search books by title, author, or keywords.  
- Intuitive navigation using arrow keys.  

## Installation  
1. Clone this repository:  
    ```bash
    git clone https://github.com/yzwbeast/BookLog.git
    cd BookLog
    ```
2.	Install Python 3.6 or above.
3.	Install required dependencies:
    ```bash
    pip install keyboard readchar
    ```
## Usage
1.	Add a Book: Input the Chinese and English titles, author, and the program will record the start time.
2.	View Records: List all books, including their reading status and timestamps.
3.	Update Status: Mark a book as “Reading” or “Finished,” automatically logging the completion time.
4.	Search: Search by title, author, or keywords.

## Example
Adding a Book:
   ```bash
   请输入书的中文名: 小王子  
请输入书的英文名（如果没有可留空）: The Little Prince  
请输入作者: 安东尼·德·圣-埃克苏佩里  
   ```
Viewing Records:
   ```bash
   1. 中文名: 小王子  
   英文名: The Little Prince  
   作者: 安东尼·德·圣-埃克苏佩里, 状态: 未读  
   开始时间: 2024-12-23 10:00:00, 完成时间: 未完成  
   ```
## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

[中文版本 README available here](README.zh.md)
