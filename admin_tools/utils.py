"""
Admin ui common utilities.
"""

from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import capfirst

class AppListElementMixin(object):
    """
    Mixin class used by both the AppListDashboardModule and the 
    AppListMenuItem (to honor the DRY concept).
    """
    def _check_perms(self, request, model, model_admin):
        mod = '%s.%s' % (model.__module__, model.__name__)
        
        if type(self).__name__ == 'ModelListDashboardModule':
            if len(self.models):
                found = False
                for pattern in self.models:
                    if mod.startswith(pattern):
                        found = True
                if not found:
                    return False
        
        elif type(self).__name__ == 'AppListDashboardModule':
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            if len(self.apps):
                found = False
                for pattern in self.apps:
                    if mod.startswith(pattern):
                        found = True
                if not found:
                    return False
        
        # check that the user has module perms
        if not request.user.has_module_perms(model._meta.app_label):
            return False

        # check whether user has any perm for this module
        print model_admin
        perms = model_admin.get_model_perms(request)
        if True not in perms.values():
            return False
        return perms

    def _get_admin_change_url(self, model):
        app_label = model._meta.app_label
        return reverse('admin:%s_%s_changelist' % (app_label,
                                                   model.__name__.lower()))

    def _get_admin_add_url(self, model):
        app_label = model._meta.app_label
        return reverse('admin:%s_%s_add' % (app_label, model.__name__.lower()))
