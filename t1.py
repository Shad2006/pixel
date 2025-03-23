import mcpi.minecraft as minecraft
from mcpi import block
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
direction = mc.player.getDirection()
new_x = pos.x + direction.x * 5
new_y = pos.y + direction.y * 5
new_z = pos.z + direction.z * 5
mc.setBlock(new_x, new_y, new_z, block.DIRT.id)
