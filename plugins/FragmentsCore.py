import datetime
import json
import os
import random
from io import BytesIO

import httpx
import yaml
from PIL import Image
from emoji import is_emoji

from plugins.tookits import get_headers, random_str


async def news():
    url = "https://api.52vmy.cn/api/wl/60s"
    time = datetime.datetime.now().strftime('%Y_%m_%d')
    #path="./news.png"
    path = "data/pictures/cache/" + time + "news.png"

    #r=requests.get(url).content
    #with open("./news.png","wb") as fp:
    #fp.write(r)
    #return
    #async with httpx.AsyncClient(timeout=20) as client:
    #r = await client.get(url)
    #url=r.json().get("tp1")
    #print(url)
    #return url
    #print(r.json().get("data").get("image")) # 从二进制数据创建图片对象
    async with httpx.AsyncClient(timeout=200, headers=get_headers()) as client:
        r = await client.get(url)
        img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
        img.save(path)  # 使用PIL库保存图片
        #print(path)
        return path


async def chaijun():
    headers = get_headers()
    url = "http://api.yujn.cn/api/chaijun.php?"
    path = "data/pictures/cache/" + random_str() + ".png"
    async with httpx.AsyncClient(timeout=20, headers=headers) as client:
        r = await client.get(url)
        img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
        img.save(path)  # 使用PIL库保存图片
        # print(path)
        return path


async def beCrazy(aim):
    headers = get_headers()
    url = f"https://api.lolimi.cn/API/fabing/fb.php?name={aim}"
    async with httpx.AsyncClient(timeout=20, headers=headers) as client:
        r = await client.get(url)
        r = r.json().get("data")
        # print(path)
        return r


async def danxianglii():
    headers = get_headers()
    time = datetime.datetime.now().strftime('%Y/%m%d')
    url = f"https://img.owspace.com/Public/uploads/Download/{time}.jpg"
    path = "data/pictures/cache/" + random_str() + ".png"
    async with httpx.AsyncClient(timeout=20, headers=headers) as client:
        r = await client.get(url)
        img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
        img.save(path)  # 使用PIL库保存图片
        # print(path)
        return path


async def moyu():
    headers = get_headers()
    url = "https://api.52vmy.cn/api/wl/moyu"
    time = datetime.datetime.now().strftime('%Y_%m_%d')
    path = "data/pictures/cache/" + time + "moyu.png"
    #path="moyu.png"

    async with httpx.AsyncClient(timeout=30, headers=headers) as client:
        r = await client.get(url)
        img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
        img.save(path)  # 使用PIL库保存图片
        #print(path)
        return path


async def xingzuo():
    url = "https://dayu.qqsuu.cn/xingzuoyunshi/apis.php"
    time = datetime.datetime.now().strftime('%Y_%m_%d')
    # path="./news.png"
    path = "data/pictures/cache/" + time + "xingzuo.png"
    #path="./xingzuo.png"
    # print(r.json().get("data").get("image")) # 从二进制数据创建图片对象
    async with httpx.AsyncClient(timeout=200, headers=get_headers()) as client:
        r = await client.get(url)
        img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
        img.save(path)  # 使用PIL库保存图片
        #rint(path)
        return path


async def nong(url, name):
    # path="./news.png"
    path = "data/Elo/" + name + ".png"
    # path="./xingzuo.png"
    if os.path.exists(path):
        return path
    else:

        # print(r.json().get("data").get("image")) # 从二进制数据创建图片对象
        async with httpx.AsyncClient(timeout=200, headers=get_headers()) as client:
            r = await client.get(url)
            img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
            img.save(path)  # 使用PIL库保存图片
            # rint(path)
            return path


async def sd(url, path):
    # path="./news.png"

    # path="./xingzuo.png"
    # print(r.json().get("data").get("image")) # 从二进制数据创建图片对象

    async with httpx.AsyncClient(timeout=200, headers=get_headers()) as client:
        r = await client.get(url)
        img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
        img.save(path)  # 使用PIL库保存图片
        # rint(path)
        return path


