# Project Security Incident Response Procedure Checklist

This is a focused, actionable checklist for the _Incident Commander_ (IC) and _Responders_ to follow during incident response. It is a companion to the [Security Incident Response Plan](security-irp.md) which provides full detail for each step.

## Contents
<!--TOC-->

- [Remember to _breathe_](#remember-to-_breathe_)
- [Assume roles](#assume-roles)
- [Incident Response Checklist](#incident-response-checklist)
  - [Initiate](#initiate)
  - [Assess](#assess)
  - [Remediate](#remediate)
  - [Post remediation](#post-remediation)
- [Special situations](#special-situations)
  - [False alarms](#false-alarms)
  - [Explicit Handoff Ceremony](#explicit-handoff-ceremony)

<!--TOC-->

----

## Remember to _breathe_

- No one's life is in danger.
- **Document all steps and findings!** (The Slack channel [#None](None) is recommended but other [communication channels](security-irp.md#communication-channels) may be used.)
   - Documentation facilitates communication and makes handoffs easier.
- Consult with the _Incident Commander_ (or other team members) if you have questions.

## Assume roles

See [Roles and Responsibilities](security-irp.md#roles-and-responsibilities) for detailed information about:
- [Responder](security-irp.md#responder)
- [Incident Commander (IC)](security-irp.md#incident-commander)
- [Communications Officer (CO)](security-irp.md#communications-officer)

Always use the [_Explicit Handoff Ceremony_](#explicit-handoff-ceremony) when transferring/changing roles.

## Incident Response Checklist

At a high level, incident response follows this process. _(For additional background, see the [Security Incident Response Process](security-irp.md#incident-response-process))_

### Initiate

An "event" (anomaly or suspected disruption) is reported and a  Incident Response Team member picks it up.

At this stage, the _First Responder_ is also the _Incident Commander_ (IC) and is usually working alone.

The _First Responder/IC_ allocates no more than five (5) minutes to determine whether this event might be a [false alarms](#false-alarm).
- If it appears to be a real incident, [broadcast notification of the incident](security-irp.md#communications-during-the-initiate-phase) via at least one of:
  1. Slack: [#None](None) using `@channel` (Notifies the team about the incident.)
     - This may have been done automatically via alarms via OpsGenie pager alarms
  2. Email: TheProject@example.com (Alerts the "on call" system admin.)
  3. [CivicActions/Project IR Team contacts](None) (Provides direct email addresses and phone numbers.)
- If the incident cannot be resolved in 15-30 minutes:
   - Recruit additional IR Team _Responders_
   - Designate, with an [explicit hand-off](#explicit-handoff-ceremony), a dedicated [**Incident Commander**](security-irp.md#incident-commander)

### Assess

The IR Team _Responders_ work to:

- Confirm the incident. _Is it a real incident?_
  - Was the event triggered by an [external dependency](contingency-plan.md#external-dependencies)?
  - Is a system failure causing the disruption?
  - If it's not a real incident, go to [False alarms](#false-alarm).
- Assess the severity, using the [rubric in the IR guide](security-irp.md#incident-severities). (Project incidents are generally ***Low*** severity.)
- Post an initial situation report, called a _sitrep_ ([example sitrep](security-irp.md#assess)), to the Slack channel [#None](None). Include a descriptive name, and identify the current Incident Commander and Responders.
- Assess whether to activate the [contingency plan](contingency-plan.md) (is Disaster Recovery required?).

As new IR team members arrive, the _First Responder_ either fully assumes the role of [_Incident Commander_ (IC)](security-irp.md#incident-commander) or transfers the IC role to another IR Team member via the [handoff ceremony](#explicit-handoff-ceremony)

The _Incident Commander_ duties include:

- Ensures all IR Team activities are being recorded in Slack, shared Google docs, or a [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident)
   - Other [communication channels](security-irp.md#communication-channels) may be set up and used.
- Creates a Project [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident) (if not already created)

### Remediate

The _Responders_ work to determine the cause, implement a resolution, and return the system to normal operations.

**If suspicious activity is suspected** or other unanswered questions exist, _before making any changes_:
- Make [CPM snapshots](https://cpm.project.com/) of relevant volumes and data.
- Preserve logs.
- Take screen captures of anomalous activity that can be used in post-remediation forensic analysis.
- Consider implementing a containment strategy. For example, reconfigure firewall rules for the affected instance to drop all ingress and egress traffic, except from specific IPs like yours, until forensics can be performed.

Make every attempt to determine the cause, as the cause can drive follow-up measures that prevent incident recurrence.

The _Incident Commander_ coordinates activity and:

- Is not involved in the remediation of the incident.
- Maintains all information (ticket and documentation) current as people work, tracking:
  - Team leads and members
  - Remediation items and their assignees
  - Work shifts for all roles if the incident lasts longer than 3 hours.
- Maintains communications with all stakeholders (or designates a _Communications Officer_ via [explicit handoff](#explicit-handoff-ceremony))
  - Shares _sitreps_ on a regular basis. (For high severity, hourly; medium severity, 2x daily; and low severity, daily).

### Post remediation

After the incident has been resolved:

- Update the JIRA ticket and set the status to _Ready for QA_.
- Share the final _sitrep_ with stakeholders.
- Schedule a [_Retrospective_](security-irp.md#retrospect).
- Thank everyone involved for their service.

## Special situations

### False alarms

If an event is determined not to be a security incident:

- Notify the Slack channel [#None](None) about the false alarm.
- Update the [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident), and set the status to _Done_.
- If any _sitreps_ were shared, send a final sitrep to all previous recipients, noting the false alarm.

### Explicit Handoff Ceremony

To hand off _Incident Commander_, _Communications Officer_ or _Responder_ ("ROLE") duties:

1. Outgoing ROLE initiates the handoff and briefs the incoming ROLE on the situation.
2. Incoming ROLE confirms the handoff and assumes responsibility.
3. Incoming ROLE updates the JIRA ticket and notes the handoff.
4. Incoming ROLE shares a _sitrep_, which notes the handoff.
5. Outgoing ROLE remains available for 15-20 minutes to ensure a smooth handoff and then logs off.