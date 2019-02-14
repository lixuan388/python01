# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

html = '''
<form method="post" name="frm1" action="/login">
    <label for="txt">用户名</label>
    <input type="text" id="txtname" name="myname">
<br/>
<br/>
    <label for="txt">密码  </label>
    <input type="text" id="txtpwd" name="mypwd">
<br/>
<br/>
    <input type="submit">
</form>
'''

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        
        print("MainHandler")
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)

class LoginHandler(BaseHandler):
    def get(self):
        
        print("LoginHandler")
        self.write(html)

    def post(self):
        
        print("LoginHandler")
        self.set_secure_cookie("user", self.get_argument("myname"))
        # self.write("POST LOGIN")
        self.redirect("/")

settings = dict(
        # template_path=TEMPLATE_PATH,
        # static_path=STATIC_PATH,
        # cookie_secret=str(uuid.uuid1()),
        cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        login_url="/login",
        # gzip=True,
        # xheaders=True,
        debug=True
    )
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler)
], **settings)
#application.add_handlers(host_pattern, host_handlers)
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
    
    