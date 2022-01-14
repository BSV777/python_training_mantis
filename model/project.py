# -*- coding: utf-8 -*-
from sys import maxsize

class Project:
    def __init__(self, id=None, name=None, status=None, inherit=False, view_state=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.inherit = inherit
        self.view_state = view_state
        self.description = description

    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
