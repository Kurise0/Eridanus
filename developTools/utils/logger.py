import logging
import os
from datetime import datetime
import colorlog

# 全局变量，用于存储 logger 实例
_logger = None

def createLogger():
    global _logger

    # 确保日志文件夹存在
    log_folder = "log"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # 创建一个 logger 对象
    logger = logging.getLogger("Eridanus")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # 防止重复日志

    # 设置控制台日志格式和颜色
    console_handler = logging.StreamHandler()
    console_format = '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    console_colors = {
        'DEBUG':    'white',
        'INFO':     'cyan',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    }
    console_formatter = colorlog.ColoredFormatter(console_format, log_colors=console_colors)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # --- 增加颜色区分消息和功能 ---
    console_format_msg = '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - [MSG] %(message)s'
    console_format_func = '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - [FUNC] %(message)s'
    console_colors_msg = {
        'DEBUG':    'white',
        'INFO':     'green',  # 服务器接收的消息用绿色
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    }
    console_colors_func = {
        'DEBUG':    'white',
        'INFO':     'blue',  # 功能信息用蓝色
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    }
    console_formatter_msg = colorlog.ColoredFormatter(console_format_msg, log_colors=console_colors_msg)
    console_formatter_func = colorlog.ColoredFormatter(console_format_func, log_colors=console_colors_func)
    # --- 结束颜色区分 ---

    # 设置文件日志格式
    file_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    file_formatter = logging.Formatter(file_format)

    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file_path = os.path.join(log_folder, f"{current_date}.log")

    # 创建文件处理器
    file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # 定义一个函数来更新日志文件（按日期切换）
    def update_log_file():
        nonlocal log_file_path, file_handler
        new_date = datetime.now().strftime("%Y-%m-%d")
        new_log_file_path = os.path.join(log_folder, f"{new_date}.log")
        if new_log_file_path != log_file_path:
            logger.removeHandler(file_handler)
            file_handler.close()
            log_file_path = new_log_file_path
            file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

    # 在 logger 上绑定更新日志文件的函数
    logger.update_log_file = update_log_file

    # --- 添加区分消息和功能的函数 ---
    def info_msg(self, message, *args, **kwargs):
        if self.isEnabledFor(logging.INFO):
            console_handler.setFormatter(console_formatter_msg)  # 设置消息格式
            self._log(logging.INFO, message, args, **kwargs)
            console_handler.setFormatter(console_formatter)  # 恢复默认格式

    def info_func(self, message, *args, **kwargs):
        if self.isEnabledFor(logging.INFO):
            console_handler.setFormatter(console_formatter_func)  # 设置功能格式
            self._log(logging.INFO, message, args, **kwargs)
            console_handler.setFormatter(console_formatter)  # 恢复默认格式

    # 将新函数绑定到 logger 类
    logging.Logger.info_msg = info_msg
    logging.Logger.info_func = info_func
    # --- 结束添加区分消息和功能的函数 ---

    _logger = logger

def get_logger():
    global _logger
    if _logger is None:
        createLogger()
    # 每次获取 logger 时检查是否需要更新日志文件
    _logger.update_log_file()
    return _logger

# 使用示例
if __name__ == "__main__":
    logger = get_logger()
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
    logger.info_msg("This is a server message.")
    logger.info_func("This is a function info.")

    logger2 = get_logger()
    print(f"logger == logger2: {logger == logger2}")