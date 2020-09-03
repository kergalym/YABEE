from direct.showbase.ShowBase import ShowBase
from panda3d.core import Texture

data = open("/tmp/yabee_exported", "r").read()
base = ShowBase()
egg_file = base.loader.loadModel(data)

for tex in render.findAllTextures():
    if tex.get_num_components() == 3:
        tex.setFormat(Texture.F_srgb)
    elif tex.get_num_components() == 4:
        tex.setFormat(Texture.F_srgb_alpha)

name = "/tmp/{0}.bam".format(egg_file.get_name())
egg_file.writeBamFile(name)

