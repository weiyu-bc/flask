import random


def handle_response(msg):
    p_msg = msg.lower()

    if p_msg.startswith('$hello'):
        return 'Hello!'

    if p_msg.startswith('?id'):
        return '30800001'

    if p_msg.startswith('process 1'):
        return str(random.randint(1, 6))

    if p_msg.startswith('?p1'):
        return "您的福利币配额为10000HCN。"

    if p_msg.startswith('?join'):
        return "您加入农场时间：2022年06月04日"

    if p_msg.startswith('?9'):
        return "Discord: 明心#777, 点击进入连接."

    if p_msg.startswith('?help'):
        info = """
        ?help  帮助信息；
        ?id     查询红叶农场会员信息；
        ?p1  查询喜币配额；
        ?join   查询加入农场时间；
        ?9  联系人工客服；
        """
        return info

    # return 'I do not know what you said.'
