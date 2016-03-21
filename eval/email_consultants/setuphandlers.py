from collective.grok import gs
from eval.email_consultants import MessageFactory as _

@gs.importstep(
    name=u'eval.email_consultants', 
    title=_('eval.email_consultants import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('eval.email_consultants.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
