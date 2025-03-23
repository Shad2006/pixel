import mcpi.minecraft as minecraft
from mcpi import block
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
start_x, start_y, start_z = pos.x + 3, pos.y, pos.z + 3

for y in range(7):
    for x in range(15):
        mc.setBlock(start_x + x, start_y + y, start_z, block.BRICK_BLOCK.id)
