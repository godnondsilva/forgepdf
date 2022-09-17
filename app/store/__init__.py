class GlobalState:
    def __init__(self):
        self.data = {
            'uid': 0,
            'username': '',
            'email': '',
            'selected_pdf': '',
            'count': 0,
            'location': 'mangalore',
            'selected_pdf': '',
            'selected_pdfs': [],
            'current_frame': ''
        }

    def get_state(self, key):
        return self.data[key]
    
    def set_state(self, key, value):
        self.data[key] = value

    def reset_state(self):
        self.data = {
            'uid': 0,
            'username': '',
            'email': '',
            'count': 0,
            'location': 'mangalore',
            'selected_pdf': '',
            'selected_pdfs': [],
            'current_frame': ''
        }

class States:
    def __init__(self):
        self.UID = 'uid'
        self.USERNAME = 'username'
        self.EMAIL = 'email'
        self.COUNT = 'count'
        self.LOCATION = 'location'
        self.SELECTED_PDF = 'selected_pdf'
        self.SELECTED_PDFS = 'selected_pdfs'
        self.CURRENT_FRAME = 'current_frame'
    
state = GlobalState()
states = States()