async def handwrite(msg):
    url = f"https://zj.v.api.aa1.cn/api/zuoye/?msg={msg}"
    path = "data/pictures/cache/" + random_str() + ".png"
    async with httpx.AsyncClient(timeout=200, headers=get_headers()) as client:
        r = await client.get(url)
        img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
        img.save(path)  # 使用PIL库保存图片
        # rint(path)
        return path
ark = {
    "方舟种族": [
        "阿达克利斯", "阿达克利斯", "阿达克利斯", "阿达克利斯", "阿戈尔", "阿戈尔", "阿戈尔", "阿戈尔", "阿纳萨",
        "阿纳萨", "阿纳萨", "阿纳缇", "阿纳缇", "阿斯兰", "阿斯兰", "埃拉菲亚", "埃拉菲亚", "埃拉菲亚", "埃拉菲亚",
        "安努拉", "安努拉", "德拉克", "德拉克", "杜林", "杜林", "杜林", "杜林", "菲林", "菲林", "菲林", "菲林", "菲林",
        "菲林", "斐迪亚", "斐迪亚", "斐迪亚", "斐迪亚", "丰蹄", "丰蹄", "丰蹄", "丰蹄", "丰蹄", "鬼", "鬼", "鬼", "鬼",
        "鬼", "精灵", "卡普里尼", "卡普里尼", "卡普里尼", "卡普里尼", "卡普里尼", "卡特斯", "卡特斯", "卡特斯",
        "卡特斯", "卡特斯", "库兰塔", "库兰塔", "库兰塔", "库兰塔", "库兰塔", "黎博利", "黎博利", "黎博利", "黎博利",
        "黎博利", "黎博利", "龙", "龙", "鲁珀", "鲁珀", "鲁珀", "鲁珀", "曼提柯", "佩洛", "佩洛", "佩洛", "佩洛",
        "佩洛", "皮洛萨", "皮洛萨", "匹特拉姆", "匹特拉姆", "奇美拉", "麒麟", "瑞柏巴", "瑞柏巴", "瑞柏巴", "萨弗拉",
        "萨弗拉", "萨弗拉", "萨卡兹", "萨卡兹", "萨卡兹", "萨卡兹", "萨科塔", "萨科塔", "萨科塔", "萨科塔", "塞拉托",
        "塞拉托", "瓦伊凡", "瓦伊凡", "瓦伊凡", "瓦伊凡", "未公开（“巨兽”）", "未公开（“神”）", "未公开（海嗣）",
        "未知（人类）", "沃尔珀", "沃尔珀", "沃尔珀", "沃尔珀", "沃尔珀", "乌萨斯", "乌萨斯", "乌萨斯", "乌萨斯",
        "依特拉", "依特拉", "札拉克", "札拉克", "札拉克", "札拉克", "未知"
    ],

    "方舟地区": [
        "阿戈尔", "玻利瓦尔", "东", "哥伦比亚", "卡西米尔", "卡兹戴尔", "拉特兰", "莱塔尼亚", "雷姆必拓", "龙门",
        "米诺斯", "萨尔贡", "萨米", "维多利亚", "乌萨斯", "谢拉格", "叙拉古", "炎", "伊比利亚", "未公开"
    ],

    "方舟职业": [
        "狙击-{}",
        "术师-{}",
        "医疗-{}",
        "辅助-{}",
        "先锋-{}",
        "近卫-{}",
        "重装-{}",
        "特种-{}"
    ],

    "狙击分支": [
        "速射手\n【特性】优先攻击空中单位",
        "投掷手\n【特性】攻击对小范围的地面敌人造成两次物理伤害（第二次为余震，伤害降低至攻击力的一半）",
        "炮手\n【特性】攻击造成群体物理伤害",
        "攻城手\n【特性】优先攻击重量最重的单位",
        "神射手\n【特性】优先攻击攻击范围内防御力最低的敌方单位",
        "重射手\n【特性】高精度的近距离射击",
        "散射手\n【特性】攻击范围内的所有敌人，对自己前方一横排的敌人攻击力提升至150%"
    ],

    "术师分支": [
        "中坚术师\n【特性】攻击造成法术伤害",
        "扩散术师\n【特性】攻击造成群体法术伤害",
        "轰击术师\n【特性】攻击造成超远距离的群体法术伤害",
        "阵法术师\n【特性】通常时不攻击且防御力和法术抗性大幅度提升，技能开启时攻击造成群体法术伤害",
        "秘术师\n【特性】攻击造成法术伤害，在找不到攻击目标时可以将攻击能量储存起来之后一齐发射（最多3个）",
        "链术师\n【特性】攻击造成法术伤害，且会在4个敌人间跳跃，每次跳跃伤害降低15%并造成短暂停顿",
        "驭械术师\n【特性】操作浮游单元造成法术伤害\n单元攻击同一敌人伤害提升（最高造成干员110%攻击力的伤害）"
    ],

    "近卫分支": [
        "剑豪\n【特性】普通攻击连续造成两次伤害",
        "强攻手\n【特性】同时攻击阻挡的所有敌人",
        "无畏者\n【特性】能够阻挡一个敌人",
        "术战者\n【特性】攻击造成法术伤害",
        "领主\n【特性】可以进行远程攻击，但此时攻击力降低至80%",
        "斗士\n【特性】能够阻挡一个敌人",
        "武者\n【特性】不成为其他角色的治疗目标，每次攻击到敌人后回复自身70生命",
        "解放者\n【特性】通常不攻击且阻挡数为0，技能未开启时40秒内攻击力逐渐提升至最高+200%且技能结束时重置攻击力",
        "收割者\n【特性】无法被友方角色治疗，攻击造成群体伤害，每攻击到一个敌人回复自身50生命，最大生效数等于阻挡数",
        "重剑手\n【特性】同时攻击阻挡的所有敌人",
        "教官\n【特性】可以攻击到较远敌人，攻击自身未阻挡的敌人时攻击力提升至120%"
    ],

    "重装分支": [
        "铁卫\n【特性】能够阻挡三个敌人",
        "哨戒铁卫\n【特性】能够阻挡三个敌人，可以进行远程攻击",
        "驭法铁卫\n【特性】技能开启时普通攻击会造成法术伤害",
        "不屈者\n【特性】无法被友方角色治疗",
        "决战者\n【特性】只有阻挡敌人时才能够回复技力",
        "守护者\n【特性】技能可以治疗友方单位",
        "要塞\n【特性】不阻挡敌人时优先远程群体物理攻击"
    ],

    "医疗分支": [
        "医师\n【特性】恢复友方单位生命",
        "咒愈师\n【特性】攻击造成法术伤害，攻击敌人时为攻击范围内一名友方干员治疗相当于50%伤害的生命值",
        "群愈师\n【特性】同时恢复三个友方单位的生命",
        "链愈师\n【特性】恢复友方单位生命，且会在3个友方单位间跳跃，每次跳跃治疗量降低25%",
        "疗养师\n【特性】拥有较大治疗范围，但在治疗较远目标时治疗量变为80%",
        "行医\n【特性】恢复友方单位生命，并回复相当于攻击力50%的元素损伤（可以回复未受伤友方单位的元素损伤）"
    ],

    "辅助分支": [
        "凝滞师\n【特性】攻击造成法术伤害，并对敌人造成短暂的停顿",
        "削弱者\n【特性】攻击造成法术伤害",
        "吟游者\n【特性】不攻击，持续恢复范围内所有友军生命（每秒相当于自身攻击力10%的生命），自身不受鼓舞影响",
        "工匠\n【特性】能够阻挡两个敌人，使用<支援装置>协助作战",
        "召唤师\n【特性】攻击造成法术伤害\n可以使用召唤物协助作战",
        "护佑者\n【特性】攻击造成法术伤害，技能开启后改为治疗友方单位（治疗量相当于75%攻击力）"
    ],

    "特种分支": [
        "处决者\n【特性】再部署时间大幅度减少",
        "推击手\n【特性】同时攻击阻挡的所有敌人，可以放置于远程位",
        "钩索师\n【特性】技能可以使敌人产生位移，可以放置于远程位",
        "陷阱师\n【特性】可以使用陷阱来协助作战，但陷阱无法放置于敌人已在的格子中",
        "行商\n【特性】再部署时间减少，撤退时不返还部署费用，在场时每3秒消耗3点部署费用（不足时自动撤退）",
        "伏击客\n【特性】对攻击范围内所有敌人造成伤害\n拥有50%的物理和法术闪避且不容易成为敌人的攻击目标",
        "傀儡师\n【特性】受到致命伤时不撤退，切换成<替身>作战（替身阻挡数为0），持续20秒后自身再次替换<替身>",
        "怪杰\n【特性】自身生命会不断流失（每秒流失3%生命值）"
    ],
    "先锋分支": [
        "冲锋手\n【特性】击杀敌人后获得1点部署费用，撤退时返还初始部署费用",
        "尖兵\n【特性】能够阻挡两个敌人",
        "情报官\n【特性】再部署时间减少，可使用远程攻击",
        "战术家\n【特性】可以在攻击范围内选择一次战术点来召唤援军，自身攻击援军阻挡的敌人时攻击力提升至150%",
        "执旗手\n【特性】技能发动期间阻挡数变为0"
    ],

    "方舟稀有度": [
        "★",
        "★★",
        "★★",
        "★★★",
        "★★★",
        "★★★",
        "★★★★",
        "★★★★",
        "★★★★",
        "★★★★",
        "★★★★★",
        "★★★★★",
        "★★★★★",
        "★★★★★",
        "★★★★★",
        "★★★★★",
        "★★★★★★",
        "★★★★★★",
        "★★★★★★",
        "★★★★★★",
        "★★★★★★",
        "★★★★★★★"
    ],

    "_测试结果": [
        "缺陷",
        "普通",
        "普通",
        "普通",
        "标准",
        "标准",
        "标准",
        "优良",
        "优良",
        "优良",
        "卓越",
        "■■"
    ],

    "干员性别": [
        "男",
        "男",
        "男",
        "女",
        "女",
        "女",
        "未知"
    ],

    "感染情况": [
        "非感染者\n【体细胞与源石融合率】0%\n【血液源石结晶密度】0.0[1d9]u/L",
        "非感染者\n【体细胞与源石融合率】0%\n【血液源石结晶密度】0.0[1d9]u/L",
        "非感染者\n【体细胞与源石融合率】0%\n【血液源石结晶密度】0.[1d9+10]u/L",
        "非感染者\n【体细胞与源石融合率】0%\n【血液源石结晶密度】0.[1d9+10]u/L",
        "非感染者\n【体细胞与源石融合率】0%\n【血液源石结晶密度】0.00u/L",
        "感染者\n【体细胞与源石融合率】[1d10]%\n【血液源石结晶密度】0.[3d6+10]u/L",
        "感染者\n【体细胞与源石融合率】[1d10]%\n【血液源石结晶密度】0.[3d6+10]u/L",
        "感染者\n【体细胞与源石融合率】[3d6]%\n【血液源石结晶密度】0.[3d6+15]u/L",
        "感染者\n【体细胞与源石融合率】[3d6]%\n【血液源石结晶密度】0.[3d6+15]u/L",
        "感染者\n【体细胞与源石融合率】[1d5+15]%\n【血液源石结晶密度】0.[5d6+25]u/L",
        "未公开\n【体细胞与源石融合率】未公开\n【血液源石结晶密度】未公开"
    ],

    "综合体检测试": [
        "【物理强度】{}\n【战场机动】{}\n【生理耐受】{}\n【战术规划】{}\n【战斗技巧】{}\n【源石技艺适应性】{}"
    ],

    "战斗经验": ["没有战斗经验", "没有战斗经验", "没有战斗经验", "未知", "未公开", "_数字a年"],

    "_数字a": ["一", "两", "三", "四", "五", "六", "七", "八", "九"],

    "干员信息作成": [
        "为{nick}生成的干员信息如下：\n{%方舟稀有度}\n【性别】{%干员性别}\n【种族】{%方舟种族}\n【出身地】{%方舟地区}\n【战斗经验】{%战斗经验}\n【身高】[3d6*5+2d12+100]cm\n【感染情况】{%感染情况}\n—综合体检测试—\n{%综合体检测试}\n【职业】{%方舟职业}"
    ],

    "干员作成": [
        "为{nick}生成的干员信息如下：\n{%方舟稀有度}\n【性别】{%干员性别}\n【种族】{%方舟种族}\n【出身地】{%方舟地区}\n【战斗经验】{%战斗经验}\n【身高】[3d6*5+2d12+100]cm\n【职业】{%方舟职业}\n【感染情况】{%感染情况}\n—综合体检测试—\n{%综合体检测试}\n—技能—\n{%一套干员技能}"
    ]
}


