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
MORE_BLUE_COLOR = "#4877a0"

"""
The linear_plot_updater function that 
"""

class video_intro(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Text("Функции", color=BEIGE_COLOR, font_size=120)
        title_top_left = Text("Функции", color=BEIGE_COLOR, font_size=45).to_corner(UL)
        subtitle = Text("V - Трансформации", color=BEIGE_COLOR, font_size=80)

        self.play(Write(title))
        self.wait()

        self.play(Transform(title, title_top_left), run_time=0.75)
        self.wait(0.25)

        self.play(Write(subtitle))
        self.wait(1.5)

        self.play(Unwrite(title), Unwrite(subtitle), run_time=0.5)
        self.wait()

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
        ## CACHING MESSES THIS UP, BE CAREFUL
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

# Graphs f(x) = g(x) + a
class vertical_translation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        left_end = ValueTracker(-5)
        right_end = ValueTracker(5)
        mending_point = ValueTracker(-1)
        def linear_plot_updater(mobj, plane, x_range, y_range, a, b, color_to_set_to):
            if mending_point is not None:
                x_range = [
                    x_range[0].get_value(),  # Left limit
                    x_range[1].get_value()  # Update dynamically
                ]
            #print(x_range[1], mending_point.get_value())
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
                plane.plot(
                    lambda x: a.get_value()*x+b.get_value(),
                    x_range=xr,
                ).set_color(color_to_set_to)
            )
        ## CACHING MESSES THIS UP, BE CAREFUL

        num_plane = always_redraw(
            lambda:
            NumberPlane(
                x_range=[-5, 5, 5],
                y_range=[-5, 5, 5],
                x_length=5,
                y_length=5,
                faded_line_ratio=5,
            )
        )

        orig_func_left_a = ValueTracker(-4)
        orig_func_left_b = ValueTracker(-8)
        orig_func_right_a = ValueTracker(1)
        orig_func_right_b = ValueTracker(-3)
        other_func_left_a = ValueTracker(-4)
        other_func_left_b = ValueTracker(-8)
        other_func_right_a = ValueTracker(1)
        other_func_right_b = ValueTracker(-3)

        orig_func_left = VMobject()
        orig_func_right = VMobject()
        other_func_left = VMobject()
        other_func_right = VMobject()
        
        ORIG_FUNC_COLOR = MORE_BLUE_COLOR
        OTHER_FUNC_COLOR = BLUE_COLOR

        orig_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=orig_func_left_a,
            b=orig_func_left_b,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_left.add_updater(orig_func_left_updater)
        
        orig_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=orig_func_right_a,
            b=orig_func_right_b,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_right.add_updater(orig_func_right_updater)
        
        other_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=other_func_left_a,
            b=other_func_left_b,
            color_to_set_to=OTHER_FUNC_COLOR
        )
        other_func_left.add_updater(other_func_left_updater)
        
        other_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=other_func_right_a,
            b=other_func_right_b,
            color_to_set_to=OTHER_FUNC_COLOR
        )
        other_func_right.add_updater(other_func_right_updater)

        some_stupid_label = always_redraw(
            lambda: (
                MathTex(
                    "f(x)",
                    "=",
                    "g(x)",
                    ("+" if other_func_left_b.get_value() - orig_func_left_b.get_value() >= 0 else "-"),
                    "{:.2f}".format(abs(other_func_left_b.get_value() - orig_func_left_b.get_value())),
                    font_size=40
                ).set_color(BEIGE_COLOR)
                .set_color_by_tex("f(x)", color=OTHER_FUNC_COLOR)
                .set_color_by_tex("g(x)", color=ORIG_FUNC_COLOR)
            ).next_to(num_plane.get_bottom(), DOWN)
            .align_to(num_plane.get_left(), LEFT)
        )

        self.add(num_plane, some_stupid_label)
        self.add(orig_func_left, orig_func_right)
        self.add(other_func_left, other_func_right)
        self.play(orig_func_left_a.animate.set_value(orig_func_left_a.get_value()),
                  orig_func_right_a.animate.set_value(orig_func_right_a.get_value()),
                  run_time=0.001)
        self.wait()
        self.play(other_func_left_b.animate.set_value(other_func_left_b.get_value() + 5),
                  other_func_right_b.animate.set_value(other_func_right_b.get_value() + 5),
                  run_time = 1)
        self.wait()
        self.play(other_func_left_b.animate.set_value(other_func_left_b.get_value() - 7),
                  other_func_right_b.animate.set_value(other_func_right_b.get_value() - 7),
                  run_time = 1)
        self.wait()
        self.play(other_func_left_b.animate.set_value(other_func_left_b.get_value() + 2),
                  other_func_right_b.animate.set_value(other_func_right_b.get_value() + 2),
                  run_time = 1)
        self.wait()

