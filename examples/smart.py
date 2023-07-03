
#%%

import screentronic.smartControl

smartControl = screentronic.smartControl.SmartControl()
blind = smartControl.blind( (1,1,1,5) )
blind.up()
blind.down()
blind.set_position( height=128, angle=192 )
print( blind.position() )