def calc():
    infected = random.choice(ark.get("感染情况")).replace('[1d9+10]', str(random.randint(11, 19))).replace('[1d9]',
                                                                                                           str(random.randint(
                                                                                                               1,
                                                                                                               9))).replace(
        '[1d10]', str(random.randint(1, 10))).replace('[3d6+10]', str(random.randint(13, 28))).replace("[3d6+15]",
                                                                                                       str(random.randint(
                                                                                                           18,
                                                                                                           33))).replace(
        '[3d6]', str(random.randint(3, 18))).replace("[1d5+15]", str(random.randint(16, 20))).replace("[5d6+25]",
                                                                                                      str(random.randint(
                                                                                                          30, 55)))
    return str(infected)


def ceshi():
    jieguo = random.choice(ark.get("综合体检测试"))
    sfas = ark.get("_测试结果")
    jieguo = jieguo.format(random.choice(sfas), random.choice(sfas), random.choice(sfas), random.choice(sfas),
                           random.choice(sfas), random.choice(sfas))
    return jieguo


def zhiye():
    zhiye = random.choice(ark.get("方舟职业"))
    mainZ = zhiye.split("-")[0] + "分支"

    zhiye = zhiye.format(random.choice(ark.get(mainZ)))
    return zhiye


def arkOperator():
    s = "为生成的干员信息如下：\n{}\n【性别】{}\n【种族】{}\n【出身地】{}\n【战斗经验】{}\n【身高】[{}]cm\n【感染情况】{}\n—综合体检测试—\n{}\n【职业】{}".format(
        random.choice(ark.get("方舟稀有度")), random.choice(ark.get("干员性别")), random.choice(ark.get("方舟种族")),
        random.choice(ark.get("方舟地区")),
        random.choice(ark.get("战斗经验")).replace("_数字a", str(random.randint(1, 34))), str(random.randint(146, 210)),
        calc(), ceshi(), zhiye())
    return s

