'''
Created on Feb 24, 2013

@author: Joshua Toledo
'''
from boilerplate import models
from boilerplate.lib.basehandler import BaseHandler
from boilerplate.lib.basehandler import user_required

class Home(BaseHandler):
    def get(self):
        self.render_template('admin.html', params)