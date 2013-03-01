from boilerplate.handlers import BaseHandler

class Home(BaseHandler):
    def get(self):
        params = {}
        return self.render_template('admin/home.html', **params)
    
    def post(self):
        pass
        self.redirect_to('/admin/')