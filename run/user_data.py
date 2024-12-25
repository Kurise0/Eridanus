from asyncio import sleep

from developTools.event.events import GroupMessageEvent
from plugins.core.userDB import add_user, get_user, record_sign_in, update_user


def main(bot,config):
    """
    数据库提供指令
    注册 #开了auto_register后，发言的用户会被自动注册
    我的信息 #查看自己的信息
    签到 #签到
    修改城市{city} #修改自己的城市
    叫我{nickname} #修改自己的昵称
    授权#{target_qq}#{level} #授权某人相应权限，为高等级权限专有指令
    """
    bot.logger.info("user_data plugin loaded")
    @bot.on(GroupMessageEvent)
    async def handle_group_message(event):
        await sleep(1) #让auto_register指令优先执行
        user_info=await get_user(event.user_id,event.sender.nickname)
        #print(user_info)
        if event.raw_message == "注册":
            data=await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id)
            r=await add_user(
                data["data"]["user_id"],
                data["data"]["nickname"],
                data["data"]["card"],
                data["data"]["sex"],
                data["data"]["age"],
                data["data"]["area"])
            await bot.send(event, r)
        elif event.raw_message =="我的信息":
            r=await get_user(event.user_id,event.sender.nickname)
            await bot.send(event, str(r))
        elif event.raw_message == "签到":
            r=await record_sign_in(event.user_id)
            await bot.send(event, r)
        elif event.raw_message.startswith("修改城市") and user_info[6]>config.controller["user_database"]["change_info_operate_level"]:
            city=event.raw_message.split("修改城市")[1]
            r=await update_user(event.user_id,city=city)
            await bot.send(event, r)
        elif event.raw_message.startswith("叫我") and user_info[6]>config.controller["user_database"]["change_info_operate_level"]:
            nickname=event.raw_message.split("叫我")[1]
            await update_user(event.user_id,nickname=nickname)
            await bot.send(event, f"已将你的昵称改为{nickname}")
        if user_info[6]>config.controller["user_database"]["permit_user_operate_level"]:
            if event.raw_message.startswith("授权#"):
                try:
                    permission=int(event.raw_message.split("#")[2])
                    target_qq=int(event.raw_message.split("#")[1])
                    await update_user(user_id=target_qq,permission=permission)
                    await bot.send(event, f"已将{target_qq}的权限设置为{permission}")
                except:
                    await bot.send(event, "请输入正确的权限值。\n指令为\n授权#{target_qq}#{level}\n如授权#1223434343#1")
    @bot.on(GroupMessageEvent)
    async def handle_group_message(event):
        if config.controller["user_database"]["auto_register"]:
            data = await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id)
            await add_user(
                data["data"]["user_id"],
                data["data"]["nickname"],
                data["data"]["card"],
                data["data"]["sex"],
                data["data"]["age"],
                data["data"]["area"])
            #await bot.send(event, r)