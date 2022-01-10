import os
import paramiko

ip = "10.244.12.21"#服务器ip
port = 22#端口号
username = "root"#用户名
password = "123"#密码

def uploadfiletoserver(local, remote,fname):  # 上传文件到服务器.local是要上传文件的本地路径；remote是上传到服务器的路径
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)

    sftp = ssh.open_sftp()
    sftp.put(local, remote)
    sftp.put(local, os.path.join(remote, fname))
    print("{:*{}25}".format('upload success', '^'))
    return remote

def upload2():
    # 获取Transport实例
    tran = paramiko.Transport("10.244.12.21", 22)
    # 连接SSH服务端
    tran.connect(username="root", password="123")
    # 获取SFTP实例
    sftp = paramiko.SFTPClient.from_transport(tran)
    # 设置上传的本地/远程文件路径
    localpath = "/Users/jackrechard/Desktop/tp.png"  ##本地文件路径
    remotepath = "/home/chengdegang"  ##上传对象保存的文件路径
    # 执行上传动作
    sftp.put(localpath, remotepath)

    tran.close()

def test():
    ces =  os.path.join('/tmp', 'ttt.txt')
    print(ces)

if __name__ == '__main__':
    uploadfiletoserver(local='/Users/jackrechard/Desktop/tp.png',remote='/home/chengdegang',fname='tp.png')
    # upload()
    # test()
