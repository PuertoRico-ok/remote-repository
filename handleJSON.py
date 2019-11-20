from flask import Flask, render_template, request, redirect, url_for
import os
import json
def create_file():
    check = os.path.exists('data.json')
    if check == False:
        open('data.json', 'a').close()
        return put_admin()
    else:
        return put_admin()


def put_admin():
    blank = os.stat('data.json').st_size == 0
    if blank == True:
        data = {}
        data['users'] = []
        data['users'].append({
        'ID': 'puerto',
        'Pass': 'rico'
        })
        with open('data.json', 'a') as admin_data:
            json.dump(data, admin_data, indent = 2, sort_keys = True)
        return get_value()
    else:
        return get_value()


def get_value():
    userid = request.form['userid']
    password = request.form['password']
    with open('data.json') as f:
        info = json.load(f)
    for idd in info['users']:
        data2 = {}
        data2.update(idd)
    if userid in data2['ID']:
        return render_template('wrong.html')
    else:
        info['users'].append({
        'ID': userid,
        'Pass': password
        })
        with open('data.json', 'w') as file:
            json.dump(info, file, indent = 2, sort_keys = True)
        return render_template('ok.html', u = userid, p = password)


def login_check():
    userid_check = request.form['userid_check']
    password_check = request.form['password_check']
    with open('data.json') as json_file:
        check = json.load(json_file)
    for passes in check['users']:
        all_data = {}
        all_data.update(passes)
    if userid_check in all_data['ID'] and password_check in all_data['Pass']:
        return render_template('ok2.html', uc = userid_check)
    else:
        return render_template('nope.html')
