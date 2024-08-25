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
        color_scheme_seed=colors.LIGHT_BLUE,
        font_family="RobotoLight",
        use_material3=True,
        page_transitions=PageTransitionsTheme(
            **{page.platform.value:PageTransitionTheme.CUPERTINO}
        )
    )
    
    page.dark_theme = Theme(
        **page.theme.__dict__
    )
    
    page.dark_theme.color_scheme_seed = page.theme.color_scheme_seed + "_accent"
    
    page.fonts = {
        "TwCenMT": "TCM_____.TTF ",
        "TwCenMTBold": "TCB_____.TTF ",
        "TwCenMTExtraBold": "TCCEB.TTF ",
        "LeelawadeeUISemiLight": "LeelUIsl.ttf",
        "LeelawadeeUI":"LeelawUI.ttf",
        "LeelawadeeUIBold": "LeelaUIb.ttf ",
        "RobotoThin": "Roboto-Thin.ttf",
        "RobotoLight": "Roboto-Light.ttf",
        "RobotoRegular": "Roboto-Regular.ttf",
        "RobotoMedium": "Roboto-Medium.ttf",
        "RobotoBold": "Roboto-Bold.ttf",
        "RobotoBlack": "Roboto-Black.ttf",
        "RobotoThinItalic": "Roboto-ThinItalic.ttf",
        "RobotoLightItalic": "Roboto-LightItalic.ttf",
        "RobotoRegularItalic": "Roboto-RegularItalic.ttf",
        "RobotoMediumItalic": "Roboto-MediumItalic.ttf",
        "RobotoBoldItalic": "Roboto-BoldItalic.ttf",
        "RobotoBlackItalic": "Roboto-BlackItalic.ttf",
    }
    
    #page.theme_mode = ThemeMode.DARK
    #page.platform = page.platform.IOS
    
    
    page.bgcolor = colors.ON_INVERSE_SURFACE #colors.with_opacity(0.6, page.theme.color_scheme_seed)
    #page.theme.page_transitions.__setattr__(page.platform.value, PageTransitionTheme.CUPERTINO)
    
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    
    page.padding = 0
    

    # Matricule/Email Input
    matricule_input = TextField(
        label="Matricule",
        label_style=TextStyle(color=colors.OUTLINE),
        border_color=colors.OUTLINE_VARIANT,
        bgcolor=colors.ON_INVERSE_SURFACE,
        border_radius=20,
        focused_border_color=colors.SECONDARY,
        focused_border_width=1,
        text_style=TextStyle(font_family="RobotoRegular"),
        content_padding=padding.symmetric(12, 20),
        input_filter=NumbersOnlyInputFilter(),
        on_submit=lambda e: password_input.focus(),
        on_focus=lambda e: e.control.label_style.__setattr__("color", colors.ON_BACKGROUND) or e.control.update(),
        on_blur=lambda e: e.control.label_style.__setattr__("color", colors.OUTLINE) or e.control.update()
    )


    # Password Input
    password_input = TextField(
        label="Mot de passe",
        label_style=TextStyle(color=colors.OUTLINE),
        border_color=colors.OUTLINE_VARIANT,
        bgcolor=colors.ON_INVERSE_SURFACE,
        border_radius=20,
        focused_border_color=colors.SECONDARY,
        focused_border_width=1,
        password=True,
        can_reveal_password=True,
        text_style=TextStyle(font_family="RobotoRegular"),
        content_padding=padding.symmetric(12, 20),
        on_submit=lambda e: connection_button_click(e),
        on_focus=lambda e: e.control.label_style.__setattr__("color", colors.ON_BACKGROUND) or e.control.update(),
        on_blur=lambda e: e.control.label_style.__setattr__("color", colors.OUTLINE) or e.control.update()
    )
    
    error_text = Text(
        "Informations incorrectes",
        size=15,
        font_family="RobotoLight",
        text_align=TextAlign.CENTER,
        color=colors.ERROR,
        width=page.width,
        visible=False
    )


    # Layout
    page.add(
        ResponsiveRow(
            [
                Container(
                    Stack(
                        [
                            Container(
                                Column(
                                    [
                                        Text(
                                            "SQUIMA",
                                            size=24,
                                            font_family="RobotoMedium",
                                            text_align=TextAlign.CENTER
                                        ),
                                        
                                        Text(
                                            "Connectez-vous à votre compte",
                                            font_family="RobotoLight",
                                            size=16,
                                            text_align=TextAlign.CENTER
                                        ),
                                        
                                        Column(
                                            [
                                                error_text,
                                                Stack(
                                                    [
                                                        matricule_input,
                                                        IconButton(
                                                            icons.EMAIL_OUTLINED,
                                                            icon_color=colors.PRIMARY,
                                                            selected_icon=icons.PIN_OUTLINED,
                                                            on_click=lambda e: e.control.__setattr__("selected", not e.control.selected) or not (d:=matricule_input.__dict__) or d.update(input_filter=None if e.control.selected else NumbersOnlyInputFilter(), label="Addresse mail" if e.control.selected else "Matricule", value= "") or matricule_input.__setattr__("__dict__", d) or page.update(),
                                                            top=0,
                                                            bottom=0,
                                                            right=3
                                                        )
                                                    ]
                                                ),
                                                password_input,
                                                    
                                                Text(
                                                    spans=[
                                                        TextSpan(
                                                            "Mot de passe oublié ?",
                                                            on_click=lambda e: e.control.__setattr__("style", TextStyle(color=page.theme.color_scheme_seed)) or e.control.update() or forgot_password_button_click(e),
                                                            on_enter=lambda e: e.control.__setattr__("style", TextStyle(color=colors.PRIMARY)) or e.control.update(),
                                                            on_exit=lambda e: e.control.__setattr__("style", TextStyle(color=colors.ON_BACKGROUND)) or e.control.update()
                                                        ),
                                                    ]
                                                )
                                            ],
                                            horizontal_alignment=CrossAxisAlignment.END,
                                            spacing=15
                                        ),
                                        
                                        FilledButton(
                                            content=Text(
                                                "Connexion",
                                                size=16,
                                                font_family="RobotoRegular"
                                            ),
                                            on_click=lambda e: connection_button_click(page, matricule_input.value, password_input.value),
                                            style=ButtonStyle(
                                                padding=padding.symmetric(horizontal=50, vertical=0),
                                                bgcolor=page.theme.color_scheme_seed
                                            ),
                                            width=page.width
                                        ),
                                        
                                        Row(
                                            [
                                                TextButton(
                                                    content=Text(
                                                        key,
                                                        size=16,
                                                        color=colors.ON_PRIMARY_CONTAINER,
                                                        font_family="TwCenMT" if key=="G" else "LeelawadeeUI",
                                                        weight=FontWeight.BOLD,
                                                    ),
                                                    style=ButtonStyle(
                                                        side=BorderSide(1, colors.OUTLINE_VARIANT),
                                                        shape=CircleBorder(),
                                                        bgcolor=colors.ON_INVERSE_SURFACE
                                                    ),
                                                    url=f"https://{value}"
                                                ) for key, value in {"G": "goole.com", "f": "facebook.com", "In": "linkedin.com"}.items()
                                            ],
                                            spacing=0,
                                            alignment=MainAxisAlignment.CENTER
                                        )
                                    ],
                                    spacing=20,
                                    tight=True,
                                    horizontal_alignment=CrossAxisAlignment.CENTER
                                ),
                                border=border.all(1, colors.OUTLINE_VARIANT), # if page.width > 400 else None,
                                border_radius=20,
                                bgcolor=colors.BACKGROUND,
                                padding=Padding(20, 70, 20, 20),
                                margin=margin.only(top=50, left=20, right=20),
                                width=350 if page.width > 350 else None,
                            ),
                            
                            Container(
                                Image(
                                    "photo copy.png",
                                    color=colors.with_opacity(1, page.theme.color_scheme_seed),
                                    fit=ImageFit.CONTAIN,
                                    color_blend_mode=BlendMode.MODULATE,
                                    filter_quality=FilterQuality.HIGH
                                ),
                                border=border.all(1, colors.OUTLINE_VARIANT),
                                border_radius=20,
                                bgcolor=colors.SECONDARY_CONTAINER,
                                width=100,
                                height=100,
                                padding=10,
                                shape=BoxShape.CIRCLE,
                                left=0,
                                right=0
                            ),
                        ]
                    ),
                    alignment=alignment.center,
                    bgcolor=colors.ON_INVERSE_SURFACE,
                    margin=0 if page.width > 400 else 0,
                    border_radius=border_radius.horizontal(0, right=0) if page.width > 400 else 0,
                    col={"md": 6, "lg": 5}
                ),
                
                Container(
                    Column(
                        [
                            Text(
                                "SQUIMA",
                                font_family="RobotoBold",
                                text_align=TextAlign.CENTER,
                                size=30,
                                width=page.width
                            ),
                            
                            Text(
                                "Une solution pour la gestion effica et intelligente de vos évaluations.\nAutomatisez la création, la distribution et la correction des évaluations.",
                                size=18,
                                text_align=TextAlign.CENTER,
                                width=page.width
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=MainAxisAlignment.CENTER,
                        spacing=30
                    ),
                    height=page.height,
                    bgcolor=colors.with_opacity(0.5, page.theme.color_scheme_seed),
                    margin=8,
                    border_radius=border_radius.horizontal(10, 10),
                    alignment=alignment.center,
                    padding=padding.symmetric(30, 50),
                    col={"xs": 0, "md": 6, "lg": 7}
                )
            ],
            expand=True,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER
        )
    )

def connection_button_click(page: Page, matricule: str, password: str):
    ...
    # Validation et vérification dans la base de données
    # ... (Remplacez par votre logique de validation et de vérification)
    # ...

    # Si la connexion est réussie, redirigez vers la page d'accueil
    # ... (Remplacez par votre logique de redirection)
    # ...

    # Sinon, affichez un message d'erreur
    # ... (Remplacez par votre logique d'affichage d'erreur)
    # ...

def forgot_password_button_click(page: Page):
    ...
    # Redirigez vers la page de réinitialisation du mot de passe
    # ... (Remplacez par votre logique de redirection)
    # ...


#import logging; logging.basicConfig(level=logging.INFO)

#app(target=main); exit()

import asyncio
import logging
from typing import Optional

import flet.fastapi
import flet.fastapi as flet_fastapi
import uvicorn, os, flet_runtime
from pathlib import Path
from flet_core.types import WebRenderer

logger = logging.getLogger(flet_fastapi.__name__)

log_level = logging.getLogger(flet_runtime.__name__).getEffectiveLevel()
if log_level == logging.CRITICAL or log_level == logging.NOTSET:
    log_level = logging.FATAL

app = flet.fastapi.FastAPI()

env_port = os.getenv("FLET_SERVER_PORT")
port = int(env_port) or 8000 if env_port else 8000

host = os.getenv("FLET_SERVER_IP") or "localhost"

def sub_main(page: Page):
    page.add(Text("This is sub app!"))

app.mount("/app", flet_fastapi.app(sub_main))

app.mount(
        "/",
        flet.fastapi.app(
            main,
            assets_dir=Path(__file__).parent / "assets"
        )
)


config = uvicorn.Config(app, host=host, port=port, log_level=log_level)
server = uvicorn.Server(config)

asyncio.run(server.serve())
