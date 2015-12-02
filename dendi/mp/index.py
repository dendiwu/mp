import os,sys
import web
from weixinInterface import WeixinInterface


urls = (
  '/weixin','WeixinInterface',
  '/','index'
)

class index:
   def GET(self):
       return render.index(None)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

if __name__ == "__main__":
   app = web.application(urls,globals())
   app.run()
