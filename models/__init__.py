
from app import db
from sqlalchemy.exc import InvalidRequestError


class ModelMixin(object):

    def save(self, commit=False, flush=False):
        db.session.add(self)
        if flush:
            db.session.flush()

        if commit:
            db.session.commit()

    def delete(self, commit=False):
        if self.id is None:
            return
        db.session.delete(self)
        if commit:
            db.session.commit()

    def refresh(self):
        try:
            db.session.refresh(self)
        except InvalidRequestError:
            db.session.add(self)


from .occupation import *
from .user import *