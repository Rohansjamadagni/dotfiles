"""My widget customizations stuff."""

from libqtile import qtile, bar, widget
import subprocess
import socket
import os

myTerm = "kitty"
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


# colors = {
#     "black": "#000000",
#     "gray": "#6e6c7e",
#     "white": "#ffffff",
#     "teal": "#b5e8e0",
#     "lighter_blue": "#dbf0fe",
#     "light_blue": "#add8e6",
#     "dark_blue": "#152238",
#     "green": "#90ee90",
#     "dark_pink": "#f28fad",
#     "light_pink": "#f5d0f0",
#     "dark_orange": "#ff8886",
#     "orange": "#ffaf7a",
#     "red": "#ff7f7f",
#     "yellow": "#ffff99",
#     "transparent": "#00000000",
# }

# backgrounds = {
#     "group_box": colors["dark_blue"],
#     "window_name": colors["teal"],
#     "gpu_block": colors["green"],
#     "cpu_block": colors["dark_pink"],
#     "memory_block": colors["light_pink"],
#     "volume_block": colors["dark_orange"],
#     "brightness_block": colors["orange"],
#     "battery_block": colors["green"],
#     "clock_block": colors["yellow"],
#     "current_layout": colors["white"],
#     "quick_exit": colors["lighter_blue"],
# }


