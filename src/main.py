#!/usr/bin/env python3

import os
from bottle import get, post, request, route, run, template, static_file
from kubernetes import client, config
from dotenv import load_dotenv

## config

load_dotenv()

## routes

@route('/', method=['GET','POST'])
def index():
    add_url = False
    error_url = False
    duplicate_url = False

    try:
        subscriptions_configmap = read_configmap()
        subscriptions_list = []
        for sub in subscriptions_configmap.data['batch'].splitlines():
            subscriptions_list = subscriptions_list + [sub]
    except KeyError as e:
        subscriptions_list = []

    if request.method == 'POST':
        if request.forms.get('url') in subscriptions_list:
            duplicate_url = request.forms.get('url')
        else:
            subscriptions_list = subscriptions_list + [request.forms.get('url')]
            subscriptions_string = '\n'.join(subscriptions_list)
            subscriptions_configmap.data['batch'] = subscriptions_string

            write = write_configmap(content=subscriptions_configmap)
            if write:
                add_url = request.forms.get('url')
            else:
                err_url = request.forms.get('url')

    return template('default', page_name='overzicht', subscriptions=subscriptions_list, add_url=add_url, error_url=error_url, duplicate_url=duplicate_url)

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

## functions

def read_configmap(namespace='youtube', configmap='config'):
    if os.getenv('KUBECONFIG'):
        config.load_kube_config()
    else:
        config.load_incluster_config()
    v1 = client.CoreV1Api()

    try:
        response = v1.read_namespaced_config_map(configmap, namespace)
    except Exception as e:
        print("Exception when calling CoreV1Api->read_namespaced_config_map: %s\n" % e)
        return False

    return response

def write_configmap(namespace='youtube', configmap='config', content={}):
    if os.getenv('KUBECONFIG'):
        config.load_kube_config()
    else:
        config.load_incluster_config()
    v1 = client.CoreV1Api()

    try:
        response = v1.patch_namespaced_config_map(configmap, namespace, content)
    except Exception as e:
        print("Exception when calling CoreV1Api->patch_namespaced_config_map: %s\n" % e)
        return False

    return response

## initialize

run(host='0.0.0.0', port=8080)