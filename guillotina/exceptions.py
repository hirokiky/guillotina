from guillotina.interfaces import IForbidden
from guillotina.interfaces import IForbiddenAttribute
from guillotina.interfaces import IUnauthorized
from zope.interface import implementer


class NoPermissionToAdd(Exception):

    def __init__(self, container, content_type):
        self.container = container
        self.content_type = content_type

    def __repr__(self):
        return "Not permission to add {content_type} on {path}".format(
            content_type=self.content_type,
            path=self.path)


class NotAllowedContentType(Exception):

    def __init__(self, container, content_type):
        self.container = container
        self.content_type = content_type

    def __repr__(self):
        return "Not allowed {content_type} on {path}".format(
            content_type=self.content_type,
            path=self.path)


class ConflictIdOnContainer(Exception):

    def __init__(self, container, ident):
        self.container = container
        self.ident = ident

    def __repr__(self):
        return "Conflict ID {ident} on {path}".format(
            ident=self.ident,
            path=self.container)


class PreconditionFailed(Exception):

    def __init__(self, container, precondition):
        self.container = container
        self.precondition = precondition

    def __repr__(self):
        return "Precondition Failed {precondition} on {path}".format(
            precondition=self.precondition,
            path=self.container)


class RequestNotFound(Exception):
    """Lookup for the current request for request aware transactions failed
    """


@implementer(IUnauthorized)
class Unauthorized(Exception):
    """Some user wasn't allowed to access a resource"""


@implementer(IForbidden)
class Forbidden(Exception):
    """A resource cannot be accessed under any circumstances
    """


@implementer(IForbiddenAttribute)
class ForbiddenAttribute(Forbidden, AttributeError):
    """An attribute is unavailable because it is forbidden (private)
    """


class NoInteraction(Exception):
    """No interaction started
    """


class ConflictError(Exception):
    pass


# Helper class for __traceback_supplement__
class TracebackSupplement(object):

    def __init__(self, obj):
        self.obj = obj

    def get_info(self):
        result = []
        try:
            cls = self.obj.__class__
            if hasattr(cls, "__module__"):
                s = "%s.%s" % (cls.__module__, cls.__name__)
            else:  # pragma NO COVER XXX
                s = str(cls.__name__)
            result.append("   - class: " + s)
        except:  # noqa
            pass
        try:
            cls = type(self.obj)
            if hasattr(cls, "__module__"):
                s = "%s.%s" % (cls.__module__, cls.__name__)
            else:  # pragma NO COVER XXX
                s = str(cls.__name__)
            result.append("   - type: " + s)
        except:  # noqa
            pass
        return "\n".join(result)


class ConfigurationError(Exception):
    """There was an error in a configuration
    """


class ComponentConfigurationError(ValueError, ConfigurationError):
    pass


class ConfigurationConflictError(ConfigurationError):

    def __init__(self, conflicts):
        self._conflicts = conflicts

    def __str__(self):  # pragma NO COVER
        r = ["Conflicting configuration actions"]
        items = self._conflicts.items()
        items.sort()
        for discriminator, infos in items:
            r.append("  For: %s" % (discriminator, ))
            for info in infos:
                for line in str(info).rstrip().split('\n'):
                    r.append("    " + line)

        return "\n".join(r)


class NoIndexField(Exception):
    pass