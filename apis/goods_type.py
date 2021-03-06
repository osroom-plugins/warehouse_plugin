# -*-coding:utf-8-*-
from flask import request

from apps.configs.sys_config import METHOD_WARNING
from apps.core.blueprint import api
from apps.core.flask.login_manager import osr_login_required
from apps.core.flask.response import response_format
from apps.plugins.warehouse_plugin.process.goods_type import get_goods_types, add_goods_types, update_goods_types, \
    del_goods_types

__author__ = "Allen Woo"

@api.route('/plug/goods/type', methods=['GET','POST','PUT','DELETE'])
@osr_login_required
def api_plug_goods_type():

    '''
    GET:

    '''

    if request.c_method == "GET":
        data = get_goods_types()

    elif request.c_method == "POST":
        data = add_goods_types()
    elif request.c_method == "PUT":
        data = update_goods_types()
    elif request.c_method == "DELETE":
        data = del_goods_types()
    else:
        data = {"msg_type":"w", "msg":METHOD_WARNING, "http_status":405}
    return response_format(data)