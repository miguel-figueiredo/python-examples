from aiohttp import web
from prometheus_async import aio
from system_metrics import SystemMetrics

system_metrics = SystemMetrics()


async def metrics(request):
    await system_metrics.update()
    return await aio.web.server_stats(request)


def main():
    app = web.Application()
    metrics_route = [web.get('/metrics', metrics)]
    app.add_routes(metrics_route)
    web.run_app(app, port=8080)


if __name__ == '__main__':
    main()
