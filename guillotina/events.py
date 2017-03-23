from guillotina.component.interfaces import IObjectEvent
from guillotina.interfaces import IBeforeObjectAddedEvent
from guillotina.interfaces import IBeforeObjectRemovedEvent
from guillotina.interfaces import IFileFinishUploaded
from guillotina.interfaces import INewUserAdded
from guillotina.interfaces import IObjectAddedEvent
from guillotina.interfaces import IObjectModifiedEvent
from guillotina.interfaces import IObjectMovedEvent
from guillotina.interfaces import IObjectPermissionsModifiedEvent
from guillotina.interfaces import IObjectPermissionsViewEvent
from guillotina.interfaces import IObjectRemovedEvent
from guillotina.interfaces import IObjectVIContainerdEvent
from zope.interface import implementer


@implementer(IObjectEvent)
class ObjectEvent(object):

    def __init__(self, object):
        self.object = object


@implementer(IObjectMovedEvent)
class ObjectMovedEvent(ObjectEvent):
    """An object has been moved"""

    def __init__(self, object, old_parent, old_name, new_parent, new_name, data=None):
        ObjectEvent.__init__(self, object)
        self.old_parent = old_parent
        self.old_name = old_name
        self.new_parent = new_parent
        self.new_name = new_name
        self.data = data


@implementer(IObjectAddedEvent)
class ObjectAddedEvent(ObjectMovedEvent):
    """An object has been added to a container"""

    def __init__(self, object, new_parent=None, new_name=None, data=None):
        if new_parent is None:
            new_parent = object.__parent__
        if new_name is None:
            new_name = object.__name__
        ObjectMovedEvent.__init__(self, object, None, None, new_parent, new_name, data=data)


@implementer(IBeforeObjectAddedEvent)
class BeforeObjectAddedEvent(ObjectAddedEvent):
    pass


@implementer(IObjectRemovedEvent)
class ObjectRemovedEvent(ObjectMovedEvent):
    """An object has been removed from a container"""

    def __init__(self, object, old_parent=None, old_name=None, data=None):
        if old_parent is None:
            old_parent = object.__parent__
        if old_name is None:
            old_name = object.__name__
        ObjectMovedEvent.__init__(self, object, old_parent, old_name, None, None)


@implementer(IBeforeObjectRemovedEvent)
class BeforeObjectRemovedEvent(ObjectRemovedEvent):
    pass


@implementer(IObjectModifiedEvent)
class ObjectModifiedEvent(object):

    def __init__(self, object, payload={}):
        self.object = object
        self.payload = payload


@implementer(IObjectVIContainerdEvent)
class ObjectVIContainerdEvent(ObjectEvent):
    """An object has been modified."""


@implementer(IObjectPermissionsViewEvent)
class ObjectPermissionsViewEvent(ObjectEvent):
    """An object has been modified."""


@implementer(IObjectPermissionsModifiedEvent)
class ObjectPermissionsModifiedEvent(ObjectModifiedEvent):
    """An object has been modified."""


@implementer(IFileFinishUploaded)
class FileFinishUploaded(ObjectEvent):
    """A file has finish uploading."""


@implementer(INewUserAdded)
class NewUserAdded(object):
    """An object has been created."""

    def __init__(self, user):
        self.user = user
