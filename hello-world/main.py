import argparse

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello world')


def make_app():
    return tornado.web.Application(handlers=[
        (r'/', MainHandler),
    ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'port',
        default=45678,
        type=int,
        nargs='?',
    )

    args = parser.parse_args()
    print('args', args)

    app = make_app()
    app.listen(args.port)
    tornado.ioloop.IOLoop.current().start()
