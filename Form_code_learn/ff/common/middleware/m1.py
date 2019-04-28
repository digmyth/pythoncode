#!/usr/bin/env python3
'''
python3 需要继承MiddlewareMixin类
'''

from django.conf import settings
from django.shortcuts import  redirect


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

class M1(MiddlewareMixin):
    def process_request(self,request,*args,**kwargs):
        if request.path_info == "/login/":
            return None

        '''
        session 验证
        '''
        if not request.session.get(settings.USER_SESSION_KEY):
            return redirect("/login")


    def process_response(self, request, response,*args,**kwargs):
        return response