# Graphs f(x) = g(x + a)
class horizontal_translation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        left_end = ValueTracker(-5)
        right_end = ValueTracker(5)
        mending_point = ValueTracker(-1)
        
        def linear_plot_updater(mobj, plane, x_range, y_range, a, b, J, color_to_set_to, is_silly=False, is_left_to_mending_point = False):
            if mending_point is not None:
                if not is_silly:
                    x_range = [
                        x_range[0].get_value() - J.get_value(),
                        x_range[1].get_value() - J.get_value()
                    ]
                else:
                    if is_left_to_mending_point:
                        x_range = [
                            x_range[0].get_value(),
                            x_range[1].get_value() - J.get_value()
                        ]
                    else:
                        x_range = [
                            x_range[0].get_value() - J.get_value(),
                            x_range[1].get_value()
                        ]
            #print(x_range[1], mending_point.get_value())
            xr = [
                (y_range[0]-b.get_value())/a.get_value() - J.get_value(),
                (y_range[1]-b.get_value())/a.get_value() - J.get_value()
            ]
            xr.sort() ## is this needed ??
            xr = [
                max(xr[0],x_range[0]),
                min(xr[1],x_range[1])
            ]
            mobj.become(
                plane.plot(
                    lambda x: a.get_value()*(x + J.get_value())+b.get_value(),
                    x_range=xr,
                ).set_color(color_to_set_to)
            )
        ## CACHING MESSES THIS UP, BE CAREFUL

        num_plane = always_redraw(
            lambda:
            NumberPlane(
                x_range=[-5, 5, 5],
                y_range=[-5, 5, 5],
                x_length=5,
                y_length=5,
                faded_line_ratio=5,
            )
        )

        orig_func_left_a = ValueTracker(-4)
        orig_func_left_b = ValueTracker(-8)
        orig_func_right_a = ValueTracker(1)
        orig_func_right_b = ValueTracker(-3)
        other_func_left_a = ValueTracker(-4)
        other_func_left_b = ValueTracker(-8)
        other_func_right_a = ValueTracker(1)
        other_func_right_b = ValueTracker(-3)
        other_func_addition = ValueTracker(0)
        empty_tracker = ValueTracker(0)

        orig_func_left = VMobject()
        orig_func_right = VMobject()
        other_func_left = VMobject()
        other_func_right = VMobject()

        ORIG_FUNC_COLOR = MORE_BLUE_COLOR
        OTHER_FUNC_COLOR = BLUE_COLOR

        orig_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=orig_func_left_a,
            b=orig_func_left_b,
            J=empty_tracker,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_left.add_updater(orig_func_left_updater)
        
        orig_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=orig_func_right_a,
            b=orig_func_right_b,
            J=empty_tracker,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_right.add_updater(orig_func_right_updater)
        
        other_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=other_func_left_a,
            b=other_func_left_b,
            J=other_func_addition,
            color_to_set_to=OTHER_FUNC_COLOR,
            is_silly=True,
            is_left_to_mending_point=True
        )
        other_func_left.add_updater(other_func_left_updater)
        
        other_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=other_func_right_a,
            b=other_func_right_b,
            J=other_func_addition,
            color_to_set_to=OTHER_FUNC_COLOR,
            is_silly=True,
            is_left_to_mending_point=False
        )
        other_func_right.add_updater(other_func_right_updater)

        some_stupid_label = always_redraw(
            lambda: (MathTex(
                "f(x)",
                "=",
                "g(x",
                ("+" if other_func_addition.get_value() >= 0 else "-"),
                "{:.2f}".format(abs(other_func_addition.get_value())),
                ")",
                font_size=40
            ).set_color(BEIGE_COLOR)
            .set_color_by_tex(")", color=ORIG_FUNC_COLOR)
            .set_color_by_tex("g(x", color=ORIG_FUNC_COLOR)
            .set_color_by_tex("f(x)", color=OTHER_FUNC_COLOR)
            ).next_to(num_plane.get_bottom(), DOWN)
            .align_to(num_plane.get_left(), LEFT)
        )

        self.add(num_plane, some_stupid_label)
        self.add(orig_func_left, orig_func_right)
        self.add(other_func_left, other_func_right)
        self.play(orig_func_left_a.animate.set_value(orig_func_left_a.get_value()),
                  orig_func_right_a.animate.set_value(orig_func_right_a.get_value()),
                  run_time=0.001)
        self.wait()
        self.play(other_func_addition.animate.set_value(2), run_time=1)
        self.wait()
        self.play(other_func_addition.animate.set_value(-3), run_time=1)
        self.wait()
        self.play(other_func_addition.animate.set_value(0), run_time=1)
        self.wait()

