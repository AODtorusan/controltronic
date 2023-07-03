#!/usr/bin/env python3

import asyncio
import logging
import typing
import screentronic.smartControl

class MyClient(screentronic.smartControl.Client):
  def __init__(self) -> None:
    super().__init__()
    self.seen_control_groups: typing.Set[screentronic.smartControl.ControlGroup] = set()

  async def handle( self, pkt ):
    if isinstance(pkt, screentronic.smartControl.SmartControlPacket):
      if not pkt.controlGroup in self.seen_control_groups:
        self.seen_control_groups.add( pkt.controlGroup )
        logging.info(f"Found new control group in use: {pkt.controlGroup}")
    logging.info(f"Received: {pkt}")

def main():
  logging.basicConfig(level=logging.INFO)
  myclient = MyClient()
  loop = asyncio.get_event_loop()
  loop.run_until_complete( myclient.loop() )

if __name__ == "__main__":
    main()
