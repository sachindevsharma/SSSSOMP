
from dash import html, register_page, page_container

from .header_bar import build_header_bar
from .home_page import build_home_page
from .tab2_layout import build_tab2_content
from .tab3_layout import build_tab3_content
from .tab4_layout import build_tab4_content
from .tab5_layout import build_tab5_content
from .tab6_layout import build_tab6_content
from .wings_education import build_wings_education
from .wings_spiritual import build_wings_spiritual

def Layout():

    return html.Div(id="main_div", children=[    
        build_header_bar(),
        html.Div(id='second_div', children=[
            page_container

        # END OF 2nd Division   
        ]),
        html.Br(),
        html.Footer(" © Copyright Sri Sathya Sai Seva Organisation Madhya Pradesh - All Rights Reserved",
            id="footer", 
            style={"textAlign": "center", "padding": "10px"},
        ),

        # This div is for firing callbacks while loading only and nothing else
        html.Div(id="loading_div"),      

    # END OF MAIN DIV
    ])


def register_app_pages():

    page_values = [
        # id , name, path, layout
        ["tab1", "Home", '/', build_home_page()],
        ["tab2", "About Us", '/about', build_tab2_content()],
        ["tab3", "Wings", '/wings', build_tab3_content()],
        ["tab4", "Activities", '/activities', build_tab4_content()],
        ["tab5", "Gallery", '/gallery', build_tab5_content()],
        ["tab7", "Contact Us", '/state_office', build_tab5_content()],

        # Sri Sathya Sai Baba
        ["sss_life", "His Life", '/his_life', build_tab5_content()],
        ["sss_message", "His Message", '/his_message', build_tab5_content()],
        ["sss_coc", "9 point Code of Conduct", '/code_of_conduct', build_tab5_content()],
        ["sss_daily_prayers", "Daily Prayers", '/daily_prayers', build_tab6_content()],
        ["sss_discourses", "Discourses", '/discourses', build_tab6_content()],
        ["sss_state_office", "State Office Bearers", '/state/office_bearers', build_tab6_content()],
        
        # Wings
        ["wings_education", "Education Wing", '/wings/education', build_wings_education()],
        ["wings_service", "Service Wing", '/wings/service', build_tab5_content()],
        ["wings_spiritual", "Spiritual Wing", '/wings/spiritual', build_wings_spiritual()],
        ["wings_youth", "Youth Wing", '/wings/youth', build_tab5_content()],

        # Activities
        ["activities_dm", "Disaster Management", '/disaster_management', build_tab5_content()],
        ["activities_ns", "Narayan Sewa", '/narayan_sewa', build_tab5_content()],
        ["activities_ps", "Prashanti Sewa", '/prashanti_sewa', build_tab5_content()],
        ["activities_ss", "Sadhna Shivir", '/sadhna_shivir', build_tab5_content()],
        ["activities_sd", "Swachhata se Divyata Tak", '/swachhata_se_divyata', build_tab5_content()],
        ["activities_vj", "Vidya Jyoti", '/vidya_jyoti', build_tab5_content()],

        # Services
        ["services_so", "Sai One", '/sai_one', ""],
        ["services_ss", "Sanatan Sarthi Hindi", '/sanatan_sarthi_hindi', ""],
        ["services_sc", "Sewa Coordinator", '/sewa_coordinator', ""],
        ["services_sr", "Sewa Registration Report", '/sewa_registration_report', ""],
    ]       

    for order, (module , name, path, layout) in enumerate(page_values):
        register_page(module, name=name, path=path, layout=layout, order=order)
    
    
