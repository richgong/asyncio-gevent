import gevent.monkey
gevent.monkey.patch_all()

import asyncio

import asyncio_gevent

asyncio.set_event_loop_policy(asyncio_gevent.EventLoopPolicy())

# Main example

import gevent

async def async_function() -> int:
    print("Sleeping...")
    await asyncio.sleep(1)
    return 42


def main() -> None:
    print("Main...")
    future = async_function()
    greenlet = asyncio_gevent.future_to_greenlet(future)
    greenlet.start()
    greenlet.join()
    assert greenlet.get() == 42

main()
