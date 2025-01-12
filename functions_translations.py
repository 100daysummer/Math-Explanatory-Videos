from manim import *
from functools import partial

BACKGROUND_COLOR = "#12121a"    # button-background-color
PURPLE_COLOR = "#292630"        # article-lighter-background-color
GREEN_COLOR = "#204e49"    # article-border-color
OTHER_BLUE_COLOR = "#375773"          # button-top-border-color
BLUE_COLOR = "#56DCC6"    # content-link-color
LIGHTER_BLUE_COLOR = "#ADEEE3"  # content-visited-link-color
BEIGE_COLOR = "#fff4d9"          # content-text-color
ORANGE_COLOR = "#ffc375"         # button-hover-bottom-border-color
YELLOW_COLOR = "#fdff91"     # button-hover-highlight-color

class testing(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # ax = Axes(x_range=[-3, 3, 1], y_range=[0, 6, 1], x_length=3, y_length=3, color=BEIGE_COLOR, tips=False)\
        #     .to_corner(UL)
        # f1 = ax.plot(lambda x: (1/3)*x**2, color = BLUE_COLOR)
        # f2 = ax.plot(lambda x: (1/3)*x**2+2, color=LIGHTER_BLUE_COLOR)

        # self.add(ax, f1, f2)
        a = ValueTracker(-4)
        b = ValueTracker(-13)
        plane1 = NumberPlane(
            x_range=[-5, 5, 5],
            y_range=[-5, 5, 5],
            x_length=5,
            y_length=5,
            faded_line_ratio=5,
        )

        pplot = VMobject()
        def pplotUpdater(mobj, x_range, y_range):
            xr = [
                (y_range[0]-b.get_value())/a.get_value(),
                (y_range[1]-b.get_value())/a.get_value()
            ]
            xr.sort()
            xr = [
                max(xr[0],x_range[0]),
                min(xr[1],x_range[1])
            ]
            mobj.become(
                plane1.plot(
                    lambda x: a.get_value()*x+b.get_value(),
                    x_range=xr
                )
            )
        pplotUpdaterWithRanges = partial(pplotUpdater, x_range=[-5, -2], y_range=[-5, 5])
        pplot.add_updater(pplotUpdaterWithRanges)

        f2_1 = plane1.plot(
            lambda x: -4 * x - 13,
            x_range=[-4.5, -2]
        ).set_color(BEIGE_COLOR)
        f2_2 = plane1.plot(
            lambda x: 2 * x - 1,
            x_range=[-2, 3]
        ).set_color(BEIGE_COLOR)
        
        self.add(plane1)

        self.add(f2_1, f2_2)
        f3_1 = plane1.plot(
            lambda x: f2_1.underlying_function(x) + 6,
            x_range=[-4, 4]
        )
        self.add(pplot)
        #self.add(f3_1)
        self.wait()
        self.play(b.animate.set_value(-6 ), run_time=2)
        self.wait()

        # label = MathTex("f(x)=sin(\\frac{1}{x})", color=BEIGE_COLOR).to_corner(UL)
        # self.add(label)

        # bla_bla = ValueTracker(1)
        # ax2_and_graph = always_redraw(
        #     lambda: VGroup(
        #         Axes(
        #             x_range=[-bla_bla.get_value(), bla_bla.get_value(), 0.5],
        #             y_range=[-bla_bla.get_value(), bla_bla.get_value(), 0.5],
        #             x_length=7.5,
        #             y_length=7.5,
        #             tips=False
        #         ).set_color(BEIGE_COLOR),
        #         Axes(
        #             x_range=[-bla_bla.get_value(), bla_bla.get_value(), 0.5],
        #             y_range=[-bla_bla.get_value(), bla_bla.get_value(), 0.5],
        #             x_length=7.5,
        #             y_length=7.5,
        #             tips=False
        #         ).plot(
        #             lambda x: np.sin(1 / x),
        #             discontinuities=[0],
        #             dt = 1e-3,
        #             use_smoothing=False,
        #             x_range=[-bla_bla.get_value(), bla_bla.get_value(), bla_bla.get_value()/2000],
        #             color=BLUE_COLOR
        #         )
        #     )
        # )

        # self.add(ax2_and_graph)
        # self.play(bla_bla.animate.set_value(5), run_time=5)
        # self.wait()