# Graphs f(x) = g(x) * a
class vertical_scaling(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        left_end = ValueTracker(-5)
        right_end = ValueTracker(5)
        mending_point = ValueTracker(-1)
        
        def linear_plot_updater(mobj, plane, x_range, y_range, a, b, J, color_to_set_to):
            if mending_point is not None:
                x_range = [
                    x_range[0].get_value(),
                    x_range[1].get_value()
                ]
            #print(x_range[1], mending_point.get_value())
            xr = [
                ((y_range[0] / J.get_value()) - b.get_value()) / a.get_value(),
                ((y_range[1] / J.get_value()) - b.get_value()) / a.get_value()
            ]
            xr.sort() ## is this needed ??
            xr = [
                max(xr[0],x_range[0]),
                min(xr[1],x_range[1])
            ]
            mobj.become(
                plane.plot(
                    lambda x: (a.get_value()*x+b.get_value()) * J.get_value(),
                    x_range=xr,
                ).set_color(color_to_set_to)
            )
        ## CACHING MESSES THIS UP, BE CAREFUL

        num_plane = always_redraw(
            lambda:
            NumberPlane(
                x_range=[-5, 5, 5],
                y_range=[-5, 5, 5],
                x_length=5,
                y_length=5,
                faded_line_ratio=5,
            )
        )

        # -4x - 8
        orig_func_left_a = ValueTracker(-4)
        orig_func_left_b = ValueTracker(-8)
        # x - 3
        orig_func_right_a = ValueTracker(1)
        orig_func_right_b = ValueTracker(-3)
        other_func_left_a = ValueTracker(-4)
        other_func_left_b = ValueTracker(-8)
        other_func_right_a = ValueTracker(1)
        other_func_right_b = ValueTracker(-3)
        scaling_factor = ValueTracker(1)
        empty_tracker = ValueTracker(1)

        orig_func_left = VMobject()
        orig_func_right = VMobject()
        other_func_left = VMobject()
        other_func_right = VMobject()

        ORIG_FUNC_COLOR = MORE_BLUE_COLOR
        OTHER_FUNC_COLOR = BLUE_COLOR

        orig_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=orig_func_left_a,
            b=orig_func_left_b,
            J=empty_tracker,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_left.add_updater(orig_func_left_updater)
        
        orig_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=orig_func_right_a,
            b=orig_func_right_b,
            J=empty_tracker,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_right.add_updater(orig_func_right_updater)
        
        other_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=other_func_left_a,
            b=other_func_left_b,
            J=scaling_factor,
            color_to_set_to=OTHER_FUNC_COLOR
        )
        other_func_left.add_updater(other_func_left_updater)
        
        other_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=other_func_right_a,
            b=other_func_right_b,
            J=scaling_factor,
            color_to_set_to=OTHER_FUNC_COLOR
        )
        other_func_right.add_updater(other_func_right_updater)

        some_stupid_label = always_redraw(
            lambda: (MathTex(
                "f(x)",
                "=",
                "g(x)",
                "*",
                "{:.2f}".format(scaling_factor.get_value()),
                font_size=40
            ).set_color(BEIGE_COLOR)
            .set_color_by_tex("f(x)", color=OTHER_FUNC_COLOR)
            .set_color_by_tex("g(x)", color=ORIG_FUNC_COLOR)
            #.set_color_by_tex("{:.2f}".format(scaling_factor.get_value()), color=OTHER_FUNC_COLOR)  # Set color for the value part
            ).next_to(num_plane.get_bottom(), DOWN)
            .align_to(num_plane.get_left(), LEFT)
        )

        self.add(num_plane, some_stupid_label)
        self.add(orig_func_left, orig_func_right)
        self.add(other_func_left, other_func_right)
        self.play(orig_func_left_a.animate.set_value(orig_func_left_a.get_value()),
                  orig_func_right_a.animate.set_value(orig_func_right_a.get_value()),
                  run_time=0.001)
        self.wait()
        self.play(scaling_factor.animate.set_value(3), run_time=1)
        self.wait()
        self.play(scaling_factor.animate.set_value(0.5), run_time=1)
        self.wait()
        self.play(scaling_factor.animate.set_value(1), run_time=1)
        self.wait()

