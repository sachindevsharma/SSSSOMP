from dash import html, register_page, page_container

from .header_bar import build_header_bar
from .tab1_layout import build_tab1_content
from .tab2_layout import build_tab2_content
from .tab3_layout import build_tab3_content
from .tab4_layout import build_tab4_content
from .tab5_layout import build_tab5_content
from .tab6_layout import build_tab6_content


def Layout(app):

    return html.Div(id="main_div", children=[    
        build_header_bar(app),
        html.Div(id='second_div', children=[
            page_container

        # END OF 2nd Division   
        ]),

    # END OF MAIN DIV
    ])


def register_app_pages():

    page_values = [
        # id , name, path, layout
        ["tab1", "Home", '/', build_tab1_content()],
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
        ["wings_spiritual", "Spiritual Wing", '/wings/spiritual', build_tab5_content()],
        ["wings_education", "Education Wing", '/wings/education', build_tab5_content()],
        ["wings_service", "Service Wing", '/wings/service', build_tab5_content()],
        ["wings_youth", "Youth Wing", '/wings/youth', build_tab5_content()],

        # Activities
        ["activities_ps", "Prashanti Sewa", '/prashanti_sewa', build_tab5_content()],
        ["activities_dm", "Disaster Management", '/disaster_management', build_tab5_content()],
        ["activities_ss", "Sadhna Shivir", '/sadhna_shivir', build_tab5_content()],
        ["activities_vj", "Vidya Jyoti", '/vidya_jyoti', build_tab5_content()],

        # Services
        ["services_ss", "Sanatan Sarthi Hindi", '/sanatan_sarthi_hindi', build_tab5_content()],
        ["services_so", "Sai One", '/sai_one', build_tab5_content()],
        ["services_sr", "Sewa Registration Report", '/sewa_registration_report', build_tab5_content()],
    ]       

    for order, (module , name, path, layout) in enumerate(page_values):
        register_page(module, name=name, path=path, layout=layout, order=order)
    
    
