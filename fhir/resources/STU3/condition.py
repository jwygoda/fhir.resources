#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 (http://hl7.org/fhir/StructureDefinition/Condition) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.

    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """

    resource_type = "Condition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.abatementAge = None
        """ If/when in resolution/remission.
        Type `Age` (represented as `dict` in JSON). """

        self.abatementBoolean = None
        """ If/when in resolution/remission.
        Type `bool`. """

        self.abatementDateTime = None
        """ If/when in resolution/remission.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.abatementPeriod = None
        """ If/when in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """

        self.abatementRange = None
        """ If/when in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """

        self.abatementString = None
        """ If/when in resolution/remission.
        Type `str`. """

        self.assertedDate = None
        """ Date record was believed accurate.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.asserter = None
        """ Person who asserts this condition.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """

        self.bodySite = None
        """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.category = None
        """ problem-list-item | encounter-diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.clinicalStatus = None
        """ active | recurrence | inactive | remission | resolved.
        Type `str`. """

        self.code = None
        """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.context = None
        """ Encounter or episode when condition first asserted.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """

        self.evidence = None
        """ Supporting evidence.
        List of `ConditionEvidence` items (represented as `dict` in JSON). """

        self.identifier = None
        """ External Ids for this condition.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.note = None
        """ Additional information about the Condition.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.onsetAge = None
        """ Estimated or actual date,  date-time, or age.
        Type `Age` (represented as `dict` in JSON). """

        self.onsetDateTime = None
        """ Estimated or actual date,  date-time, or age.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.onsetPeriod = None
        """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """

        self.onsetRange = None
        """ Estimated or actual date,  date-time, or age.
        Type `Range` (represented as `dict` in JSON). """

        self.onsetString = None
        """ Estimated or actual date,  date-time, or age.
        Type `str`. """

        self.severity = None
        """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.stage = None
        """ Stage/grade, usually assessed formally.
        Type `ConditionStage` (represented as `dict` in JSON). """

        self.subject = None
        """ Who has the condition?.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """

        self.verificationStatus = None
        """ provisional | differential | confirmed | refuted | entered-in-error
        | unknown.
        Type `str`. """

        super(Condition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend([
            ("abatementAge", "abatementAge", age.Age, "Age", False, "abatement", False),
            ("abatementBoolean", "abatementBoolean", bool, "boolean", False, "abatement", False),
            ("abatementDateTime", "abatementDateTime", fhirdate.FHIRDate, "dateTime", False, "abatement", False),
            ("abatementPeriod", "abatementPeriod", period.Period, "Period", False, "abatement", False),
            ("abatementRange", "abatementRange", range.Range, "Range", False, "abatement", False),
            ("abatementString", "abatementString", str, "string", False, "abatement", False),
            ("assertedDate", "assertedDate", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("asserter", "asserter", fhirreference.FHIRReference, "Reference", False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("clinicalStatus", "clinicalStatus", str, "code", False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("context", "context", fhirreference.FHIRReference, "Reference", False, None, False),
            ("evidence", "evidence", ConditionEvidence, "ConditionEvidence", True, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("onsetAge", "onsetAge", age.Age, "Age", False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, "dateTime", False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, "Period", False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, "Range", False, "onset", False),
            ("onsetString", "onsetString", str, "string", False, "onset", False),
            ("severity", "severity", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("stage", "stage", ConditionStage, "ConditionStage", False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, "Reference", False, None, True),
            ("verificationStatus", "verificationStatus", str, "code", False, None, False),
        ])
        return js


from . import backboneelement

class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.

    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """

    resource_type = "ConditionEvidence"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Manifestation/symptom.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.detail = None
        """ Supporting information found elsewhere.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """

        super(ConditionEvidence, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, "Reference", True, None, False),
        ])
        return js


class ConditionStage(backboneelement.BackboneElement):
    """ Stage/grade, usually assessed formally.

    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """

    resource_type = "ConditionStage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.assessment = None
        """ Formal record of assessment.
        List of `FHIRReference` items referencing `ClinicalImpression, DiagnosticReport, Observation` (represented as `dict` in JSON). """

        self.summary = None
        """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ConditionStage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("assessment", "assessment", fhirreference.FHIRReference, "Reference", True, None, False),
            ("summary", "summary", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
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
