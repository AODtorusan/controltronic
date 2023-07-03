#!/usr/bin/env python3

import asyncio
import logging

from screentronic.smartControl import *

logging.basicConfig(level=logging.INFO)

class MyClient(Client):
  async def handle( self, pkt ):
    logging.info(f"Received: {pkt}")

async def tester():
  await asyncio.sleep(0.1)
  smartControl = SmartControl()
  blind: SmartBlind = smartControl.blind( (1,1,1,5) )
  logging.warning(f"Posision: {blind.position()}")
  await asyncio.sleep(1)
  blind.set_position(200, 255)
  await asyncio.sleep(1)
  logging.warning(f"Posision: {blind.position()}")
  await asyncio.sleep(30)
  logging.warning(f"Posision: {blind.position()}")
  await asyncio.sleep(1)
  blind.set_position(255, 255)
  await asyncio.sleep(1)
  logging.warning(f"Posision: {blind.position()}")


myclient = MyClient()

loop = asyncio.get_event_loop()
loop.run_until_complete( asyncio.gather(
  myclient.loop(),
  tester()
) )