def get_cp_mesg(gong, shou):
    with open('data/text/cp.json', "r", encoding="utf-8") as f:
        cp_data = json.loads(f.read())
    return random.choice(cp_data['data']).replace('<攻>', gong).replace('<受>', shou)


async def emojimix(emoji1, emoji2):
    if is_emoji(emoji1) and is_emoji(emoji2):
        pass
    else:
        print("not emoji")
        return None
    url = f"http://promptpan.com/mix/{emoji1}/{emoji2}"
    #url=f"https://emoji6.com/emojimix/?emoji={emoji1}+{emoji2}"
    path = "data/pictures/cache/" + random_str() + ".png"
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url)
        #print(r.content)
        with open(path, "wb") as f:
            f.write(r.content)  # 从二进制数据创建图片对象
        # print(path)
        return path
url = "https://www.ipip5.com/today/api.php"
url2 = "https://api.pearktrue.cn/api/steamplusone/"


async def hisToday():
    async with httpx.AsyncClient(timeout=100) as client:
        data = {"type": "json"}
        r = await client.get(url, params=data)
        return r.json()


async def steamEpic():
    async with httpx.AsyncClient(timeout=100) as client:
        data = {"type": "json"}
        r = await client.get(url2, params=data)
        #print(str(r.json().get("data")).replace(",","\n"))
        st = ""
        for i in r.json().get("data"):
            st += "名称：" + i.get("name") + "\n"
            st += "开始时间：" + i.get('starttime') + "\n"
            st += "结束时间:" + i.get('endtime') + "\n"
            st += "平台:" + i.get('source') + "\n"
            st += "链接:" + i.get('url') + "\n"
            st += "======================\n"
        #print(st)
        return st