colors = [
    ["#282c34", "#282c34"],  # panel background
    ["#3d3f4b", "#434758"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#ff5555", "#ff5555"],  # border line color for current tab
    [
        "#74438f",
        "#74438f",
    ],  # border line color for 'other tabs' and color for 'odd widgets'
    ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
    ["#e1acff", "#e1acff"],  # window name
    ["#ecbbfb", "#ecbbfb"],
]  # backbround for inactive screens
COLORS = {
    "black": "#161925",
    "red": "#e06c75",
    "green": "#98c379",
    "yellow": "#e5c07b",
    "blue": "#61afef",
    "magenta": "#c678dd",
    "cyan": "#56b6c2",
    "grey": "#abb2bf",
    "white": "#ffffff",
}

def get_tmux_ls():
    number = subprocess.Popen(
        ["tmux ls | wc -l"],
        stdout=subprocess.PIPE,
        shell=True,
    )
    (out, _) = number.communicate()
    return str(out.decode("utf-8").strip("\n"))

def get_audio_if():
    symbol = subprocess.Popen(
        ["/home/rohanj/.config/scripts/get_audio_symbol.sh"],
        stdout=subprocess.PIPE,
        shell=True,
    )
    (out, _) = symbol.communicate()
    return str(out.decode("utf-8").strip("\n"))


def aave_health():
    aave = subprocess.Popen(
        [
            """ curl -s "https://api.debank.com/portfolio/list?project_id=matic_aave&user_addr=0x76d71b4b89605cf4875e67e10b02dd0495206aa7" | jq '.data.portfolio_list[0].detail.health_rate'| cut -c -5 """
        ],
        stdout=subprocess.PIPE,
        shell=True,
    )
    (out, err) = aave.communicate()
    return str(out.decode("utf-8").strip("\n"))


def get_gpu_usage():
    """Get GPU % usage."""
    gpu = subprocess.Popen(
        [
            "nvidia-smi "
            "--query-gpu=utilization.gpu --format=csv,nounits "
            "| "
            "awk '/[0-9]/ {print $1}'"
        ],
        stdout=subprocess.PIPE,
        shell=True,
    )
    (out, err) = gpu.communicate()
    return str(out.decode("utf-8").strip("\n")) + "%"


def get_gpu_mem_usage():
    """Get GPU VRAM usage."""
    gpu = subprocess.Popen(
        [
            "nvidia-smi "
            "--query-gpu=memory.used,memory.total --format=csv,nounits "
            "| "
            "awk '/[0-9]/ {printf \"%dM\",$1}'"
        ],
        stdout=subprocess.PIPE,
        shell=True,
    )
    (out, err) = gpu.communicate()
    return str(out.decode("utf-8").strip("\n"))


# def powerline_symbol(direction, foreground, background, fontsize=25):
#     """Powerline arrow key symbol."""
#     if direction == "left":
#         text = ""
#     elif direction == "right":
#         text = ""
#     return [
#         widget.TextBox(
#             text=text,
#             foreground=foreground,
#             background=background,
#             fontsize=fontsize,
#             padding=0,
#             font="MesloLGS NF",
#         ),
#     ]


def group_box():
    """Workspaces."""
    return [
        widget.GroupBox(
            font="Ubuntu Mono",
            fontsize=13,
            margin_y=4,
            margin_x=0,
            padding_y=6,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=True,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
    ]


def window_name():
    """Active window name."""
    return [
        widget.WindowName(
            foreground=colors[6], background=colors[0], padding=0
        ),
    ]


def get_bar_widgets(primary: bool, laptop: bool) -> bar.Bar:
    """Return an object of bar.Bar."""
    widgets = [
        widget.Sep(
            linewidth=0, padding=6, foreground=colors[2], background=colors[0]
        ),
        widget.GenPollText(
            background=colors[0],
            foreground=colors[6],
            fontsize=13,
            margin_y=4,
            margin_x=0,
            padding_y=6,
            padding_x=3,
            update_interval=2,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(myTerm)
            },
            func=get_tmux_ls
        ),
        widget.Sep(
            linewidth=0, padding=6, foreground=colors[2], background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Mono",
            fontsize=13,
            margin_y=4,
            margin_x=0,
            padding_y=6,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=True,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
            foreground=colors[3],
            background=colors[1],
        ),
        widget.Sep(
            linewidth=0, padding=40, foreground=colors[2], background=colors[0]
        ),
        widget.TaskList(
            foreground=colors[6],
            background=colors[0],
            margin_y=4,
            margin_x=0,
            padding_y=6,
            padding_x=3,
            scroll=True
        ),
        widget.Sep(
            linewidth=0, padding=6, foreground=colors[0], background=colors[0]
        ),
        widget.TextBox(
            text="AAVE:",
            foreground=COLORS["red"],
            background=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("brave app.aave.com")
            },
            padding=5,
        ),
        widget.GenPollText(
            func=aave_health,
            update_interval=300,
            background=colors[0],
            foreground=COLORS["red"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("brave app.aave.com")
            },
            fontsize=12,
        ),
        widget.TextBox(
            text="|", foreground=COLORS["red"], background=colors[0], padding=5
        ),
        widget.CPU(
            foreground=COLORS["blue"],
            background=colors[0],
            format="CPU: {load_percent}%",
            padding=2,
        ),
        # widget.ThermalSensor(
        #          foreground = colors[2],
        #          background = colors[5],
        #          threshold = 90,
        #          padding = 5
        #          ),
        widget.TextBox(
            text=" MEM:",
            foreground=COLORS["blue"],
            background=colors[0],
            padding=2,
            fontsize=14,
        ),
        widget.Memory(
            foreground=COLORS["blue"],
            background=colors[0],
            format="{MemUsed:.0f}{mm}",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")
            },
            padding=0,
        ),
        widget.TextBox(
            text=" T:",
            foreground=COLORS["blue"],
            background=colors[0],
            padding=2,
        ),
        widget.ThermalSensor(
            foreground=COLORS["blue"],
            background=colors[0],
            tag_sensor="Tctl",
        ),
        widget.TextBox(
            text="|",
            foreground=COLORS["blue"],
            background=colors[0],
            padding=5,
        ),
        widget.TextBox(
            text="GPU:",
            padding=2,
            foreground=COLORS["green"],
            background=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(myTerm + " -e nvtop")
            },
            Fontsize=14,
        ),
        widget.GenPollText(
            func=get_gpu_usage,
            update_interval=2,
            background=colors[0],
            foreground=COLORS["green"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(myTerm + " -e nvtop")
            },
            padding=0,
            fontsize=14,
        ),
        widget.TextBox(
            text="VMEM:",
            padding=2,
            foreground=COLORS["green"],
            background=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    myTerm + " -e watch -n0.5 nvidia-smi"
                )
            },
            fontsize=14,
        ),
        widget.GenPollText(
            func=get_gpu_mem_usage,
            update_interval=2,
            background=colors[0],
            foreground=COLORS["green"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    myTerm + " -e watch -n0.5 nvidia-smi"
                )
            },
            padding=0,
            fontsize=14,
        ),
        widget.NvidiaSensors(
            foreground=COLORS["green"],
            background=colors[0],
            format=" T:{temp}°C",
            # padding = 2,
            fontsize=14,
        ),
        widget.TextBox(
            text="|",
            foreground=COLORS["green"],
            background=colors[0],
            padding=5,
        ),
        widget.TextBox(
            text=" VOL:",
            foreground=COLORS["yellow"],
            background=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("pavucontrol")
            },
            padding=0,
        ),
        widget.Volume(
            foreground=COLORS["yellow"], background=colors[0], padding=5
        ),
        widget.GenPollText(
            func=get_audio_if,
            update_interval=2,
            background=colors[0],
            foreground=COLORS["yellow"],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    "/home/rohanj/.config/scripts/audio_change.sh"
                )
            },
            fontsize=12,
        ),
        widget.TextBox(
            text="|",
            foreground=COLORS["yellow"],
            background=colors[0],
            padding=5,
        ),
        widget.CurrentLayout(
            foreground=COLORS["magenta"], background=colors[0], padding=5
        ),
        widget.TextBox(
            text="|",
            foreground=COLORS["magenta"],
            background=colors[0],
            padding=5,
        ),
        widget.Clock(
            foreground=COLORS["cyan"],
            background=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("arcolinux-logout")
            },
            format="%A, %B %d - %H:%M ",
        ),
        widget.WidgetBox(
            foreground=COLORS["cyan"],
            background=colors[0],
            widgets=[

            widget.Systray(background=colors[0], padding=5),
            ]
        )
    ]

    # Add the GPU block if it exists on the machine
    # Add systray only on one primary monitor to avoid systray crash
    if primary:
        del widgets[-1]

    return bar.Bar(widgets, 30, opacity=1.0)
