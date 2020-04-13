from flask import Flask, request,render_template, jsonify, request, send_from_directory, abort
import os,time,sys,logging,subprocess
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
import socket
import pymysql,datetime
app = Flask(__name__,template_folder='templates',static_folder='templates/css',)#2
basedir = os.path.abspath(os.path.dirname(__file__))

global address
# host_name = socket.gethostname()
# ip = socket.gethostbyname(host_name)
# print(ip)
# try:ip=sys.argv[1]
# except:
ip='localhost:127'
address=f'{ip}'
# 用于判断文件后缀


@app.route('/', methods=['GET', 'POST'])
#4

def web_1():
	liststr='<div style="height: 20%;bottom:100px;" id="s">'
	conn=pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='20091222toby',
    )#登录我的数据库
	try:
		
		
    
		cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
		sql1="select * from chatroom.chat_msg order by msg_time desc"
	
		num=cursor.execute(sql1)
		t=cursor.fetchmany(num)
		for i in t:
			name=i['name']
			text=i['msg']
			time=i['msg_time']
			liststr+=f'<pre>{name} 在 {time} 说：<br>{text}<br></pre>'
		conn.close()
		liststr+='</div>'
		return render_template('index.html').replace('$add$',liststr)
		# return ''
	except Exception as e:
		print(str(e))
		conn.close()
		return render_template('index.html').replace('$add$',liststr)
	

	

@app.route('/chat', methods=['GET', 'POST'])
def web_2():
	conn=pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='20091222toby',
    )#登录我的数据库
	try:
		name=request.args.get('name')
		text=request.args.get('content').replace('<','＜').replace('>','＞')
		print(name+'发送了消息：'+text)          
		
    
		cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
		sql1="insert into chatroom.chat_msg (name, msg,msg_time) values (%s, %s,%s);"
	
		cursor.execute(sql1,[name,text,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
		conn.commit()
		conn.close()
		
		return f' <meta http-equiv="refresh" content="0;url=http://{address}">'
	except:
		conn.close()
		return '<center><br><br><br><br><br><br><h1>哎呀，发送失败！</h1><br><a href="http://127.0.0.1:127"><button>返回>>></button></a></center>'
@app.route('/login', methods=['GET', 'POST'])
def web_3():
	return render_template('login.html')


@app.errorhandler(500)
def server_error(e):
	return f"""<head></head><body style="background-color:grey;"><center><h1><br><br><br><br><br><br><br>500错误，服务器脚本错误，去暴揍管理员吧（滑稽）""", 500
@app.errorhandler(404)
def not_found(e):
	return f"""<head></head><body style="background-color:grey;"><center><h1><br><br><br><br><br>404?! 你要找的页面跑了~""", 404


if __name__=='__main__':#6
	
	print("\033[1;34m starting\033[0m",end='')
	# app.run(host='127.0.0.1',port=81)
	try:
		print("\033[1;34m .\033[0m",end='')
		http_server = WSGIServer((address.split(':')[0], int(address.split(':')[1])), app)
		print("\033[1;34m . .\033[0m",end='                  ')
		print("\033[1;32m [OK]\033[0m")
		print(f'服务器运行于{address}')
		http_server.serve_forever()
		http_server._stop_event.wait()
	except Exception as e:
		print("\033[1;31m 发生错误：\033[0m",end=' ')
		print(e)
		sys.exit(0)

