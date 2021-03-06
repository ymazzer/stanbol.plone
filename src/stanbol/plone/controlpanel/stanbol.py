'''
Created on Jul 7, 2011

@author: "Encolpe Degoute"
@author: "Jens W. Klein"
@author: "Yannis Mazzer"
'''

from zope.schema import (
    Int,
    TextLine,
    Tuple,
)

from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements

from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase

from zope.formlib.form import FormFields
from plone.app.controlpanel.form import ControlPanelForm

from zope.i18nmessageid import MessageFactory
_ = MessageFactory(u'stanbol.plone')

#from stanbol.plone import StanbolMessageFactory as _

class IStanbolSchema(Interface):
    """
    Stanbol Preference Pane Interface
    """
    stanbol_server_address = Tuple (
        title=u'Stanbol server address',
        description=_('help_stanbol_server_address',
            default=u"Please enter the address of your Stanbol server instance"
        ),
        value_type = TextLine()
    )
    stanbol_server_port = Tuple (
        title=u'Stanbol server port',
        description=_('help_stanbol_server_port',
            default=u'Please enter the port of your Stanbol server instance'
        ),
        value_type = Int()
    )
      

class StanbolControlPanelAdapter(SchemaAdapterBase):
    """
    Stanbol Preference Pane Schema Adapter
    """
    adapts(IPloneSiteRoot)
    implements(IStanbolSchema)
    
    def __init__(self, context):
        super(StanbolControlPanelAdapter, self).__init__(context)
        
    stanbol_server_address = ProxyFieldProperty(IStanbolSchema['stanbol_server_address'])
    stanbol_server_port = ProxyFieldProperty(IStanbolSchema['stanbol_server_address'])
        



class StanbolControlPanel(ControlPanelForm):
    """
    Stanbol Control Panel Form
    """
    form_fields = FormFields(IStanbolSchema)
    form_fields['stanbol_server_address'].custom_widget = TextLine
    form_fields['stanbol_server_port'].custom_widget = TextLine
    
    id = 'portal_stanbol'
    label = _('Stanbol server settings')
    description = _('Enter Stanbol server settings to use with this site.')
    form_name = _('Stanbol')
    
