from asyncio import sleep

import asyncio

from developTools.event.events import GroupMessageEvent
from plugins.core.llmDB import delete_user_history, clear_all_history
from plugins.core.userDB import add_user, get_user, record_sign_in, update_user
async def call_user_data_register(bot,event,config):
    data = await bot.get_group_member_info(group_id=event.group_id, user_id=event.user_id)
    r = await add_user(
        data["data"]["user_id"],
        data["data"]["nickname"],
        data["data"]["card"],
        data["data"]["sex"],
        data["data"]["age"],
        data["data"]["area"])
    await bot.send(event, r)
async def call_user_data_query(bot,event,config):
    r = await get_user(event.user_id, event.sender.nickname)
    await bot.send(event, str(r))
async def call_user_data_sign(bot,event,config):
    r = await record_sign_in(event.user_id)
    await bot.send(event, r)
async def call_change_city(bot,event,config,city):
    user_info = await get_user(event.user_id, event.sender.nickname)
    if user_info[6]>=config.controller["user_data"]["change_info_operate_level"]:
        r = await update_user(event.user_id, city=city)
        await bot.send(event, r)
    else:
        await bot.send(event,"权限好像不够呢.....")
async def call_change_name(bot,event,config,name):
    user_info = await get_user(event.user_id, event.sender.nickname)
    if user_info[6]>=config.controller["user_data"]["change_info_operate_level"]:
        await update_user(event.user_id, nickname=name)
        await bot.send(event, f"已将你的昵称改为{name}")
    else:
        await bot.send(event,"权限好像不够呢.....")
async def call_permit(bot,event,config,target_qq,level):
    user_info = await get_user(event.user_id, event.sender.nickname)
    if user_info[6] >= config.controller["user_data"]["permit_user_operate_level"]:
        await update_user(user_id=target_qq, permission=level)
        await bot.send(event, f"已将{target_qq}的权限设置为{level}")
    else:
        await bot.send(event,"权限不足以进行此操作。")
async def call_delete_user_history(bot,event,config):
    await delete_user_history(event.user_id)
    await bot.send(event, "已清理对话记录")
async def call_clear_all_history(bot,event,config):
    if event.user_id==config.basic_config["master"]["id"]:
        await clear_all_history()
        await bot.send(event, "已清理所有用户的对话记录")
    else:
        await bot.send(event, "你不是master，没有权限进行此操作。")


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
    master_id = config.basic_config["master"]["id"]
    master_name = config.basic_config["master"]["name"]
    asyncio.run(add_user(master_id, master_name, master_name))
    asyncio.run(update_user(master_id, permission=9999, nickname=master_name))
    if master_id not in config.censor_user["whitelist"]:
        config.censor_user["whitelist"].append(master_id)
        config.save_yaml(str("censor_user"))
    @bot.on(GroupMessageEvent)
    async def handle_group_message(event):
        await sleep(1) #让auto_register指令优先执行
        try:
            user_info=await get_user(event.user_id,event.sender.nickname)
        except Exception as e:
            bot.logger.error(f"Error in creating users!: {e}")
            return
        #print(user_info)
        if event.raw_message == "注册":
            await call_user_data_register(bot,event,config)
        elif event.raw_message =="我的信息":
            await call_user_data_query(bot,event,config)
        elif event.raw_message == "签到":
            await call_user_data_sign(bot,event,config)
        elif event.raw_message.startswith("修改城市"):
            city=event.raw_message.split("修改城市")[1]
            await call_change_city(bot,event,config,city)
        elif event.raw_message.startswith("叫我") and user_info[6]>=config.controller["user_data"]["change_info_operate_level"]:
            nickname=event.raw_message.split("叫我")[1]
            await call_change_name(bot,event,config,nickname)

        if event.raw_message.startswith("授权#"):
            try:
                permission=int(event.raw_message.split("#")[2])
                target_qq=int(event.raw_message.split("#")[1])
                await call_permit(bot,event,config,target_qq,permission)
            except:
                await bot.send(event, "请输入正确的权限值。\n指令为\n授权#{target_qq}#{level}\n如授权#1223434343#1")

