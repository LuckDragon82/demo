from boilerplate.handlers import BaseHandler

class Home(BaseHandler):
    def get(self):
        params = {}
        return self.render_template('home.html', **params)
    
    def post(self):
        pass
        self.redirect('/')