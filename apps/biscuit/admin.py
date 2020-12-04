from django.contrib import admin

from apps.biscuit.models.biscuit import Biscuit
from apps.biscuit.models.unfit_biscuit import UnfitBiscuit

admin.site.register(Biscuit)
admin.site.register(UnfitBiscuit)