# Graphs f(x) = g(x * a)
class horizontal_scaling(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        left_end = ValueTracker(-5)
        right_end = ValueTracker(5)
        mending_point = ValueTracker(-1)
        
        def linear_plot_updater(mobj, plane, x_range, y_range, a, b, J, color_to_set_to, is_left = False):
            if mending_point is not None:
                if is_left:
                    x_range = [
                        x_range[0].get_value(),
                        x_range[1].get_value() / J.get_value()
                    ]
                else:
                    x_range = [
                        x_range[0].get_value() / J.get_value(),
                        x_range[1].get_value()
                    ]
            #print(x_range[1], mending_point.get_value())
            xr = [
                ((y_range[0]) - b.get_value()) / a.get_value() / J.get_value(),
                ((y_range[1]) - b.get_value()) / a.get_value() / J.get_value()
            ]
            xr.sort() ## is this needed ??
            xr = [
                max(xr[0],x_range[0]),
                min(xr[1],x_range[1])
            ]
            mobj.become(
                plane.plot(
                    lambda x: (a.get_value() * x * J.get_value() + b.get_value()),
                    x_range=xr,
                ).set_color(color_to_set_to)
            )
        ## CACHING MESSES THIS UP, BE CAREFUL

        num_plane = always_redraw(
            lambda:
            NumberPlane(
                x_range=[-5, 5, 5],
                y_range=[-5, 5, 5],
                x_length=5,
                y_length=5,
                faded_line_ratio=5,
            )
        )

        # -4x - 8
        orig_func_left_a = ValueTracker(-4)
        orig_func_left_b = ValueTracker(-8)
        # x - 3
        orig_func_right_a = ValueTracker(1)
        orig_func_right_b = ValueTracker(-3)
        other_func_left_a = ValueTracker(-4)
        other_func_left_b = ValueTracker(-8)
        other_func_right_a = ValueTracker(1)
        other_func_right_b = ValueTracker(-3)
        scaling_factor = ValueTracker(1)
        empty_tracker = ValueTracker(1)

        orig_func_left = VMobject()
        orig_func_right = VMobject()
        other_func_left = VMobject()
        other_func_right = VMobject()

        ORIG_FUNC_COLOR = MORE_BLUE_COLOR
        OTHER_FUNC_COLOR = BLUE_COLOR

        orig_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=orig_func_left_a,
            b=orig_func_left_b,
            J=empty_tracker,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_left.add_updater(orig_func_left_updater)
        
        orig_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=orig_func_right_a,
            b=orig_func_right_b,
            J=empty_tracker,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_right.add_updater(orig_func_right_updater)
        
        other_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=other_func_left_a,
            b=other_func_left_b,
            J=scaling_factor,
            is_left = True,
            color_to_set_to=OTHER_FUNC_COLOR
        )
        other_func_left.add_updater(other_func_left_updater)
        
        other_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=other_func_right_a,
            b=other_func_right_b,
            J=scaling_factor,
            color_to_set_to=OTHER_FUNC_COLOR
        )
        other_func_right.add_updater(other_func_right_updater)

        some_stupid_label = always_redraw(
            lambda: (MathTex(
                "f(x)",
                "=",
                "g(x",
                "*",
                "{:.2f}".format(scaling_factor.get_value()),
                ")",
                font_size=40
            ).set_color(BEIGE_COLOR)
            .set_color_by_tex(")", color=ORIG_FUNC_COLOR)
            .set_color_by_tex("f(x)", color=OTHER_FUNC_COLOR)
            .set_color_by_tex("g(x", color=ORIG_FUNC_COLOR)
            #.set_color_by_tex("{:.2f}".format(scaling_factor.get_value()), color=OTHER_FUNC_COLOR)  # Set color for the value part
            ).next_to(num_plane.get_bottom(), DOWN)
            .align_to(num_plane.get_left(), LEFT)
        )

        self.add(num_plane, some_stupid_label)
        self.add(orig_func_left, orig_func_right)
        self.add(other_func_left, other_func_right)
        self.play(orig_func_left_a.animate.set_value(orig_func_left_a.get_value()),
                  orig_func_right_a.animate.set_value(orig_func_right_a.get_value()),
                  run_time=0.001)
        self.wait()
        self.play(scaling_factor.animate.set_value(3), run_time=1)
        self.wait()
        self.play(scaling_factor.animate.set_value(0.5), run_time=1)
        self.wait()
        self.play(scaling_factor.animate.set_value(1), run_time=1)
        self.wait()