async def arkSign(url):
    url = f"https://api.lolimi.cn/API/ark/a2.php?img={url}"
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url)
    #print(r.text)
    #print(r.text,type(r.json()))
    return str(r.text)
async def pic():
    url = "https://iw233.cn/api.php?sort=random"
    # url+="tag=萝莉|少女&tag=白丝|黑丝"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
        "Referer": "https://weibo.com/"}
    async with httpx.AsyncClient(timeout=20) as client:
        r=await client.get(url, headers=headers)
        r=r.content
    ranpath = random_str()

    with open("data/pictures/wallpaper/" + ranpath + ".png", mode="wb") as f:
        f.write(r)  # 图片内容写入文件
    return "data/pictures/wallpaper/" + ranpath + ".png"
async def setuGet(data, withPic, grayPic):
    ranpath = random_str()
    path = "data/pictures/wallpaper/" + ranpath + ".png"
    url = "https://api.lolicon.app/setu/v2?"
    async with httpx.AsyncClient(timeout=100) as client:
        r = await client.get(url, params=data)
        #print(r.json().get("data")[0].get("urls").get("regular"))
        url = r.json().get("data")[0].get("urls").get("regular")
        if not withPic:
            return url, None
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url)
        img = Image.open(BytesIO(r.content))  # 从二进制数据创建图片对象
        if grayPic:
            # open colour image
            image_raw = img
            # convert image to black and white
            image_black_white = image_raw.convert('1')
            image_black_white.save(path)
            return url, path
            #image_black_white.show()
        img.save(path)  # 使用PIL库保存图片
        return url, path
