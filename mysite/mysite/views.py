
import socket
import json

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .form.LoginForm import LoginForm
from .form.ConfigForm import ConfigForm

from .config.config import sys_config

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

def config(conf):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.sendto(bytes(conf, 'utf-8'), (server_ip, server_port))
    result = s.recv(1024).decode('utf-8')
    status_code = (json.loads(result))['return']
    status = "config success" if (status_code == 1) else "config failed"
    print(status)

    s.close()

    return status

def index(request):
    # temp = loader.get_template('index.html')
    psd = request.COOKIES.get('psd')

    if psd != 'jiang':
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

            status = config(json.dumps(conf))


    # else:
    #     data = query()
    #     print(data)
    #     # data = json.load(query(cmd))
    #     form = ConfigForm(json.loads(data))


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
                res.set_cookie('psd', sys_config['password'], expires=60*60*24)
                return res
                # return HttpResponseRedirect('/').set_cookie('psd', 'jiang', expires=60*60*24)
            else:
                message = "wrong password"

    else:
        form = LoginForm()

    res = render(request, 'login.html', {'form': form, 'message': message})
    res.delete_cookie('psd')
    return res


