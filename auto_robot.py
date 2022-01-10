import itchat


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if not msg['FromUserName'] == myUserName:
        # 群名 发消息人 信息
        print(msg['User']['NickName'] + ' ' + msg['ActualNickName'] + ' ' + msg['Content'])
        if msg['User']['NickName'] == '测试群':
            itchat.send_image("C:\\a.png", 'filehelper')


if __name__ == '__main__':
    itchat.auto_login()

    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
    print(myUserName)