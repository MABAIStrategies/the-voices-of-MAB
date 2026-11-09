"""Deterministic policy tests for MAB draft agent. These do NOT test remote scheduling or LLM quality."""
from dataclasses import dataclass

@dataclass
class Case:
    name: str
    category: str
    already_replied: bool = False
    existing_draft: bool = False
    unsafe: bool = False
    missing_facts: bool = False
    expected: str = ''

def route(c):
    if c.already_replied or c.existing_draft:
        return 'SKIP_DUPLICATE'
    if c.category in {'newsletter','phishing','otp','bot_notice'}:
        return 'SKIP_NONCORRESPONDENCE'
    if c.unsafe or c.category in {'legal_commitment','payment_change'}:
        return 'ESCALATE_NO_SEND'
    if c.missing_facts:
        return 'DRAFT_QUALIFIED_REVIEW'
    if c.category in {'registration','lead','partner','support','event','vendor_followup'}:
        return 'DRAFT_REVIEW'
    return 'SKIP_UNCLASSIFIED'

cases = [
    Case('Seminar registration, confirmed policy','registration',expected='DRAFT_REVIEW'),
    Case('Seminar registration, uncertain discount','registration',missing_facts=True,expected='DRAFT_QUALIFIED_REVIEW'),
    Case('Threadline support, unknown launch status','support',missing_facts=True,expected='DRAFT_QUALIFIED_REVIEW'),
    Case('Already replied to contact','partner',already_replied=True,expected='SKIP_DUPLICATE'),
    Case('Existing draft in thread','lead',existing_draft=True,expected='SKIP_DUPLICATE'),
    Case('Security-code email','otp',expected='SKIP_NONCORRESPONDENCE'),
    Case('Phishing link masquerading as Chamber','phishing',expected='SKIP_NONCORRESPONDENCE'),
    Case('Newsletter from vendor','newsletter',expected='SKIP_NONCORRESPONDENCE'),
    Case('Customer issue, remediation not verified','support',missing_facts=True,expected='DRAFT_QUALIFIED_REVIEW'),
    Case('Contractual promise demand','legal_commitment',expected='ESCALATE_NO_SEND'),
    Case('Payment instruction change','payment_change',expected='ESCALATE_NO_SEND'),
    Case('Partner invitation','partner',expected='DRAFT_REVIEW'),
]
for c in cases:
    assert route(c) == c.expected, (c.name, route(c), c.expected)
print(f'{len(cases)}/{len(cases)} deterministic routing-policy assertions passed. Not an end-to-end agent test.')
