# The end of the tunnel

import matplotlib.pyplot as plt
import numpy as np
import copy


class Block:

    def __init__(self, corner_coords, index=1, color="b"):
        x1 = corner_coords[0][0]
        y1 = corner_coords[0][1]
        x2 = corner_coords[1][0]
        y2 = corner_coords[1][1]
        x_center = (x1 + x2)/2
        y_center = (y1 + y2)/2
        dx = x2 - x1
        dy = y2 - y1
        self.corners = [
            (x1, y1),
            (x_center + (-dy/2), y_center + (dx/2)),
            (x2, y2),
            (x_center + (dy/2), y_center + (-dx/2)),
        ]
        self.index = index
        self.color = color
        self.polygon = self.corners + [self.corners[0]]
        self.x = []
        self.y = []
        for coords in self.polygon:
            self.x.append(coords[0])
            self.y.append(coords[1])


class Ray:

    def __init__(self, start, angle, color="r"):
        self.x = start[0]
        self.y = start[1]
        self.angle = angle
        self.color = color


class Tunnel:

    def __init__(self, index=1, mode="all", dl=0.001, max_l=5):  # mode : all, refract, reflect
        self.index = index
        self.mode = mode
        self.rays = []
        self.blocks = []
        self.dl = dl
        self.max_l = max_l
        self.rays = []
        self.ray_lines = []

    def add_ray(self, ray):
        ray.env = "none"
        self.rays.append(ray)

    def add_block(self, block):
        self.blocks.append(block)

    def segment_length(self, p, q):
        return np.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)

    def on_segment(self, p, q, r):
        return (
            min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1])
        )

    def intersection(self, p1, q1, p2, q2):
        (xp1, yp1) = p1
        (xq1, yq1) = q1
        (xp2, yp2) = p2
        (xq2, yq2) = q2

        a1 = yq1 - yp1
        b1 = xp1 - xq1
        c1 = a1*xp1 + b1*yp1

        a2 = yq2 - yp2
        b2 = xp2 - xq2
        c2 = a2*xp2 + b2*yp2

        det = a1*b2 - a2*b1

        if det == 0:
            return None

        x = (b2*c1 - b1*c2) / det
        y = (a1*c2 - a2*c1) / det

        pt = (x, y)

        if self.on_segment(p1, pt, q1) and self.on_segment(p2, pt, q2):
            return pt

        return None

    def find_ang(self, p, q):
        if q[0] - p[0] == 0:
            line_ang = np.pi/2
        else:
            rat = (q[1] - p[1])/(q[0] - p[0])
            line_ang = np.arctan(abs(rat))*(1 if rat >= 0 else -1)
        return line_ang

    def calculate_rays(self):
        rays_to_draw = copy.deepcopy(self.rays)
        while rays_to_draw != []:
            current_ray = rays_to_draw[0]
            print(current_ray.x, current_ray.y, current_ray.angle)
            p1 = (current_ray.x, current_ray.y)
            angle = current_ray.angle
            dx = np.cos(angle)*self.dl
            dy = np.sin(angle)*self.dl
            q1 = (current_ray.x + dx, current_ray.y + dy)
            color = current_ray.color
            limit_reached = False
            while not limit_reached:
                if self.segment_length(p1, q1) >= self.max_l:
                    self.ray_lines.append([p1, q1, current_ray.color])
                    limit_reached = True
                else:
                    for block in self.blocks:
                        n_of_points = len(block.x)
                        for line in range(n_of_points):
                            m = (line + 1) % n_of_points
                            p2 = (block.x[line],  block.y[line])
                            q2 = (block.x[m],  block.y[m])
                            intersection = self.intersection(p1, q1, p2, q2)
                            if intersection is not None:
                                self.ray_lines.append([p1, q1, color])
                                line_ang = self.find_ang(p2, q2)
                                i = (-np.pi/2) + angle - line_ang
                                sin = np.sin(i)
                                if current_ray.env == "none":
                                    print("case1")
                                    if sin < block.index/self.index:
                                        r = -np.arcsin(
                                            (self.index/block.index)*np.cos(line_ang - angle))
                                        new_angle = r + line_ang - np.pi/2
                                        print("new ray :", new_angle *
                                              (180/np.pi), q1)
                                        new_ray = Ray(
                                            q1, new_angle, color="b"
                                        )
                                        new_ray.env = block
                                        rays_to_draw.append(new_ray)
                                elif current_ray.env == block:
                                    print("case2")
                                    if sin < self.index/block.index:
                                        r = -np.arcsin(
                                            (self.index/block.index)*np.cos(line_ang - angle))
                                        new_angle = r + line_ang - np.pi/2
                                        print("new ray :", new_angle *
                                              (180/np.pi), q1)
                                        new_ray = Ray(
                                            q1, new_angle, color="g"
                                        )
                                        new_ray.env = "none"
                                        rays_to_draw.append(new_ray)
                                else:
                                    raise Exception(
                                        "dont know how to handle this")
                                limit_reached = True
                    q1 = (q1[0] + dx, q1[1] + dy)

            rays_to_draw.pop(0)

    def show(self):
        fig, ax = plt.subplots()

        for block in self.blocks:
            plt.plot(block.x, block.y, color=block.color)

        for line in self.ray_lines:
            plt.plot(
                [line[0][0], line[1][0]],
                [line[0][1], line[1][1]],
                color=line[2])

        plt.show()


t = Tunnel(max_l=2)
b = Block([[1, 1], [0, 0]], index=1)
t.add_block(b)

r = Ray((-1, 0.5), np.pi/180 * 20)
t.add_ray(r)
t.calculate_rays()
t.show()
