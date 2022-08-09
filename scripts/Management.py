try:
    import tkinter
    import dataclasses
    import tkinter.font as tkfont
    from typing import (Union , AnyStr , final)
    
finally:
    ...
    
    


@final
@dataclasses.dataclass
class Materials:
    
    class Colors:
        dark: Union[str , AnyStr] = '#1C1C1C'
        dark2: Union[str , AnyStr] = '#242424'
        dark3: Union[str , AnyStr] = '#383838'
        dark4: Union[str , AnyStr] = '#2A2D2E'
        dark5: Union[str , AnyStr] = '#212226'
        black: Union[str , AnyStr] = '#000000'
        white: Union[str , AnyStr] = '#ffffff'
        green: Union[str , AnyStr] = '#00B273'
        green2: Union[str , AnyStr] = '#078B5D'
        green3: Union[str , AnyStr] = '#3DCA9D'
        grey: Union[str , AnyStr] = '#999999'
        grey2: Union[str , AnyStr] = '#999999'
        whitesmoke: Union[str , AnyStr] = '#F5F5F5'
        darkgrey: Union[str , AnyStr] = '#696969'
        lightgrey: Union[str , AnyStr] = '#D1D5D8'
        tomato: Union[str , AnyStr] = '#F3350C'
        red: Union[str , AnyStr] = '#A8362B'
        # belizehole: Union[str , AnyStr] = '#2980B9'
        # peterriver: Union[str , AnyStr] = '#3498DB'
        
    class Cursors:
        hand: str = 'hand2'
        
    class Themes:
        dark: str = 'Dark'
        light: str = 'Light'
        
    class States:
        normal: str = tkinter.NORMAL
        active: str = tkinter.ACTIVE
        
    class FontWeight:
        bold: str = tkfont.BOLD
        normal: str = tkfont.NORMAL
        italic: str = tkfont.ITALIC
        
    class Alignments:
        both: str = tkinter.BOTH
        right: str = tkinter.RIGHT
        center: str = tkinter.CENTER