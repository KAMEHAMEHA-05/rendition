import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt

class Object:
    def __init__(self, sx, sy, sz):
        self.sx = sx
        self.sy = sy
        self.sz = sz

class World:
    def __init__(self, xlim, ylim, zlim):
        self.world = np.zeros(shape=(xlim, ylim, zlim), dtype=int)
        self.xlim = xlim
        self.ylim = ylim
        self.zlim = zlim
        print(self.world.shape)
    
    def place(self, object, px, py, pz):
        sx = object.sx
        sy = object.sy
        sz = object.sz
        for x in range(px, px+sx):
            for y in range(py, py+sy):
                for z in range(pz, pz+sz):
                    self.world[z, y, x] = 1

class Frame:
    def __init__(self, world, angle, aspect, dims, render_distance):
        self.world = world
        self.angle = angle
        self.dims = dims
        self.aspect = aspect
        self.frame = np.zeros(dims)
        self.render_distance = render_distance

    def layer(self, coord, lx, ly):
        x, y, z = coord

        lx1 = int(max(0, x-lx/2))
        lx2 = int(min(lx/2+x, self.world.xlim))

        ly1 = int(max(0, y-ly/2))
        ly2 = int(min(ly/2+y, self.world.ylim))

        z = int(min(max(0, z), self.world.zlim))
        print(lx1, lx2, ly1, ly2, z)

        layer = self.world.world[z, ly1:ly2, lx1:lx2]

        return layer

    def render(self, coord):
        chunk = np.array([])
        rendition = self.frame
        ax, ay = self.angle
        lx, ly = self.dims
        i=0
        while i<self.render_distance:
            layer = self.layer(coord, lx, ly)
            # print(layer.shape)
            layer = resize(layer, self.dims)
            layer*=(1-0.01*i)
            np.append(chunk, layer)
            rendition = np.logical_or(rendition, layer)
            # print(np.sum(rendition))
            # plt.imshow(rendition, cmap='gray')
            # plt.show()
            lx*=ax
            ly*=ay
            i+=1
            coord[2]+=1

        self.frame = rendition

        return self.frame


world = World(1000, 1000, 1000)
b1 = Object(100, 100, 500)
b2 = Object(100, 100, 500)
# b3 = Object(10, 10, 10)
# b4 = Object(10, 20, 20)

world.place(b1, 100, 0, 0)
world.place(b2, 300, 0, 0)
# world.place(b3, 210, 0, 50)
# world.place(b4, 310, 0, 50)
# plt.imshow(world.world[0], cmap='gray')
# plt.show()
# print(np.sum(world.world))

cam = Frame(world, (1.02, 1.02), (4, 3), (100, 100), 50)
cam.render([250, 50, 0])

print(cam.frame.shape)
plt.imshow(cam.frame, cmap='gray')
plt.show()