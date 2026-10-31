import numpy as np
import cv2
import matplotlib.pyplot as plt

def graphic_or(arr1, arr2):
    res = np.zeros(shape=arr1.shape, dtype=float)
    count_alt = 0
    for i, (y1, y2) in enumerate(zip(arr1, arr2)):
        for j, (x1, x2) in enumerate(zip(y1, y2)):
            if x1==0:
                res[i, j] = x2
                count_alt+=1
            else:
                res[i, j] = x1
    # print(np.sum(res))
    # print(count_alt)
    return res

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
        # print(lx1, lx2, ly1, ly2, z)

        layer = self.world.world[z, ly1:ly2, lx1:lx2]

        return layer

    def render(self, coord):
        chunk = np.array([])
        rendition = self.frame
        ax, ay = self.angle
        lx, ly = self.dims
        i=0
        while i<self.render_distance:
            layer = np.array(self.layer(coord, lx, ly), dtype=np.uint8)
            # print(layer.shape)
            layer = np.array(cv2.resize(layer, self.dims), dtype=float)
            layer*=(1-0.01*i)
            np.append(chunk, layer)
            rendition = graphic_or(rendition, layer)
            lx*=ax
            ly*=ay
            i+=1
            coord[2]+=1

        self.frame = rendition

        return self.frame


world = World(1000, 1000, 1000)
b1 = Object(100, 30, 500)
b2 = Object(100, 30, 500)

world.place(b1, 100, 0, 0)
world.place(b2, 300, 0, 0)

cam = Frame(world, (1.01, 1.01), (4, 3), (150, 150), 500)
cam.render([250, 50, 0])

print(cam.frame.shape)
plt.imshow(cam.frame, cmap='gray', vmin=0, vmax=1, origin='lower')
plt.show()