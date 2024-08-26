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
        color_scheme_seed=colors.CYAN or colors.LIGHT_BLUE,
        font_family="RobotoLight",
        use_material3=True,
        page_transitions=PageTransitionsTheme(
            **{page.platform.value:PageTransitionTheme.CUPERTINO}
        )
    )
    
    """page.dark_theme = Theme(
        **page.theme.__dict__
    )
    
    page.dark_theme"""
    
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
    
    page.scroll = None if page.width > 800 else ScrollMode.ADAPTIVE
    
    
    page.bgcolor = colors.ON_INVERSE_SURFACE #colors.with_opacity(0.6, page.theme.color_scheme_seed)
    #page.theme.page_transitions.__setattr__(page.platform.value, PageTransitionTheme.CUPERTINO)
    
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    
    page.padding = 0
    
    page.appbar = AppBar(
        leading=IconButton(
            icons.MENU_ROUNDED
        ),
        
        title=Text(
            "SQUIMA",
            font_family="RobotoRegular"
        ),
        
        center_title=True,
        
        actions=[
            IconButton(
                icons.BRIGHTNESS_6_ROUNDED,
                colors.PRIMARY,
                on_click=lambda e: page.__setattr__("theme_mode", ThemeMode.DARK if (page.theme_mode == ThemeMode.SYSTEM and page.platform_brightness == Brightness.LIGHT) or page.theme_mode == ThemeMode.LIGHT else ThemeMode.LIGHT) or page.update()
            ),
            IconButton(
                icons.MORE_VERT_ROUNDED
            )
        ],
        bgcolor=colors.INVERSE_PRIMARY,
        visible=not page.width > 800
    )

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
        keyboard_type=KeyboardType.NUMBER,
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
        on_submit=lambda e: connection_button_click(page, matricule_input, password_input, error_text),
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
    
    # VARIABLES
    page.page_index = 1


    # Layout
    page.add(
        Container(    
                Tabs(
                [
                    Tab(
                        "Accueil",
                        icon=icons.HOME_ROUNDED,
                        #tab_content=Image("home_app_logo.svg")
                    ),
                    Tab(
                        "Professeurs",
                        icon=icons.SUPERVISOR_ACCOUNT_ROUNDED,
                    ),
                    Tab(
                        "Etudiants",
                        icon=icons.GROUPS_ROUNDED,
                    ),
                    Tab(
                        "Finances",
                        icon=icons.PAID_ROUNDED,
                    ),
                    Tab(
                        "Comptes",
                        icon=icons.MANAGE_ACCOUNTS_ROUNDED,
                    ),
                    Tab(
                        "Paramètres",
                        icon=icons.SETTINGS_ROUNDED,
                    )
                ],
                visible=page.width > 800,
                indicator_padding=padding.symmetric(0, 0),
                indicator_thickness=1,
                tab_alignment=TabAlignment.CENTER,
                #indicator_tab_size=True,
                animation_duration=500,
                #divider_height=0,
                #on_change=lambda e: not hasattr(page, "tab_index") and page.__setattr__("tab_index", 0) or e.control.tabs[page.tab_index].__setattr__("icon", e.control.tabs[page.tab_index].icon.removesuffix("rounded")+"outlined") or e.control.tabs[int(e.data)].__setattr__("icon", e.control.tabs[int(e.data)].icon.removesuffix("outlined").removesuffix("rounded")+"rounded") or page.__setattr__("tab_index", int(e.data)) or e.control.update()
            ),
            bgcolor=colors.INVERSE_PRIMARY,
            visible=False
        ),
        
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
                                            visible=not page.width > 800,
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
                                                            on_click=lambda e: e.control.__setattr__("selected", not e.control.selected) or matricule_input.__setattr__("label", "Addresse mail" if e.control.selected else "Matricule") or matricule_input.__setattr__("value", "") or matricule_input.__setattr__("input_filter", None if e.control.selected else NumbersOnlyInputFilter()) or matricule_input.__setattr__("keyboard_type", KeyboardType.EMAIL if e.control.selected else KeyboardType.NUMBER) or page.update(),
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
                                            on_click=lambda e: connection_button_click(page, matricule_input, password_input, error_text),
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
                                border=border.all(1, colors.OUTLINE_VARIANT), # if page.width > 800 else None,
                                border_radius=20,
                                bgcolor=colors.BACKGROUND,
                                padding=Padding(20, 70, 20, 20),
                                margin=margin.only(top=50, left=20, right=20),
                                width=350 if page.width > 350 else None,
                            ),
                            
                            Container(
                                Image(
                                    "photo copy.png",
                                    color=page.theme.color_scheme_seed,
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
                            
                            IconButton(
                                icons.BRIGHTNESS_6_ROUNDED,
                                colors.PRIMARY,
                                on_click=lambda e: page.__setattr__("theme_mode", ThemeMode.DARK if (page.theme_mode == ThemeMode.SYSTEM and page.platform_brightness == Brightness.LIGHT) or page.theme_mode == ThemeMode.LIGHT else ThemeMode.LIGHT) or page.update(),
                                visible=page.width > 800,
                                top=50,
                                right=20
                            ),
                        ]
                    ),
                    alignment=alignment.center,
                    bgcolor=colors.ON_INVERSE_SURFACE,
                    margin=0 if page.width > 800 else 0,
                    height=page.height-(0 if page.width > 800 else 150),
                    border_radius=border_radius.horizontal(0, right=0) if page.width > 800 else 0,
                    col={"xs": 12, "md": 6, "lg": 5}
                ),
                
                Container(
                    Column(
                        [
                            Column(
                                [
                                    
                                    Text(
                                        "Connectez-vous !",
                                        font_family="RobotoBold",
                                        text_align=TextAlign.CENTER,
                                        size=30,
                                        width=page.width,
                                        visible=page.width > 800
                                    ),
                                    
                                    Text(
                                        "Accédez à votre compte administrateur, professeur ou étudiant grâce à votre matricule ou addresse mail.\n\nSi vous rencontrez des problèmes, réinitialisez le mot de passe ou contactez l'administrateur.",
                                        size=16,
                                        text_align=TextAlign.CENTER,
                                        width=page.width
                                    )
                                ],
                                spacing=50,
                                expand=page.width > 800,
                                alignment=MainAxisAlignment.CENTER
                            ),
                            
                            Row(
                                [
                                    TextButton(
                                        content=Text(
                                            text,
                                            color=colors.SECONDARY
                                        )
                                    ) for text in ["Centre d'aide", "Termes et conditions", "Politique de confidentialité"]
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                run_spacing=0,
                                wrap=True
                            )
                        ],
                        #alignment=MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        spacing=30
                    ),
                    height=page.height if page.width > 800 else None,
                    bgcolor=colors.with_opacity(0.5, page.theme.color_scheme_seed),
                    margin=8,
                    border_radius=border_radius.horizontal(10, 10),
                    alignment=alignment.center,
                    padding=padding.symmetric(30, 100 if page.width > 800 else 30),
                    col={"xs": 12, "md": 6, "lg": 7}
                )
            ],
            expand=page.width > 800,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            run_spacing=0,
            #visible=not page.width > 800
        ),
        
        Row(
            [
                Container(
                    Column(
                        [
                            Container(
                                Row(
                                    [
                                        Column(
                                            [
                                                Container(
                                                    Image(
                                                        "photo copy.png",
                                                        color=page.theme.color_scheme_seed,
                                                        fit=ImageFit.CONTAIN,
                                                        color_blend_mode=BlendMode.MODULATE,
                                                        filter_quality=FilterQuality.HIGH
                                                    ),
                                                    border=border.all(1, colors.OUTLINE),
                                                    width=80,
                                                    height=80,
                                                    padding=10,
                                                    shape=BoxShape.CIRCLE
                                                ),
                                                
                                                Text(
                                                    "SQUIMA",
                                                    size=24,
                                                    font_family="RobotoMedium",
                                                    text_align=TextAlign.CENTER
                                                )
                                            ]
                                        )
                                    ],
                                    alignment=MainAxisAlignment.CENTER
                                ),
                                bgcolor=colors.PRIMARY_CONTAINER,
                                padding=padding.symmetric(15),
                            ),
                        
                            pages := Column(
                                [
                                    Container(
                                        Container(
                                            Row(
                                                [
                                                    IconButton(
                                                        icon+"_outlined",
                                                        icon_color=None,
                                                        selected_icon_color=None,
                                                        selected_icon=icon+"_rounded",
                                                        selected=i==page.page_index
                                                        
                                                    ) if text != "Accueil" else Container(
                                                        Image(
                                                            "home_app_logo.svg",
                                                            width=25, height=25,
                                                            color=colors.PRIMARY,
                                                            fit=ImageFit.CONTAIN,
                                                            color_blend_mode=BlendMode.MODULATE,
                                                            filter_quality=FilterQuality.HIGH
                                                        ),
                                                        padding=padding.symmetric(8, 6)
                                                    ),
                                                    Text(text, color=None if i != page.page_index else None, size=16, width=100)
                                                ] if text.strip() else [CircleAvatar(opacity=0)],
                                                alignment=MainAxisAlignment.CENTER,
                                                spacing=5
                                            ),
                                            padding=padding.symmetric(2),
                                            ink=True,
                                            bgcolor=colors.INVERSE_PRIMARY if i != page.page_index else None,
                                            border_radius=border_radius.only(20, 10 if i==page.page_index+1 else 0, 20, 10 if i==page.page_index-1 else 0),
                                            ink_color=colors.PRIMARY_CONTAINER,
                                            on_click=None if not text.strip() else lambda e: pages.controls[page.page_index-1].content.__setattr__("border_radius", border_radius.horizontal(20)) or pages.controls[page.page_index+1].content.__setattr__("border_radius", border_radius.horizontal(20)) or pages.controls[page.page_index].content.__setattr__("bgcolor", colors.INVERSE_PRIMARY) or pages.controls[page.page_index].content.content.controls[0].__setattr__("selected", False) or page.__setattr__("page_index", [i for i, c in enumerate(pages.controls) if c.content == e.control][0]) or pages.controls[page.page_index+1].content.__setattr__("border_radius", border_radius.only(20, 10, 20)) or pages.controls[page.page_index-1].content.__setattr__("border_radius", border_radius.only(20, 0, 20, 10)) or e.control.__setattr__("bgcolor", colors.ON_INVERSE_SURFACE) or e.control.content.controls[0].__setattr__("selected", True) or page.update(),
                                            on_hover=None if not text.strip() else lambda e: hasattr(e.control.content.controls[0], "selected") and e.control.content.controls[0].selected or e.control.__setattr__("bgcolor", colors.SECONDARY_CONTAINER if e.data == "true" else colors.INVERSE_PRIMARY) or e.control.update()
                                        ),
                                        bgcolor=colors.ON_INVERSE_SURFACE,
                                        border_radius=border_radius.horizontal(20),
                                        margin=margin.only(left=10)
                                        
                                    ) for i, (text, icon) in enumerate(
                                        {
                                            "": "",
                                            "Accueil": icons.HOME,
                                            "Professeurs":icons.SCHOOL,
                                            "Etudiants": icons.GROUPS,
                                            "Finances": icons.PAID,
                                            "Comptes": icons.MANAGE_ACCOUNTS,
                                            "Paramètres": icons.SETTINGS,
                                            " ": ""
                                        }.items()
                                    )
                                ],
                                spacing=0
                            ),
                            
                            Column(
                                [
                                    Row(
                                        [
                                            FilledTonalButton(
                                                "Déconnecter",
                                                icons.LOGOUT_ROUNDED
                                            )
                                        ],
                                        alignment=MainAxisAlignment.CENTER
                                    )
                                ],
                                expand=True,
                                alignment=MainAxisAlignment.END
                            )
                        ]
                    ),
                    width=200,
                    bgcolor=colors.INVERSE_PRIMARY,
                    border_radius=border_radius.horizontal(right=10),
                    padding=padding.only(bottom=10)
                ),
                
                Column(
                    [
                        Container(
                            Row(
                                [
                                    Text(
                                        "Professeurs",
                                        font_family="RobotoBold",
                                        size=18
                                    ),
                                    
                                    Container(
                                        SearchBar(
                                            bar_overlay_color=colors.BACKGROUND,
                                            view_hint_text="Rechercher",
                                            view_trailing=[Icon(icons.SEARCH_ROUNDED)],
                                            view_elevation=0,
                                            view_hint_text_style=TextStyle(color="red"),
                                            view_header_text_style=TextStyle(color="blue"),
                                            divider_color=colors.BACKGROUND,
                                            view_surface_tint_color=colors.BACKGROUND,
                                            view_bgcolor=colors.BACKGROUND,
                                            width=300
                                        ),
                                        padding=10
                                    ),
                                    
                                    Row(
                                        [
                                            IconButton(
                                                icons.BRIGHTNESS_6_ROUNDED,
                                                colors.PRIMARY,
                                                on_click=lambda e: page.__setattr__("theme_mode", ThemeMode.DARK if (page.theme_mode == ThemeMode.SYSTEM and page.platform_brightness == Brightness.LIGHT) or page.theme_mode == ThemeMode.LIGHT else ThemeMode.LIGHT) or page.update()
                                            ),
                                            
                                            Stack(
                                                [
                                                    IconButton(icons.EMAIL_ROUNDED),
                                                    CircleAvatar(content=Text("5", font_family="RobotoRegular",color=colors.BACKGROUND, size=11), bgcolor=colors.ERROR, width=15, height=15, right=0)
                                                ]
                                            ),
                                            
                                            Stack(
                                                [
                                                    IconButton(icons.NOTIFICATIONS_ROUNDED),
                                                    CircleAvatar(content=Text("2", font_family="RobotoRegular",color=colors.BACKGROUND, size=11), bgcolor=colors.ERROR, width=15, height=15, right=0)
                                                ]
                                            ),
                                            
                                            ListTile(
                                                horizontal_spacing=5,
                                                content_padding=0,
                                                dense=True,
                                                title=Text("Adonis Rwabira", font_family="RobotoRegular"),
                                                leading=Image(
                                                    "profil.png",
                                                    error_content=Icon(icons.ACCOUNT_CIRCLE_ROUNDED, size=45),
                                                    height=45
                                                ),
                                                hover_color=colors.SECONDARY_CONTAINER,
                                                bgcolor_activated=colors.PRIMARY_CONTAINER,
                                                mouse_cursor=MouseCursor.CLICK,
                                                subtitle=Text("Etudiant"),
                                                trailing=Icon(icons.EXPAND_MORE_ROUNDED),
                                                width=180
                                            )
                                        ],
                                        vertical_alignment=CrossAxisAlignment.CENTER
                                    )
                                ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=CrossAxisAlignment.CENTER
                            ),
                            height=60,
                            padding=padding.only(30, right=5),
                            border_radius=border_radius.vertical(bottom=20),
                            margin=margin.only(right=10),
                            bgcolor=colors.BACKGROUND
                        ),
                        
                        ResponsiveRow(
                            [
                                Container(
                                    Column(
                                        [
                                           
                                        ]                                   
                                    ),
                                    bgcolor=colors.BACKGROUND,
                                    border_radius=10,
                                    margin=margin.only(bottom=10),
                                    col=9
                                ),
                                
                                Container(
                                    Column(
                                        [
                                            
                                        ]                                   
                                    ),
                                    bgcolor=colors.BACKGROUND,
                                    border_radius=10,
                                    margin=margin.only(right=10, bottom=10),
                                    col=3
                                )
                            ],
                            expand=True
                        )
                    ],
                    expand=True
                )
            ],
            expand=True,
            spacing=15,
            visible=False#page.width > 800
        )
    )
    
    #page.client_storage.set("users", {"admin": {"matricule": 19314, "mail": "adonisbitigaywa@gmail.com", "mot_de_passe": "admin"}}) 
    
def connection_button_click(page: Page, matricule_input: TextField, password_input: TextField, error_text: Text):
    if user := list(filter(lambda user: int(matricule_input.value or 0) in user[1].values() and password_input.value in user[1].values(), (page.client_storage.get("users") or {}).items())):
        print(user[0])
        
    else:
        error_text.value = "Informations incorrectes" if matricule_input.value and password_input.value else "Complétez tous les champs" if not matricule_input.value and not password_input.value else f"Entrez votre {matricule_input.label.lower()}" if not matricule_input.value else "Entrez le mot de passe"
        
        matricule_input.border_color = colors.OUTLINE_VARIANT if matricule_input.value else colors.ERROR
        password_input.border_color = colors.OUTLINE_VARIANT if password_input.value else colors.ERROR
        
        if matricule_input.value and password_input.value or not matricule_input.value and not password_input.value: matricule_input.border_color = password_input.border_color = colors.ERROR
        
    error_text.visible = True
    page.update()

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
