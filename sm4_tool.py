# sm4_tool.py
# 24级计科读书实践周 - Git版本管理示例代码

class SM4Context:
    def __init__(self):
        self.sk = [0] * 32
        self.mode = 1  # 1 为加密

def sm4_set_key(key):
    """
    模拟设置SM4密钥逻辑
    """
    print(f"密钥已设置: {key.hex() if isinstance(key, bytes) else key}")
    return [0] * 32  # 简化演示

def sm4_one_round(sk, input_data):
    """
    模拟SM4单轮加密变换
    """
    # 实际开发中这里会包含复杂的异或和线性变换
    return input_data[::-1] 

def main():
    print("=== SM4 加密工具本地测试 ===")
    key = b"1234567812345678"
    data = "HelloGit"
    
    # 模拟加密过程
    sm4_set_key(key)
    result = sm4_one_round(None, data)
    
    print(f"原始数据: {data}")
    print(f"加密结果: {result}")

if __name__ == "__main__":
    main()