
#%%

import logging
import time
from screentronic.directControl import *

logging.basicConfig(level=logging.DEBUG)

module = next( ST2134.discover(), None )
#module = ST2134( mac=[0x50, 0x4b, 0x5b, 0x00, 0x00, 0x00] )
logging.info(f"Found the following device: {module=}")

module.identify()

blind = module.blind( 4 )
blind.up()
time.sleep(60)
blind.stop()

logging.info( blind.get_position() )
blind.position(160, 128)
time.sleep(30)
logging.info( blind.get_position() )

blind.height(150)
time.sleep(30)
logging.info( blind.get_position() )