async def querys(city, API_KEY) -> str:
    """查询天气数据。"""
    async with httpx.AsyncClient(timeout=20) as client:
        try:
            resp = await client.get(f'https://api.seniverse.com/v3/weather/now.json', params={
                'key': API_KEY,
                'location': city,
                'language': 'zh-Hans',
                'unit': 'c',
            })
            resp.raise_for_status()
            data = resp.json()
            return f'当前{data["results"][0]["location"]["name"]}天气为' \
                   f'{data["results"][0]["now"]["text"]}，' \
                   f'气温{data["results"][0]["now"]["temperature"]}℃。'
        except (httpx.NetworkError, httpx.HTTPStatusError, KeyError):
            return f'抱歉，没有找到{city}的天气数据。'
with open('data/text/jokes.yaml', 'r', encoding='utf-8') as f:
    jokes = yaml.load(f.read(), Loader=yaml.FullLoader)
def get_joke(joke_tp):
    if joke_tp == '法国':
        return random.choice(jokes["french_jokes"])
    elif joke_tp == '美国':
        return random.choice(jokes["america_jokes"])
    elif joke_tp == '苏联':
        return random.choice(jokes["soviet_jokes"])
    else:
        if joke_tp == '':
            joke_tp = 'yiris'
        return random.choice(jokes["jokes"]).replace('%name%', joke_tp)
