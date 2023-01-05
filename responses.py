import random


def handle_response(msg):
    p_msg = msg.lower()

    if p_msg.startswith('$hello'):
        return 'Hello!'

    if p_msg.startswith('?id'):
        return ''

    if p_msg.startswith('process 1'):
        return str(random.randint(1, 6))

    if p_msg.startswith('?p1'):
        return "。"

    if p_msg.startswith('?join'):
        return ""

    if p_msg.startswith('?9'):
        return "."

    if p_msg.startswith('?help'):
        info = """
        ?help  帮助信息；
        ?id     ；
        ?p1  查询；
        ?join   查询；
        ?9  联系；
        """
        return info

    # return 'I do not know what you said.'
