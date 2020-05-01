def myfunc_1(cmd):
    import re
    import random

    if re.match(r"roll\s*\d+d\d+", cmd):
        pattern = re.compile(r'\d+')
        num = pattern.findall(cmd)
        result = 0
        for _ in range(int(num[0])):
            result += random.randint(1, int(num[1]))
        print(f'点数{result}')    # 所以才说他写的屎 每一个函数都应该分离出来 await应该在主循环结构里
        return

if __name__ == '__main__':
    msg = 'roll2d20'
    msg1 = 'roll3d30'
    msg2 = 'rolld10'
    # 这样测试你的函数 各种情况都要确保正确
    # 每一个新功能都这样做
    for item in [msg,msg1,msg2]:
        myfunc_1(item)