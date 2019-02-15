#!/home/c4850/tryrest.na4u.ru/.env/bin/python
import json
from aiohttp import web
import config
from utils import get_logger

logger = get_logger('RestHandler')


async def from_vsts(req):
    logger.debug('Request with params :: {}'.format(req.query))
    data = await req.json()
    logger.debug('Request with body :: {}'.format(data))

    response_obj = {'status': data}
    return web.Response(text=json.dumps(response_obj))

if __name__ == '__main__':
    app = web.Application()
    app.router.add_post(config.VSTS_PUSH_PATH, from_vsts)

    web.run_app(app, host=config.IP, port=config.PORT)
