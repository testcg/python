name = "chengeng"
print(type(name))
# 字节串
name = b"chengeng"
print(name)
print(type(name))

# 变量或者包含非英文字符的字符串转换为字节串方法 ：str.encode()
s = "张三"
name = s.encode()
print(type(name))
print(name)
# 字节串转换为字符串方法 : bytes.decode()
print(name.decode())
