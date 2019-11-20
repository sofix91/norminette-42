class Token:
    def __init__(self, tkn_type, pos, tkn_value=None):
        self.type = str(tkn_type)
        self.pos = int(pos)
        if tkn_value != None:
            self.value = str(tkn_value)
            self.length = len(tkn_value)
        else:
            self.value = None
            self.length = 0

    def __repr__(self):
        """
        Token representation for debugging, using the format <TYPE=value>
        or simply <TYPE> for non-printables characteres
        """
        r = f'<{self.type}={self.value}>' if self.value else f'<{self.type}>'
        return r
