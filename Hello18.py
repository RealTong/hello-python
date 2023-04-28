# IO 流

try:
    f = open ("C:/Users/RealTong/Desktop/wg0.conf",'r')
    # 一个字节一个字节读取文件内容
finally:
    if f:
        f.close()
