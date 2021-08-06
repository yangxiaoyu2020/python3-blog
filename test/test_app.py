from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web

from health.health_handlers import health


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """

        app = web.Application()
        app.router.add_get('/health', health)
        return app

    # the unittest_run_loop decorator can be used in tandem with
    # the AioHTTPTestCase to simplify running
    # tests that are asynchronous
    @unittest_run_loop
    async def test_health(self):
        resp = await self.client.request("GET", "/health")
        assert resp.status == 201
        text = await resp.json()
        assert text["status"] == "ok"

