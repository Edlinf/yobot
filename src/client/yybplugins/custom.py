'''
自定义功能：

在这里可以编写自定义的功能，
编写完毕后记得 git commit，
（只接收pcr相关功能，最好发到GitHub，我不怎么看Gitee）

这个模块只是为了快速编写小功能，如果想编写完整插件可以使用：
https://github.com/richardchien/python-aiocqhttp
或者
https://github.com/richardchien/nonebot
'''

import asyncio,re,random
from typing import Any, Dict, Union
# 代码都在src文件夹里 其他的文件夹可能对你有帮助 虽然我都是不看的
# 当一直read time out的时候 考虑挂个加速器
# 需要安装这些包
# file -> setting ->project:yobot -> project interpreter -> +号 搜索包名
# 这个方法可能会失败 多试几次
# 或者 D:\Python36\Scripts\pip.exe install ...
# 安装成功 这里的红色报错消失了 OHHHHHHHHHHHHHHHHHHH
from aiocqhttp.api import Api
# 其他的地方动手试一试叭
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from quart import Quart


class Custom:
    def __init__(self,
                 glo_setting: Dict[str, Any],
                 scheduler: AsyncIOScheduler,
                 app: Quart,
                 bot_api: Api,
                 *args, **kwargs):
        '''
        初始化，只在启动时执行一次

        参数：
            glo_setting 包含所有设置项，具体见default_config.json
            bot_api 是调用机器人API的接口，具体见<https://python-aiocqhttp.cqp.moe/>
            scheduler 是与机器人一同启动的AsyncIOScheduler实例
            app 是机器人后台Quart服务器实例
        '''
        # 注意：这个类加载时，asyncio事件循环尚未启动，且bot_api没有连接
        # 此时不要调用bot_api，如需初始化请使用api_init
        # 此时没有running_loop，不要直接使用await或asyncio.creat_task

        # 如果需要使用，请注释掉下面一行
        #return

        self.setting = glo_setting
        self.api = bot_api

        # # 注册定时任务，详见apscheduler文档
        # @scheduler.scheduled_job('cron', hour=8)
        # async def good_morning():
        #     await bot_api.send_group_msg(group_id=123456, message='早上好')

        # # 注册web路由，详见flask与quart文档
        # @app.route('/is-bot-running', methods=['GET'])
        # async def check_bot():
        #     return 'yes, bot is running'

    async def execute_async(self, ctx: Dict[str, Any]) -> Union[None, bool, str]:
        '''
        每次bot接收有效消息时触发

        参数ctx 具体格式见：https://cqhttp.cc/docs/#/Post
        '''

        # 如果需要使用，请注释掉下面一行
        #return

        cmd = ctx['raw_message']
        if cmd == '你好':

            # 调用api发送消息
            await self.api.send_private_msg(
                user_id=ctx['user_id'], message='收到问好')

            # 返回字符串：发送消息并阻止后续插件
            return '世界'
        if cmd == '我的测试':
            pass

        if re.match(r"roll\s*\d+d\d+",cmd):
            pattern = re.compile(r'\d+')
            num = pattern.findall(cmd)
            result = 0
            for _ in range(int(num[0])):
                result += random.randint(1, int(num[1]))
            await self.api.send_private_msg(
                user_id=ctx['user_id'], message=f'roll:{result}')
            return
        # 返回布尔值：是否阻止后续插件
        return False
