

def HeaderBarApi(server):
    @server.route("/api/header/options", methods=["POST"])
    def header_bar_options():
        header_options = [
            # Name, Sub headings
            ["Sri Sathya Sai Baba", True],
            ["SSSSOMP", False],
            ["Wings", True],
            ["Activities", True],
            ["Gallery", False],
            ["Services", True], 
            ["Contact Us", False],
        ]
        return {'options': [i[0] for i in header_options], 
                "sub_headings": [i[1] for i in header_options]}
