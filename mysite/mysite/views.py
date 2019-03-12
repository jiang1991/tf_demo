
import socket
import json
import base64

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .form.LoginForm import LoginForm
from .form.ConfigForm import ConfigForm

from .config.config import sys_config
from .data import json_res

# CMD
cmd = '{"cmd" : "get_data"}'

server_ip = sys_config['serverIp']
server_port = sys_config['serverPort']

def query():
    # udp query
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(bytes(cmd, 'utf-8'), (server_ip, server_port))
    sql_query = s.recv(1024).decode('utf-8')
    s.close()

    return sql_query

def index_config(conf):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.sendto(bytes(conf, 'utf-8'), (server_ip, server_port))
    result = s.recv(1024).decode('utf-8')
    status_code = (json.loads(result))['return']
    status = "config success" if (status_code == 1) else "config failed"
    print(status)

    s.close()

    return status


def console(request):
    if request.COOKIES.get('psd') == None:
        res = HttpResponseRedirect('signin')
        res.delete_cookie('psd')
        return res

    print("console" + request.COOKIES.get('psd'))

    # temp = loader.get_template('index.html')
    psd = base64.b64decode(request.COOKIES.get('psd')).decode('utf-8')
    print("console" + psd)

    if psd != sys_config['password']:
        res = HttpResponseRedirect('signin')
        res.delete_cookie('psd')
        return res

    res = render(request, 'console.html')
    return res


def config(request):
    if request.COOKIES.get('psd') == None:
        res = HttpResponseRedirect('signin')
        res.delete_cookie('psd')
        return res

    print("console" + request.COOKIES.get('psd'))

    # temp = loader.get_template('index.html')
    psd = base64.b64decode(request.COOKIES.get('psd')).decode('utf-8')
    print("console" + psd)

    if psd != sys_config['password']:
        res = HttpResponseRedirect('signin')
        res.delete_cookie('psd')
        return res

    res = render(request, 'config.html')
    return res


def index(request):

    if request.COOKIES.get('psd') == None:
        res = HttpResponseRedirect('login')
        res.delete_cookie('psd')
        return res

    print(request.COOKIES.get('psd'))

    # temp = loader.get_template('index.html')
    psd = base64.b64decode(request.COOKIES.get('psd')).decode('utf-8')
    print(psd)

    if psd != sys_config['password']:
        res = HttpResponseRedirect('login')
        res.delete_cookie('psd')
        return res

    status = ""

    if request.method == 'POST':
        form = ConfigForm(request.POST)

        if form.is_valid():
            conf = {}

            conf['mode'] = form.cleaned_data['mode']
            conf['coin_count'] = form.cleaned_data['coin_count']
            conf['game_count'] = form.cleaned_data['game_count']
            conf['game_time'] = form.cleaned_data['game_time']
            conf['music_volume'] = form.cleaned_data['music_volume']
            conf['sound_volume'] = form.cleaned_data['sound_volume']
            conf['resolution'] = form.cleaned_data['resolution']
            conf['spare_1'] = form.cleaned_data['spare_1']
            conf['spare_2'] = form.cleaned_data['spare_2']
            conf['spare_3'] = form.cleaned_data['spare_3']
            conf['spare_4'] = form.cleaned_data['spare_4']
            conf['spare_5'] = form.cleaned_data['spare_5']

            print(json.dumps(conf))

            status = index_config(json.dumps(conf))

            data = query()
            print(data)
            # data = json.load(query(cmd))
            form = ConfigForm(json.loads(data))

            # res = render(request, 'index.html', {'form': form, 'message': status})
            # return res
            return HttpResponseRedirect('/', {'message': status})


        else:
            print(form.errors)
            return render(request, "index.html", {'form': form, 'error': form.errors})


    else:
        data = query()
        print(data)
        # data = json.load(query(cmd))
        form = ConfigForm(json.loads(data))

        res = render(request, 'index.html', {'form': form, 'message': status})
        return res



def login(request):

    message = ""

    if ('password' not in sys_config or sys_config['password'] == ''):
        message = "password not set"

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            psd = form.cleaned_data['password']

            if psd == sys_config['password']:
                res = HttpResponseRedirect('/')
                cookie = base64.b64encode(str.encode(sys_config['password'])).decode()
                print("cookie: " + cookie)
                res.set_cookie('psd', cookie, expires=60*60*24)

                return res
                # return HttpResponseRedirect('/').set_cookie('psd', 'jiang', expires=60*60*24)
            else:
                message = "wrong password"

    else:
        form = LoginForm()

    res = render(request, 'login.html', {'form': form, 'message': message})
    res.delete_cookie('psd')
    return res


def signin(request):

    res = render(request, 'signin.html')
    return res


def test(request):

    res = render(request, 'test.html')
    return res


def api_login(request):
    print(type(request.body))
    psd = json.loads(str(request.body,'utf-8'))["password"]
    message = ''

    if ('password' not in sys_config or sys_config['password'] == ''):
        message = "password not set"

    if psd != sys_config['password']:
        message = "wrong password"

    if (message == ''):
        resp = {'status': 'ok'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'status': 'error', 'error': message}
        return HttpResponse(json.dumps(resp), content_type="application/json")


def api_json(request):
    cmd = json.loads(request.body)['cmd']

    res = ''

    if cmd == 'get_data':
        res = json_res.res_get_Data
    elif cmd == 'modify_data':
        res = json_res.res_modify_data
    elif cmd == 'set_wifi_state':
        res = json_res.res_set_wifi
    elif cmd == 'scan_robot':
        res = json_res.res_scan_robot
    elif cmd == 'get_robot_info':
        res = json_res.res_get_robot_info
    elif cmd == 'set_robot_info':
        res = json_res.res_set_robot_info
    elif cmd == 'auto_pairing':
        res = json_res.res_pair

    return HttpResponse(res, content_type="application/json")

