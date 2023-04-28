from .header_bar_callbacks import callbacks_header_bar
from .tab1_callbacks import callbacks_tab1
from .tab2_callbacks import callbacks_tab2
from .wings_education_callbacks import callbacks_wings_education
from .wings_spiritual_callbacks import callbacks_wings_spiritual



def Callbacks():
    callbacks_header_bar()
    callbacks_tab1()
    callbacks_tab2()
    callbacks_wings_education()
    callbacks_wings_spiritual()