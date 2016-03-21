from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from five import grok
from collective.grok import gs
from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('eval.email_consultants')

_ = MessageFactory

class HiddenProducts(grok.GlobalUtility):
    """This hides the upgrade profiles from the quick installer tool."""
    implements(INonInstallable)
    grok.name('eval.email_consultants.upgrades')

    def getNonInstallableProducts(self):
        return [
            'eval.email_consultants.upgrades',
        ]

gs.profile(name=u'default',
           title=u'eval.email_consultants',
           description=_(u''),
           directory='profiles/default')
