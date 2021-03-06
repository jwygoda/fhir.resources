#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class AllergyIntolerance(domainresource.DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).

    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """

    resource_type = "AllergyIntolerance"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assertedDate = None
        """ Date record was believed accurate.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.asserter = None
        """ Source of the information about the allergy.
        Type `FHIRReference` referencing `Patient, RelatedPerson, Practitioner` (represented as `dict` in JSON). """

        self.category = None
        """ food | medication | environment | biologic.
        List of `str` items. """

        self.clinicalStatus = None
        """ active | inactive | resolved.
        Type `str`. """

        self.code = None
        """ Code that identifies the allergy or intolerance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.criticality = None
        """ low | high | unable-to-assess.
        Type `str`. """

        self.identifier = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.lastOccurrence = None
        """ Date(/time) of last known occurrence of a reaction.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.note = None
        """ Additional text not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.onsetAge = None
        """ When allergy or intolerance was identified.
        Type `Age` (represented as `dict` in JSON). """

        self.onsetDateTime = None
        """ When allergy or intolerance was identified.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.onsetPeriod = None
        """ When allergy or intolerance was identified.
        Type `Period` (represented as `dict` in JSON). """

        self.onsetRange = None
        """ When allergy or intolerance was identified.
        Type `Range` (represented as `dict` in JSON). """

        self.onsetString = None
        """ When allergy or intolerance was identified.
        Type `str`. """

        self.patient = None
        """ Who the sensitivity is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """

        self.reaction = None
        """ Adverse Reaction Events linked to exposure to substance.
        List of `AllergyIntoleranceReaction` items (represented as `dict` in JSON). """

        self.recorder = None
        """ Who recorded the sensitivity.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """

        self.type = None
        """ allergy | intolerance - Underlying mechanism (if known).
        Type `str`. """

        self.verificationStatus = None
        """ unconfirmed | confirmed | refuted | entered-in-error.
        Type `str`. """

        super(AllergyIntolerance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("assertedDate", "assertedDate", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("asserter", "asserter", fhirreference.FHIRReference, "Reference", False, None, False),
            ("category", "category", str, "code", True, None, False),
            ("clinicalStatus", "clinicalStatus", str, "code", False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("criticality", "criticality", str, "code", False, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("lastOccurrence", "lastOccurrence", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("onsetAge", "onsetAge", age.Age, "Age", False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, "dateTime", False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, "Period", False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, "Range", False, "onset", False),
            ("onsetString", "onsetString", str, "string", False, "onset", False),
            ("patient", "patient", fhirreference.FHIRReference, "Reference", False, None, True),
            ("reaction", "reaction", AllergyIntoleranceReaction, "AllergyIntoleranceReaction", True, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, "Reference", False, None, False),
            ("type", "type", str, "code", False, None, False),
            ("verificationStatus", "verificationStatus", str, "code", False, None, True),
        ])
        return js


from . import backboneelement

class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.

    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """

    resource_type = "AllergyIntoleranceReaction"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Description of the event as a whole.
        Type `str`. """

        self.exposureRoute = None
        """ How the subject was exposed to the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.manifestation = None
        """ Clinical symptoms/signs associated with the Event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.note = None
        """ Text about event not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.onset = None
        """ Date(/time) when manifestations showed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.severity = None
        """ mild | moderate | severe (of event as a whole).
        Type `str`. """

        self.substance = None
        """ Specific substance or pharmaceutical product considered to be
        responsible for event.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(AllergyIntoleranceReaction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("description", "description", str, "string", False, None, False),
            ("exposureRoute", "exposureRoute", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("manifestation", "manifestation", codeableconcept.CodeableConcept, "CodeableConcept", True, None, True),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("onset", "onset", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("severity", "severity", str, "code", False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
