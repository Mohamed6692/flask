from flask import Blueprint

Hom_File = Blueprint('Hom_File', __name__, template_folder='templates')

from app.Hom_File import routes
