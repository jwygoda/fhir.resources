#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 (http://hl7.org/fhir/StructureDefinition/List) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class List(domainresource.DomainResource):
    """ Information summarized from a list of other resources.

    A set of information summarized from a list of other resources.
    """

    resource_type = "List"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ What the purpose of this list is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.date = None
        """ When the list was prepared.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.emptyReason = None
        """ Why list is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.encounter = None
        """ Context in which list created.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """

        self.entry = None
        """ Entries in the list.
        List of `ListEntry` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.mode = None
        """ working | snapshot | changes.
        Type `str`. """

        self.note = None
        """ Comments about the list.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.orderedBy = None
        """ What order the list has.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.source = None
        """ Who and/or what defined the list contents (aka Author).
        Type `FHIRReference` referencing `Practitioner, Patient, Device` (represented as `dict` in JSON). """

        self.status = None
        """ current | retired | entered-in-error.
        Type `str`. """

        self.subject = None
        """ If all resources have the same subject.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """

        self.title = None
        """ Descriptive name for the list.
        Type `str`. """

        super(List, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, "Reference", False, None, False),
            ("entry", "entry", ListEntry, "ListEntry", True, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("mode", "mode", str, "code", False, None, True),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("source", "source", fhirreference.FHIRReference, "Reference", False, None, False),
            ("status", "status", str, "code", False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, "Reference", False, None, False),
            ("title", "title", str, "string", False, None, False),
        ])
        return js


from . import backboneelement

class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.

    Entries in this list.
    """

    resource_type = "ListEntry"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.date = None
        """ When item added to list.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.deleted = None
        """ If this item is actually marked as deleted.
        Type `bool`. """

        self.flag = None
        """ Status/Workflow information about this item.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.item = None
        """ Actual entry.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """

        super(ListEntry, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("deleted", "deleted", bool, "boolean", False, None, False),
            ("flag", "flag", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("item", "item", fhirreference.FHIRReference, "Reference", False, None, True),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
