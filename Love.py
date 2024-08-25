from flet import *
import threading
from time import sleep


def main(page: Page):
    page.title = "SQUIMA"
    
    page.window.width = 380
    page.window.top = 40
    page.window.left = page.width - page.window.width + 195
    
    page.window.always_on_top = True
    
    page.theme = Theme(
        color_scheme_seed=colors.LIGHT_BLUE
    )
    
    page.theme.page_transitions.__setattr__(page.platform.name, PageTransitionTheme.CUPERTINO)
    
    page.fonts = {
        "Palace Script MT": "ITCEDSCR.ttf"
    }
    
    page.bgcolor = colors.with_opacity(0.95, colors.WHITE)
    
    #page.theme_mode = ThemeMode.DARK
    
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    
    page.spacing = 0
    page.padding = 0
    
    text_widget = Text(
        spans=[
            TextSpan(
                "Julietta",
                TextStyle(
                    size=100,
                    weight=FontWeight.W_500,
                    font_family="Palace Script MT",
                    foreground=Paint(
                        gradient=PaintLinearGradient(
                            (0, 20), (300, 20), [colors.PINK_200, colors.PINK_300]
                        )
                    ),
                ),
            )
        ],
        animate_offset=Animation(1000, AnimationCurve.BOUNCE_IN_OUT),
        offset=Offset(0, 0),
        #on_animation_end=lambda e: not e.control.__setattr__("offset", Offset(0, 0) if e.control.offset == Offset(0, -.02) else Offset(0, -.02)) and e.control.update(),
    )
    
    coeur_battant = Icon(
        icons.FAVORITE_ROUNDED,
        size=60,
        color=colors.PINK_500,
        animate_scale=Animation(500, AnimationCurve.BOUNCE_IN_OUT),
        scale=1,
        offset=Offset(.2, -.4),
        on_animation_end=lambda e: not e.control.__setattr__("scale", 1 if e.control.scale == 1.2 else 1.2) and (sleep(5 if e.control.scale == 1.5 else 0),  e.control.update()),
    )
    
    ombre = Icon(
        icons.FAVORITE_ROUNDED,
        size=60,
        color=colors.PINK_100,
        animate_scale=Animation(500, AnimationCurve.BOUNCE_IN_OUT),
        scale=1,
        offset=Offset(.18, -.38),
        on_animation_end=lambda e: not e.control.__setattr__("scale", 1 if e.control.scale == 1.2 else 1.2) and (sleep(5 if e.control.scale == 1.5 else 0),  e.control.update()),
    )
    
    page.add(
        text_widget,
        Stack([ombre, coeur_battant]),
        Markdown(
            f"""```python\n   while je_suis_vivant:\n \tprint("{text_widget.spans[0].text} 💓")\n```""",
            True,
            MarkdownExtensionSet.GITHUB_WEB,
            "xcode",
            TextStyle(20, font_family="verdana", letter_spacing=1)
        )
    )

    def change_gradient(inc=1):
        nonlocal text_widget  # Declare text_widget as nonlocal to modify it inside the function

        # Define the gradient sequences
        gradient_sequences = [
            [colors.PINK_200],
            [colors.PINK_200, colors.PINK_300],
            [colors.PINK_200, colors.PINK_400],
            [colors.PINK_200, colors.PINK_500],
            [colors.PINK_200, colors.PINK_600],
            [colors.PINK_200, colors.PINK_700],
            [colors.PINK_200, colors.PINK_800],
            [colors.PINK_200, colors.PINK_900],
            [colors.PINK_200, colors.DEEP_PURPLE],
        ]

        # Get the current gradient colors
        current_colors = text_widget.spans[0].style.foreground.gradient.colors

        # Find the index of the current gradient sequence
        current_index = gradient_sequences.index(current_colors)

        # Move to the next gradient sequence (looping back to the beginning)
        next_index = (current_index + inc) % len(gradient_sequences)

        # Update the gradient colors
        text_widget.spans[0].style.foreground.gradient.colors = gradient_sequences[next_index]
        text_widget.update()

        inc = -inc if next_index in (len(gradient_sequences) -1, 0) else inc

        # Schedule the next change
        threading.Timer(.5 if next_index in (len(gradient_sequences) -1, 0) else .2, change_gradient, (inc,)).start()

    # Start the timer
    change_gradient(1)
    
    
    sleep(1)
    
    text_widget.offset=Offset(0, -.02)
    coeur_battant.scale=ombre.scale=1.2
    
    page.update()


app(target=main)
