import random
from read_csv import read_csv_file
from read_mysql import search_db_with_name, insert_user, delete_user


def get_id_by_name(name):
    name = str(name)
    mem_id_list, discord_list, farm_id_list = read_csv_file('test_id.csv')

    if name not in discord_list:
        return "not exist"
    else:
        position = discord_list.index(name)
        return mem_id_list[position], farm_id_list[position]


def get_info_by_name_db(name):
    name = str(name)

    # search DB with name
    result = search_db_with_name(name)
    print()

    # compare the DB search result, return info
    if result == "not exist":
        return "not exist"
    else:
        return result[2], result[3]


def add_name_db(name):
    name = str(name)

    # add DB with name
    return insert_user(name)


def delete_name_db(name):
    name = str(name)

    # add DB with name
    result = delete_user(name)


def handle_response(msg, user_msg):
    p_msg = user_msg.lower()
    username = msg.author
    channel = msg.channel
    # print(msg.channel)

    if p_msg.startswith('$hello'):
        return 'Hello!'

    if p_msg.startswith('?id') or p_msg.startswith('？id'):
        # user_id = get_id_by_name(username)
        user_id = get_info_by_name_db(username)

        if user_id == "not exist":
            return f'{username}  查询不到您的编号，请联系人工客服。'
        else:
            return f'{username}  您的喜币复核ID {user_id[0]}，农场编号 {user_id[1]}'

    if p_msg.startswith('?hcn') or p_msg.startswith('？hcn'):
        num = 10000
        #return f'{username},您的喜币配额：{num}'
        return f'{username}  您好。该项目正在建设中。。。'

    if p_msg.startswith('?9') or p_msg.startswith('？9'):
        return "https://discord.com/channels/1048762780116856882/1048762780846669895"

    if p_msg.startswith('?t') or p_msg.startswith('？t'):
        user_id = get_id_by_name(username)
        if user_id == "not exist":
            return f'{username}  您不在参会战友列表中，请联系人工客服。'
        else:
            return f'{username}  您好！🙏 本次会议链接如下：https://gettr.com/user/redmaplejustice'

    # 特定权限管理员，添加删除会员信息
    if p_msg.startswith('@1'):
        # 只有指定有权限管理员，才可以添加用户
        if str(channel) in "general":
            try:
                user = p_msg.split(' ')[1]
                # print(user)
            except:
                return "请指定discord用户。"
            result = add_name_db(user)
            if result == "add success":
                return f"{user} 添加成功."
            else:
                return f"{user} 已经存在."

        # 非管理员，直接返回
        else:
            return f"{username} 您没有相应权限。"

    # 特定权限管理员，添加删除会员信息
    if p_msg.startswith('@0'):
        # 只有指定有权限管理员，才可以删除用户
        if str(channel) in "general":
            try:
                user = p_msg.split(' ')[1]
                # print(user)
            except:
                return "请指定discord用户。"
            delete_name_db(user)
            return f"{user} 删除成功."

        # 非管理员，直接返回
        else:
            return f"{username} 您没有相应权限。"


    if p_msg.startswith('?') or p_msg.startswith('？'):
        info = """
        ?  可查询如下信息:
        ?id   -- 查询您的会员信息
        ?t    -- 获取参会链接
        ?hcn  -- 查询您的喜币配额
        ?9    -- 接入人工客服咨询
        
        """
        return info


if __name__ == '__main__':
    id_name = get_id_by_name("96118#6902")
    print(id_name)
