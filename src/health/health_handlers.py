from aiohttp import web
from aiohttp.web_response import Response


async def health(request):
    """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Health check
    produces:
    - text/plain
    responses:
        "200":
            description: successful operation. Return "status"
        "405":
            description: invalid HTTP Method
    """
    res = {"status": "ok"}
    return web.json_response(res, status=201)

