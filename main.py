import tornado.ioloop
import tornado.web
from pymongo import Connection


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        self.set_header('Content-Type:', 'text/plain')
        con = Connection()
        db = con.post
        post = db.post
        message = self.get_argument('messages')
        data = {"message": message}
        post.insert(data)
        self.write('You wrote ' + self.get_argument('messages'))

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
