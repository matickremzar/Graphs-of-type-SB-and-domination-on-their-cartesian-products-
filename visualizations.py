from manim import *

class GraphPlanarDegrees(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"
        g = Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [(1, 2), (1, 3), (1, 4), (1, 5), (2, 6), (2, 7), (2, 8),
                  (3, 9), (4, 10), (5, 11), (6, 9), (7, 10), (8, 11), (5, 7)],
                   layout={
                       1: [-2, -3, 0],
                       2: [2, -3, 0],
                       3: [-3, 0, 0],
                       4: [-3.8, 0, 0],
                       5: [-2.2, 0, 0],
                       6: [3, 0, 0],
                       7: [2.2, 0, 0],
                       8: [3.8, 0, 0],
                       9: [0, 2.8, 0],
                       10: [-0.8, 2.8, 0],
                       11: [0.8, 2.8, 0]
                   },
                   layout_config={"center": [0, 0]}, layout_scale=0.9,
                   vertex_config={
                       1: {"fill_color": BLACK},
                       2: {"fill_color": BLACK},
                       3: {"fill_color": BLACK},
                       4: {"fill_color": RED},
                       5: {"fill_color": RED},
                       6: {"fill_color": BLACK},
                       7: {"fill_color": RED},
                       8: {"fill_color": RED},
                       9: {"fill_color": BLACK},
                       10: {"fill_color": RED},
                       11: {"fill_color": RED}
                   },
                   edge_config={
                       (1, 2): {"stroke_color": BLACK},
                       (1, 3): {"stroke_color": BLACK},
                       (1, 4): {"stroke_color": BLACK},
                       (1, 5): {"stroke_color": BLACK},
                       (2, 6): {"stroke_color": BLACK},
                       (2, 7): {"stroke_color": BLACK},
                       (2, 8): {"stroke_color": BLACK},
                       (3, 9): {"stroke_color": BLACK},
                       (4, 10): {"stroke_color": BLACK},
                       (5, 11): {"stroke_color": BLACK},
                       (6, 9): {"stroke_color": BLACK},
                       (7, 10): {"stroke_color": BLACK},
                       (8, 11): {"stroke_color": BLACK},
                   }
        )

        e1 = g.edges[(1, 4)]
        dashed1 = DashedLine(e1.get_start(), e1.get_end(), dash_length=0.1).set_color(BLACK)

        e2 = g.edges[(1, 5)]
        dashed2 = DashedLine(e2.get_start(), e2.get_end(), dash_length=0.1).set_color(BLACK)

        e3 = g.edges[(2, 7)]
        dashed3 = DashedLine(e3.get_start(), e3.get_end(), dash_length=0.1).set_color(BLACK)

        e4 = g.edges[(2, 8)]
        dashed4 = DashedLine(e4.get_start(), e4.get_end(), dash_length=0.1).set_color(BLACK)

        e5 = g.edges[(4, 10)]
        dashed5 = DashedLine(e5.get_start(), e5.get_end(), dash_length=0.1).set_color(BLACK)

        e6 = g.edges[(5, 11)]
        dashed6 = DashedLine(e6.get_start(), e6.get_end(), dash_length=0.1).set_color(BLACK)

        e7 = g.edges[(7, 10)]
        dashed7 = DashedLine(e7.get_start(), e7.get_end(), dash_length=0.1).set_color(BLACK)

        e8 = g.edges[(8, 11)]
        dashed8 = DashedLine(e8.get_start(), e8.get_end(), dash_length=0.1).set_color(BLACK)

        e9 = g.edges[(5, 7)]
        dashed9 = DashedLine(e9.get_start(), e9.get_end(), dash_length=0.1).set_color(BLACK)

        circle1 = Circle(radius=1.0, fill_color=RED,fill_opacity=1)
        circle1.move_to((-3, 0, 0))
        circle1.z_index=-1

        circle2 = Circle(radius=1.0, fill_color=RED, fill_opacity=1)
        circle2.move_to((3, 0, 0))
        circle2.z_index=-1

        circle3 = Circle(radius=1.0, fill_color=RED, fill_opacity=1)
        circle3.move_to((0, 2.8, 0))
        circle3.z_index=-1

        h1 = Tex('h1', color=BLACK)
        h1.move_to((-2.8, -3.2, 0))

        h2 = Tex('h2', color=BLACK)
        h2.move_to((2.8, -3.2, 0))

        a1 = Tex('A1', color=BLACK)
        a2 = Tex('A2', color=BLACK)
        astar = Tex('A*', color=BLACK)
        a1.move_to((-4.5, 0, 0))
        a2.move_to((4.5, 0, 0))
        astar.move_to((-1.5, 3, 0))

        self.add(circle1, circle2, circle3)
        self.add(g)
        self.add(h1, h2, a1, a2, astar)
        self.remove(e1)
        self.remove(e2)
        self.remove(e3)
        self.remove(e4)
        self.remove(e5)
        self.remove(e6)
        self.remove(e7)
        self.remove(e8)
        self.remove(e9)
        self.add(dashed1)
        self.add(dashed2)
        self.add(dashed3)
        self.add(dashed4)
        self.add(dashed5)
        self.add(dashed6)
        self.add(dashed7)
        self.add(dashed8)
        self.add(dashed9)
