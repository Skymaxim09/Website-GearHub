from .models import Keyboard, Switch, Keycap, Mouse, ModTool

CATEGORY_MAP = {
    'ban-phim': {
        'model': Keyboard,
        'filter_fields': ['layout', 'keyboard_type', 'connection']
    },
    'switch': {
        'model': Switch,
        'filter_fields': ['switch_type',]
    },
    'keycap': {
        'model': Keycap,
        'filter_fields': ['profile', 'material', 'print_tech']
    },
    'chut': {
        'model': Mouse,
        'filter_fields': ['connection', 'brand', 'mouse_type']
    },
    'dng-c-mod': {
        'model': ModTool,
        'filter_fields': ['mt_type',]
    },
}