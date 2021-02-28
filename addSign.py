import requests
import random


from mongoutlis import add


def add_sign(id):
    sxAddress = getInfo(id).get("sxAddress")
    address = (
        ('address', sxAddress),
        ('uid', "服务器获取"),
    )
    # 此接口为另外的接口，根据输入地址模糊搜索地址的，返回的是经纬度，使用的是百度地图的api
    add = requests.get("http://dl.hqgml.com/wx/ssm/sx/address", params=address)
    address_new = add.json()

    params = (
        ('formAction', 'stuPosSign'),
    )

    lng = address_new.get("lng")
    lat = address_new.get("lat")
    split_lng = str(lng)[0:7] + str(random.randint(0, 999))
    split_lat_ = str(lat)[0:6] + str(random.randint(0, 999))

    data = {
        'id': id,
        'dqLongitude': split_lng,
        'dqDimension': split_lat_,
        'dqAddress': sxAddress,
        'sxLongitude': address_new.get("lng"),
        'sxDimension': address_new.get("lat"),
        'sxAddress': sxAddress,
    }
    response = requests.post('http://m.shixi.rzpt.cn/mobSignMgr.do', params=params, data=data)
    return response.json()

def get_user_info(id):

    params = (
        ('formAction', 'userInfoLook'),
    )

    data = {
        'id': id
    }
    response = requests.post('http://m.shixi.rzpt.cn/mobUserInfoMgr.do', params=params, data=data)

    return response.json()

def login(username, password):
    data = {
        'userid': username,
        'pwd': password
    }
    response = requests.post('http://m.shixi.rzpt.cn/MobUserLoginAction.do', data=data)
    return response.json()


def getInfo(id):
    params = (
        ('formAction', 'userSigns'),
    )
    data = {
        'id': id
    }

    response = requests.post('http://m.shixi.rzpt.cn/mobSignMgr.do', params=params, data=data)
    return  response.json()


def signone(id,qq):
    user_info = get_user_info(id)
    u_name = user_info.get("stuInfo").get("stuName")
    sign_info = add_sign(id)
    print(sign_info)


def action(username, password,qq):
    user = login(username, password).get("userId").replace('\'', '')
    signone(user,qq)
    user_info = get_user_info(user)
    u_name = user_info.get("stuInfo").get("stuName")
    add(user, qq,u_name)



# action("账号","密码","邮箱(qq邮箱)")


