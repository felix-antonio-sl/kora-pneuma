---
urn: urn:gn:kb:kb-gestion-meyer-org-structure
nombre: kb-gestion-meyer-org-structure
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre kb-gestion-meyer-org-structure; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/core/gestion/kb_gn_meyer_org_structure_koda.yml (sha256:19dd2a7f613add5385b1a4586903daf82aa222c7eebf5a7fdf847433de02fe26); URN KODA legado urn:gorenuble:kb:gestion:meyer-org-structure:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2026-01-29
lang: es
tags: ["gn", "gore-os", "koda", "core", "gestion", "kb", "meyer", "org"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:kb:gestion:meyer-org-structure:1.0.0"
  title: "Principle-based Organizational Structure"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/core/gestion/kb_gn_meyer_org_structure_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "KODA-TRANSFORMER"
    created_at: "2026-01-29"
    last_modified_at: "2026-01-29"
    signature: null

ID: MEYER-ORG-STRUCTURE-KODA-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "S/D (fuente: meyer.md)"
Human-Editor: "FS"
Model-Collaborator: "GPT-5.2"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2026-01-29"
Modification-Date: "2026-01-29"
Source: "/Users/felixsanhueza/Developer/_workspaces/diagnostico_dgi/complement/meyer.md"
Ctx: 'Transformación KODA de alta densidad del documento "Principle-based Organizational Structure" (meyer.md).'
Warn: "Contenido derivado de fuente potencialmente protegida por copyright; uso interno; verificar derechos antes de redistribuir."

XRef_Required: "urn:kora:kb:spec:1.0.0"
XRef: "urn:kora:kb:transform:1.0.0"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

    REFERENCE POLICY: Ref: internal only—must point to existing ID within THIS document. XRef/XRef_Required: external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

    LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
    END_LLM_INSTRUCTIONS

Metrics:
  Source_Chars: 230054
  Artifact_Chars: 269846
  CR: 0.853
  FS: "100% (estructura preservada; contenido telegráfico preservado)"

Principle_Based_Organizational_Structure:
  ID: MEYER-DOC-01
  Title: "Principle-based Organizational Structure"
  Sections:
    - ID: MEYER-SEC-0001
      Title: "0. Document Overview"
      Text: |-
        Purp: Provide handbook for engineering entrepreneurial thinking and teamwork into organizations of any size.
        Dest: Leaders, executives, managers responsible for organizational design.
        Nat: Engineering science applied to organizational structure.
    - ID: MEYER-SEC-0002
      Title: "1. Core Thesis"
      Text: |-
        Mssn: Enable leaders to design high-performance organizational structures based on scientific principles.
        Fnd: Organizational structure is engineering science with firm principles and constructs.
      Sections:
        - ID: MEYER-SEC-0003
          Title: "1.1. Fundamental Premise"
          Text: |-
            - Cpt: Organizational Machine.
              - Def: Organization as machine that either achieves vision or frustrates ambitions.
              - Src: Sergio Paiz observation: "Most managers focus on operating poorly designed machine, struggle with it, rather than stepping back and redesigning machine."
              - Ex: Google case.
                - Ctx: Bill Coughran, senior vice president of engineering, led group from 2003 to 2011 that built Google's "engine room".
                - Ctx: Knew Google File System (GFS) would have to be replaced within couple of years.
                - Obj: Build organization capable of innovating continually over time.
                - Fnd: Role of leader of innovation not to set vision and motivate others to follow it; to create community willing and able to generate new ideas.

            - Cpt: Three Strategic Vectors.
              - Def: Great leaders pursue three parallel strategic vectors.
              - Cpt: Market Vector. Def: Alignment with customers.
              - Cpt: Technical Vector. Def: Product/service capabilities.
              - Cpt: Organizational Vector. Def: The machine itself.
              - Ctx: This document addresses organizational strategy.
        - ID: MEYER-SEC-0004
          Title: "1.2. Power of Structure"
          Text: |-
            Purp: Establish structure as most powerful element of organizational design.

            - Cpt: Key Elements of Organizational Design.
              - Def: Structure, culture, resource-governance processes, methods, metrics.
              - Cpt: Structure Primacy. Def: Structure is most powerful of all elements.

            - Cpt: Structure Definition.
              - Def: Organization chart defining everybody's domains, and processes combining those specialists on teams.
    - ID: MEYER-SEC-0005
      Title: "2. Benefits and Symptoms"
      Sections:
        - ID: MEYER-SEC-0006
          Title: "2.1. Benefits of Healthy Structure"
          Text: |-
            - Res: Individual accountabilities for results clear; people deliver results.
            - Res: Staff focused on excellence in single profession; perform better.
            - Res: Staff customer focused; relationships with clients improve; organization well aligned with clients' needs and strategies; synergies across clients' businesses discovered.
            - Res: Teams form spontaneously; work well together in flexible, well-defined processes tailored to needs of specific projects and services.
            - Res: Organization delivers commitments reliably, more quickly, with lower risk.
            - Res: Costs competitive; redundancies eliminated; internal entrepreneurs accountable for offering best value.
            - Res: Product quality increases; product line better integrated.
            - Res: Staff creative and entrepreneurial; pace of innovation in every discipline improves.
            - Res: Organization great place to work; staff empowered; conflicts of interests eliminated; jobs don't expect impossible.
            - Res: Structure lasting; not designed around incumbent personalities; defines accountabilities for all domains (current and future); automatically evolves as strategies and technologies change.
            - Res: Well-designed organizational structure contributes directly to shareholder value (mission of organization).
        - ID: MEYER-SEC-0007
          Title: "2.2. Symptoms of Poor Structure"
          Text: |-
            - Warn: Unclear individual accountabilities for results; staff task or process (rather than results) focused; confusion about who does what; redundant efforts; territorial disputes; internal competition.
            - Warn: Poor performance; people going too many ways at once; jobs too big for most people to succeed; need for all "A players".
            - Warn: Lack of customer focus; weak or strained relationships with clients; initiatives product or technology (rather than business) driven.
            - Warn: Difficulties with cross-boundary teamwork; slow response to new challenges; organization of independent "silos".
            - Warn: Slow or unreliable delivery.
            - Warn: High costs; lack of concern for frugality; empire building.
            - Warn: Poor quality; poorly integrated product line.
            - Warn: Lack of entrepreneurial spirit; staff not creative; don't take initiatives to improve functions.
            - Warn: Lagging in innovation; lack of accountability for planning and creating future.
            - Warn: Low morale and motivation; disempowerment; dead-end jobs; cynicism; stress.
            - Warn: Repeated restructurings, each fixing some problems and creating others.

            - Res: Unhealthy structure not "supplier of choice" to customers (internal or external), nor "employer of choice" to staff.
            - Res: Stressful place to work; tough organization to lead; takes lots of attention to keep running right; little time for strategic thinking.
    - ID: MEYER-SEC-0008
      Title: "3. Science of Structure"
      Text: |-
        Fnd: Organizational structure is engineering science, not matter of personalities, politics, personal style.
      Sections:
        - ID: MEYER-SEC-0009
          Title: "3.1. Definition of Science"
          Text: |-
            Def: Observation, identification, description, experimental investigation, theoretical explanation of phenomena.
            Src: American Heritage Dictionary.
            Nat: Applied science with firm principles and constructs.
            Ctx: Organizations are systems; present engineering challenge.
        - ID: MEYER-SEC-0010
          Title: "3.2. Evolution of Science"
          Text: |-
            Proc: Real-world empirical observations revealed patterns, generalized to principles and frameworks, tested over decades of actual implementation experiences.
            Res: Principles now so clear that one can look at any organization chart and know who's fighting with whom, who's not making objectives, who has ulcers.
        - ID: MEYER-SEC-0011
          Title: "3.3. Common Guidance Without Science"
          Text: |-
            Ctx: When executives don't study science of structure, reorganizations guided by:

            - Incumbents' personalities and careers; attempts to work around managers who don't do essential aspects of jobs.
            - Overly simplistic models (like "build versus run") or industry fads (like matrix).
            - Client pressures (such as groups dedicated to them).
            - Today's work, priorities, strategies.
            - Intuition.

            Res: Structure evolves through series of incremental changes by different executives, each with own philosophies and exigencies; resembles patchwork quilt of mismatched pieces.
        - ID: MEYER-SEC-0012
          Title: "3.4. Reasons to Study Science"
          Text: |-
            - Cpt: Avoid Organization du Jour.
              - Def: Without guiding principles, each restructuring solves some problems while creating others.
              - Warn: Never-ending, painful, costly series of disruptions; staff endure endless stream of unsettling changes; little real difference in way things work; costs but few benefits.
              - Res: Science helps engineer organization charts systematically, making deliberate decisions about key trade-offs.
              - Res: Structure performs well at multitude of challenges; doesn't cause unintended consequences.
              - Res: Principle-based structure dynamically adapts to changes in world; lasting investment; repeated reorganizations not required.

            - Cpt: Easier to Explain.
              - Res: Makes it easier to explain how things supposed to work.
              - Res: Easier for staff to understand; more likely to make it work as intended.
              - Res: With clear principles, executive can invite participation from leadership team without fear of endless haggling and parochial politics.
              - Res: Participation takes advantage of people's in-depth knowledge; builds deep understanding; engenders tremendous commitment.

            - Cpt: Don't Blame People.
              - Fnd: Leaders have moral obligation to study science of structure.
              - Just: Critical to know difference between poorly performing person and good person in poorly designed job.
              - Ex: University case.
                - Ctx: Growing accredited university; Sondra hired to enhance corporate "outreach".
                - Obj: Encourage corporations to utilize University as part of professional development programs (sales function).
                - Obj: Build "School of Continuing Studies" to deliver continuing education to non-traditional students.
                - Res: Sondra good at sales; pulled together existing corporate-outreach staff; gave them sales training; developed sales objectives and dashboard; increased revenues by nearly $4 million in one year.
                - Warn: Sondra failed at second objective.
                - Ctx: President hoped she would sell University's current course offerings to new audiences, perhaps repackaging into smaller programs for badges or certificates, or defining new paths to existing degree offerings.
                - Req: To do this, Sondra would have to bring opportunities to rest of University (who already knew how to put together programs and deliver education) and coordinate enterprisewide initiatives.
                - Res: Instead, Sondra came up with own plan, as if setting up parallel school; plan inconsistent with University's processes; not feasible.
                - Cause: Coordinating enterprisewide initiatives is challenging job in own right, requiring competencies quite different from sales.
                - Cause: Sondra's failure not because she was poor performer (sales success proved this); because structure gave her two very different jobs; no one could be expected to excel at both.
                - Res: President studied science of structure; saw real problem before firing great sales leader.
              - Warn: Futile and cruel to blame people for poor performance when structure is root cause of problems.
              - Req: To know difference, need to understand science of structure.

            - Cpt: New Levels of Performance.
              - Res: Principle-based structure can perform far better.
              - Src: Preston Simons, CIO at Aurora Health Care, former CIO at Abbott Laboratories.
              - Ctx: Led organizations ranging from hundreds of employees regionally to thousands globally; implemented these principles of structure in each case.
              - Res: Powerful, yet pragmatic approach consistently leads to improved role clarity; better teamwork; customer focus; entrepreneurship; improved performance; commitment.
              - Res: Uses principles as forensic tool for insights about inherited structure.
              - Res: Provides basis for participative change process allowing leadership team to contribute knowledge and build organization they truly understand and support.
    - ID: MEYER-SEC-0013
      Title: "4. Insufficiency of Alternative Approaches"
      Sections:
        - ID: MEYER-SEC-0014
          Title: "4.1. Great People Alone Not Enough"
          Sections:
            - ID: MEYER-SEC-0015
              Title: "4.1.1. Common Argument"
              Text: |-
                - Cpt: Informal Organization Argument.
                  - Def: Working relationships formed despite structure, creating "informal organization" that really determines how things get done.
                  - Cpt: Conclusion. Def: Success depends simply on hiring and developing great people who work hard, work well together, "do what's right" for organization.
                  - Res: Leads to designing organizational structures around unique talents or career needs of key executives.
            - ID: MEYER-SEC-0016
              Title: "4.1.2. Problems with This Approach"
              Text: |-
                - Cpt: Problem 1: Constant Restructuring.
                  - Def: Must restructure organization whenever anyone changes jobs.
                  - Cause: Successive managers, each with own unique talents, find carefully tailored jobs impossible to fill.
                  - Res: Each restructuring disruptive and expensive; repeated reorganizations do little to improve effectiveness; reinforce belief that structure doesn't matter (self-fulfilling prophecy).

                - Cpt: Problem 2: Fragility.
                  - Def: Organizations depending only on great people require leadership teams that work so well together that structure doesn't matter.
                  - Req: People look past own job descriptions and personal interests for good of organization.
                  - Warn: Altruism not natural; not reliable process.
                  - Res: Organizations fragile; require charismatic leader and tightly knit, dedicated leadership team; generally fall apart when executive who created team or key members leave (or get tired).

                - Cpt: Problem 3: Impracticality.
                  - Def: Organization depending on everyone being "great" is impractical.
                  - Warn: Organization requiring everyone above average difficult to staff (can't always afford best, may not be available); limited in growth potential (can only hire so many super-achievers).
            - ID: MEYER-SEC-0017
              Title: "4.1.3. Reality Check"
              Text: |-
                - Cpt: Truth About Great People.
                  - Def: Superior people who work well with peers, motivated by inspiring leader, willing to work long hours and set aside own best interests (and those of staff) to do what's best for organization, can overcome most structural dysfunctions.
                  - Warn: If structure poorly designed, inordinate amount of leaders' time, energy, goodwill spent resolving confusion and friction rather than doing real work.
                  - Rec: Rather have great people focus precious time and energies on achieving great things than dealing with self-imposed obstacles which can (and should) be fixed.

                - Cpt: Structure as Powerful Force.
                  - Ex: Large airline case.
                    - Ctx: Large airline divided IT department into two computer centers: business systems and reservations system.
                    - Ctx: Operations director tasked with keeping critical systems running efficiently, safely, reliably.
                    - Ctx: Systems-engineering manager reported to operations director.
                    - Res: Business systems group retained expensive old mainframe; systems-engineering manager failed to innovate; fired.
                    - Res: Two years later, successor fired for same reason.
                    - Res: Two years after that, another systems-engineering manager fired.
                    - Ctx: All three managers bright, experienced people good at their professions; problem wasn't their lack of ability.
                    - Cause: Operations director paid to keep things running efficiently, safely, reliably; rewarded for stability.
                    - Cause: Innovation inevitably disrupts operational stability.
                    - Res: Systems-engineering manager set up to fail.
                  - Warn: No matter how good people may be, structure is powerful force.
                  - Warn: If structure causing people to do wrong things, then "better" people will just do wrong things faster.

                - Cpt: Conclusion.
                  - Def: Great people in bad structure will fail, or at least not perform to potential.
                  - Def: Normal bell-curve of people in healthy structure can succeed.
                  - Def: Great organizations are, by design, those where average people can succeed, and super-achievers can super-succeed.
        - ID: MEYER-SEC-0018
          Title: "4.2. Great Processes Alone Not Enough"
          Sections:
            - ID: MEYER-SEC-0019
              Title: "4.2.1. Common Argument"
              Text: |-
                - Cpt: Process Engineering Argument.
                  - Def: Carefully engineered business processes are key to success.
                  - Def: As long as everybody does their part in well-designed processes, organization will perform well.
            - ID: MEYER-SEC-0020
              Title: "4.2.2. Problems with This Approach"
              Text: |-
                - Cpt: Problem 1: Process Effectiveness Depends on Structure.
                  - Def: If nobody specializes in given discipline, processes depending on that competency will fail.
                  - Req: Organization chart must provide groups dedicated to every needed discipline.

                - Cpt: Problem 2: Structure Can Override Processes.
                  - Def: Sometimes processes ask people to do things at odds with job descriptions.
                  - Cond: When staff caught between conflicting forces, they'll optimize performance appraisals, even if some processes fail.
                  - Res: Always easy to blame others involved in process for failure.

                - Cpt: Problem 3: Rigidity.
                  - Cond: Predefined processes only make sense when work highly structured and routine.
                  - Ctx: Most organizations require much more than people performing routine tasks on predefined assembly-line.
                  - Cond: In functions where projects have unique requirements, where flexibility and innovation critical components of success, simply giving everybody clearly defined role in carefully engineered process makes organization more rigid and less creative.
            - ID: MEYER-SEC-0021
              Title: "4.2.3. Conclusion"
              Text: |-
                Def: Great people working with great processes can't perform well unless structure they live in is well designed.
        - ID: MEYER-SEC-0022
          Title: "4.3. Structure Drives Performance"
          Text: |-
            Fnd: Structure is foundation on which good people and processes thrive.

            - Cpt: Performance Impacts.
              - Def: Structure is one of most powerful drivers of organization's performance: efficiency, effectiveness, agility, quality, creativity, innovation, competitiveness, customer satisfaction.

            - Cpt: Staff Impacts.
              - Def: Structure is key element of staff's competence, job satisfaction, motivation, commitment, happiness, loyalty.
    - ID: MEYER-SEC-0023
      Title: "5. Seven Fundamental Principles"
      Text: |-
        Fnd: Seven Principles provide foundation for science of structure.
        Ctx: Principles illustrated by case studies; IT organizations used as examples (largest and most complex internal support function, offers rich microcosm of companies as whole).

        | Principle   | Statement                                                                                                                                       |
        | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
        | Principle 1 | Golden Rule: Authority and accountability must match.                                                                                           |
        | Principle 2 | Specialization and Teamwork: You can only be world-class at one thing at a time; but you can't specialize if you can't team.                    |
        | Principle 3 | Precise Domains: Define clear boundaries with no overlaps or gaps.                                                                              |
        | Principle 4 | Basis for Substructure: Divide function into groups based on what it's supposed to be good at.                                                  |
        | Principle 5 | Avoid Conflicts of Interests: Don't expect people to go in two opposing directions.                                                             |
        | Principle 6 | Cluster by Professional Synergies: Cluster groups under common boss based on similar professions.                                               |
        | Principle 7 | Business Within a Business: Every manager is entrepreneur whose job is to satisfy customers (internal and external) with products and services. |
      Sections:
        - ID: MEYER-SEC-0024
          Title: "5.1. Principle 1: Golden Rule - Authority and Accountability Must Match"
          Text: |-
            Def: Authorities and accountabilities must match.
            Nat: Most important principle; absolutely essential to success of every organization.
          Sections:
            - ID: MEYER-SEC-0025
              Title: "5.1.1. The Golden Rule Statement"
              Text: |-
                Req: Authorities and accountabilities must match.
            - ID: MEYER-SEC-0026
              Title: "5.1.2. Consequences of Violation"
              Text: |-
                Cond: If authorities and accountabilities separated, serious problems inevitably arise.

                - Cpt: Authority Without Accountability.
                  - Def: Person with authorities but not matching accountabilities becomes unconstrained tyrant.
                  - Mech: Such people can make decisions without bearing consequences; can tell others what to do while others held accountable for results.
                  - Res: Little to stop them from issuing edicts that may not be practical, then letting others take blame when commands backfire.
                  - Res: Without checks and balances, they do as they please.

                - Cpt: Accountability Without Authority.
                  - Def: Those with accountabilities but insufficient authorities are disempowered and can't get jobs done.
                  - Fnd: People cannot be held accountable for results if they don't have resources and authorities necessary to achieve those results.
                  - Warn: Trying to hold staff accountable for things they can't control won't lead to good performance; only establishes scapegoat to blame when things go wrong.
                  - Res: Over time, disempowered people adopt helpless "victim" mentality, take no initiatives, spend time reading Dilbert and laughing about how futile it is to try to accomplish anything important.
            - ID: MEYER-SEC-0027
              Title: "5.1.3. Case Studies"
              Text: |-
                - Ex: Process Owners Case.
                  - Ctx: CIO appointed "process owners" at suggestion of process-improvement consultants.
                  - Ctx: Each assigned process engaging people from various parts of organization in producing specific service.
                  - Ctx: Process owners had authority over processes; had final say.
                  - Warn: Process owners didn't have matching accountability for effectiveness of processes (not always ones accountable for delivering services).
                  - Res: Process owners had authority without accountability; everybody else had accountability without authority.
                  - Res: If service-delivery groups failed, no way to know whether due to their own poor performance or due to bad process; nonetheless, they took blame.
                  - Res: Process owners implemented detailed, rigorous processes; succeeded at their mission.
                  - Res: Organization became bureaucratic, slow, inflexible.

                - Ex: CFO Mandates Others' Budgets.
                  - Ctx: In many companies, budgets determined by Chief Financial Officer.
                  - Ctx: CFO held accountable for company's financial targets, but not for business results.
                  - Mech: To achieve goals, CFO cuts others' budgets with little regard for impacts on business.
                  - Res: CFO rewarded for cost savings, not blamed for poor performance caused throughout rest of company.

                - Ex: Customer Service Held Accountable for Resolving Incidents.
                  - Ctx: Industrial products company.
                  - Ctx: Customer-service manager held accountable for resolving problems, not just coordinating resolution.
                  - Warn: Manager didn't have resources or authorities to solve many problems.
                  - Ctx: Those who created problems (production, shipping, billing, etc.) not held accountable for remediating them.
                  - Res: Resolution impeded; customers' satisfaction suffered.
            - ID: MEYER-SEC-0028
              Title: "5.1.4. Healthy Organization Model"
              Text: |-
                - Req: Everybody is "process owner" for own products and services.
                - Req: Everybody accountable for frugality, not just CFO.
                - Req: Everybody accountable for resolving any problems they create, not just customer-service group.
            - ID: MEYER-SEC-0029
              Title: "5.1.5. Empowerment"
              Text: |-
                - Def: Empowerment means everybody accountable for own results, has authority over all information, resources, decisions needed to do jobs.
                - Prohib: Empowerment does not mean anarchy; not blank check whereby people can do whatever they please.
                - Def: With accountability comes equal measure of authority (and freedom).
                - Req: People must be given no more authorities than warranted by accountabilities.
                - Nat: Fixed-sum equation; if anyone has more authorities than accountabilities, somebody else has less (or they fight for control).
                - Just: Empowerment not just fad or nicety; absolute necessity in today's competitive business environment.
                - Just: Organizations can't afford to waste one iota of talents people have to offer; every bright mind has to be engaged in achieving success.
                - Just: Empowerment fundamental to employee motivation; people want to feel proud of work; hard to feel good if treated as child and told what to do all time.
            - ID: MEYER-SEC-0030
              Title: "5.1.6. Empowerment at Every Level"
              Text: |-
                - Req: Empowerment not limited to senior managers; everyone (in every job, at every level, in every corner of organization) should be empowered to manage their piece of business, however large or small.
                - Cond: If subordinates inexperienced, not ready to take on very much on own.
                - Rec: Not to disempower them by telling them how to do jobs; rather, empower them in smaller chunks (series of small assignments, each within capabilities).
                - Res: Even relatively junior people can be empowered with authorities matching accountabilities; both equipped and motivated to succeed.
            - ID: MEYER-SEC-0031
              Title: '5.1.7. Mandating "How" Instead of "What"'
              Text: |-
                - Cpt: Implication of Golden Rule.
                  - Req: Organizations should hold people accountable for results, leave them free (within bounds) to decide how to attain those results.

                - Ex: SOx Compliance Waste.
                  - Ctx: Wallace, IT consultant, on last two projects (major ERP implementation programs in two different big companies).
                  - Src: Wallace claimed close to one-third of costs of these projects wasted in name of Sarbanes-Oxley (SOx) compliance.
                  - Def: 50 percent increase in project costs over what they otherwise would have been.
                  - Ctx: Not talking about costs of complying with SOx; saying companies could have complied to same degree at much lower cost.
                  - Ctx: One SOx requirement is documentation of IT's development and testing processes; additional work-products with cost.
                  - Cause: Waste resulted from requirement to do all IT documentation in specific way; both companies mandated use of specific documentation method (UML, Unified Modeling Language).
                  - Ctx: ERP systems well documented by vendors; documentation required by SOx would have been standard fare, much supplied by vendors.
                  - Warn: Vendors' documentation doesn't fit neatly into required format; developing documentation in specific format extremely time consuming.
                  - Res: IT leadership drove costs sky-high when issued across-the-board edict dictating "how" as well as "what".

                - Ex: Project-Management Method.
                  - Def: Common example of disempowerment is requiring staff to use particular project-management method.
                  - Warn: Standard method may be too cumbersome for small, agile projects, or insufficiently robust for really complex projects.
                  - Res: If people perform poorly, unclear if their fault or fault of imposed method.

                - Cpt: Distinction.
                  - Def: Not disempowering to clearly define every aspect of "what," including artifacts like documentation and project status reports.
                  - Def: Is disempowering to require specific "how".
            - ID: MEYER-SEC-0032
              Title: "5.1.8. Leader's Role in Empowered Organization"
              Text: |-
                - Cpt: Golden Rule doesn't preclude managers from making decisions; they have authority because they have ultimate accountability for performance of their groups.

                - Cpt: Specific Authorities and Accountabilities of Leaders.
                  - Act: Decide rules of game (create organizational ecosystem: structure, resource-governance processes, culture).
                  - Act: Once right structure in place, adjust domains as needed, arbitrate boundary disputes, ensure teamwork occurring as it should.
                  - Act: Develop talent within group (recruiting, inspiring, coaching subordinates).
                    - Ctx: Coaching offered as advice which staff may or may not choose to follow.
                    - Cond: If staff forced to follow manager's "suggestions," then manager must share accountability for their results.
                  - Act: Manage performance (negotiating staff's objectives, giving frequent feedback, measuring results, deciding rewards, managing performance problems).
                  - Act: Manage commitments and resources (assigning work within group).
                  - Act: Coordinate shared decisions within group (decisions on common methods and tools, agreements on professional practices).
                  - Act: Make decisions where consensus cannot be reached.
                  - Act: Guide business and product (technology) strategies within group (recognizing that within group's overall strategies, entrepreneurs at next level empowered to determine own strategies).
                  - Act: Serve as diplomat, representing group to peers and superiors.

                - Cpt: Leader's Job Summary.
                  - Def: Create right environment, do everything possible to help subordinates succeed.

                - Cpt: Control in Empowered Organization.
                  - Def: Managing by results can give more, not less, control.
                  - Mech: Focus moves up from micro-managing subordinates to more leveraged level of orchestrating right results.
                  - Res: Instead of being cog in machine, leader becomes driver of machine.
                  - Res: Working at more strategic level good for organization and for career.
            - ID: MEYER-SEC-0033
              Title: "5.1.9. Implications for Structure"
              Text: |-
                - Req: Define jobs based on what people produce, not by how they do work (processes, methods, tools, tasks).
                - Req: Rather than language "responsible for doing" (tasks), job descriptions should be phrased in terms like "accountable for delivering".
                - Prohib: Never create job whose purpose is to disempower others.
                - Prohib: Don't create steering committees or process owners ("integrating managers") who constrain others' prerogatives.
                - Rec: If concerned about teamwork, far better answer is to install systemic processes that align everybody's priorities and link them on teams without disempowerment.
        - ID: MEYER-SEC-0034
          Title: "5.2. Principle 2: Specialization and Teamwork"
          Text: |-
            Def: You can only be world-class at one thing at a time; but you can't specialize if you can't team.
          Sections:
            - ID: MEYER-SEC-0035
              Title: "5.2.1. Case Study: Customer-centric Structure"
              Text: |-
                - Ctx: CIO in large insurance company under pressure; business executives complaining about IT department's opacity, unresponsiveness, poor understanding of business strategies; frustrated couldn't control IT's priorities; didn't understand why many requests not being fulfilled.
                - Ctx: Trend toward decentralization; many business units started own little IT groups ("shadow IT"); groups existed because business units didn't want to do business with Corporate IT.
                - Act: CIO dedicated group to each client business unit; divided engineering staff among them; each group relatively self-sufficient, with all skills needed to deliver any applications requested by assigned business unit.
                - Ctx: Senior managers also served as primary liaisons to those business units.
                - Ctx: Structure: Janice (Sales and Marketing), Bill (Finance), Henry (HR and other Corporate functions), Eugene (Engineering and Manufacturing), IT infrastructure and operations.
                - Ctx: Client-aligned structure akin to decentralization, but with formal lines of reporting remaining within Corporate IT.

                - Cpt: Initial Success.
                  - Res: For while, structure seemed successful; Sales and Marketing clients felt IT more responsive to needs.
                  - Cause: Clients understood limits to resources (people in group) and could control priorities; more understanding when couldn't do everything.
                  - Res: Clients felt IT better understood their business; better partnership developed.
                  - Res: At first, clients happy and CIO felt less "heat" from executive peers.

                - Cpt: Problems Emerged.
                  - Warn: Client-liaison function part-time job; with big group to manage, didn't have much time to spend with clients; at best, provided point of contact; didn't add much value to clients' strategic thinking.
                  - Warn: Faced conflict of interests; advice offered biased by capabilities of applications engineers in group; regardless of clients' real needs, only delivered traditional applications.
                  - Warn: Engineering function sub-optimized; needed variety of technical specialists in group to satisfy clients' needs; each technology sub-specialty scattered among various client-dedicated groups.
                  - Res: Limited professional exchange; when staff ran into technical challenges, might not have known someone in another group already figured out answer; even if heard of others' work, peers busy with other priorities; costs rose and response times slowed as everybody reinvented solutions to common problems.
                  - Res: Little impetus for standards; people built systems optimal for specific clients, not for enterprise as whole; when company sought cost savings through consolidation ("rationalization") of applications, found it difficult; few existing applications could be used more broadly.
                  - Res: Structure reduced engineers' ability to specialize; each group had to produce every type of application needed by clients; with reduced specialization, costs rose, quality suffered, response times slowed.
                  - Res: Pace of innovation slowed; couldn't hire expert in emerging technology when only enough demand for one person to be shared across whole enterprise; had to wait until demand grew to point where each business unit alone could justify headcount.
                  - Res: Business opportunities missed; didn't have specialists in web and mobile applications; missed opportunities to build customer loyalty.
                  - Res: Impacts extended beyond IT's performance; all clients needed information about money, customers, employees, products; over time, structure led to multiple general-ledger systems and multiple records for same customer; synergies lost.

                - Cpt: Conclusion.
                  - Res: Customer-aligned organization didn't deliver advantages of its size; performed no better than number of small decentralized groups.
                  - Res: Business unit executives demanded decentralization of applications engineering function, rightly pointing out little benefit to centralized reporting.
                  - Res: CIO failed to gain benefits of being one organization; organization didn't deserve to stay together because wasn't adding value.
            - ID: MEYER-SEC-0036
              Title: "5.2.2. Why Organizations Exist"
              Text: |-
                - Cpt: Fundamental Question.
                  - Def: Why would organization of 10, 100, or 1000 people perform any better than equal number of individuals scattered around enterprise or among small companies?

                - Cpt: Common Purpose Insufficient.
                  - Def: One obvious answer is people within organization work toward common purpose.
                  - Cond: For very simple tasks, might be enough; 100 individuals picking up trash along stretch of roadside may perform as well as 100-person organization; only have to agree on territories to avoid redundant work.
                  - Ex: 100 individuals, working independently, each trying to make cars; each would have to be expert in virtually every branch of design, engineering, manufacturing, etc.
                  - Warn: No one person can possibly know enough about all those professions to succeed.
                  - Res: Independent people agreeing to work toward common purpose solves problem of volume, but not of complexity.
            - ID: MEYER-SEC-0037
              Title: "5.2.3. Cybernetic Variety"
              Text: |-
                - Cpt: Human Mind Limitations.
                  - Cause: Reason found in limitations of human mind.
                  - Def: We can think only so many thoughts in day, read only so much, know only so much.
                  - Def: We have finite number of "brain cycles" each day.

                - Cpt: Cybernetics.
                  - Def: Study of dynamic systems (like thermostat that turns on heater when it gets too cold).
                  - Ctx: Organizations can be viewed as large, complex cybernetic systems.

                - Cpt: Variety Definition.
                  - Def: In cybernetics, term "variety" has special meaning.
                  - Def: Complexity inherent in system, multiplied by pace of activities (e.g., volume of work per day).
                  - Mdl: VARIETY = COMPLEXITY x PACE
                  - Def: Measure of throughput or bandwidth; amount and diversity of information confronting organization at any point in time.
                  - Res: As complexity increases, as volume increases, as time-frames shorten, variety goes up.

                - Cpt: Implication.
                  - Def: World around us swarming with immense variety, way too much for any one person to grasp.
                  - Def: We're all limited in our variety-processing abilities.
            - ID: MEYER-SEC-0038
              Title: "5.2.4. Definition of Specialist"
              Text: |-
                - Cpt: Three Choices for Finite Brain Cycles.
                  - Cpt: Choice 1: Generalist.
                    - Def: Know little bit about everything; proverbial "jack of all trades, and master of none".
                    - Res: Able to do many things, but none particularly well; never know enough about any one field to master it.
                    - Ctx: Describes many individuals working independently.
                  - Cpt: Choice 2: Extreme Specialist.
                    - Def: Focus all variety-processing abilities on one topic, learn virtually nothing about anything else.
                    - Res: Excel at that one thing; wouldn't be able to work well with others.
                    - Warn: This degree of specialization not practical.
                  - Cpt: Choice 3: T-shaped Specialist.
                    - Def: Focus on one profession, while still using some brain-cycles to know little about lots of things so as to be able to work well with others.
                    - Def: This "T-shaped" person is definition of practical specialist.

                - Cpt: Cybernetics Conclusion.
                  - Def: Cybernetics tells us people can only be world-class experts at one thing at a time.
                  - Ctx: May rotate among specialties in course of careers; but at any point in time, each must concentrate on single profession to master it.
                  - Def: Only T-shaped people can be really good at what they do.
                  - Src: Niels Bohr: "An expert is person who has made all mistakes that can be made in very narrow field".
            - ID: MEYER-SEC-0039
              Title: "5.2.5. Why Organizations Exist - Answer"
              Text: |-
                - Def: Organizations exist to allow people to specialize.
                - Mech: When T-shaped specialists in diverse range of fields work together, organization has both depth and breadth; can process more variety.
                - Warn: Organization of generalists performs no better than equal number of individuals.
                - Fnd: Whole point of forming organizations is to permit people to specialize.
                - Def: Within some practical limits, more that people specialize, better they (and their organizations) perform.
            - ID: MEYER-SEC-0040
              Title: "5.2.6. Benefits of Specialization"
              Text: |-
                Src: Adam Smith described advantages of "division of labor" in 1776.
                Fnd: By specializing, people gain deep knowledge of one discipline; study its ever-evolving methods and tools, stay abreast of innovations; by applying discipline many times in many different circumstances, specialists accumulate experience; get really good at what they do.

                - Res: Productivity: Specialists more efficient; increased productivity translates into cost savings.
                - Res: Speed: With all experience, specialists have ready answers; don't have to climb learning curve with each new challenge; know latest methods and technologies in field, which can leverage time; things get done faster.
                - Res: Quality: Specialists produce higher quality because they know how; products more usable, more capable, more maintainable, have lower life-cycle costs.
                - Res: Risk: People with more competence and experience deliver results more reliably, with fewer risks.
                - Res: Innovation: Specialists can keep up with literature; first to learn about emerging technologies and techniques; pace of innovation improves.
                - Res: Reduced stress: Specialists experience less stress; may be under pressure to produce lot, but confident of abilities; more productive, stable, happy.
                - Res: Motivation: With greater competence, easier to excel and rise up ranks in fields; specialists more valued in market than generalists; better career opportunities.

                - Cpt: Conclusion.
                  - Def: Specialists always outperform generalists.
            - ID: MEYER-SEC-0041
              Title: "5.2.7. Concerns About Specialization"
              Text: |-
                - Cpt: Practical Limits.
                  - Warn: Organizations can't afford to specialize to point of becoming "one deep" (dependent for critical services on just one individual).
                  - Warn: Person may become bottleneck; problems when takes vacation or leaves company.
                  - Rec: Sometimes cross-training can address this problem; in other cases, structure must define domains more broadly (sacrificing some specialization) to avoid groups of one.

                - Cpt: Job Narrowing Concern.
                  - Def: People do same thing, day after day (like on assembly line where people specialize in specific set of tasks).
                  - Warn: Narrow jobs disempowering, waste talent, demotivate staff.
                  - Def: Healthy specialization is not job narrowing.
                  - Def: Specialists do everything in their field of study: work with customers; deliver today's work; support past work; keep up with innovations; plan and develop future offerings; improve their processes.
                  - Res: As much job diversity in doing all that within one specialty as there is in doing little bit in many fields.

                - Cpt: Market Reality.
                  - Def: Market rewards specialists, not generalists.
                  - Warn: Some resist specialization to avoid accountability for excellence in any one thing; would be best suited to very small organizations, ideally "organizations" of one.
            - ID: MEYER-SEC-0042
              Title: "5.2.8. Specialization Requires Teamwork"
              Text: |-
                - Cpt: The Catch.
                  - Ex: Organization made of specialists, all very good at respective professions, but each acting independently without teamwork.
                  - Res: Would perform terribly; worse than collection of independent generalists.
                  - Cause: No one specialist sees big picture; collectively unlikely to get anything done.
                  - Def: More people specialize, more they become interdependent.
                  - Def: You can't specialize if you can't team.

                - Cpt: Gating Factor.
                  - Def: This often gating factor.
                  - Cond: If organization not good at cross-boundary teamwork (assembling just right mix of specialists onto teams, getting them to work well together), then must back away from specialization so groups are independent rather than interdependent.
                  - Res: Must sacrifice performance to avoid teamwork.
                  - Res: Leads to "silo" organization.
            - ID: MEYER-SEC-0043
              Title: "5.2.9. The Silo Organization"
              Text: |-
                - Cpt: Common Belief.
                  - Def: Some leaders believe only way to get people to work well together is to put them under common boss, who presumably will form teams and force staff to cooperate.
                  - Just: Citing Golden Rule, they add that to hold managers accountable for results, must give them authority over all needed resources.
                  - Res: Accept current, limited teaming capabilities of organizations; design structure to minimize interdependencies and "hand offs"; put all skills needed by function under its manager.

                - Cpt: Silo Definition.
                  - Def: Organization made up of groups that are self-sufficient and don't need to work together all that much (like bunch of vertical silos that never touch).

                - Cpt: Result of Silos.
                  - Def: Each profession scattered among various groups that need it.
                  - Res: Fragmentation reduces specialization; each member of that profession within each silo must cover entire profession.
                  - Res: Lower performance; benefits of specialization lost.

                - Cpt: Alternative.
                  - Def: Don't need to build silo structures to match authorities to accountabilities.
                  - Ex: Doing so like saying need to own own grocery store to control what you eat.
                  - Def: Just as managers have authority over external vendors, they can manage team-members in other groups who are assigned to them.
                  - Def: Antidote to silos is effective teamwork across boundaries.
            - ID: MEYER-SEC-0044
              Title: "5.2.10. Implications for Structure"
              Text: |-
                - Req: More people specialize, better they perform; don't design jobs for generalists, or expect people to be experts at too many things; jobs should be designed around well-focused specialties.
                - Req: Can't specialize if can't team well across boundaries; more willing to invest in cross-boundary teamwork, more can specialize (avoid silos of generalists) and better organization will perform.
                - Fnd: Organizations exist in order to allow people to specialize, which in turn depends on effective teamwork.
        - ID: MEYER-SEC-0045
          Title: "5.3. Principle 3: Precise Domains"
          Text: |-
            Def: Define clear boundaries with no overlaps or gaps.
          Sections:
            - ID: MEYER-SEC-0046
              Title: "5.3.1. Domain Definition"
              Text: |-
                - Def: Organization chart determines everybody's "domains" (boundaries within which each group functions).
                - Warn: Sometimes group's domain defined only by few words in box; when different people interpret those words in different ways, three problems occur: overlaps, gaps, lack of focus.
            - ID: MEYER-SEC-0047
              Title: "5.3.2. Case Study: Vague Domains"
              Text: |-
                - Ctx: CIO put Rick in charge of "Infrastructure" group, Charlie managed "Enterprise Architecture" (EA).
                - Ctx: Charlie (Enterprise Architecture) believed his job was to design infrastructure; proposed cutting-edge technologies that weren't yet stable, but constituted elegant design.
                - Ctx: Rick fought that; looked bad when resisted innovation; but knew couldn't deliver reliable services with technologies not ready for production environment; ignored Charlie and designed own infrastructure.
                - Cause: Rick and Charlie didn't dislike one another; fought because they were paid to fight; both believed they had authority over design of infrastructure.
            - ID: MEYER-SEC-0048
              Title: "5.3.3. Overlaps"
              Text: |-
                - Def: Lack of clarity may cause multiple groups to think they're responsible for same function (overlapping domains).
                - Res: When domains overlap, staff fight and compete with one another.

                - Cpt: Intentional Internal Competition.
                  - Def: Some leaders create overlapping domains intentionally, thinking internal competition will elicit better performance.
                  - Def: Might argue it maximizes creativity, with different alternatives coming from various competing groups.
                  - Warn: Internal competition should never be needed.
                  - Just: Most companies face competition; in monopoly, not-for-profit, government organizations, external metrics (customer satisfaction, cost benchmarks) can keep people sharp.
                  - Just: For internal service providers, there's competition from vendors; nothing sacred; product development, manufacturing, sales, all support functions can be outsourced.
                  - Just: Another form of competition for internal service providers is decentralization (business units have own support functions rather than work with shared-services provider).
                  - Def: Don't need overlapping domains to motivate performance or creativity.
                  - Rec: If need for competitive performance not clear to staff, outsourcing or benchmarking study can serve as wake-up call, provide metrics of staff's competitiveness.

                - Cpt: Costs of Overlapping Domains.
                  - Warn: Reduced specialization: Splitting profession into multiple groups reduces specialization; costs include lower productivity, slower delivery, lower quality, greater risk, less innovation, more stress, lower motivation. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.
                  - Warn: Redundant efforts: More than one group does same research, produces same kind of products; solutions reinvented rather than reused; wastes time and money, increasing costs.
                  - Warn: Less innovation: When two groups study same thing, something else that one might otherwise have explored is missed.
                  - Warn: Confusion: When two groups offer same service, customers don't know where to go for what; organization appears confused and inefficient.
                  - Warn: Product dis-integration: Multiple, incompatible versions of same product can undermine enterprise synergies; in engineering, overlaps may result in dozens of different fasteners (nuts and bolts) with essentially same purpose, increasing costs of manufacturing, inventories, support.
                  - Warn: Less teamwork: Internal competition may be friendly, limited to just part of staff's work; but inevitable friction undermines teamwork; no amount of team-building can overcome this force built into structure.
                  - Warn: Lack of entrepreneurship: Whenever single line of business fragmented, no one feels "ownership" as entrepreneur accountable for its performance, now and in future.

                - Cpt: Conclusion.
                  - Def: Whether by deliberately pitting people against one another or inadvertently leaving boundaries vague, internal competition is costly.
                  - Req: Good structure defines distinct domains, with no overlapping boundaries.
            - ID: MEYER-SEC-0049
              Title: "5.3.4. Case Study: Gaps"
              Text: |-
                - Ctx: In many fields, multiple layers of engineering, each building on lower layers.
                - Ctx: One IT department had applications development groups, but no groups dedicated to lower-layer technologies (other than infrastructure managed by Operations).
                - Ctx: Jim given responsibility for manufacturing and supply-chain systems; while working on just-in-time inventory management, studied electronic data interchange (EDI); as automated factory, learned lot about document management.
                - Ctx: Donna's financial applications group developed expertise in forecasting algorithms and reporting tools.
                - Ctx: Carey's customer applications group learned to quickly deliver small web applications and analyze masses of data company collected on customers.
                - Ctx: Structure: Jim (manufacturing and supply-chain applications plus EDI and document management), Donna (financial applications plus forecasting models and reporting tools), Carey (customer applications plus Agile development methods and big-data analytics), Operations.
                - Warn: Encouraged to share knowledge with one another; but rarely happened; managers allocated all resources to own projects; when Jim asked Donna for help with user-friendly reporting tool for inventory data, her staff too busy developing financial applications to work on his projects.
                - Res: Whenever needed technology missing (or just out of reach), people muddled through; multiple learning curves and replication of efforts costly; working outside one's expertise eroded performance, quality, reliable delivery.
                - Res: No single leader had job of ensuring comprehensive range of supporting technologies available; some critical new technologies ignored; business opportunities lost.
            - ID: MEYER-SEC-0050
              Title: "5.3.5. Gaps"
              Text: |-
                - Def: When function is missing, gaps occur.

                - Cpt: Results of Gaps.
                  - Warn: Unreliable delivery: With no one thinking about function on daily basis, it's "catch as catch can" (done when need becomes urgent and obvious, or when people have spare time and happen to think of it); not reliable process.
                  - Warn: Reduced specialization: Staff filling gap outside their specialty aren't experts; don't have time to learn that other profession; costs described under Principle 2. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.
                  - Warn: Overlaps: Gaps create overlaps; group that needs missing specialty fills gap, but only for itself since not its primary mission; in time, multiple groups fill same gap, creating overlaps.
            - ID: MEYER-SEC-0051
              Title: "5.3.6. Focus"
              Text: |-
                - Def: People naturally want to feel proud of their work.
                - Warn: When domains unclear, staff don't know what they're supposed to be good at; sense of direction becomes foggy; natural drive for excellence thwarted.
                - Res: May try to be good at too many things and become generalists; or may just follow personal interests, and gaps or overlaps occur unpredictably.

                - Cpt: Benefits of Clear Domains.
                  - Res: Give people focus they need to excel.
                  - Res: Tell people what literature, which conferences, which methods and technologies, what research to study.
                  - Res: Staff develop feeling of pride in their group's unique function; strive to do it well.
                  - Res: Clear domains basis for effective performance management; performance objectives and other metrics can be clearly defined only if jobs clearly defined.
                  - Res: Organization as whole requires clear domains to operate as planned; both customers and staff need to know where in organization to go for help they need.
                  - Res: Good structure provides crystal clear definitions of each group's domain; entire scope of organization divided among groups within it, with no gaps or overlaps, with clearly worded boundaries.
            - ID: MEYER-SEC-0052
              Title: "5.3.7. Case Study: Roles and Responsibilities"
              Text: |-
                - Ctx: Traditional "roles and responsibilities" blur accountabilities and authorities.
                - Ctx: IT organization where applications-development process very confused.
                - Ctx: Aaron ran applications engineering group; "business analysts" in Mark's group worked with clients to define requirements and high-level designs; "project managers" reporting to Jay (PMO) responsible for large strategic projects.
                - Ctx: Structure: Aaron (applications engineering), Mark (business analysts), Jay (project management office PMO).
                - Ctx: Lot of friction; CIO instructed them to work out respective "roles and responsibilities".
                - Ctx: Answer: Aaron responsible for applications-development process; Jay decided project-management methods; promised they knew difference; Aaron defined projects for his group; Mark's analysts responsible for specifications and high-level designs; once specs and high-level designs done, Mark handed projects off to Jay's project managers (if big and "strategic") or to Aaron's group (for smaller projects); Jay and Aaron both responsible for project delivery; even for big projects Jay's PMO managed, Aaron had role (supplied engineers to do most of work); Aaron retained responsibility for maintenance and support of applications once deployed.
                - Res: CIO asked: "Who's responsible for project success?" Mark looked away; not his problem, even though analysts controlled critical step in process; both Aaron and Jay raised hands; if small project (enhancement to existing application), Aaron's group responsible; anything big deemed "strategic project" and Jay's PMO took over.
                - Warn: Delivery problems persisted; neither Jay nor Aaron could control resources needed to get job done; Jay pulled engineers out of Aaron's group to staff strategic initiatives; Aaron yanked engineers off Jay's projects to deal with urgent maintenance issues, putting Jay's projects in jeopardy.
                - Warn: Even small, urgent projects took long time; Mark chose requirements-planning method; Aaron chose meticulous development method which slowed projects; Jay decided project-management method (also slowed projects); three methods didn't mesh, required lots of paperwork for every hand-off; all three managers shared responsibility for overall process, but none had power to fix it.
                - Warn: Aaron's engineers, responsible for small projects, got little support from Jay's PMO staff who busy with big initiatives; project-management capabilities remained weak.
                - Warn: Aaron held accountable for long-term integrity of applications; but couldn't control all decisions that affected it; all made decisions that impacted quality of applications.
                - Res: All set up to fail, with overlapping accountabilities and without authorities needed to deliver results; even though divided up tasks, stepped on each other's toes and tensions rose.
            - ID: MEYER-SEC-0053
              Title: "5.3.8. RACI Framework"
              Text: |-
                - Def: RACI method sorts who has Responsibility for doing it, to whom they are Accountable, with whom they have to Consult, whom they're to keep Informed.

                - Cpt: RACI Problems.
                  - Warn: Responsibilities: Like simple roles and responsibilities, defines accountabilities for tasks and processes, not results.
                  - Warn: Accountable: Person with authority to make or approve decisions may or may not be customer; risks separating authorities from accountabilities.
                  - Warn: Consulted: RACI defines key contributors, but not their deliverables; they lack accountability for results; fixed list of contributors may not be right for every project.
                  - Warn: Informed: Fixed list may or may not be right stakeholders for every project; bureaucratic, not flexible and dynamic; people spend lot of time "consulting" and "informing," whether or not it adds value.
            - ID: MEYER-SEC-0054
              Title: "5.3.9. Downside of Jobs Designed Around Tasks"
              Text: |-
                - Warn: People execute tasks; not asked to think creatively about how to attain intended results; wastes insights of those in best position to know best way to get things done; tedious jobs lead to boredom and degrade morale.
                - Warn: Each group sub-optimizes (and perpetuates) its steps in current process; if tasks don't add up to intended results, not in position to fix it.
                - Warn: Boss who coordinates all tasks must plan every project in detail, monitor everyone's work, adjust tasks when things go wrong; busy managing tasks, doesn't have time to think about own challenges (building relationships, innovation, business strategies).
                - Warn: If project requires new task, may be nobody's job and hence task may not get done; puts ultimate deliverable in jeopardy.
                - Warn: When disempowered people interact with customers, both parties frustrated; customers ask for results that task-focused staff not able to offer; staff feel badly that can't satisfy customers.
                - Warn: People believe they've done enough if put in required hours and completed tasks, whether or not job is done; go through motions, without caring (or even knowing) whether motions produce intended results.
                - Warn: When sorting tasks among groups, nothing to stop accidentally separating accountabilities and authorities.
                - Warn: Roles and responsibilities don't define accountabilities for leadership (improving methods and tools, sorting out processes and relationships with peers, exploring emerging technologies, selecting and managing vendors, developing strategies); doesn't appoint leaders responsible for managing today's business and planning tomorrow's.
                - Res: All adds up to unhappy customers and staff.
                - Def: Problem with "roles and responsibilities" is, can sort tasks in excruciating detail, and still won't know who's accountable for delivering organization's products and services.
            - ID: MEYER-SEC-0055
              Title: "5.3.10. Domains Based on Results"
              Text: |-
                - Def: Organizations don't make money by going through motions; make money by producing results.
                - Def: Key to good domains is bounding what people produce rather than what they do.
                - Res: Dividing up results actually lot easier than sorting tasks; list of organization's products and services far shorter than all tasks people do and roles they play.
                - Res: By defining who produces what, automatically know who does what.

                - Ex: Applications Manager Example.
                  - Ctx: Aaron is applications manager; accountable for entire portfolio of applications.
                  - Cond: If Aaron not clear about exactly what customer needs, may get help from Mark's business analysts; Mark's group produces requirements definitions, not product designs (not even at high level, since design is engineering task).
                  - Ctx: Once requirements clear, Aaron runs project; produces anything related to applications engineering (repair, enhancement, even major strategic initiatives); single point of accountability for all applications.
                  - Ctx: Jay is expert in project management, but that doesn't give him right to take over Aaron's projects; Jay sells Aaron project plans, training, project facilitation, project administration services; whether or not Aaron's engineers get help from Jay, still accountable for delivering projects, big and small.
                  - Ctx: Aaron's job to stay abreast of innovations in engineering methods; Mark continually refines requirements-planning methods; Jay runs consulting business and has to keep up with project-management methods and tools.
                  - Res: Since each group only produces results within its domain, boundaries clear; roles and responsibilities (and hand-offs) clear because everybody knows what they produce, for clients and for one another.
            - ID: MEYER-SEC-0056
              Title: "5.3.11. Implications for Structure"
              Text: |-
                - Req: Provide every group with precisely worded boundaries.
                - Req: Ensure no overlaps; never create internal competition.
                - Req: Ensure no gaps; place every needed specialty within domain of one group.
                - Req: Domains should bound what people produce, not roles they play or tasks they're responsible for.
                - Req: Clear domains take more than few words in box on organization chart (vague phrases like "infrastructure" or "operations"); each box should be accompanied by carefully worded paragraph that clearly bounds what each group produces.
                - Res: Precise domains, defined by results, help people understand how structure supposed to work; clients know whom to call for what; staff better understand what's expected of them.
                - Res: Teamwork improves because everybody empowered to do what it takes to deliver their products and services; they know where to go for help when they need it.
        - ID: MEYER-SEC-0057
          Title: "5.4. Principle 4: Basis for Substructure"
          Text: |-
            Def: Divide function into groups based on what it's supposed to be good at.
            Ctx: Organization big enough to require multiple groups in essentially same profession; Principle 3 says domains defined by respective results; but how divide all various deliverables among those multiple groups?
          Sections:
            - ID: MEYER-SEC-0058
              Title: "5.4.1. Case Study: Structure by Clients' Business Processes"
              Text: |-
                - Ctx: CIO viewed IT as means of supporting clients' business processes; rather limited view; but at least wanted to focus staff on business rather than just technologies.
                - Act: Dedicated group to each of company's core processes; Gail given responsibility for corporate product-development process; Jerry looked after entire order-to-invoice process; Tom supported all company's financial and administrative processes.
                - Ctx: Structure: Gail (product-development process), Jerry (order-to-invoice process), Tom (financial and administrative processes).
                - Ctx: Each group expected to become familiar with workflows, design solutions that optimized these business processes.

                - Cpt: Problems in Practice.
                  - Warn: Redundant learning curves: Various processes all required many common skills; caused lot of parallel learning curves; under influence of innovative clients in R&D, Gail first to develop applications on then-new mobile devices; later, when Jerry embarked on sales-force automation project, his group had to research same technologies; while helped one another with advice, weren't able to flexibly deploy existing expertise to one another's project teams; staff still needed time for learning what others already knew; increased costs and delayed projects.
                  - Warn: Redundant work: Parallel efforts led to redundant work; both Gail and Jerry developed document-tracking modules; drove costs up further.
                  - Warn: Reduced specialization: Skills needed by multiple processes scattered among groups, reducing staff's ability to specialize; Gail and Jerry both needed expertise in product data; Jerry and Tom both worked on customer, sales, financial data; all three worked on human resources data; became specialists in clients' business processes, but generalists with regard to own profession of engineering specific types of applications; performance naturally suffered.
                  - Warn: Product dis-integration: Each group independently developed own versions of financial, customer, product databases; fragmented data caused confusion when different reports gave clients conflicting views of "same" data; when did collaborate on few common applications and databases, other problems occurred; each enhanced same applications at various times; as result of "patch on patch," systems integrity deteriorated.
                  - Warn: Weak client relationships: CIO expected structure would bring IT closer to clients; however, not evident; most business units involved in numerous business processes; Manufacturing involved in both product development and production; thus, both Gail and Jerry served Manufacturing executives, focusing on different aspects of jobs; with no single point of contact for client like Manufacturing, appeared various IT groups competing for clients' attention; IT appeared poorly coordinated; also meant clients had to determine which workflow wished to discuss before could know whom to call; IT's client liaisons not included in clients' thinking early on, where real strategic discoveries made; furthermore, since processes touched multiple clients, IT managers couldn't focus on just one business unit; with more business units to cover, had less time to get to know people in each; also distanced IT from clients; finally, some clients weren't involved in any of core business processes; doesn't mean weren't important; top executives rarely engaged in routine business processes; clients such as president and executive vice president of planning and business development had no designated client liaisons, received poor service.
                  - Warn: Biased business diagnosis: Group dedicated to business process naturally biased in favor of automating that workflow; Gail, for example, paid to believe automating product-development process most important thing to do; however, corporate engineering function might have benefited far more from solutions that improve effectiveness of key individuals (e.g., engineering design tools) that have nothing to do with automating workflow; similarly, Manufacturing executive might be involved in critical decision, like consolidating plants, requiring decision support or collaboration tools (challenges that have nothing to do with any of chosen processes); due to bias for automating business processes built into structure, high-payoff opportunities missed.
            - ID: MEYER-SEC-0059
              Title: "5.4.2. Basis for Substructure Definition"
              Text: |-
                - Def: Way you divide domains among groups within profession is termed basis for substructure.
                - Def: Determines people's specialties (their bottom-of-the-T).

                - Cpt: Examples of Different Bases.
                  - Ex: If assign groups to clients' business processes, they'll become experts on those workflows, but generalists with regard to clients, their engineering disciplines, and services.
                  - Ex: If assign groups to clients (for internal service providers, business units; for companies, territories), they'll become very close to those clients while becoming generalists with regard to organization's products and services.
                  - Ex: If assign groups to technologies and disciplines (e.g., specific products), they'll become experts in those products while becoming generalists with regard to clients.
                  - Ex: If assign groups to services, they'll become experts in delivery of those services, while becoming generalists with regard to organization's clients and its products.
            - ID: MEYER-SEC-0060
              Title: "5.4.3. Consequences of Wrong Basis"
              Text: |-
                - Warn: Reduced specialization: If basis for substructure anything other than function's expertise, then staff will specialize in something other than their primary mission; in case study, groups specialized in business processes, not in knowing clients or in their engineering profession; as another example, when Sales substructured by product lines (sales force within each business unit), specialization in clients' business reduced; since each Sales group must cover all clients, staff have less time with each client, get to know them less well; as per Principle 2, when specialization reduced, performance suffers: lower productivity, slower delivery, lower quality, greater risk, less innovation, more stress, lower motivation. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.
                - Warn: Domain overlaps: At same time, inappropriate substructure often creates overlapping domains; if Engineers divided into client-dedicated groups, multiple groups deliver essentially same solutions to respective clients; often lot of reinvention; when Sales substructured by product line, clients confused by multiple points of contact, where have to call one person for some products and another for others; costs of overlaps described in Principle 3. Ref: ORG-STRUCT-PRINCIPLE3-OVERLAPS-01.
                - Warn: Inappropriate biases: Wrong basis for substructure can induce wrong biases; staff give poor advice, optimize wrong objectives; Sales force divided by product lines can't be trusted advisors to clients; recommendations always biased toward own product lines, not clients' real needs.
                - Warn: Disempowerment: Another problem occasionally resulting from inappropriate substructure is violation of Principle 1 (Golden Rule); two groups may fulfill essentially same function, one doing thinking (e.g., planning, or designing processes) while other does delivery; neither wholly responsible for results; costs of this disempowerment described under Principle 1. Ref: ORG-STRUCT-PRINCIPLE1-VIOLATIONS-01.
            - ID: MEYER-SEC-0061
              Title: "5.4.4. Implications for Structure"
              Text: |-
                - Def: Organization chart defines everybody's specialties (their "bottom-of-the-T"); people concentrate on whatever their job's domain may be, become generalists at everything else.
                - Req: Use basis for substructure that exactly matches what people are supposed to be good at.
                - Ctx: There's no one right answer for entire organization; but for each specific function, specialty ("bottom of T"), and hence right basis for substructure, should be evident.
                - Ex: If want engineers to be good at designing things, define their domains by what they design; if job of Sales is to know clients, define their domains by clients they serve.
        - ID: MEYER-SEC-0062
          Title: "5.5. Principle 5: Avoid Conflicts of Interests"
          Text: |-
            Def: Don't expect people to go in two opposing directions.
            Ctx: To support empowerment, Principle 3 states groups' domains should be defined by results they produce; organization produces many different results; what goes best with what? What's right way to cluster set of results into group's domain? Two considerations: conflicts of interests (this Principle 5), and professional synergies (Principle 6).
          Sections:
            - ID: MEYER-SEC-0063
              Title: "5.5.1. Case Study: Governance and Client Liaison Group"
              Text: |-
                - Ctx: IT organization found itself overwhelmed with unchecked demand coming from both clients and internal projects; needed to better manage process by which new work taken in; CIO also wanted to better align IT with clients' business strategies by setting right priorities.
                - Act: Instead of addressing demand management and alignment through business-driven resource-governance processes, CIO put Martha in charge of "Governance" group; responsibilities included business relationship managers, demand management (deciding priorities among proposed projects), project portfolio management (PMO).
                - Ctx: Other groups responsible for project delivery and ongoing services.

                - Cpt: Martha's Conflicts of Interests.
                  - Warn: Had authority to decide project priorities; since not all benefits measured to point of calculating accurate returns (ROI), couldn't just go by numbers; had to judge merits of clients' projects; conflicts with business relationship management role which attempts to be on clients' side of table; will clients be open and trust people who will later judge merits of their requests?
                  - Warn: Similarly, judging internal projects proposed by peers undermines service orientation expected in project management function, which supposed to help peers deliver those projects.
                  - Warn: Since Martha's job was to limit demand to available resources, will business relationship managers be aggressive about seeking new high-payoff opportunities (which makes limiting demand more difficult)?
                  - Warn: Business relationship managers help some clients discover new opportunities; will projects that other clients define on own (without this group's help) get fair treatment when comes to setting project priorities?
                  - Warn: Will discovery process (which should be business driven and unbiased) recommend services as well as projects, despite bias toward projects coming from Martha's project-management function?
                  - Warn: Some high-payoff opportunities may be urgent; project-management function not going to like these disruptions to well-planned project schedule.
            - ID: MEYER-SEC-0064
              Title: "5.5.2. Five Fundamental Conflicts of Interests"
              Text: |-
                Def: If put wrong deliverables together in single job, can inadvertently create conflicts of interests (two or more missions that are in some way opposed).
                Def: Five fundamental conflicts of interests inherent in all businesses, and in many organizations within enterprises.

                - Cpt: Conflict 1: Invention Versus Operations.
                  - Def: Invention (major innovations) versus operational stability.
                  - Def: Some managers find themselves responsible for both researching and developing new technologies (invention), and also for operating them; combining invention and operations may be attempt to give manager complete piece of business to run; however, misguided.
                  - Ex: George Case.
                    - Ctx: Manager given both infrastructure operations and infrastructure engineering responsibilities.
                    - Res: 6 months later, stabilized operations but holding up projects.
                    - Ctx: Working 60-hour weeks to document procedures; still had ways to go; hadn't started thinking about capacity planning, change control, disaster recovery, security administration; half day went into fire-fighting; last thing needed was another major application coming on-stream.
                    - Act: Decided once-a-month window for installing new applications would be more than ample; instituted lot more rigor around testing and quality control, even for small projects like enhancements.
                    - Res: Made great progress stabilizing operations, but innovation stopped.
                  - Ex: Telecommunications Cable Manufacturer.
                    - Ctx: Promising executive given responsibility for both business development (acquisitions) and operating acquired companies during transition into corporation.
                    - Res: After first major acquisition, CEO disappointed to find little done in way of new deals.
                    - Cause: Running and integrating acquired company required executive's full attention; after first big acquisition, had no time for new deals; by combining invention and operations, CEO left without business development function.
                  - Def: Term "invention" meant to imply creating entirely new things (developing new ideas, products, methods); special type of innovation, beyond marginal changes of continual improvement.
                  - Def: Invention is crux of this conflict of interests; any function can be innovative; but invention and operations antithetical.
                  - Cause: When one person asked to do both, not likely to find ideal balance; operational issues tend to take precedence; fire-fighting swamps invention; short-term problems take attention away from long-term opportunities; those who "keep things running" have little time for future-oriented invention.
                  - Cause: Not just matter of having time; invention not in their best interests; major changes threaten stability and efficiency of operations; operations staff will pursue innovation on margin (get better at what currently do); unlikely to pursue breakthroughs which inevitably disrupt operational stability.
                  - Ctx: Generally, conflict constrains invention; but cases where opposite true (under leader who prefers engineering, invention takes precedence; every new idea finds way into production, whether or not can be supported reliably; operations never stabilize).

                - Cpt: Conflict 2: Purpose-specific Solutions Versus Components.
                  - Def: Many organizations produce two different kinds of products: some purpose-specific, others components which may stand alone or be part of purpose-specific solutions (complete products versus parts that go into them).
                  - Ex: Construction industry: Some experts design buildings (architects), other experts design bridges (civil engineers); both draw on experts in common components (structural engineers, electrical engineers, traffic engineers).
                  - Ex: IT: Business applications purpose-specific; one team of developers may specialize in financial applications, another in customer applications; all different applications engineers draw on experts in component technologies (computing platforms, databases, middleware).
                  - Warn: If group expected to produce both purpose-specific solutions and component solutions, unhealthy bias built into organization chart; staff tend to put everything on familiar platforms.
                  - Res: Conversely, keeping them separate has advantages.
                  - Ex: PDC Bleach Operation.
                    - Ctx: PDC bought bleach operation with two factories; one factory produces hypochlorite (base chemical); sent to second factory which dilutes it and blends with fragrances to produce consumer bleach (application managed by Consumer Division).
                    - Res: Industrial Division quick to figure out hypochlorite used in several industrial applications like mining and agroindustry; distinguishing purpose-independent (base chemical) from purpose-specific (consumer bleach) products led to new source of revenues.

                - Cpt: Conflict 3: Enterprisewide Thinking Versus Focus of Specialist.
                  - Def: Some decisions (policies, plans, standards) are enterprisewide, affecting many different stakeholders.
                  - Warn: If these enterprisewide decisions assigned to any one of impacted domains, decisions will tend to be biased in favor of that one stakeholder; knowledge and interests of other affected groups may not be fairly represented.
                  - Ex: IT technology standards: Standards affect all IT applications and infrastructure domains, as well as operational services, customer support, in some cases even clients; if network standards decided by network engineers, may neglect interests of other engineers who must design systems compatible with network, and concerns of infrastructure services group accountable for running network.

                - Cpt: Conflict 4: Product Specialization Versus Unbiased Diagnosis of Clients' Needs.
                  - Def: Technical excellence requires deep understanding of single domain (subset of organization's products and services).
                  - Def: Specialization brings quality, but also brings bias; bias not unhealthy, but rather natural outcome of dedicating career to particular specialty.
                  - Def: On other hand, when diagnosing clients' needs, organization should be completely unbiased; must listen carefully to clients' business challenges, prescribe most relevant subset of entire product line.
                  - Warn: If staff expected to do both, conflict of interests arises; as product specialists, should be biased; but when talking to clients, expected to provide unbiased, business-driven advice and "sell" whatever most needed.
                  - Warn: Impossible for people to be both biased and unbiased; as old saying goes, "Give child hammer, and everything looks like nail!" Despite best efforts to be objective, staff see only needs for their favored solutions; higher-payoff opportunities may be missed.

                - Cpt: Conflict 5: Service Orientation Versus Audit.
                  - Def: Primary mission of most functions is serving others (peers inside organization, clients throughout enterprise, or external customers); customer focus is key success factor.
                  - Def: May also be need for "audit" function which judges others, may even have veto-power over others' decisions (e.g., auditors necessary to ensure compliance with financial laws, regulations, policies, ethics principles).
                  - Warn: Mixing audit functions with service functions creates conflict of interests; impossible to build relationship with customers while also judging them; just can't say, "I'm from Internal Revenue Service; I'm here to help!"
                  - Ex: IT example: Giving PC group power to decide whether users need new PC; clients wouldn't perceive them as service oriented, wouldn't openly discuss real needs.
            - ID: MEYER-SEC-0065
              Title: "5.5.3. Consequences of Conflicts of Interests"
              Text: |-
                Def: When structure tells individual to go in two (or more) opposing directions, adverse consequences both for organization and for individuals involved.

                - Warn: Gaps: Putting people in conflict-of-interests situations doesn't produce excellence at both missions; with finite brain cycles, people might be mediocre at both missions; more commonly, prefer one (based on predilections), and performance at other mission falls short; in George example, operations took precedence and infrastructure engineering (invention) became gap.
                - Warn: Unpredictable balance: Balance between conflicting missions not deliberate process, interplay among peers that analyzes trade-offs; people independently decide balance based on limited view of organization's needs, intuitions, personal preferences; as one manager leans one way and another in opposite direction, when decisions added up, statistics tells us tendency toward mean, regardless of needs of business at that time; meanwhile, organization's top executive has little control over balance; if organization needs to emphasize operational efficiencies to save money, or innovation to reap opportunities, top executive has no knob to turn; no explicit way to adjust balance on conflicting objectives.
                - Warn: Stress: More personal consequence is stress; when people expected to go in opposing directions, don't know what to do; typically fully aware of failure to succeed at both; highly stressful jobs lead to poor motivation, performance deficiencies, even health problems (like ulcers).
            - ID: MEYER-SEC-0066
              Title: "5.5.4. Implications for Structure"
              Text: |-
                - Def: Since organizations may face all these conflicts of interests, top executives inevitably must cope with these paradoxes and decide balance point on each.
                - Prohib: At lower levels, not healthy to combine functions with opposing objectives.
                - Req: Reserve conflicts of interests for highest possible level in organization chart, ideally for top executive alone.
                - Req: Healthy structure defines jobs that focus on only one side of each paradoxical dimension; gives staff clear, non-conflicting job objectives; allows executive to explicitly adjust balance by shifting resources between groups.
        - ID: MEYER-SEC-0067
          Title: "5.6. Principle 6: Cluster by Professional Synergies"
          Text: |-
            Def: Cluster groups under common boss based on similar professions.
            Ctx: As combine organization's many deliverables into domains, first consideration is avoiding conflicts of interests; second is professional synergies.
          Sections:
            - ID: MEYER-SEC-0068
              Title: "5.6.1. Case Study: Process-centric Groups"
              Text: |-
                - Ctx: With some critical internal processes in need of attention, CIO tried process-centric structure; dedicated groups to each major process within IT to minimize "hand-offs".
                - Ctx: Structure included: Ruth (applications development process), Bob (infrastructure engineering process), Matt (incident management process), Art (operational service delivery process).
                - Ctx: Optimizing processes is good thing; but this structure created "silo" groups for each process, each containing various specialists it needed; scattered "campus" of similar professionals.

                - Cpt: Problems.
                  - Warn: With each group attempting to cover many engineering disciplines, all became less specialized, hence less effective; costs rose, quality suffered, pace of innovation slowed.
                  - Warn: Structure was disempowering; Art forced to operate whatever infrastructure Bob developed; accountable for service delivery, even though had only indirect control of own assets.
                  - Warn: Smaller, less-visible processes not represented in structure (business opportunity analyses, standards planning); since counting on organization chart to make processes work, these other critical processes languished.
                  - Warn: Structure sent wrong signals; staff focused on executing existing processes, not on running businesses and pursuing innovations in their professions.
                  - Warn: Technology experts scattered among various groups didn't coordinate professional practices (methods and tools); didn't share components; did poorly at product integration; both professional and enterprise synergies lost.

                - Cpt: Conclusion.
                  - Def: Structuring by internal processes extremely costly way to optimize workflows.
                  - Rec: If concerned about effectiveness of internal processes, process-facilitation function can help.
                  - Def: As long as willing to invest in processes and teamwork, no need to put diverse professions under common boss just to get them to work together.
            - ID: MEYER-SEC-0069
              Title: "5.6.2. Clustering Similar Professions"
              Text: |-
                Fnd: If don't have to put people under common boss to get them to work together, then free to cluster staff by their professions.
                Def: Produces many kinds of synergies.

                - Cpt: Synergy 1: Professional Synergies.
                  - Def: Working together in same group encourages professional exchange (sharing experiences, discoveries, refinements of techniques, best practices).
                  - Res: Reduces redundant learning curves; everybody better informed; improves speed, quality, innovation; institutional knowledge better preserved by concentrating (rather than scattering) it.
                  - Res: Similar professionals can share work products; even if each project unique and solutions customized for each client, may be opportunities to reuse lower-level modules and designs; at minimum, staff can make use of others' experiences.
                  - Res: Sharing in any of these forms saves time and money; common components may improve quality and maintainability of organization's products.
                  - Warn: Conversely, scattering profession destroys "campus effect"; people don't get together often enough to learn from one another; relearn and reinvent; wastes time and slows delivery; dampens pace of learning and innovation; reduces depth of expertise; result is lower productivity and quality, at higher cost.

                - Cpt: Synergy 2: Management Synergies.
                  - Def: Manager focused on set of similar professions better understands how to manage those specialists; better leader and mentor; can create sub-culture appropriate to profession.
                  - Warn: Conversely, when small group in one profession placed under manager of completely different profession, boss may not understand function well enough to lead it; mentoring weak; sub-culture may be inappropriate.
                  - Warn: With given profession reporting to multiple managers, less management control; harder to develop common methods and enforce professional standards.

                - Cpt: Synergy 3: Workload Synergies.
                  - Def: Larger pool of staff can better manage workloads; when one person or group becomes too busy, common manager can temporarily assign people from other closely related disciplines; since professional skills similar, reasonable chance loaned staff will be productive.
                  - Warn: When scattered about, little group of professionals under one manager finds it difficult to manage peak loads; hard to borrow people from group reporting to completely different manager.

                - Cpt: Synergy 4: Negotiating Power.
                  - Def: When profession consolidated, its manager has more buying power and can negotiate better deals from suppliers; group may also be able to save money by sharing tools (e.g., software licenses) and vendor services.
                  - Warn: When profession divided into multiple groups, each procuring own tools and services, buying power diminished.

                - Cpt: Synergy 5: Career Paths.
                  - Def: Single, larger group of all those in given profession offers better career opportunities; supervisory positions within that larger group may provide promotional opportunities for those excellent in profession.
                  - Warn: By contrast, when profession scattered into small groups under other functions, staff find it difficult to advance; positions at next level up may not benefit from their professional expertise; when look for career path, no place to go other than to leave their field of study behind.

                - Cpt: Synergy 6: Domain Adjudication.
                  - Def: Common manager overseeing collection of similar domains resolves boundary issues, ensures accountabilities for emerging technologies and disciplines assigned to one group; reduces chances of domain overlaps and gaps.
                  - Warn: If profession scattered around organization chart, groups may only meet at level of top executive; busy leader doesn't have time to personally adjudicate domains, or ensure every new sub-specialty covered somewhere, without overlapping domains; result typically domain overlaps and gaps; Principle 3 described problems. Ref: ORG-STRUCT-PRINCIPLE3-OVERLAPS-01.

                - Cpt: Synergy 7: Simplicity.
                  - Def: Putting similar professions in one place makes it easier for others to understand structure and find source of needed products and services.
                  - Warn: When profession scattered, harder to know where to go; creates confusion for clients as well as others in organization.

                - Cpt: Synergy 8: Product Synergies.
                  - Def: When similar professionals collaborate more, organization's products likely to be better integrated; can produce enterprise synergies (e.g., when clients collaborate better by using common tools and services).
                  - Ex: When all IT engineers who work on customer applications in one group, more likely to create systems that allow all enterprise's business units and functions to share holistic view of customers.
                  - Warn: Alternatively, if pieces of profession report to many different managers, tendency for each group to go own way; for lack of collaboration, organization's products don't fit well together (product dis-integration); silo structures tend to produce monolithic products, not modular, interoperable product line; increases costs and sacrifices enterprise synergies.
            - ID: MEYER-SEC-0070
              Title: "5.6.3. Implications for Structure"
              Text: |-
                - Req: Cluster domains based on professional synergies (not who works with whom).
                - Req: Put all staff who share common profession together under common boss.
                - Fnd: If trust that will build processes of cross-boundary teamwork, no need to cluster functions based on who works with whom.
                - Req: Cluster similar specialties to maximize professional synergies.
        - ID: MEYER-SEC-0071
          Title: "5.7. Principle 7: Business Within a Business"
          Text: |-
            Def: Every manager is entrepreneur whose job is to satisfy customers (internal and external) with products and services.
            Ctx: Seventh (and last) Principle speaks to way you think about domains, and staff's authorities and accountabilities.
            Warn: Common mistake is to hold people accountable for implementing their specialties; may sound logical; but dangerous.
          Sections:
            - ID: MEYER-SEC-0072
              Title: "5.7.1. Case Study: Safety Group Accountable for Safety"
              Text: |-
                - Ctx: Local water district serving nearly 10 million households employed staff in three shifts to operate and repair facilities.
                - Ctx: Separately, Safety and Environmental Compliance group did inspections, supervised handling of hazards, oversaw Operations staff while they did work (monitored oxygen in man-holes while workers inside, inspected welders' equipment, oversaw excavations).
                - Ctx: Structure: Randy (operations and repairs), Barry (safety and environmental compliance).

                - Cpt: Problems.
                  - Warn: Safety was reduced: Work crews weren't trained in safety, since Safety group supposed to take care of that; but Safety staff couldn't oversee every detail; worse, sometimes work crews grew impatient waiting for Safety staff to show up, went ahead without them; mistakes made, number of safety incidents went up.
                  - Ctx: After paying large fine for environmental accident, Board hired respected consulting firm to benchmark water district against high-performing peers; study found they suffered incidents five to seven times average, incurred fines three to five times average.
                  - Warn: Costs increased: At that time, 80-person Safety group requesting additional 20 staff; however, same study found best practices were just 5 to 10 safety experts dedicated to establishing policies, training workers, collecting data.
                  - Res: Economics clear; Safety group held accountable for other people's behaviors was less effective and more expensive.

                - Cpt: Conclusion.
                  - Def: Safety is attribute of people's work, not product in itself; everybody must run safe businesses and produce safe products.
                  - Def: Safety group should have been in business of providing training and consulting to Operations, not "implementing safety".
                  - Fnd: Like in any function, success depends on understanding what business you're in.
            - ID: MEYER-SEC-0073
              Title: "5.7.2. Why Entrepreneurs Love Their Jobs"
              Text: |-
                Def: Each group should be defined as business within business.
                Ctx: Since 1980, advocate of managing groups within organizations as businesses within business; beliefs validated when met with highly successful entrepreneurs; each led profitable business, employing from dozens to thousands of people; clearly very smart and well-educated people who could have been top executives in global companies; instead, chose to build own small businesses; asked why; perhaps surprisingly, wasn't for money.

                - Cpt: What Entrepreneurs Said: Empowerment.
                  - "...owning my time, choosing which hours I work."
                  - "I work as I wish to, within my own sense of professionalism and ethics."
                  - "...control over decisions."
                  - "I'm not good rule-follower; I like making my own rules."
                  - "...the creativity -- there's no limitations on my ideas."

                - Cpt: What Entrepreneurs Said: Identity with Results.
                  - "...make things happen."
                  - "...the adventure of starting something and getting it done."
                  - "...building and creating value."
                  - "...the sense of accomplishment."
                  - "...knowing that I've added value."
                  - "...setting my own goals in life, and then reaching them."
                  - "I'm an artist of necessities; I love filling society's needs."
                  - "I want to be game-changer."

                - Cpt: Conclusion.
                  - Def: No reason can't create these same motivational forces (empowerment, identity with results) inside large organizations, at every level.
                  - Def: This is goal of business-within-a-business paradigm.
            - ID: MEYER-SEC-0074
              Title: "5.7.3. What It Means to Be a Business Within a Business"
              Text: |-
                - Prohib: Business-within-a-business paradigm doesn't mean operating internal service functions as profit centers; doesn't require chargebacks, where managers actually pay one another for internal services; certainly doesn't imply arm's-length relationship where support staff don't care about well-being of enterprise.
                - Def: Simply means every manager thinks and acts like entrepreneur running his/her own little business.
                - Def: Regardless of size of organization, every group should understand its purpose is to "sell" its products and services to customers (whether or not money changes hands).
                - Def: As entrepreneurs, staff should define their catalog of products and services, know whom their customers are; customers may be peers within organization, clients throughout enterprise, or external customers.
                - Def: Most every business has competition; when speaking about company in competitive market, obvious; but same true of organizations inside enterprises; internal service providers compete with both outsourcing and decentralization.
                - Def: Even if seems to internal service providers as if clients must work through them, surest way to lose monopoly is to behave as monopolist; everyone should strive to earn customers' business through performance, as supplier-of-choice in market that has right to go elsewhere (even if really can't).
                - Ctx: Other terms for business-within-a-business paradigm: shared services, "intrapreneurship"; all imply same thing: empowered, entrepreneurial organizations.
            - ID: MEYER-SEC-0075
              Title: "5.7.4. Benefits of Business-Within-a-Business Paradigm"
              Text: |-
                Def: Business-within-a-business paradigm brings out best in people.

                - Res: Customer focus: "I understand those are my customers, not unruly children or helpless victims of my decisions; in many cases, they have right to choose what they buy from me."
                - Res: Results orientation: "It's my product line; I know I'm accountable for delivering everything I promise."
                - Res: Quality: "I'm proud of my work; it's my job to make it best."
                - Res: Efficiency and cost control: "I have to be best deal in town."
                - Res: Teamwork: "To stay competitive, I have to focus on my own domain; I get help from peers when I need other specialties."
                - Res: Judicious risk-taking: "I have no choice but to take some risks to keep up with my competition; but I do so thoughtfully."
                - Res: Use of vendors: "I manage business, not just resources I've been given; if buying something more cost-effective than building it internally, or if I need more capacity, I'll be first to offer 'buy' option alongside 'make' approach."
                - Res: Innovation: "I've got to stay ahead of (or at least keep up with) my competition; so I'd better innovate."
                - Def: These all traits of successful entrepreneurs.

                - Cpt: What You Won't Hear.
                  - Warn: "My job is to get budget at beginning of year, make sure it's used up by year end."
                  - Warn: "We're in public service; we're not business; so I don't have to listen to any customers."
                  - Warn: "My customer is enterprise as whole; I know what's best for you."
            - ID: MEYER-SEC-0076
              Title: '5.7.5. Why Not "Partners"'
              Text: |-
                - Cpt: Opposition to Business-Within-a-Business.
                  - Def: Some oppose business-within-a-business paradigm because believe best way to encourage collaboration is to declare groups "partners" in shared goal.
                  - Ex: IT and clients they serve are "partners" in pursuing technology-enabled business strategies; as such, share authorities and accountabilities.
                  - Warn: May sound nice on surface; but what does it really mean?
                  - Def: Some interpretations of partnership induce behaviors that undermine relationships, not strengthen them.

                - Cpt: Dangerous Definition 1: We Share Everything.
                  - Def: Partnership means IT staff and clients are one team, decide everything jointly.
                  - Def: "All for one, one for all" notion of partnership sounds like should induce great collaboration.
                  - Warn: In practice, respective authorities and accountabilities unclear; each party has right to meddle in other's domain of expertise.
                  - Warn: IT staff feel have right to tell clients how to run businesses, may even claim authority to force changes on clients to make best use of technologies.
                  - Warn: Clients feel have right to tell IT staff how to manage technology projects.
                  - Res: Instead of each contributing unique competencies, decisions influenced by people who aren't fully qualified to make them.
                  - Warn: Shared accountability equivalent to no accountability; without clearly defined individual accountabilities, team members struggle for control and projects mire; when things go wrong, everybody takes cover under banner of "partnership".

                - Cpt: Dangerous Definition 2: We're the Experts.
                  - Def: "We are partners, and hence equals; and since we're IT experts in this partnership, we'll decide what technologies you get."
                  - Warn: This is opposite of customer focus; "we know what's best for you" attitude can only serve to erode relationships.
                  - Warn: This definition of partnership fundamentally disempowering and unproductive; would be unfair to hold clients accountable for business results if can't control means of production, including IT; that's Golden Rule. Ref: ORG-STRUCT-PRINCIPLE1-01.
                  - Res: Using concept of partnership to justify disempowering clients leads to resentment, disputes over authority, strained relationships; can also induce delays or inaction as two parties struggle to come to agreement.
            - ID: MEYER-SEC-0077
              Title: "5.7.6. Better Form of Partnership: Customer-Supplier Relationships"
              Text: |-
                - Def: Better answer found in business-within-a-business paradigm; effective partnerships built on customer-supplier relationships.

                - Cpt: Customer-Supplier Model.
                  - Def: Suppliers (like IT) respect customers' rights to make purchase decisions; present options and share what they know, then let customers decide what they'll buy.
                  - Def: Customers decide what they'll buy, then let suppliers figure out how to produce it; suppliers choose own methods and tools, manage their staff (including contractors) and vendors; empowered and proactive, without disempowering customers in any way.

                - Cpt: Matching Authorities and Accountabilities.
                  - Def: With authority comes accountability.
                  - Def: Customers have authority to decide what they'll buy, hence accountable for justifying utilization of internal services, paying all life-cycle costs, realizing benefits.
                  - Def: Suppliers have authority to decide how they'll produce those results; accountable for reliable delivery of products and services at competitive costs.

                - Cpt: Benefits.
                  - Def: Customer-supplier relationships clean and mutually respectful; match authorities and accountabilities.
                  - Def: They're synergistic; synergies only result from taking advantage of people's different strengths, assigning distinct authorities and accountabilities, without any loss of commitment to one another's success; mutually respectful customer-supplier relationships do exactly that.
            - ID: MEYER-SEC-0078
              Title: "5.7.7. Proactive Entrepreneurship"
              Text: |-
                Def: Entrepreneurs strive to please customers; but does not mean they're passive order-takers; proactive in many ways.

                - Act: Internal entrepreneurs market value of their products and services; not meant to be self-serving; to lift customers' awareness of possibilities so as to engender more creative uses of offerings.
                - Act: Entrepreneurial organizations proactively schedule time to talk to customers about business challenges; "sales" in best sense of profession (not pushing products, but helping customers solve problems and achieve goals); result is opportunities closely aligned with customers' objectives.
                - Act: In response to customers' requirements, suppliers proactively offer alternative solutions (as in Chevrolet, BMW, Rolls-Royce); make customers aware of better ways to address needs without going so far as to choose for them.
                - Act: Internal entrepreneurs help customers analyze alternatives in context of customers' values (not their own); not matter of making recommendation (form of "we know what's best for you" that takes on some accountability for customers' success); rather, consultative process: "If speed most important to you, pick alternative A; but if costs more important, select B."
                - Ctx: If suppliers done good job of sharing all they know, likely customers will come to same conclusions as they did; but if customers select alternative other than one supplier would recommend, perhaps know something about business suppliers don't know; or perhaps applying own values to trade-offs; in any case, entrepreneurs respect customers' purchase decisions.
                - Act: Entrepreneurial organizations can be proactive about facilitating enterprisewide decisions (policies and standards); decisions made by community of relevant stakeholders, not unilaterally by any one expert; but suppliers can put forward issues and coordinate stakeholders' decisions on behalf of enterprise.
                - Act: Internal entrepreneurs proactively invest in own businesses (process improvements, technology innovation, new products) to remain competitive; decide own business strategies, research and professional-development priorities.
                - Act: Entrepreneurs proactively maintain and evolve infrastructure ("Infrastructure" means assets owned by organization for purpose of producing services); internal entrepreneurs don't ask customers' permission before buy new manufacturing capacity; empowered to acquire whatever need to satisfy customers' demands for services; decisions based on market needs in total (enterprise capacity plans), not demand from any single customer.
                - Act: Entrepreneurs don't wait for customers to tell them to offer new products and services; proactively evolve product lines (without forcing solutions on customers); put new products "on shelf" (making available to customers), but only take them "off shelf" (actually deploying) when customers agreed to buy them.
                - Act: Entrepreneurs proactively reduce costs and improve quality to remain competitive.

                - Cpt: Summary.
                  - Def: In business-within-a-business paradigm, everybody is "product manager"; some sell to external customers, generate profits for enterprise; others sell products and services internally, probably at breakeven; but all are entrepreneurs accountable for managing businesses.
                  - Def: As proactive as they are, there's line they don't cross; entrepreneurs respect that customers know businesses best, are accountable for business results; therefore, by Golden Rule, customers must have authority to decide what they "buy" from internal service providers. Ref: ORG-STRUCT-PRINCIPLE1-01.
            - ID: MEYER-SEC-0079
              Title: "5.7.8. Implications for Structure"
              Text: |-
                - Def: Business-within-a-business paradigm sends all right signals and rewards right behaviors; harnesses everybody's creativity; aligns work of customers and suppliers; builds highly effective partnerships.
                - Def: Organizational structure is key to achieving such entrepreneurial organization.
                - Req: Define groups as lines of business, bounded by products and services they produce (by what each "sells," not what it does); not suggesting money changes hands.
                - Def: Designing healthy structure is matter of dividing organization's various internal and external products and services among its groups, laying out mosaic of entrepreneurships.
                - Res: This capstone Principle creates empowered jobs, where staff customer focused, accountable for results, creative and entrepreneurial, highly motivated.
    - ID: MEYER-SEC-0080
      Title: "6. Building Blocks of Organization Charts"
      Text: |-
        Src: Socrates: "The beginning of wisdom is the definition of terms."
        Def: Engineering science comprises both principles and components; Part 2 described seven Principles of structure; this Part describes components.
        Def: Useful to think of these components as "Building Blocks" that can assemble into organization chart.
        Fnd: Way Building Blocks defined is crucial; Principles guide us in how to do that (as well as in how to assemble them).
        Def: Most salient to definition of Building Blocks is Principle 7 (business-within-a-business paradigm); tells us Building Blocks should be lines of business that exist within organizations; when assemble Building Blocks into organization chart, assured every job is empowered entrepreneurship.
        Def: This Part defines all lines of business that exist within organizations.
      Sections:
        - ID: MEYER-SEC-0081
          Title: "6.1. Overview of Building Blocks"
          Text: |-
            - Def: Building Blocks are lines of business that exist within organizations.
            - Ctx: Appear in every industry (corporations, not-for-profit organizations, higher education, governments, even clubs).
            - Ctx: Same lines of business exist within departments inside enterprises; like whole companies, most internal service providers (IT, HR, Finance, Facilities) include operations functions that produce ongoing services (like manufacturing), gurus in disciplines (like engineering), customer service, even internal sales and marketing (relationship managers that link internal service provider to rest of enterprise).
            - Ctx: Some departments may not include all Building Blocks; nonetheless, their work can be defined in this same language.
            - Def: Building Blocks help avoid gaps (Principle 3); essentially checklist of all possible lines of business in any organization, so can be sure have all pieces needed somewhere in new organization chart. Ref: ORG-STRUCT-PRINCIPLE3-GAPS-01.
            - Def: All Building Blocks important; some may be larger than others; some may be more strategic to future growth; some may serve clients, while others serve customers within organization itself (internal support services).
            - Fnd: All are businesses, all should be creative, customer focused, entrepreneurial; all essential, should be treated with respect; any biases or discrimination can only serve to diminish effectiveness of victimized group, ultimately performance of entire organization; in healthy organization, there are no second-class citizens.
            - Def: At high level, five Building Blocks (five types of businesses); each has sub-categories.

            - Warn: Caution 1: This framework of Building Blocks not prescribed organization chart; no such thing as off-shelf organization chart right for everybody; rather, Building Blocks simply language you can use to describe organization charts.
            - Warn: Too often, leaders get together to plan new organization chart; but each leaves meeting with somewhat different understanding of words like "engineering" and "operations"; Building Blocks provide clear, precise, common language for analyzing, discussing, designing organization charts.
            - Res: Executives can use this common language to diagnose current structure; understand one another's proposals; make structural decisions in factual, analytic manner; establish common understanding of missions and boundaries.

            - Warn: Caution 2: Some names of these Building Blocks may sound familiar; may have "Engineering" department today; but may, in fact, be combination of multiple Building Blocks; pieces of "Engineers" Building Block may be found in other departments.
            - Warn: Don't confuse name of Building Block with name of group in current organization.
        - ID: MEYER-SEC-0082
          Title: "6.2. Distinguishing Engineers and Service Providers"
          Text: |-
            - Def: By "line of business," don't mean industry; who's in business of airplanes? Boeing, all airlines, companies that clean planes, companies that cater food, local government organizations that run airports, federal government that controls air traffic and sets rules, and more.
            - Def: Can't just say "airplanes" and know what business people in; similarly, within enterprise, can't just say "operations" or "infrastructure" and know what business staff in; framework of Building Blocks has to be more refined.
            - Def: Consider difference between Boeing (sells airplanes) and airline (sells transportation service); or Ford and Hertz; or building contractor and hotel.
            - Def: Pick any industry, see two very different kinds of businesses: Engineers design and produce products (assets), support those assets with design expertise; Service Providers buy those assets, own and operate them, use them to deliver service.
            - Ex: For most any type of asset, see both; with regard to airplanes, Boeing is Engineer, airline is Service Provider; for cars, Ford is Engineer, Hertz is Service Provider.
            - Def: Same split occurs in internal service providers; in IT, Engineers implement computers, storage devices, networks, applications; Service Providers own and operate those assets to deliver services (computer time, data storage, connectivity, applications hosting, software as service like email).
            - Fnd: Engineers and Service Providers very different businesses (differing in competencies, business models, cultures, products and services); thus, separate Building Blocks.
        - ID: MEYER-SEC-0083
          Title: "6.3. Building Block: Engineers"
          Text: |-
            Def: Engineers create organization's products; discipline or technology specialists, designers, gurus in those products.
          Sections:
            - ID: MEYER-SEC-0084
              Title: "6.3.1. Engineers Definition and Services"
              Text: |-
                - Def: Engineers maintain locus of expertise in specific engineering discipline, technology, or professional specialty; use expertise to design, build, install "solutions," perhaps utilizing vendors' products then adding value; solution may be physical asset, software, or design of intellectual property.
                - Def: Also enhance, tune, repair, configure, support those solutions; definition does not distinguish those who design and build products from those who repair them; essentially same bottom-of-T required to do both.
                - Def: Engineers sell anything requiring in-depth expertise in design of organization's products (knowledge of what's inside that "black box").

                - Cpt: Services of Engineers (all based on in-depth product-design expertise).
                  - Solutions (entirely new, or enhancements)
                  - Repairs
                  - Configuration tuning
                  - Domain specific incident management (a.k.a., second-level support, as point of escalation for customer-service)
                  - Documentation and training materials, and training
                  - Expert time, studies, presentations, sales support

                - Cpt: Examples Across Industries.
                  - IT: applications developers, infrastructure systems engineers
                  - HR: compensation and benefits design, performance-management systems design
                  - Finance: tax law, investment financial analysis
                  - Product manufacturers: product designers, manufacturing engineers
                  - Health care: outcomes management, doctors
                  - Education: schools and professors, curriculum and instructional design
                  - Government: policy and program design, decisions on grants

                - Def: Engineers don't own solutions they produce (other than work in progress); sell solutions to others, be they peers within organization (such as Service Providers) or external clients.
            - ID: MEYER-SEC-0085
              Title: "6.3.2. Applications versus Base Engineers"
              Text: |-
                - Def: In many functions and industries, multiple layers of Engineers; some design fully assembled products; others experts in components that go into various products.
                - Ex: Automobile engineering: those who design cars, those who design trucks; both "applications" draw on "base" components like engines, transmissions, electrical systems.
                - Ctx: In some fields, many layers of engineers; in IT, computer engineers, databases and middleware, applications; each layer draws on lower layers, supports next layer up.
                - Def: Those who assemble components into complete products (top layer) called "Applications Engineers"; produce purpose-specific products tailored to various kinds of customers' needs.
                - Def: All lower layers termed "Base Engineers"; design components that go into various applications; components purpose-independent in that serve multiple applications.
                - Ex: Engineers who build cars and those who build trucks are Applications Engineers (specialize in different purposes); Base Engineers contribute parts and advice to both.
                - Ex: At Boeing, Applications Engineers design different kinds of airplanes; employ Base Engineers who design engines, control systems, interiors, etc.
                - Ex: Higher education: various schools are Applications Engineers; curriculum and instructional design experts are Base Engineers.
                - Ex: IT: term "application" refers to data-object-specific software (systems designed to handle information about particular topic); Base Engineers sell and support data-object-independent technologies (computing platforms, database engines, middleware, telecommunications networks/infrastructure, end-user-computing and data-analysis tools, software-engineering tools and methods, models such as artificial intelligence).
            - ID: MEYER-SEC-0086
              Title: "6.3.3. Engineers Competencies"
              Text: |-
                - Def: Bottom-of-T: Specific domain of technology, field of science, professional discipline, or branch of engineering.
                - Def: Significant top-of-T competency: Engineering methods and tools (e.g., for design and testing) as well as project management.
                - Warn: If expected to produce anything other than solutions, depth in professional domain bound to suffer; if not given clear requirements for things to design, may have to learn about customers' businesses to help customers define requirements (product of different Building Block); any time spend studying customers' businesses is time away from real specialty.

                - Mdl: Competencies Profile.
                  - Bottom of T: Domain of technology, science, or discipline
                  - Key methods: Design and testing, project management
                  - Technical skill: High
                  - Project management: High
                  - Service management (operations): Low
                  - Business of organization's customers: Low
                  - Interpersonal skills: Low
                  - People supervision: Medium
            - ID: MEYER-SEC-0087
              Title: "6.3.4. Engineers Biases"
              Text: |-
                Ctx: To avoid conflicts of interests (as per Principle 5), important to know biases of each Building Block. Ref: ORG-STRUCT-PRINCIPLE5-01.

                - Def: Engineers love innovation, but quickly become bored (may get sloppy) when asked to do routine "keep it running" work.
                - Def: Laser focused on domain of expertise, love to study nuances and leading-edge discoveries; count on other equally focused Engineers when other skills needed.
                - Def: Engineers willing to produce anything customers need (from enterprisewide to highly customized solutions); but not experts in customers' businesses; cannot assess customers' needs in unbiased, business-driven manner, since paid to live and breathe own domain of solutions.

                - Mdl: Biases Profile (Five Fundamental Conflicts).
                  - Invention versus operational stability: Invention
                  - Purpose-specific solutions versus components: Applications (purpose-specific), Base (components)
                  - Enterprisewide thinking versus focus of specialist: Specialist
                  - Technical specialization versus unbiased diagnosis of clients' needs: Technical specialization
                  - Service oriented versus audit: Service oriented
        - ID: MEYER-SEC-0088
          Title: "6.4. Building Block: Service Providers"
          Text: |-
            Def: Service Providers deliver ongoing services; may buy products from Engineers, then use those assets to deliver service (like airline that buys airplanes and sells transportation service); or service may be delivered primarily by people.
          Sections:
            - ID: MEYER-SEC-0089
              Title: "6.4.1. Service Providers Definition"
              Text: |-
                - Def: Distinguishing attribute of Service Providers is ongoing nature of services; doesn't include stream of small, unique projects (like repairs Engineers sell); rather, essentially same routine service, day after day; think of services as water flowing from spigot.
                - Def: Service Providers keep things running reliably, safely, efficiently.
                - Ctx: Building Block includes manufacturing, customer service, range of support services.
            - ID: MEYER-SEC-0090
              Title: "6.4.2. Asset-based Service Providers"
              Text: |-
                - Def: Some services based on ownership of assets, where customers essentially buying use of those assets; termed "Asset-based Service Providers".
                - Def: Business model: look for cases where customers can share use of asset; acquire those assets, termed "infrastructure," from organization's Engineers (or directly from vendors), use them to produce services.
                - Ex: IT: may all own own PCs; but not possible for each to run own networks and data centers; Asset-based Service Providers see as business opportunity; acquire networks and shared-use computers, sell use of them to others.
                - Ctx: Assets include information as well as tangible properties.

                - Cpt: Examples Across Industries.
                  - IT: computer time, data storage, connectivity
                  - HR: benefits administration, employee data administration
                  - Finance: accounting services, treasury
                  - Product manufacturers: factories, warehouses, logistics
                  - Health care: hospital rooms, clinics, labs
                  - Education: classrooms, residence halls, library
                  - Government: roads, parks, ports and airports, air traffic control (air space), welfare, data services

                - Def: Asset-based Service Providers not technology specialists; rely on Engineers to build, document, upgrade, repair assets; know how to operate infrastructure; but real expertise is in providing services, and all that entails.
            - ID: MEYER-SEC-0091
              Title: "6.4.3. People-based Service Providers"
              Text: |-
                - Def: People-based Service Providers sell services produced by people rather than assets; equipment (such as computers) employed only to make people more productive at tasks conceivably could do manually; but use of asset not really what customers buying; buying "use" of people.

                - Cpt: Examples Across Industries.
                  - IT: service desk, field technicians, writers and trainers
                  - HR: counseling, recruiting, onboarding, job grading
                  - Finance: procurement, customer service
                  - Product manufacturers: customer service, field technicians
                  - Health care: admissions, nursing, non-medical services
                  - Education: registrar, admissions processing, student counseling, business services
                  - Government: social services, elections, weather forecasts

                - Cpt: Three Types of People-based Service Providers.
                  - Type 1: Product support: Services help customers get value from rest of organization's products and services; common example is customer service (help desk); another example is training in use of organization's products.
                  - Type 2: Internal support: Services leverage time and enhance abilities of others within organization; example is project management office (PMO) which helps others manage projects, offering services (project plans/PERT charts/work-breakdown structures, project tracking and reporting); they don't manage projects; other examples are field technicians who follow instructions of other Building Blocks, technical writers who help others communicate knowledge.
                  - Type 3: Business services: Services outside primary intent of organization; from CEO's perspective, Administration, IT, Finance, HR departments contain all Building Blocks but classed as People-Based Service Providers; similarly, when internal services decentralized (finance or administration function within IT department), classed as People-based Service Providers.
            - ID: MEYER-SEC-0092
              Title: "6.4.4. Service Providers Competencies"
              Text: |-
                - Def: Specialized expertise of both types of Service Providers is service management; includes assessing market and determining which services to offer; defining those services; acquiring and managing any needed assets, methods, vendor services; contracting with customers (service-level agreements); managing capacity; managing ongoing delivery of those services.

                - Mdl: Competencies Profile.
                  - Bottom of T: Specific services and how they're produced
                  - Key methods: Service delivery and management
                  - Technical skill: Medium
                  - Project management: Low
                  - Service management (operations): High
                  - Business of organization's customers: Low
                  - Interpersonal skills: Asset-based (Low), People-based (High)
                  - People supervision: Asset-based (Medium), People-based (High)
            - ID: MEYER-SEC-0093
              Title: "6.4.5. Service Providers Biases"
              Text: |-
                - Def: Service Providers responsible for stability, responsiveness, reliability, security, low cost; readily solve problems in service delivery, continually improve existing services, offer new services when time right.
                - Warn: Major innovations (inventions) inevitably disrupt smooth operations; Service Providers intentional damper on innovation, proceeding only when potential market demand justifies investment and technologies evolved to point of being ready to produce reliable, safe services; biased to favor stability over innovation; change only when safe.

                - Mdl: Biases Profile (Five Fundamental Conflicts).
                  - Invention versus operational stability: Operational stability
                  - Purpose-specific solutions versus components: Agnostic
                  - Enterprisewide thinking versus focus of specialist: Specialist
                  - Technical specialization versus unbiased diagnosis of clients' needs: Unbiased
                  - Service oriented versus audit: Service oriented
        - ID: MEYER-SEC-0094
          Title: "6.5. Building Block: Coordinators"
          Text: |-
            Def: Some things require consensus among stakeholders (people throughout organization, in some cases clients as well); Coordinators drive those shared decisions.
          Sections:
            - ID: MEYER-SEC-0095
              Title: "6.5.1. Coordinators Definition"
              Text: |-
                - Ex: Planning: Every internal entrepreneur responsible for planning own business within business (that's empowerment); but all plans must be coordinated to add up to organization's plan; furthermore, planning specialty in own right (methods and analytical skills require study); thus, role for "Planning Coordinator" whose job not to decide plan, but rather help everybody develop own plans in coordinated manner.
                - Def: Coordinators help stakeholders (within organization and beyond) come to agreement on shared decisions (policies, plans, standards).
                - Act: Establish processes for decision making; enable processes with methods and project plans; ensure right stakeholders involved; provide common information (assumptions and trends, templates and formats, conceptual frameworks, timeframes); help individuals with respective duties in process; facilitate collaboration on interdependencies, such that each group's plan fits into higher-order enterprisewide or organizationwide plan.
                - Warn: You're not Coordinator if, like all other stakeholders, you participate in these decisions; only Coordinator if job is to facilitate decision process.
                - Act: Coordinators also help people utilize resulting shared decisions; compile results and make them available; help others find, interpret, apply relevant policies, standards, plans.
                - Prohib: Coordinators not accountable for content; participating stakeholders are; Coordinators just accountable for effective consensus-based decision-making processes.
                - Warn: If stakeholders can't reach consensus, little Coordinator can do; would be mistake to give Coordinators authority to force decision; since not accountable for others' results, doing so would violate Golden Rule. Ref: ORG-STRUCT-PRINCIPLE1-01.
                - Ctx: Perhaps premature to expect consensus; but if important to make decision now, Coordinators can help executives motivate stakeholders to want to agree.
            - ID: MEYER-SEC-0096
              Title: "6.5.2. Types of Coordinators: Business-Oriented"
              Text: |-
                Def: Numerous topics require coordination; each distinct line of business; some business oriented, others more technical and product specific; most common to all functions; few function-specific.

                - Cpt: Strategy Planning Coordinator.
                  - Def: Strategic plan answers questions: "What businesses do we want to be in? How will we get from here to there?" Answers based on continually changing environment, organization's strengths, weaknesses, opportunities, threats.
                  - Ctx: Entrepreneurs at every level accountable for strategies of own groups; but individual strategies must fit together to achieve strategies at next level up; strategy planning science in own right; leaders need help with process as well as coordination.
                  - Def: Expert in strategic planning methods, in business environment (including competitors) and how environment creates threats and opportunities; doesn't decide strategies, but helps everybody decide own respective strategies, in coordinated fashion.

                - Cpt: Operational Planning Coordinator.
                  - Def: Operating plan looks one or two years ahead, answers questions: "What do we plan to deliver in coming year? How will we fulfill that demand (including needed resources, such as budgets)?"
                  - Def: Expert in business and budget planning methods (especially investment-based budgeting), in tools used to create operating plan and budget based on forecasted demand.

                - Cpt: Research Coordinator.
                  - Def: Within organizations, research means investigating new products, services, technologies, or disciplines; in manufacturing company, may develop new products or manufacturing techniques; in IT, example is investigation of new vendor products and services.
                  - Prohib: Research Coordinator doesn't do any research; helps others do research, by sharing expertise in research methods and in how to develop research proposals; helps executive decide which research projects to fund, as portfolio of investments aligned with organization's strategies.
                  - Ex: Akin to US National Science Foundation which distributes research grants to universities and corporations (who do actual research), but doesn't do any research itself.

                - Cpt: Organizational Effectiveness Coordinator.
                  - Def: Focus on how organization does business (not what business produces); scope includes: culture, structure, resource-governance processes ("internal economy"), shared methods and tools, metrics and rewards.
                  - Def: Distinct from Human Resources in that engineers "organizational ecosystem," whereas HR focuses on employment relationship.
                  - Def: Expert in principles of design of those organizational systems, in methods of change (not just generic change management, but methods specific to engineering organizational system).
                  - Act: Leads transformation projects (including restructuring), then helps everybody work within organizational design; may also coordinate employee communications.

                - Cpt: Audit Response Coordinator.
                  - Prohib: Coordinators do not audit or judge people they're meant to serve; but external parties may audit organization; when happens, organization must provide point of contact, coordinated response.
                  - Def: Helps everybody respond to auditors and provides point of contact, but content of audit response is responsibility of appropriate groups throughout organization.
                  - Ctx: Response includes initial provision of information, as well as coordinated projects to remediate any problems revealed by audits.
                  - Act: With knowledge of questions auditors ask, can offer "assessments" to help others prepare for audit; assessments voluntary service, not audit; results provided strictly to those being inspected.

                - Cpt: Regulatory Compliance Coordinator.
                  - Def: Everybody accountable for complying with laws and regulations; helps them do so by providing expertise in laws and regulations, in how they apply to organization.
                  - Act: Provides point of contact for regulators, coordinates any compliance examinations and remediation projects.
                  - Act: Like Audit Response Coordinator, may offer internal assessments to help others comply.

                - Cpt: Business Continuity Coordinator.
                  - Def: In case of disaster, organization must ensure staff safe, stabilize situation, bring business back to normal operations (disaster recovery); beyond that, business-continuity planning can mitigate damage done by disasters.
                  - Act: Helps everybody develop own plans, coordinates interdependencies to optimize resilience of organization; coordinates tests of plan, and (if triggered by actual incident) execution of plan.

                - Cpt: Security Coordinator.
                  - Def: Security means minimizing risks of harm from espionage, theft, sabotage.
                  - Def: In empowered organization, everybody responsible for own security, for providing safe, secure products and services to customers; Security Coordinator helps them do so.
                  - Def: Expert in threats; helps everybody come to consensus on security policies; keeps people informed of threats and defense strategies; leads investigations of and responses to security incidents; coordinates recovery and mitigation projects done by appropriate managers.
                  - Prohib: Not audit function; doesn't check up on everybody's compliance with policies; not Service Provider offering ongoing services like guards, building access control, or IT firewalls and identity management; works at higher, organizationwide level, as service to others accountable for own safety.
                  - Ctx: In IT, titled Chief Information Security Officer (CISO).
            - ID: MEYER-SEC-0097
              Title: "6.5.3. Types of Coordinators: Technical"
              Text: |-
                - Cpt: Standards Coordinator.
                  - Def: Organizations set product design standards to ensure interoperability and supportability of products.
                  - Ex: In home, shape of electrical outlet example of standard; in manufacturing industries, simple example is constraints on variety of nuts and bolts used in products; in IT, standards are protocols, APIs, interfaces.
                  - Def: Standards are conscious constraints on design (not preferred brands and models); permit evolutionary change without loss of integration and interoperability.
                  - Ctx: Many stakeholders affected by standards (Engineers, Asset-based Service Providers, some People-based Service Providers, in some instances clients); all perspectives should be considered before standard decided; not only is knowledge valuable; involvement in decision encourages compliance.
                  - Prohib: Standards Coordinator does not decide standards; creates framework; then, on ongoing basis, pulls together appropriate stakeholders to decide each "cell" within framework (specific standards), helps them come to consensus.
                  - Act: Helps Engineers access and interpret agreed standards in course of designing solutions.

                - Cpt: Design Patterns Coordinator.
                  - Def: To optimize best interests of customers who buy multiple things from organization, various products and services should be designed to fit well together; involves agreements among various Engineers and Service Providers about "design patterns".
                  - Def: Expert in "ripples" (how decisions about, or changes in, one domain affect others); facilitates consensus on design guidelines that affect all domains, helps individuals apply guidelines to decisions and understand ripples.
                  - Ex: In community, city planning and zoning example, dictating which types of buildings belong in each area of city.
                  - Ex: Distribution company: pricing, sales incentives, marketing promotions for one product line may affect company's ability to sell other product lines; impacts cross channels, product categories, services (distribution, sales, marketing); coordination of policies, of requests for variances, needed to reduce risk of optimizing one product while sabotaging sales of others.
                  - Ex: Higher education: drives enterprise programs to enhance student success, helps multiple groups package offerings for different audiences (e.g., for non-traditional students).
                  - Ex: IT: design patterns suggest where various functions fit in broader enterprise architecture (e.g., what software goes on personal devices/PCs/mobile devices versus on shared servers); maintains map of how existing systems interconnected and how data flows through them, to help Engineers anticipate how changes in one system will affect other systems.
                  - Ctx: In IT, combination of Standards and Design Patterns Coordinators called "enterprise architect".
            - ID: MEYER-SEC-0098
              Title: "6.5.4. Types of Coordinators: Function-Specific"
              Text: |-
                - Cpt: Information Policy Coordinator (IT).
                  - Def: In IT, need for coordination of policies with regard to how information handled; one example is retention policies (particularly complex given electronic records interdependent, so information that has to be retained may depend on availability of other data that should be destroyed).
                  - Ctx: Other examples: how system-of-record determined; how data owners chosen, their accountabilities and authorities; what information to be shared (i.e., access-rights); how privacy maintained; what may and may not be said using enterprise resources (web sites, blogs, electronic mail).

                - Cpt: Employment Policy Coordinator (HR).
                  - Def: Employees hired with expectation they'll evolve in careers through multiple jobs within enterprise; staff considered employees of enterprise, not just group that initially hired them; thus, some decisions about employment relationship should be made by consensus, not by each department alone (or by HR).
                  - Ex: Compensation must be coordinated to avoid inequities, so two people doing similar jobs in different places in enterprise paid roughly same; enterprise may collectively decide to pay above market to attract top talent, or below market to improve near-term margins; business decision, not strictly HR decision.
                  - Def: Role: bring enterprise stakeholders to consensus on such policies.
            - ID: MEYER-SEC-0099
              Title: "6.5.5. Coordinators Competencies"
              Text: |-
                - Def: All Coordinators similar in that facilitate and coordinate shared decisions; experts in identifying stakeholders and in bringing teams to consensus.
                - Def: In addition, each expert in structure of content they are coordinating; know enough about content to understand trade-offs in decisions; but cannot be expert in everybody's domains to point of deciding content, must not disempower others (even if do know lot about subject).
                - Ex: Planning Coordinator knows what goes into good plan; but actual content of plan comes from participating managers.

                - Mdl: Competencies Profile.
                  - Bottom of T: Topic being coordinated
                  - Key methods: Consensus building, information structuring
                  - Technical skill: Low (business) to Medium (technical)
                  - Project management: Medium
                  - Service management (operations): Low
                  - Business of organization's customers: Low
                  - Interpersonal skills: High
                  - People supervision: Low
            - ID: MEYER-SEC-0100
              Title: "6.5.6. Coordinators Biases"
              Text: |-
                Def: Critical that Coordinators are unbiased facilitators of shared decisions; but do have biases.

                - Mdl: Biases Profile (Five Fundamental Conflicts).
                  - Invention versus operational stability: Invention
                  - Purpose-specific solutions versus components: Agnostic
                  - Enterprisewide thinking versus focus of specialist: Enterprisewide (or organizationwide) decisions
                  - Technical specialization versus unbiased diagnosis of clients' needs: Unbiased
                  - Service oriented versus audit: Service oriented
        - ID: MEYER-SEC-0101
          Title: "6.6. Building Block: Sales and Marketing"
          Text: |-
            Def: Fourth of five Building Blocks; Sales and Marketing is client-facing part of organization; adds value in two ways: enhances organization's relationships with clients (not single point of contact, but default point of contact; facilitates effective communications between clients and everybody in organization); helps clients address challenges (problems and opportunities) using organization's products and services.
          Sections:
            - ID: MEYER-SEC-0102
              Title: "6.6.1. Sales and Marketing Definition"
              Text: |-
                - Def: Sales staff help clients acquire just right products and services from organization's entire catalog; align organization with clients' strategies and business needs; help clients discover high-payoff opportunities for organization's products and services.
                - Warn: Word "sell" has two meanings: to provide product, or to help customers buy others' products; this Building Block does latter; brokers sales; not accountable for delivery of other groups' products and services.
            - ID: MEYER-SEC-0103
              Title: "6.6.2. Internal Service Providers Need Sales"
              Text: |-
                - Def: In companies, need for Sales and Marketing obvious; but Building Block equally essential to internal service providers; have tough competition from decentralization and outsourcing; despite monopolies in few areas, must earn "market share" by developing great relationships with clients.
                - Def: Internal service provider must find ways to contribute value to clients' critical challenges and strategic opportunities; Sales provides linkage to clients and expertise to do that.
                - Def: In companies, goal of Sales is maximize revenues; but for internal service providers, goal not to convince clients to spend more (expense to enterprise); rather, maximize organization's contributions to clients' success (i.e., generate right business that delivers most value).
                - Ctx: Internal service providers may not want to call this function "sales"; term may offend some clients (because don't understand value); wouldn't want to imply out to get as much money as possible from internal clients; within internal service providers, Sales may be named "business relationship managers" or "consultancy"; "Chief Digital Officer" role, in best incarnations, is Sales role within IT.
            - ID: MEYER-SEC-0104
              Title: "6.6.3. What Good Selling Is About"
              Text: |-
                - Def: External or internal, whatever name, great salesmanship focuses on helping clients, not on helping organization "push" products and services; in sales literature, termed strategic selling, consultative selling, or partnership selling.
                - Def: Great relationships built by recognizing what's unique about each client, understanding business challenges, connecting with right suppliers in organization; why Sales staff spend most time with clients.
                - Def: Beyond relationship building, Sales helps clients discover creative, high-payoff uses of organization's products and services; linkage between clients' business and organization's deliverables sometimes called "strategic alignment".
                - Def: Not matter of passive order-taking; Sales proactively meets with key clients to discover ways organization can help achieve goals; always works in business-driven manner, not pushing any particular products or services.
                - Def: Purpose of internal Marketing not to aggrandize organization; to help clients understand organization's value, so make better use of, gain more benefit from, offerings; Marketing also helps internal service provider better understand clients' needs through market research.
            - ID: MEYER-SEC-0105
              Title: "6.6.4. Decentralized Sales Functions"
              Text: |-
                Def: Some internal service providers decentralize Sales function, having it report to clients rather than to shared-services organization.
                Ctx: True that Sales staff must be very close to clients, spend most time with clients; may even be substructured by client business unit (dedicated to specific clients); but doesn't mean should report to clients.

                - Cpt: Problems with Decentralization of Internal Sales.
                  - Warn: When function decentralized, seems to devolve into full-service support function, rather than remain focused on just Sales Building Block for shared-services organization.
                  - Warn: Decentralized Sales staff often treat centralized department as adversary, as if role is to defend business units against them, rather than facilitate great relationships between two organizations.
                  - Warn: Makes hard to balance workloads (e.g., number of small business units share one Sales person while large business units may warrant team).
                  - Warn: Generally difficulties introducing essential methods of Sales for lack of common boss.
                  - Warn: Often miss cross-business-unit opportunities (e.g., when "consortium" of clients band together to share asset such as ERP software).
                  - Warn: Decentralized Sales staff generally don't provide services to other Building Blocks within shared-services department (like briefings on business trends and client interactions).
                  - Warn: Some believe better access to clients if part of clients' business units; but in practice, rank often gets in way; easier for shared-services person with "Director" title to attend meetings of business-unit Vice Presidents, than for Director within that business unit.
                  - Fnd: For many reasons, decentralization of Sales function not advisable.
            - ID: MEYER-SEC-0106
              Title: "6.6.5. Three Types of Sales"
              Text: |-
                Def: Three distinct types of Sales (not counting Marketing).

                - Cpt: Type 1: Account Sales.
                  - Def: High-level account representatives responsible for entire client accounts, regardless of geography; in companies, might be called "named account managers," where accounts are one or more global companies; in internal service providers, might be "business relationship managers," where accounts are one or more business units.
                  - Def: Responsible for relationship with entire account; in addition, proactively meet with selected client executives, produce stream of strategic projects by helping key clients discover high-payoff opportunities.
                  - Def: Very senior function; Account Sales professionals can (and should) attend clients' executive-level meetings and credibly discuss business strategies and challenges (without descending into product discussions); kind of people clients would like to hire for senior management positions.
                  - Ctx: While may not manage many people or big budget, strategic impact immense and job grade should be as high as most senior leaders in organization.

                - Cpt: Type 2: Retail Sales.
                  - Def: Not dedicated to any specific accounts; instead, territory is geographic; in companies, geographic sales force and any retail storefronts for walk-in customers; in internal service providers, default points of contact for clients' inquiries and concerns; may even manage showroom or demonstration center.
                  - Ctx: May also include business analysts who convert high-level opportunities (discovered by Account Sales) into detailed requirements.
                  - Def: To differentiate: Account Sales proactive, provide premium service to selected clients (top executives and key influencers of business strategies); Retail Sales reactive, available to anyone on demand.
                  - Fnd: Both types of Sales staff more than just order takers; add value by helping clients understand what most need to buy from organization to address business challenges.

                - Cpt: Type 3: Function Sales.
                  - Def: Experts in clients' professions or specific business processes (disciplines relevant to multiple accounts, hence needed by multiple Account Sales staff).
                  - Def: Don't have territory; "second-tier" salesforce called in by Account and Retail Sales to help make presentations and diagnose clients' needs.
                  - Ex: Medical device manufacturer: Account Sales staff had responsibility for hospitals; when demonstrated device in hospital's hematology laboratory, brought in trained hematologist; when same Account Sales representative demonstrated same device in same hospital's immunology laboratory, brought in trained immunologist; second-tier Function Sales force shared by all Account Sales representatives.
                  - Ex: IT: experts in "digital enterprise" (application of technology to enterprise's relationship with customers); expertise of "Chief Digital Officer" can be applied to many business units (hence, not Account Sales function); draws on many different technologies (hence, not Engineer function).
            - ID: MEYER-SEC-0107
              Title: "6.6.6. Marketing"
              Text: |-
                - Def: Marketing focuses on clients as whole (either all, or segments with similar needs and buying patterns); distinguishes it from Sales which works with clients individually.
                - Def: Marketing includes two sub-specialties: Marketing Communications (one-to-many), and Market Research (many-to-one).

                - Cpt: Marketing Communications.
                  - Def: Helps others in organization communicate with clients; across all communications channels, Marketing coordinates organization's messages for consistency with strategies and brand, ensure various entrepreneurs within organization don't over-saturate channels.
                  - Ctx: Includes branding and marketing communications strategies; publications (brochures, web sites, newsletters); advertising and direct communications; promotions; customer events.
                  - Def: In companies, goal is generate demand; for internal service providers, encourage understanding of value of function and improve client satisfaction.

                - Cpt: Market Research.
                  - Def: Inbound communications channel, serving organization as window to entire client community (its market); answers questions about what clients think, want, need, will buy; ranges from simple customer-satisfaction surveys to complex buying-pattern analyses and market-demand forecasting models.
            - ID: MEYER-SEC-0108
              Title: "6.6.7. Sales and Marketing Competencies"
              Text: |-
                - Def: Takes right people to build effective Sales and Marketing function.
                - Def: Great relationships and strategic value both depend on people who know clients, their businesses, their strategies; ideally, Sales staff have background much like clients, with similar education, experience in industry and in clients' jobs.
                - Def: Additionally, Sales staff have deep understanding of linkage between organization and clients' businesses; understand how organization's products and services can enable clients' strategies.
                - Def: Sales staff need excellent interpersonal skills; bottom-of-T also includes methods to identify clients' key concerns and needs; to discover high-payoff, strategic opportunities; to quantify benefits of proposed solutions (strategic as well as cost savings).
                - Def: Marketing also customer facing; experts in communications and market-research methods, in way customers think about organization's products and services.

                - Mdl: Competencies Profile.
                  - Bottom of T: Clients, their business strategies, linkage to organization's products/services
                  - Key methods Sales: opportunity identification and requirements planning, relationship management, benefits estimation, contract brokerage
                  - Key methods Marketing: market communications, marketing strategy, market research
                  - Technical skill: Low ("smart buyer's" knowledge of organization's entire product line)
                  - Project management: Low
                  - Service management (operations): Low
                  - Business of organization's customers: High
                  - Interpersonal skills: High
                  - People supervision: Low
            - ID: MEYER-SEC-0109
              Title: "6.6.8. Sales and Marketing Biases"
              Text: |-
                - Def: To align with clients' business strategies, organization must be prepared to flexibly offer any subset of products and services in completely business-driven manner; Sales and Marketing function represents entire organization without any product bias.
                - Def: But do have other biases.

                - Mdl: Biases Profile (Five Fundamental Conflicts).
                  - Invention versus operational stability: Agnostic
                  - Purpose-specific solutions versus components: Agnostic
                  - Enterprisewide thinking versus focus of specialist: Account (Specialist in clients), Others (Enterprisewide)
                  - Technical specialization versus unbiased diagnosis of clients' needs: Unbiased!
                  - Service oriented versus audit: Service oriented
        - ID: MEYER-SEC-0110
          Title: "6.7. Building Block: Audit"
          Text: |-
            Def: Audit Building Block includes more than traditional financial and compliance auditors; any function which inspects and judges others, and reports results to someone other than those being inspected, is considered Audit.
          Sections:
            - ID: MEYER-SEC-0111
              Title: "6.7.1. Audit Definition"
              Text: |-
                - Def: Audit may even have some authority to block others (veto requests or decisions); only Building Block with such power; all rest focus on serving, not judging, others.
                - Def: Audit distinguished from service-oriented Building Blocks in that delivers findings to someone other than people being judged; while Auditors should be polite and treat everyone professionally, people they judge not their customers.
                - Ex: Epic failure of Arthur Anderson example of misunderstanding this; financial crises in 2008 was, in part, caused by rating agencies paid by banks whose securities they judge.
                - Def: Audit sells services to people other than those whom inspect (such as enterprise's Board or external entities).
                - Ex: To illustrate difference, testing service not Audit (it's Service Provider); Engineers can voluntarily use it (or not), test results reported back to Engineers.
                - Ex: Similarly, "assessment" distinct from Audit; assessment voluntary (requested by manager, perhaps to prepare for real audits); results reported back to those who were inspected.
                - Def: By contrast, audit imposed; results reported to someone other than those being judged.
                - Def: Audit's job: catch people not in compliance with rules (laws, regulations, policies, standards, codes of conduct, financial reporting), or stop people from making mistakes by vetoing decisions.
            - ID: MEYER-SEC-0112
              Title: "6.7.2. Need for Audit"
              Text: |-
                - Def: Audit often necessary, but should be considered control mechanism of last resort; far more expensive, less effective, than systemic controls.
                - Def: When rules of game induce people to comply (i.e., when compliance in everyone's parochial self-interests), then control systemic and Audit unnecessary; don't have to force people to optimize performance appraisals, or inspect entrepreneurs to ensure producing profits.
                - Def: When systemic controls not feasible, manual inspections and judgments required.
                - Ex: Situation illustrating need: when customers can't perceive differences in product quality; if everyone had device that could identify contaminants in food, never another case of food poisoning; because consumers cannot know if item in grocery store contaminated, government (US: Food and Drug Administration) inspects food producers (Audit function); can't examine every piece of food; periodically inspect processes and test samples (expensive and imperfect control, but better than nothing).
                - Ex: Another situation: when employees have ability to gain personally by sacrificing well-being of organization (e.g., where personal conflicts of interests might induce fraud); where occurs, if systemic checks-and-balances not practical, control such as Audit needed.
            - ID: MEYER-SEC-0113
              Title: "6.7.3. Scope of Audit"
              Text: |-
                - Def: Mission of Audit strictly to uncover problems.
                - Prohib: Must not recommend corrective actions to those problems; Auditors' expertise in finding problems doesn't qualify them to design solutions (expertise of other Building Blocks).
                - Warn: Furthermore, recommending solution would be exercising undue influence, conflict of interests; imagine Internal Revenue Service recommending solve compliance problem by buying particular brand of financial software!
                - Warn: If Audit recommends solutions, would no longer be "arm's length"; might judge more harshly solution that complies but isn't what recommended, or overlook problems just because people followed recommendations.
                - Prohib: Additionally, Auditors must not disempower managers by setting objectives or giving orders; to have legitimacy, order to comply with rules and policies must come through chain of command, as should directive to cooperate with Auditors.
            - ID: MEYER-SEC-0114
              Title: "6.7.4. Audit Competencies"
              Text: |-
                - Def: Auditors experts in policies, regulations, or rules they are judging; also experts in audit process (i.e., how to collect and analyze data needed to make judgments).

                - Mdl: Competencies Profile.
                  - Bottom of T: Topic being judged
                  - Key methods: Audit process
                  - Technical skill: High
                  - Project management: Medium
                  - Service management (operations): Low
                  - Business of organization's customers: Low
                  - Interpersonal skills: Medium
                  - People supervision: Low
            - ID: MEYER-SEC-0115
              Title: "6.7.5. Audit Biases"
              Text: |-
                - Def: Audit biased in favor of compliance, regardless of needs of business.

                - Mdl: Biases Profile (Five Fundamental Conflicts).
                  - Invention versus operational stability: Operational stability
                  - Purpose-specific solutions versus components: Agnostic
                  - Enterprisewide decisions versus specialized expertise: Agnostic
                  - Technical specialization versus unbiased diagnosis of clients' needs: Specialization in topic of audits
                  - Service oriented versus audit: Audit

                - Fnd: Audit not only distinct Building Block; to avoid conflicts of interests, must be kept entirely separate from all other service-oriented Building Blocks; if in service business, can't build open, collaborative relationship with customers while also judging them.
    - ID: MEYER-SEC-0116
      Title: "7. Applying the Principles: Rainbow Analysis"
      Text: |-
        Src: Paul Cezanne: "We live in a rainbow of chaos."
        Ctx: Now ready to look at any organization chart and anticipate where structure getting in way of people's performance.
        Def: This Part introduces method (one which puts Principles and Building Blocks to work to diagnose organization chart).
      Sections:
        - ID: MEYER-SEC-0117
          Title: "7.1. Diagnosing an Organization Chart: The Rainbow Analysis"
          Sections:
            - ID: MEYER-SEC-0118
              Title: "7.1.1. Rainbow Analysis Overview"
              Text: |-
                - Def: First step in analyzing organization chart is applying Building Blocks to it.
                - Def: "Rainbow Analysis" does that, then guides through four questions to diagnose all problems designed into current organization chart; reveals strengths and weaknesses of current structure (who's set up to fight with whom, who's set up to fail).
                - Ctx: Rainbow Analysis can also be used to examine proposed organization chart before implemented; if about to announce new structure, will greatly improve odds of success; may even help avoid costly mistakes.
                - Warn: Identifying structural problems not meant to accuse organization of failing, or make people defensive; good people can overcome almost any structural dysfunction if work hard enough; Rainbow Analysis only predicts potential problems, not actual failures; highlights areas where structure making it harder for people to succeed.
            - ID: MEYER-SEC-0119
              Title: "7.1.2. Rainbow Analysis Workshop"
              Text: |-
                - Def: Rainbow Analysis is basis of highly interactive workshop in which leadership team diagnoses current organization chart; in workshop, can come to consensus on whether, and how much, change needed; experience helps understand more deeply science of structure.
                - Ctx: Facilitated Rainbow Analysis workshop for dozens of leadership teams, in corporate, government, not-for-profit enterprises; invariably, eye opener; participants see organizations and jobs in new ways; even if don't decide to restructure, understand where problems coming from and why people struggling.
                - Ctx: Can do same analysis on own; steps exactly same.
            - ID: MEYER-SEC-0120
              Title: "7.1.3. Data Collection"
              Text: |-
                - Act: Process begins with organization chart (current structure or proposed new structure); if doing Rainbow Analysis in workshop, print organization chart in poster size and put up on wall.
                - Ctx: Typically, sufficient to examine just two tiers of organization chart; in large organizations, additional management layers may be needed.
                - Ctx: Need set of eight or more colored marker-pens.
                - Act: Considering one Building Block at time, revisit definition, interpret it in context of mission of organization.
                - Act: Each leader takes turn putting colored stripe under box on chart if performs that function; put red stripe under any box doing Sales work; blue stripe under Applications Engineers; purple under Base Engineers; and so on.
                - Def: Color-code organization chart, identifying which Building Blocks within each group (often augment colors by noting Building Block and its sub-domain).
                - Warn: If analyzing current organization, be honest and color-code based on what people actually do, regardless of what organization chart says supposed to do.
                - Res: In most organizations, result is very colorful chart; why called "Rainbow Analysis".
                - Res: Data-collection step helps build deeper understanding of definitions of Building Blocks, essential to learning and applying science of structure to organization.
                - Res: Provides data for analysis; once color coding (or labeling) done, four questions will tell where problems are.
            - ID: MEYER-SEC-0121
              Title: "7.1.4. Question 1: Gaps"
              Text: |-
                - Def: Gap is any color (line of business) that's missing, or is done part-time by people whose primary focus is another function (color spread around chart in combination with other colors); nobody's primary job.
                - Ctx: Color may be there but some sub-specialties within it may be missing; to find these gaps, look more closely at specific sub-domains within each group marked with given color.

                - Cpt: Consequences of Gaps.
                  - Warn: Unreliable delivery: With no one thinking about line of business on daily basis, unreliable process; organization misses opportunities (may not even know what missed). Ref: ORG-STRUCT-PRINCIPLE3-GAPS-01.
                  - Warn: Reduced specialization: Work done by people who don't specialize in that profession. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.
                  - Res: As result of both problems, function unreliable and ineffective.
                  - Warn: Beyond that, gaps lead to overlaps when groups compete for control of missing domains (or just fill gaps for own needs).

                - Mdl: Summary of Gap Consequences.
                  - Unreliable processes [Principle 3]: unreliable product/service delivery
                  - Reduced specialization [Principle 2]: lower productivity, slower delivery (time to market), lower quality, greater risk, less innovation, more stress, lower motivation
                  - Overlaps [Principle 3]: reduced specialization, redundant efforts, less innovation, confusion, product dis-integration, territorial friction, lack of entrepreneurship
            - ID: MEYER-SEC-0122
              Title: "7.1.5. Question 2: Rainbows"
              Text: |-
                - Def: "Rainbows" easy to spot; groups marked with more than one color, delivering multiple Building Blocks.

                - Cpt: Problems Created by Rainbows.
                  - Warn: Reduced specialization: In rainbow groups, people expected to be experts at too many different things; thus, mediocre at many assignments, may neglect other duties altogether. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.
                  - Warn: Conflicts of interests: More serious problem results from combination of incompatible Building Blocks. Ref: ORG-STRUCT-PRINCIPLE5-01.
                  - Ex: Staff may be expected to keep operations stable (Service Providers), and also to innovate (Engineers).
                  - Ex: May be expected to specialize in subset of organization's products or services (Engineers or Service Providers); at same time, may represent entire organization to clients (Sales) where supposed to be completely unbiased.
                  - Warn: Combination of Audit with any other Building Block is serious conflict of interests; cannot both judge people, and build service-oriented partnership with them.

                - Mdl: Summary of Rainbow Consequences.
                  - Reduced specialization [Principle 2]: lower productivity, slower delivery, lower quality, greater risk, less innovation, more stress, lower motivation
                  - Conflicts of interests [Principle 5]: domain gaps, unpredictable and uncontrollable balance of conflicting objectives, stress
            - ID: MEYER-SEC-0123
              Title: "7.1.6. Question 3: Scattered Campuses"
              Text: |-
                - Def: When color appears many different places on organization chart, that's "scattered campus"; in worst cases, all different sub-specialties within Building Block only come together at level of organization's top executive.

                - Cpt: Problems Created by Scattered Campuses.
                  - Warn: Reduces professional exchange of experiences, discoveries, techniques, work products; leads to higher costs, slower delivery times, product dis-integration. Ref: ORG-STRUCT-PRINCIPLE6-01.
                  - Warn: Reduces coordination of profession (weaker mentoring and management controls, less load balancing, limited career paths, confusion, missed enterprise synergies).
                  - Warn: If single line of business divided, no one may feel accountable for managing that business; worse, if one group's job to oversee or decide how another group does work, then neither is whole business and both disempowered. Ref: ORG-STRUCT-PRINCIPLE1-01, ORG-STRUCT-PRINCIPLE7-01.
                  - Warn: Over time, scattered campus often leads to gaps and overlaps, since no one manager (short of top executive) in position to adjudicate domains.

                - Mdl: Summary of Scattered Campus Consequences.
                  - Less professional exchange [Principle 6]: higher costs, slower delivery times, product dis-integration
                  - Less coordination [Principle 6]: weaker mentoring and management controls, less load balancing, limited career paths, confusion, missed enterprise synergies
                  - Domain overlaps [Principle 3]: reduced specialization, redundant efforts, less innovation, confusion, product dis-integration, territorial friction, lack of entrepreneurship
                  - Domain gaps [Principle 3]: unreliable delivery, reduced specialization
                  - Disempowerment [Principles 1, 7]: lack of customer focus and entrepreneurship, less business planning, disempowerment
            - ID: MEYER-SEC-0124
              Title: "7.1.7. Question 4: Inappropriate Substructure"
              Text: |-
                - Def: To analyze final question, look at both colors and words in boxes; color (Building Block) tells what group's specialty supposed to be; scan across organization chart to see how that domain subdivided; if basis for substructure anything other than what Building Block supposed to be good at, that's inappropriate substructure. Ref: ORG-STRUCT-PRINCIPLE4-01.
                - Ex: Might see Engineers divided into groups based on clients' organization chart, or business processes, rather than types of products they produce; or Service Providers divided up based on technologies they use rather than services they provide.

                - Mdl: Appropriate Bases for Substructure.
                  - Service Providers: Service
                  - Engineers, Application: Purpose (in IT, data object)
                  - Engineers, Base: Engineering discipline
                  - Coordinators: What they coordinate (broadly classed into business, technical)
                  - Sales, Account: Client territories (business units)
                  - Sales, Retail: Geography, venue
                  - Sales, Function: Client profession or business process
                  - Marketing communications: Communications channel, service
                  - Marketing research: Service (e.g., design, data collection, analysis)

                - Cpt: Problems Created by Inappropriate Substructure.
                  - Warn: Wrong basis for substructure reduces specialization; results in lower productivity, slower delivery, lower quality, more risk, less innovation, more stress, poor morale. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.
                  - Warn: Generally creates overlapping domains; creates confusion, causes redundant efforts, undermines product integration, creates territorial friction, diminishes entrepreneurship. Ref: ORG-STRUCT-PRINCIPLE3-OVERLAPS-01.
                  - Warn: May induce inappropriate biases; Sales function divided by product line would give clients product-driven (rather than purely business-driven) recommendations; essentially, structure leads people to optimize wrong objectives. Ref: ORG-STRUCT-PRINCIPLE4-CONSEQUENCES-01.
                  - Warn: Worst of all, if groups divided by anything other than line of business (such as by tasks, or where one group's job to oversee another), serious consequences of disempowerment. Ref: ORG-STRUCT-PRINCIPLE1-01.

                - Mdl: Summary of Inappropriate Substructure Consequences.
                  - Reduced specialization [Principle 2]: lower productivity, slower delivery, lower quality, greater risk, less innovation, more stress, lower motivation
                  - Domain overlaps [Principle 3]: reduced specialization, redundant efforts, less innovation, confusion, product dis-integration, territorial friction, lack of entrepreneurship
                  - Inappropriate biases [Principle 4]: poor advice, optimizing wrong objectives
                  - Disempowerment [Principles 1, 7]: lack of customer focus and entrepreneurship, less business planning, disempowerment
            - ID: MEYER-SEC-0125
              Title: "7.1.8. Interpreting the Rainbow Analysis"
              Text: |-
                - Act: When facilitate leadership team workshops, as go through four questions, discuss each potential dysfunction, take notes of relevant problems (those which really seem to be affecting organization); list specific examples (exactly which sub-specialties missing, or where domains overlap).
                - Act: Then, considering list of relevant problems with existing structure, raise next question: Is change needed? If so, need just few small "tweaks" or "clean sheet of paper" approach?

                - Cpt: Choices at That Point.
                  - A. Do nothing
                  - B. Tweaks: few small changes to existing structure
                  - C. Clean sheet of paper: completely new structure

                - Warn: Be forewarned: Many small tweaks more difficult than Clean Sheet approach; typically less effective, lacking whole-system perspective; unless current structure very close to right, clean sheet of paper generally right way to go.
                - Rec: If doing this on own (rather than in workshop with leadership team), follow same steps; take notes as analyze each question, then assess how serious organization's problems are.
    - ID: MEYER-SEC-0126
      Title: "8. Structures Designed to Fail: Case Studies"
      Text: |-
        Src: Confucius: "Study the past if you would divine the future."
        Def: Before start drawing boxes for own organization, useful to practice; this Part is series of case studies describing approaches to structure others have tried (some may find familiar); use Rainbow Analysis to analyze faults.
        Ctx: Case studies give practice looking at organization charts and anticipating problems; warn about approaches that may be popular but have serious flaws, so won't risk repeating mistakes others made.
      Sections:
        - ID: MEYER-SEC-0127
          Title: "8.1. Strategy as Basis for Structure"
          Sections:
            - ID: MEYER-SEC-0128
              Title: "8.1.1. Situation"
              Text: |-
                - Ctx: In 1962, Alfred D. Chandler put forth well-known proposition that "structure follows strategy"; theorized organization's structure could be fine-tuned to accomplish well-defined strategy.
                - Ctx: Some still believe this; Satya Nadella, CEO Microsoft (June 17, 2015): "I'm certain that matching our structure to our strategy will best position us to build products and services our customers love and ultimately drive new growth."
                - Def: On surface, may seem logical to organize around strategies; but serious flaws in this reasoning.
            - ID: MEYER-SEC-0129
              Title: "8.1.2. Rainbow Analysis"
              Text: |-
                - Warn: Gaps: "Strategy" rarely singular; enterprises pursue multiple strategies, each with many facets; not every strategy can be represented in structure; inevitably gaps; strategies ever changing; when new strategy, or variant of strategy, occurs, may be no group dedicated to it; with such gaps, some strategies either ignored or poorly executed.
                - Warn: Rainbows: Approach creates "silo" organization, where each strategy-centric group includes all professional specialties needs to achieve objectives; reduction in specialization hampers every strategy.
                - Warn: Scattered campus: Many strategies draw on same specialties; if organization divides talent into groups by strategy, specialties scattered around organization; overall enterprise strategy likely to become disjointed; economies of scale and synergies lost.
                - Warn: Inappropriate substructure: Staff encouraged (by nature of structure) to specialize in enterprise strategy, rather than in competencies supposed to contribute to that strategy; inappropriate basis for substructure; again, reduced specialization hampers performance.
            - ID: MEYER-SEC-0130
              Title: "8.1.3. Common Sense Argument"
              Text: |-
                - Def: Pace of business changed; in Chandler's day, business strategies may have been relatively stable and long-term; but no more! Strategies can, and do, shift quickly and continually; to remain competitive, organizations must learn to be flexible and responsive ("turn on dime").
                - Warn: If structure were to follow strategy, organizations would have to restructure on frequent basis; prohibitively disruptive, expensive, disconcerting to staff; would delay response to new strategies.
                - Warn: If don't continually restructure, organizations tuned to do excellent job of today's strategies destined to perform poorly at tomorrow's strategies.
                - Warn: Perhaps worse, organization structured around today's strategies will fail to discover tomorrow's strategies.
            - ID: MEYER-SEC-0131
              Title: "8.1.4. Alternative"
              Text: |-
                - Def: Well-designed organization chart, combined with effective teamwork, can handle any strategy.
                - Mech: Strategy translates into specific initiatives; for each initiative, clear domains identify one and only group that "sells" that product or service; becomes "prime contractor" for that strategic initiative; then, teamwork processes take over; prime contractor may get help from any other groups anywhere in organization, they in turn from still others.
                - Res: This way, each strategic initiative draws from existing structure all needed competencies; organization can quickly recombine talents on new teams to address unlimited number of strategies.
                - Res: Healthy structure responds effectively to continually changing mix of strategies; yet provides stability that allows people to focus on specialties, which cultivates excellence.
                - Res: In entrepreneurial organization, everybody continually develops own strategies as entrepreneurial businesses within business.
                - Fnd: Healthy organizations flexibly respond to diverse client strategies, while continually generating own strategies (reversing old adage that structure follows strategy).
        - ID: MEYER-SEC-0132
          Title: "8.2. Outsource Non-Core Competencies"
          Sections:
            - ID: MEYER-SEC-0133
              Title: "8.2.1. Situation"
              Text: |-
                - Ctx: Michael Treacy and Fred Wiersema posited three "competencies" organizations require: operational excellence, product/technology leadership, customer intimacy; explained why companies (or business units) must choose just one on which to base market reputation and strategies.
                - Ctx: Although cautioned against abandoning other two, some theorists recommend organizations optimize structure to focus on just one.
                - Ctx: Innumerable vendors and consultants suggest outsource everything not considered core competency, to point where axiom become common wisdom.
            - ID: MEYER-SEC-0134
              Title: "8.2.2. Why Not Outsource"
              Text: |-
                - Warn: Outsourcing entire functions not effective for many reasons.
                - Warn: Outsourcing less critical competencies doesn't magically strengthen remaining competency; doesn't leave any more people focused on chosen competency.
                - Warn: Managing vendors certainly not easier than managing staff; vendor contracts often difficult to exercise, distracting executives with complex legal negotiations.
                - Warn: Even in less critical (but still needed) competencies, outsourcing can damage performance; can reduce flexibility, since any unanticipated requirements generally must be negotiated, contracted, come at high price.
                - Warn: Vendors can never be as well aligned with business strategies as insiders; despite talk of partnership, vendors morally obliged to optimize best interests of their shareholders, not yours.
                - Warn: Even when vested interests aligned with yours, vendors don't contribute to strategies in same way; do as told (in contracts); despite talk of "partnership," never contribute to strategic thinking at same level as leaders within enterprise.
                - Warn: In many cases, outsourcing doesn't save money; in fact, just opposite; paying vendors profit to do what otherwise could do can turn out to be expensive.
                - Fnd: Ultimately, outsourcing entire function weakens it.
            - ID: MEYER-SEC-0135
              Title: "8.2.3. Rainbow Analysis"
              Text: |-
                - Warn: Gaps: Organization designed around single competency sacrifices effectiveness at other competencies; risky for two reasons: First, most strategies require mix of competencies; weakness in any competency can jeopardize strategy (e.g., strategy focused on customer intimacy requires operational excellence in points of customer interface like customer service and web applications; innovation strategies like product development require input from sales/marketing and manufacturing; operational efficiency strategies built on excellence in engineering). Second, business conditions volatile, so strategies must be dynamic; dip in economy may require shift in emphasis from innovation to operational efficiency, to be reversed when economy recovers; organization designed to pursue only one competency ill-equipped to respond when business imperatives require other strengths.
                - Fnd: No organization can afford to focus exclusively on just one competency, settle for mediocrity in others.
            - ID: MEYER-SEC-0136
              Title: "8.2.4. Alternative"
              Text: |-
                - Def: For each Building Block, one competency dominant: Sales/Marketing dedicated to customer intimacy; Engineering to innovation; Service Providers to operational efficiency.
                - Def: When diverse groups combined into organization, organization as whole can include all Building Blocks (and all competencies); no reason why organization can't excel at all competencies; in addition to enabling any strategies, ensures voice for each perspective in strategy-formulation process.
            - ID: MEYER-SEC-0137
              Title: "8.2.5. When to Use Outsourcing"
              Text: |-
                - Def: Although outsourcing not good substitute for strong internal function, vendors can add lot of value; in some cases, may be cheaper, better, more flexible, responsive.
                - Def: External vendors more cost-effective when: Multiple corporations can share vendor's assets (only has value when economies of scale cross corporate boundaries, e.g., telecommunication networks); due to size, vendor can afford higher degree of specialization (particularly valuable in high-tech professions where only largest organizations can afford qualified individual); company requires more capital than available, willing to pay premium in operating expenses to use other companies' capital; business volumes vary widely, or grow more quickly than organization can hire staff and acquire resources (worth paying more to make costs variable rather than fixed).
            - ID: MEYER-SEC-0138
              Title: "8.2.6. Extended Staffing"
              Text: |-
                - Def: Appropriate way to take advantage of vendors without giving up internal competencies: Vendors should never be used as alternative to internal staff; instead, vendors hired by internal staff to extend productive capabilities or improve value proposition.
                - Def: Call this approach "extended staffing"; essentially, vendors part of staff of appropriate internal function, not independent service provider that works directly with other functions; clients get product or service from internal staff, who may use vendors as part of delivery capability.
                - Def: Should occur naturally in entrepreneurial organization; entrepreneurs don't focus on growing empires (costs and headcount); strive to be supplier-of-choice to customers; if more economic to "buy" than "make," first to propose it; that way, always offer best deal.
                - Prohib: Not "brokerage," as some proposed; brokerage implies just connecting buyer and seller, with no accountability for deliverables; instead, internal staff are "value-added resellers" of vendor services; people who know profession (and work for shareholders/taxpayers/donors) ones who make commitments to clients, manage vendors, retain accountability for results.
                - Def: Services internal entrepreneurs offer customers may not precisely match those vendors sell to them; staff may add value to vendor-services to better meet needs of internal customers (integration, security, business continuity, compliance, ongoing support); may assemble multiple vendor-services into more complete service; or may just repackage service, perhaps charge for it (distribute costs) in different way.
                - Res: Extended staffing promotes tight vendor integration; internal staff oversee vendors to ensure performance and compliance with internal policies, standards, plans; incorporate them in internal service-delivery processes.
                - Res: Internal staff incur costs in managing vendors (at least own time); but since specialists in professions, more effective and efficient for them to manage vendors than for consumers to do so.
                - Res: Another advantage: dynamic nature; when industry economics shift in either direction, staff can utilize vendors more or less; enterprise gets best balance between "make" and "buy" at any point in time.
                - Fnd: Extended staffing gives enterprises benefits of outsourcing, without forsaking internal competencies.
        - ID: MEYER-SEC-0139
          Title: "8.3. Managers as Client Liaisons"
          Sections:
            - ID: MEYER-SEC-0140
              Title: "8.3.1. Situation"
              Text: |-
                - Ctx: In one company, client executives complained Corporate IT didn't understand strategies, people, needs; when demanded single point of contact, CIO assigned set of business units to each senior leader; each leader had two roles: Role #1: Manage technology-engineering or service group, ostensibly available to all clients; Role #2: Serve as liaison to set of client business units, ostensibly representing entire IT department.
                - Ex: Phil headed group of IT applications developers for financial systems (general ledger, accounts payable, tax); assigned to Finance department (not just for own team's projects, but for all projects and services delivered to clients in Finance); considered "relationship manager" on behalf of all IT to CFO.
                - Ctx: Structure: Phil (financial applications + Finance clients), Sam (customer applications + Sales/Marketing clients), Bev (employee applications + HR clients).
            - ID: MEYER-SEC-0141
              Title: "8.3.2. Rainbow Analysis"
              Text: |-
                - Warn: Gaps: Clients rightly want IT liaisons readily available; Sales function should spend most time with clients; in terms of time commitment alone, full-time job; but Phil had big group to manage; couldn't spend sufficient time with clients (attending meetings; getting to know people and businesses; working to discover new opportunities; brokering clear agreements; delivering account reviews; resolving relationship issues); beyond that, Sales role requires specialized skills and methods, especially critical if function to do more than facilitate relationships and take orders; Phil knew to do function well would require study and experience; not matter of capability; confident if given proper time and training, could learn to perform client-liaison job well; but while did so, who would manage applications development group? Phil didn't have time to do both; even if had time, didn't have right background (IT expert, not finance professional; understood accounting processes; but didn't really understand business challenges and strategies); most time, Phil remained focused on original Engineering job (project pressures demanded it; technology first love and focus of career; people in group depended on guidance, coaching, leadership); thus, Sales function remained gap; senior managers provided point of contact which improved relations; but didn't do much to add value to clients' strategic challenges.
                - Warn: Rainbows: To extent Phil spent time with clients, most interactions with Accounting department (primary users of financial applications); couldn't help but notice traditional clients some of least influential of Finance department's senior management; saw Jane (manager of small Financial Planning group reporting to CFO) seemed to get more attention; Phil called Jane, told looking for high-payoff strategic IT projects, wondered if could serve; Jane invited Phil; when visited, found Jane analyzing staffing cost trends; what really needed was access to employee data, market data, data-analytics tools; but what did Phil recommend? Can't honestly expect manager of financial applications developers to prescribe anything other than extensions to general-ledger application!? Despite best intentions, technological bias crept in; project Phil suggested only of mild interest to Jane; structure put Phil in conflict-of-interests situation; as expert in set of technologies (financial applications), paid to be biased (natural bias of specialist); at same time, in client-liaison role, expected to be unbiased and represent entire IT product line; no matter how well-educated and well-intentioned, organizational forces working against him; wasn't that Phil made conscious decision to be parochial; honestly believed financial solutions to which dedicated greatest thing since sliced bread, just didn't see opportunities outside own specialty; rainbow of Sales and Engineering led to product-driven, rather than business-strategy-driven, recommendations; conflict of interests not lost on Jane; found difficult to trust objectivity of someone who also had responsibility for (hence vested interest in selling) one particular solution.
                - Warn: Inappropriate substructure: Jane persisted and got Phil to recognize need for solution other than financial systems; but then ran into another problem; other groups who supplied needed data and tools busy serving own clients; Jane needed employee data; but Bev's clients in HR set priorities for staff; Jane's Finance project didn't make list; Phil still had to find way to get job done; when couldn't get help from Bev, group developed small HR application (outside domain of expertise); similarly, clients outside Finance department had trouble getting help from Phil's group, since priorities set by CFO; result, multiple overlapping financial applications cropped up throughout company; structure led to costly replication of efforts and dis-integration of data; ultimately, structure devolved into client-dedicated Engineering groups; productivity and quality suffered; enterprisewide synergies lost.
            - ID: MEYER-SEC-0142
              Title: "8.3.3. Alternative"
              Text: |-
                - Def: Mixture of clients and technologies was attempt to fill gap in structure: Account Sales function.
                - Def: Sales not part-time job for internal service provider's senior leaders, any more than engineering and manufacturing executives can serve as corporation's sales force in spare time; Sales should be separate group, within internal service providers as within companies.
                - Warn: Some may say organization can't afford it; but truth is, small, dedicated team of Sales professionals will perform far better than same number of person-hours spent on client-liaison work distributed among managers of other functions.
                - Warn: Some may say clients won't accept "sales" function in internal shared-services organization; okay, give different name; but in addition, define services Sales delivers to help clients understand value to them.
                - Fnd: Sales is profession in own right, warrants dedicated specialists.
        - ID: MEYER-SEC-0143
          Title: "8.4. Decentralization"
          Sections:
            - ID: MEYER-SEC-0144
              Title: "8.4.1. Situation"
              Text: |-
                - Def: Business unit leaders may prefer to have own support staff rather than work with enterprise shared-services department (i.e., choose decentralization).

                - Cpt: Allure Typically Comes Down to Five Things.
                  - Customer focus: Own staff will respect them and treat well; but shared-services providers may treat as nuisance rather than customer, ignore requests, attempt to control rather than serve.
                  - Understanding business: Own staff "closer to business" and understand unique needs, whereas some shared-services providers believe "one size fits all" and force solutions that don't fit needs.
                  - Control of priorities: Can control priorities of own decentralized groups; but some shared-services providers make wait in line, beg for attention, work through committees and bureaucratic hurdles to get what need.
                  - Control of costs: If shared-services providers allocate costs, business unit leaders can control expenses more easily when group reports to them.
                  - Accountability: Mistaken belief among some corporate executives that decentralization required to hold business-unit leaders fully accountable for results (as if doing business with vendor diminishes authority over, hence accountability for, business performance).
            - ID: MEYER-SEC-0145
              Title: "8.4.2. Rainbow Analysis"
              Text: |-
                - Ctx: Decentralization de facto substructures all Building Blocks by client.
                - Warn: Gaps: Managers of decentralized support groups still not effective at Account Sales function, being busy managing groups; rarely study methods needed to discover new strategic opportunities; result: less strategic value; decentralized groups do little to improve collaboration with shared-services providers; often see role as defending business unit against corporate function; result: strained relationships.
                - Warn: Scattered campus: Each specialty scattered among business units; small groups that have to cover many domains can't specialize to same degree as consolidated function; result: lower performance, less innovation, higher costs.
                - Warn: Inappropriate substructure: Every specialty substructured by client; each builds parochial solutions, undermining enterprise synergies; enterprise synergies can be found in every internal support function (shared information/IT, talent management/HR, space/Facilities, product standards and parts/Engineering, external customer touch-points/Marketing, production facilities/Manufacturing); all can create shared or compatible solutions that encourage collaboration across business units; decentralization undermines collaboration among business units.
            - ID: MEYER-SEC-0146
              Title: "8.4.3. Case Examples"
              Text: |-
                - Ex: Heavy-Equipment Manufacturing: In spirit of autonomy, each division built own manufacturing plant; increased costs for reasons: Capacity sat idle in one plant while another pressured beyond capacity; ultimately, lots of excess capacity ("safety stock") built into system; one division had plant in country while another did not; instead of using local plant, other division shipped products from own plant in neighboring country, transportation costs rose; one division pioneered new manufacturing techniques, but other divisions didn't learn until much later when CEO intervened and commissioned corporatewide task-force to rationalize production capacity; while could have been significant economies if some plants designed around long, stable manufacturing runs while others designed for rapid re-tooling, none of divisions alone could afford to specialize to that degree.
                - Ex: Engineering Function: Each division had own design engineering function; with all reinvention, number of parts corporation had to make or buy skyrocketed; CEO-sponsored task-force found dozen different electric motors with roughly same specifications; costs of development, manufacturing, inventories, support all went up.
                - Ex: Insurance IT: Decentralization of IT function resulted in multiple customer databases; since customer-numbers varied, enterprise not able to spot customers who bought from multiple business units; Specialty Automotive business unit cancelled policy covering vintage sports car, saying no longer interested in that type of business; customer moved all insurance to another company (policies for other cars, home, personal liability umbrella, corporation); company never knew this; because customer databases fragmented among business units, knew customer as few discrete policies, not as one customer with diverse needs; decentralization undermines synergies across enterprise.

                - Fnd: Decentralization inevitably results in higher costs, slower delivery times, lower quality, less innovation, reduced career opportunities for staff, fragmented products and services which undermine enterprise synergies.
                - Warn: Only thing worse than decentralization is shared-services organization that's not customer focused; doesn't understand unique needs of each business unit; denies clients ability to control how much spend and what buy.
            - ID: MEYER-SEC-0147
              Title: "8.4.4. Federated Model"
              Text: |-
                - Def: In companies where decentralization prevalent, may be weak enterprise function for just obvious common services; all other services left to decentralized support groups; sometimes termed "federated" model.
                - Warn: Nice name doesn't solve any problems caused by decentralization; little more than truce, such that shared-services and decentralized functions not competing for territory.
                - Warn: Adopting federated model actually makes things worse; institutionalizes decentralization; ideally, shared-services providers should compete for business by offering business units better deal whenever possible; competition doesn't have to undermine local authority; shared-services providers can work through decentralized counterparts, as suppliers to them.
            - ID: MEYER-SEC-0148
              Title: "8.4.5. Dotted Lines from Decentralized Groups"
              Text: |-
                - Def: Some companies attempt to ameliorate problems caused by decentralization with "dotted line" drawn from decentralized groups up to leader of enterprise-level internal service provider.
                - Warn: From cynical perspective, might be attempt by top executives to make corporate executives accountable for behavior of people they cannot control, in spirit of holding one person accountable for entire function; violates Golden Rule: accountability without real authority. Ref: ORG-STRUCT-PRINCIPLE1-01.
                - Warn: In response, corporate leaders may try to claim degree of supervisory authority over decentralized staff; may grant business units can decide what to be done, but try to decide how work done (professional practices); some even attempt to manage career paths and contribute to performance appraisals; any attempts to exercise authority over people who don't report to you results in political struggles; real managers naturally fight any incursion on authorities; see use of dotted line as reducing ability to meet obligations; with close relationships with local business-unit executives, real (decentralized) managers generally win political battles; meanwhile, decentralized staff caught in middle; not fair to subject employee to potentially conflicting directions and priorities.
                - Fnd: Pragmatically, dotted line gives shared-services executives no real authority; decentralized staff get funding from business units, answer to business-unit leaders, quite willing to defend business units against corporate meddling; holding shared-services executive accountable for things cannot control just induces strained relationships, sets up executive to take blame when business units misbehave; to be effective, CEO must direct staff through legitimate lines of authority (through business-unit executives), not expect shared-services leaders to do "dirty work."
            - ID: MEYER-SEC-0149
              Title: "8.4.6. Roles of Shared Services Amidst Decentralization"
              Text: |-
                - Def: If have to tolerate decentralized (federated) environment, enterprise shared-services organizations can still fulfill five roles.
                  - Full-service provider to clients in corporate headquarters.
                  - Sole (monopoly) provider of short list of products and services where synergies and economies of scale widely accepted (often, services based on large, expensive assets like manufacturing plant or data center; or services that link everyone in enterprise like network); products and services on short list should be determined through consensus of business-unit leaders, not imposed by corporate executives, so as not to further strain relations.
                  - "Outsourcing" supplier whenever decentralized groups wish to buy from it; decision as to what shared-services provider will do for business unit completely at discretion of business unit; shared-services staff must earn business through excellent performance, value, relationships; by selling through (not around) decentralized counterparts, not disempowering autonomous business units in any way; yet as earn market share, can deliver some economies of scale and synergies.
                  - Sole provider of coordination services where decisions must be made that affect entire enterprise; Coordinators have no formal power; job to facilitate consensus among stakeholders on standards, policies, plans; can also facilitate collaboration among business units with common needs (shared vendor contracts/purchasing service, consortia where business units share product or service); both coordination and facilitation services just that (services); business units may or may not choose to participate; up to CEO and business-unit executives to motivate stakeholders to collaborate (demanding enterprisewide standards and policies, or common business processes); only then will decentralized staff choose to utilize these services.
                  - Spokesperson for profession, promoting best interests of all staff throughout enterprise; key: never speak for others or make commitments for others, or attempt to manage staff who report elsewhere; shared-services leader can further profession by encouraging collaboration (professional interest groups) and representing profession's interests in enterprise policy discussions.

                - Res: By accepting accountability only for these five roles, shared-services organization can contribute to enterprisewide objectives without threatening business unit autonomy, antagonizing potential customers, becoming scapegoat that takes blame for problems engendered by decentralization.
                - Res: By always treating decentralized counterparts in respectful, customer-focused manner, relationships improve and shared-services leaders find themselves with more, not less, actual influence; sometimes "soft" approach actually strong approach.
                - Warn: Despite these services, most costs of decentralization remain.
            - ID: MEYER-SEC-0150
              Title: "8.4.7. Alternative: Shared Services"
              Text: |-
                - Def: All patches only marginally effective; right answer is consolidation of shared services.
                - Def: "Shared services" refers to internal service provider that serves multiple clients; instead of each business unit owning own little group, clients buy products and services from central supplier.

                - Cpt: Benefits of Shared Services.
                  - Costs reduced when redundancies eliminated; can eliminate parallel training, product R&D, policy formulation, support functions.
                  - Shared services does not mean "one size fits all"; centralized (shared-services) team of specialists can tailor solutions to unique customers' needs at lower cost and higher quality than small groups of decentralized generalists.
                  - Can spot opportunities for "consortia" where multiple clients share single solution; even if different business units require unique solutions, can at least reuse some components, certainly reuse knowledge and competencies.
                  - Consolidation offers economies of scale in both staff and infrastructure by better balancing workloads; one business unit's peak load may occur when other business units slow; total peak demand generally less than sum of each business unit's peak; centralization reduces need for "safety stocks."
                  - Consolidates buying power; vendor licenses may be shared at lower cost; bigger organization has more bargaining power and can drive better deal.
                  - Sheer size improves performance; larger organization can support broader, more diverse product line; can support products better globally, 24 by 7; can afford higher-caliber management.
                  - Substructuring staff in appropriate way (rather than by client) increases specialization, with performance improvements (lower cost, higher quality, more innovation).
                  - Greatest benefits from potential enterprisewide business synergies; as business units find themselves using same services, may collaborate more (and better) across boundaries; implications for enterprise performance as profound as reasons why business units under same corporate umbrella in first place.

                - Fnd: Well-designed and well-managed shared-services organization not only performs better, but can improve performance throughout enterprise.
            - ID: MEYER-SEC-0151
              Title: "8.4.8. Prerequisites for Shared Services"
              Text: |-
                - Def: Before business units give up decentralized groups, shared-services organization has to address reasons clients like decentralization; five problems that drive decentralization, all can be more effectively addressed in other ways.
                  - Customer focus: Matter of culture (habits and practices within organization); can be addressed by teaching staff specific behaviors that embody spirit of customer focus (including respect for customers' purchase decisions and willingness to tailor solutions to clients' unique needs); but first, structure has to clarify whom customers are.
                  - Understanding clients' businesses: Job of Account Sales function; answer is to dedicate Account Sales professional, not Engineers, to each client business unit.
                  - Control over priorities: Decentralization gives clients understanding of limits to resources, control over priorities; but better way to address resource-governance challenge; clients can be given control of spending power rather than dedicated staff.
                  - Control of costs: Costs of shared services should never be allocated to business units on any basis other than utilization; holding business-unit executives accountable for costs can't control is futile and unfair.
                  - Accountability: Business unit leaders must be held accountable for use of shared services, just as accountable for purchases from vendors; to support this, shared-services organizations must be able to portray costs by business unit, based on consumption; until can do so, shared-services costs must not be part of business units' cost structures.

                - Fnd: If meets these requirements, shared-services organization doesn't threaten business unit autonomy any more than buying from external vendors (which shared across corporations); should be no need for decentralization.
    - ID: MEYER-SEC-0152
      Title: "9. Special Situations"
      Text: |-
        Def: This Part describes number of common challenges that, on surface, might seem to force deviation from ideal structure; but will see ways to approach challenges without compromising Principles.
        Ctx: Special situations discussed: Self-managed groups, Shared people, Remote locations, Project management office, Compliance and governance.
      Sections:
        - ID: MEYER-SEC-0153
          Title: "9.1. Self-managed Groups"
          Text: |-
            - Def: What if line of business small, perhaps just few people, and no one person significantly more senior than others? Example: small group of "gurus" in distinct discipline (few experts in technology).
            - Def: Could put staff under manager of related line of business; but may risk extending manager too far, or creating undesirable "rainbow".
            - Def: Alternative: leave line of business as box on organization chart, but with no manager; termed "self-managed group"; group manages itself as if there were supervisor over it.

            - Cpt: Advantages of Self-managed Groups.
              - Maintains focus on that line of business, rather than burying within another line of business.
              - Provides growth path for function that may someday warrant manager.
              - Useful when members need to be placed at higher level in structure to get political visibility needed to be effective (e.g., in internal service provider, few senior Account Sales staff may all report directly to organization's executive to attract high-level talent to critical function and make visible to internal client executives).
              - Helpful when members need to be placed at higher level to get job-grade (compensation) needed (e.g., when antiquated HR policies do not permit people to report to someone of same grade level).

            - Def: People and line of business still need supervision; in self-managed group, staff share duties that boss otherwise would perform; how do so should be agreed by members of group and manager above them.

            - Cpt: Choices for Sharing Supervisory Duties.
              - Boss (level up) does it.
              - "Lead" (perhaps on rotating basis) does it.
              - Any individual can do it independently.
              - Group collaborates on it (e.g., through consensus).

            - Def: Sharing of supervisory duties should be reinforced with some degree of shared destiny to ensure collaboration; some portion of everyone's performance appraisal should be based on performance of whole group.
            - Warn: Contrary to first impressions, self-managed groups do not save headcount; supervisory duties must still be fulfilled, even if shared by members of group; total supervisory workload may actually increase as result of transactions costs of rotating or sharing supervisory duties.

            - Cpt: Disadvantages of Self-managed Groups.
              - Emanate from weaker leadership; may not be as coherent in business strategies and directions, nor as strong in representing views at next level up (e.g., competing for resources and influence).
              - May be slower to acquire new methods and tools; new lines of business tend to get off to slower start.
              - Require more attention from manager above them, at minimum to do individual performance management, coaching, career counseling; manager above must ensure supervisory duties being performed effectively by group.
              - While supposed to behave as single direct report, inevitably reduce feasible span of manager at next level up, which might cost additional layer of structure elsewhere in organization.

            - Fnd: Self-managed groups not goal in themselves (although empowerment is); simply way of treating situations that warrant structural separation but not manager; approach should be used with caution; proper supervisory agreements and rewards must be cultivated to make them work.
        - ID: MEYER-SEC-0154
          Title: "9.2. Shared People: Temporary Duty"
          Text: |-
            - Def: Sometimes appropriate for one manager to loan individual to another, part time or full time, temporarily or indefinitely; borrowing term from military, call this "temporary duty" (even though may be ongoing arrangement).

            - Cpt: When Temporary Duty Needed.
              - Certain individuals have skills beyond domain of their group ("rainbow" people); not good to expand group's domain to encompass skills for three reasons: would create "rainbow" group, perhaps overlapping domains; would create anomalous structure that may outlive individual's tenure, causing difficulties for others who follow (or create need for another restructuring when individual moves on); would set precedent that acceptable to violate Principles; better to put person on loan to other group whose domain includes person's other skills.
              - Move portions of headcount from one group to another as workloads shift; "load balancing" particularly handy in smaller organizations.

            - Def: Borrowing person not contract between two groups for delivery of service, since lending group cannot sell services outside domain; simply loan of person; all accountability for work remains with receiving group, which manages borrowed individual as if part-time employee; receiving managers may even pay individual's salary for that period of time.
            - Def: If situation permanent, temporary duty equivalent to individual holding two part-time jobs, reporting to two different managers who individually supervise portions of time.
            - Prohib: Not "dual reporting" where two managers supervise person doing single job; person works in two distinct domains, hence has two distinct part-time jobs.
            - Def: Regardless of longevity of arrangement, two managers must be very clear about allocation of person's time, must agree on when that time available to each (e.g., may agree on 50/50 split, 2.5 days per week to each group; but one group may need person full-time for one week, in trade for no time another week).
            - Def: In all cases, individual should have "home" group, reporting to one manager who administratively accountable; administrative manager is point of contact for human-resources issues.
            - Def: While administrative manager takes lead responsibility for writing individual's performance appraisal, other manager who borrowed person should contribute to performance appraisal in proportion to amount of time spent working under direction.
        - ID: MEYER-SEC-0155
          Title: "9.3. Remote Locations"
          Text: |-
            - Def: In geographically dispersed organizations, some remote locations may have very few staff; but organization still has to deliver all products and services to clients in that location.
            - Def: Four ways to address remote locations.
          Sections:
            - ID: MEYER-SEC-0156
              Title: "9.3.1. Option 1: Rainbow Groups"
              Text: |-
                - Def: Create "rainbow" group that combines all Building Blocks; similar to decentralization, although shared-services executive still has supervisory authority.
                - Res: Advantages: simplicity, since minimal teamwork across geographic distances required, everyone reports to one boss.
                - Warn: Has all disadvantages of silo: reduces specialization, may create jobs in remote locations too broad for anyone to succeed at; remote people not part of core professional team, limited input to enterprise directions; explicit mechanisms must be established to coordinate research, product offerings, engineering standards, professional practices; despite efforts, remote people rarely receive sufficient technical direction from appropriate experts (busy with own projects); consistency at risk; dis-integration of organization's product line (due to rogue groups doing own thing) increases support costs and undermines enterprise synergies; establishing "rainbow" groups sends signal acceptable to violate Principles; sets bad precedent.
                - Fnd: Generally, location-specific "rainbow" groups should be avoided; only necessary when collaboration between remote location and headquarters so difficult that location must be run autonomously, despite costs and risks; with internet and modern collaborative tools, rare in most businesses.
            - ID: MEYER-SEC-0157
              Title: "9.3.2. Option 2: Site Coordinators"
              Text: |-
                - Def: In larger remote groups where headcount sufficient to permit individuals to specialize in single function, each specialist can report to appropriate manager at central location.
                - Res: Advantages: single boss, consistency in technical directions, remote staff participation in professional directions.
                - Def: In this alternative, one of remote people (typically most senior) should be appointed "site coordinator" to deal with location-specific issues (personnel policies, dress codes, hours of operation); site-oriented issues should be clearly defined, to delineate responsibilities of site coordinators from those of managers; generally issues that affect all employees at location.
                - Def: Additionally, site coordinators can serve as agent for remote staff's real managers; may help distant managers with generic (not domain-specific) supervisory duties; manager for each remote individual should clearly define which duties wishes to delegate to site coordinator.
                - Def: Site coordinators should have input to remote staff's performance appraisals (done by real manager).
                - Def: Site coordinator duties distinct from client-liaison function (i.e., Retail Sales for that location), although Retail Sales person may happen to be designated site coordinator.
                - Def: Site-coordinator duties over-and-above person's normal functional responsibilities, though additional workload must be taken into account.
            - ID: MEYER-SEC-0158
              Title: "9.3.3. Option 3: Technician Services"
              Text: |-
                - Def: In small remote groups where staff work in multiple domains, remote group may be deemed "Technician Services" business (People-based Service Provider); technicians sell time to others within organization, acting as their agents ("eyes and hands in field"); all technical direction comes from subject-matter experts who hire them.
                - Def: Technicians don't sell anything directly to clients; communicate directly with clients; but just agents of another group, accountability flows through appropriate function.
                - Def: Technicians may report to supervisor in same location (if big enough), or to manager who supervises technicians in multiple locations.
                - Warn: Doesn't work for Account Sales or Coordinators, where delegation to field technicians (requires clear documentation of what to do) not generally feasible; these functions should be delivered centrally, even to remote locations.
            - ID: MEYER-SEC-0159
              Title: "9.3.4. Option 4: Temporary Duty"
              Text: |-
                - Def: If predominant function in location and all staff there involved in that to some degree, manager and staff may report to that function; to fulfill other functions in location, any of staff (manager included) can be loaned to other groups as temporary duty.
        - ID: MEYER-SEC-0160
          Title: "9.4. Project Management Office"
          Text: |-
            - Def: Excellence in project management essential to reliable project delivery; on large, complex projects, particularly critical; what's best way to incorporate PMO in structure?
            - Warn: Traditionally, project leader accountable for managing every aspect of project, including tasks assigned to every team member; but for large projects, few people have sufficient project-management skills; some leaders address by creating small group of "super project managers" for difficult projects; creates problems.
          Sections:
            - ID: MEYER-SEC-0161
              Title: "9.4.1. Case Study: PMO that Manages Projects"
              Text: |-
                - Ctx: Since Fred's applications engineers weak in project-management skills, CIO asked Kathy to form Project Management Office (PMO); Kathy wasn't there to help Fred manage projects; other way around; Kathy accountable for big or complex projects, Fred just "body shop" supplying people to work on Kathy's projects; led to numerous problems.
                - Warn: Kathy's project managers experts in project management, not applications engineering; nonetheless, controlled who on project team and their assignments, schedules, key design decisions that affected delivery dates; with non-technical people calling shots, quality suffered.
                - Warn: Exacerbating this, incentives biased against quality; Kathy not accountable for long-term applications support; but certainly accountable for on-time delivery; cut corners to get projects out on time.
                - Warn: Meanwhile, Fred disempowered; couldn't control key design decisions; but still accountable for future support, maintenance, operational efficiency, integrations.
                - Warn: Fred didn't really own line of business; with Kathy taking over delivery of products from time to time, wasn't empowered entrepreneur who could plan future, define products, optimize methods and costs, evolve capabilities.
                - Warn: Fred's staff, being just body shop on all interesting projects, demoralized; had little incentive to improve project-management skills (root cause of problem).
                - Res: As expected, Kathy and Fred at odds, not because didn't get along but because structure set them up to fight.
            - ID: MEYER-SEC-0162
              Title: "9.4.2. Project Management as Service"
              Text: |-
                - Def: Project-management experts important; PMO in itself not problem; in fact, great way to bring discipline and proficiency to project delivery.
                - Def: Problems come from PMO that's accountable for projects, occasionally taking over delivery of other groups' products.
                - Fnd: Effective PMO is People-based Service Provider, accountable for delivering project planning and facilitation services; helps everyone succeed at respective projects, without assuming project leadership or accountability for results.
        - ID: MEYER-SEC-0163
          Title: "9.5. Compliance and Governance"
          Text: |-
            - Def: "Compliance" processes ensure organizations follow rules, including own policies and standards, contractual obligations, myriad laws and regulations; how should compliance be represented in organization chart?
            - Def: Compliance implemented through "governance," which means all processes that coordinate and control organization's resources and actions.
            - Def: Governance not limited to oversight; controls can be embedded in organizational ecosystem (structure, culture, resource-management processes, metrics); but too often, executives assume "governance" means person or committee with authority to control others.
          Sections:
            - ID: MEYER-SEC-0164
              Title: "9.5.1. Case Study: Chief Compliance Officer"
              Text: |-
                - Ctx: Allison appointed Chief Compliance Officer in IT department of huge financial services company; enthusiastically told of importance of compliance in industry, hence stature of position as one person accountable for compliance of entire IT function; "CIO gave me authority to make that happen."
                - Warn: Time and again, history proven this approach doesn't work; others have businesses to run, not going to let peer get in way; sure, comply when easy or when really have to (with big, visible initiatives); but on day-to-day basis, three factors working against: Allison accountable for compliance, not peers (won't put much effort into something not in own performance objectives); others accountable for business results, not going to compromise missions to help Allison with objectives (may have incentives to thwart if compliance gets in way); third factor is killer: others don't need to worry about compliance (Allison's problem); so if mess up and bad things happen, she'll take blame; may as well been given title "Chief Scapegoat".
                - Fnd: All factors encourage Allison's peers to find ways around controls to get jobs done; ultimately, succeed.
            - ID: MEYER-SEC-0165
              Title: "9.5.2. Who Decides Trade-offs"
              Text: |-
                - Def: Realists know there are trade-offs; to illustrate extreme: if compliance means shutting down business for while, maybe right answer to wait to implement controls, hope nothing bad happens in meantime; on other hand, if risks of non-compliance huge (people getting hurt or very large fines), rational person would choose to shut down business to implement controls.
                - Def: Trade-offs had to be made with full understanding of both risks and business impacts; somebody has to decide these trade-offs; no matter who, if something bad happens, whole organization suffers consequences; only question is, who should make decisions (compliance officer, or managers running business)?
                - Def: Either compliance officer could study business and make decisions, or teach others risks and let those who know business decide.
                - Warn: If compliance officer makes decisions, battle brewing (fighting to minimize risks, while managers fight to maintain operations); best decisions not going to come from internal fighting; far more effective if decisions collaborative.
            - ID: MEYER-SEC-0166
              Title: "9.5.3. Everyone Must Be Accountable"
              Text: |-
                - Def: Only one way to make managers want to collaborate: hold all accountable for own compliance.
                - Def: Golden Rule: authority and accountability must match; if compliance officer makes decisions, has to be held accountable not just for compliance but for everybody's business results; otherwise, what's to stop from deciding in favor of too much compliance, sacrificing business results, letting others take blame when critical services fail? Ref: ORG-STRUCT-PRINCIPLE1-01.
                - Fnd: Right approach: hold everybody accountable for own behaviors, including own compliance; then, willingly implement compliance initiatives to protect own hides; overall, success rate of compliance initiatives higher, not lower, when authority and accountability in right place.
            - ID: MEYER-SEC-0167
              Title: "9.5.4. Compliance as Service"
              Text: |-
                - Def: When everybody accountable for own compliance, organization doesn't need someone who forces others to comply; but still needs compliance officer.
                - Def: Job of Compliance Officer: help others succeed with compliance accountabilities; service based on expertise in how regulations affect organization and its clients.
                - Def: Compliance is Coordinator function; helps others succeed at accountabilities, including helping agree on shared decisions and processes.
                - Def: If regulators request information or impose audit, can coordinate organization's response and serve as communications channel to regulator (single point of contact); but just accountable for coordination services, while everybody accountable for own portion of response.
                - Def: Can help individual managers put together own policies and plans; at higher level, bring stakeholders to consensus on shared policies and plans, consolidate individual plans into integrated organizational plan.
                - Def: Can help others agree on shared initiatives that improve compliance; then, help implement agreed changes, not as manager accountable for results but as facilitator and subject-matter expert.
                - Def: As Coordinator, can manage tests of plans, while everybody remains accountable for own groups' responses.
                - Def: Through all services, can teach others regulatory requirements, risks of non-compliance, kinds of changes required to mitigate risks; educating others equips them to better decide trade-offs.
            - ID: MEYER-SEC-0168
              Title: "9.5.5. Oversight"
              Text: |-
                - Def: May be need for oversight; but shouldn't be mixed with service role.
                - Warn: Real auditors outside (regulators, hackers for security, Mother Nature for business continuity); if seen as auditor, doors close as approach, won't have much impact.
                - Def: Remaining service oriented, can sell "compliance assessment studies" that help managers get ready for real external audit (or know how subordinates doing); describing this way keeps on their side of table, there to help them, not judge them; must maintain good relationships to implement meaningful change.
            - ID: MEYER-SEC-0169
              Title: "9.5.6. Scapegoat Trap"
              Text: |-
                - Warn: Many functions can fall into scapegoat trap by claiming authority over, hence accepting accountability for, others' behaviors.
                - Ex: "Security" group thinks accountable for security, rather than helping everyone operate in secure manner.
                - Ex: "Business continuity" group unilaterally designs plan.
                - Ex: "Quality assurance" or "testing" group tries to take accountability for quality through inspection and control, rather than providing testing service to others accountable for producing quality products.
                - Fnd: These all examples of familiar theme: Total Quality Management; quality, in all forms, is attribute of product or service, not separate deliverable; producing products, and quality of those products, not two distinct jobs; experiences in every industry prove same principle: responsibility for compliance, safety, security, every other aspect of quality should never be separated from responsibility for doing work.
                - Fnd: In every case, better results achieved when everybody held accountable for own behaviors; Coordinators help others with accountabilities; if oversight (Audit) needed, must be kept arm's-length from service-oriented Coordinators.
    - ID: MEYER-SEC-0170
      Title: "10. Workflows: Teamwork Processes"
      Text: |-
        Src: James A. Garfield: "Commerce links all mankind in one common brotherhood of mutual dependence and interests."
        Def: To this point, focused on design of organization chart; now time to turn attention to processes of cross-boundary teamwork.
        Def: Teamwork not luxury; essential aspect of organizational design; as per Principle 2, can't specialize if can't team. Ref: ORG-STRUCT-PRINCIPLE2-01.
        Ctx: Indeed, word "structure" includes both organization charts and teamwork processes; Henry Mintzberg: "Structure of organization can be defined simply as sum total of ways in which labor divided into distinct tasks and... [how] coordination achieved among these tasks."
      Sections:
        - ID: MEYER-SEC-0171
          Title: "10.1. Importance of Teamwork"
          Text: |-
            - Def: Teamwork often gating factor in organizational design; organizations not very good at it deliberately create "silo" groups which can function relatively independently.
            - Warn: In doing so, scatter profession among all groups that need it, hence reduce specialization; in other words, consciously give up some organizational performance to avoid having to invest in more effective teamwork processes.
            - Warn: Even if self-sufficient silos not created deliberately, occur automatically if neglect teamwork processes; no matter what organization chart says, if can't get help from peers, forced to replicate skills and muddle through on own; without effective teamwork, groups inevitably evolve into silos of self-sufficient generalists.
            - Fnd: Bottom-line: better organization is at cross-boundary teamwork, more can afford to specialize and, in doing so, optimize performance; if want to build high-performance structure, must be prepared to invest in mechanisms of teamwork.
            - Def: By investing in teamwork, don't mean team-building; lot more to it than liking and trusting one another; effective cross-boundary teamwork depends on explicit mechanisms for forming and coordinating teams.
        - ID: MEYER-SEC-0172
          Title: "10.2. What Not to Do to Improve Teamwork"
          Sections:
            - ID: MEYER-SEC-0173
              Title: "10.2.1. Case Study: Randy's Teamwork Challenges"
              Text: |-
                - Ctx: When Randy hired as CIO, inherited seasoned executives technically qualified, generally liked by staff, nice people; one little detail: didn't team at all well; cordial with one another and cooperated on organizational decisions like policies and plans; but each ran group as independent silo with minimal collaboration on projects and services.
                - Warn: Obviously costing company money; many skills replicated across groups, people spread thinly as tried to do too many things, hurt productivity; another problem: people managed functions didn't know much about (applications developers ran own development servers without much security, continuity planning, even back-ups; meanwhile, infrastructure group adept at running servers had own applications developers for billing system); each department had own support functions (budgeting, purchasing); two infrastructure control centers (one for computing, another for network); three different help desks (one for PCs and infrastructure, another for applications, still another for telecommunications networks); for lack of teamwork, hand-offs rough; when application ready for production, often delays due to poor coordination between developers and infrastructure staff; perhaps most embarrassing, each department had own client liaisons (Sales); organization looked foolish when clients got different, sometimes conflicting, answers from different "single points of contact," one hand didn't know what other hand doing.
            - ID: MEYER-SEC-0174
              Title: "10.2.2. Failed Approach 1: Team-building"
              Text: |-
                - Ctx: Randy hired consultant to do one-day seminar on teamwork; consultant taught leaders importance of teaming, team problem-solving techniques, effective communications skills; everyone agreed with everything said; but back on job, nothing changed.
                - Ctx: Randy brought consultant back to do more extensive team-building process; leaders spent three days at resort playing games that required mutual trust, talking about how felt about one another and interdependencies, playing golf; got to know one another lot better, everyone had great time; but back on job, nothing changed.
            - ID: MEYER-SEC-0175
              Title: "10.2.3. Failed Approach 2: Job Rotations"
              Text: |-
                - Ctx: Getting frustrated, Randy tried job swapping; head of infrastructure group assigned to applications development; head of applications went to client support; head of client support moved to infrastructure group.
                - Res: Leaders developed lot of empathy for one another; but still nothing changed; wasn't long before former head of infrastructure, now leading applications group, requesting money to upgrade development servers; meanwhile, new head of infrastructure fiercely defended need for own billing application developers.
                - Res: Scheme lasted about three months, at which time Randy put everyone back (just moments before organization collapsed due to leaders who knew nothing about functions managed); cynics among staff got good laugh at this experiment.
            - ID: MEYER-SEC-0176
              Title: "10.2.4. Failed Approach 3: Process Engineering"
              Text: |-
                - Ctx: Randy's next attempt: define cross-boundary processes so people would know duties within teams; for service-management, hired consultant to train staff and implement ITIL "best practices" processes; for applications development, hired another consultant to implement "DevOps," including well-defined process (and tools to support) to move code from development into production; for other processes, chartered teams to document and redesign workflows that spanned organization, supported by another consultant who specialized in Lean-Six Sigma process engineering.
                - Warn: Processes defined everybody's tasks; but no one accountable for results (delivery of services to customers); Randy designated "process owners" to oversee processes end-to-end.
                - Warn: Introduced lot of strife into organization, since process owners violated Golden Rule by trying to tell others how to do jobs; many months (and dollars) later, few processes actually implemented; for those which were, additional headcount required to administer processes and coordinate hand-offs; organization became more bureaucratic, less flexible, less accountable. Ref: ORG-STRUCT-PRINCIPLE1-01.
                - Res: Going in wrong direction!
            - ID: MEYER-SEC-0177
              Title: "10.2.5. Failed Approach 4: Forced Consolidation"
              Text: |-
                - Ctx: Randy gave up on participative style and mandated reorganization; consolidated three help desks, moved development server into computer center, set up single Client Liaison group reporting directly to him.
                - Res: Resulted in utter chaos for while; after few months, things settled down: unified help desk did fine job of transferring calls to three "level-two" help desks; development servers moved into computer center, but applications developers insisted on managing themselves; reliability and security issues remained.
    - ID: MEYER-SEC-0178
      Title: "11. Benefits and Cultural Transformation"
      Text: |-
        Src: Max De Pree: "First responsibility of leader is to define reality. Last is to say thank you. In between two, leader must become servant."
        Def: Final Part helps executives think through role and plans with regard to structure of organizations.
      Sections:
        - ID: MEYER-SEC-0179
          Title: "11.1. Should I Do This? Benefits That Justify Costs"
          Text: |-
            - Def: Restructuring organization not easy; easy to simply draw boxes and assign names; but as most experienced, doing so does little to improve organization's effectiveness.
            - Def: Reason executives take ineffective short-cuts: building high-performance organization takes meticulous planning; transformational, participative process adds to leaders' workloads; plus, process stressful (people worry about careers, status, power).
            - Def: Benefits that justify costs: principle-based structure delivers both efficiencies and effectiveness; transforms organization's culture as well.
          Sections:
            - ID: MEYER-SEC-0180
              Title: "11.1.1. Efficiencies"
              Text: |-
                - Cpt: Sources of Efficiencies.
                  - Overlaps eliminated: Time saved by eliminating redundant efforts, territorial disputes, time managers spend sorting out who does what.
                  - Role clarity permits greater span: With clear domains, groups self-directed to far greater extent; permits flatter organization, reduces supervisory workloads.
                  - Professional collaboration encouraged: Bringing together related specialties induces more professional exchange; precludes redundant research, accelerates organizational learning, improves productivity, enables more reusable components instead of reinvention.

                - Warn: Be cautious about using efficiency gains to justify restructuring initiative; may lead to expectations of reduced budgets and headcount.
                - Def: In practice, efficiencies often reinvested in doing more with same budget, not same with less budget; organizations catch up on critical sustainment tasks (training, innovation, planning, relationship building); improve quality of services and reduce risks; catch up on deferred maintenance; more responsive to customers, addressing backlogs and pent-up demand; find new opportunities to deliver more value by filling gaps.
                - Warn: Promising cost savings from restructuring associates new organization with job losses; can set staff against change, making tough to realize potential benefits.
                - Warn: Efficiencies develop gradually over time as new structure settles into place, not instantly upon announcement of new organization chart.
            - ID: MEYER-SEC-0181
              Title: "11.1.2. Effectiveness"
              Text: |-
                - Def: Effectiveness more important than efficiency, even in companies concerned about costs; efficiencies produce marginal cost savings, whereas improving effectiveness enhances organization's contribution to business (highly-leveraged benefit).
                - Ex: Reducing headcount by one might save $100,000 per year; but if greater effectiveness means one more strategic project each year, benefits could be counted in millions.

                - Cpt: Reasons Well-Designed Structure Improves Effectiveness.
                  - Gaps eliminated: Assigning accountability for missing lines of business can deliver value not available from old organization (even if not full-time jobs); if Engineers or Service Providers missing, filling gaps delivers new products and services; creating new Sales function in internal service provider improves relationships and strategic alignment, should lead to ongoing stream of very high-payoff projects; if Coordinator functions missing, filling gaps improves product architecture and standardization, planning, policies, safety (security, compliance, risk).
                  - Specialization increases: As scattered campuses consolidated, and by choosing right basis for substructure, impossibly diverse jobs replaced with well-focused specialties; staff become more competent, conflicts of interests eliminated; greater focus and specialization produces improved productivity, faster and more reliable delivery, higher quality, lower risk, more innovation, less stress, greater staff motivation.
                  - Accountabilities for results clear: Groups defined as lines of business, accountable for delivering products and services; results-orientation delivers results; helps clients and internal customers, easy to know where to go for needs; precise domains facilitate performance management (easier to hold staff accountable for results-based metrics); people feel good about jobs when see value of work to customers.
                  - Teamwork enhanced: Teamwork not limited to few visible projects where executives assemble teams; happens all time, whenever any group gets help from peers; better teamwork improves performance; instead of each group attempting to be self-sufficient, best talent from wide range of relevant specialties contributes to each project; produces far better results than generalists working alone.
                  - Organization scalable: Healthy structure makes easier for organization to grow, take on new technologies and missions, integrate acquisitions and consolidations; not only clear where new opportunities fit, clear who's accountable for discovering them; for internal service providers, changes in clients' structure or strategies have minimal impact on organization's structure (outside of Account Sales); entirely possible to design structure that lasts lifetime, evolving naturally as new opportunities arise without need for another major restructuring.
                  - Executive bottleneck eliminated: Empowered staff don't need to be micro-managed; executives can rise above day-to-day and focus on more strategic challenges.
            - ID: MEYER-SEC-0182
              Title: "11.1.3. Cultural Transformation"
              Text: |-
                - Def: In addition to improved efficiency and effectiveness, healthy structure has powerful impacts on organization's culture.

                - Cpt: Empowerment.
                  - Def: When jobs defined by what people "sell" (results), accountabilities well defined; staff can be empowered to produce results as see fit.
                  - Res: Improves reliable delivery, since people have resources and authorities need to get job done.
                  - Res: Encourages creativity and innovation, as staff think about best ways to accomplish results agreed to deliver.
                  - Res: Encourages quality, since staff fully responsible for own results; people know have to maintain what sell; incentive to do things right first time, rather than wasting time and money correcting mistakes later; core principle of Total Quality Management embedded into fabric of organization.

                - Cpt: Customer Focus.
                  - Def: Running businesses within business, staff recognize funded (given budget) to serve customers, both within and outside organization.
                  - Res: Focus on delivering products and services to customers, rather than on bureaucratic territories, procedures, tasks.
                  - Res: Understand what customers want by listening, responding to customers' priorities (not own).
                  - Res: Build effective working relationships with customers, pleasant to do business with.

                - Cpt: Entrepreneurship.
                  - Def: Since groups defined as lines of business, everybody is entrepreneur.
                  - Res: Entrepreneurs know have to be reliable to stay in business; learn not to make commitments can't keep, to keep every commitment.
                  - Res: Entrepreneurs continually seek new opportunities to add value; proactively discover ways to contribute to customers' success.
                  - Res: Entrepreneurs optimize costs and methods; continually seek ways to deliver more value at lower cost.
                  - Res: Entrepreneurs plan future of businesses; develop strategies, invest in capabilities, evolve product lines.
        - ID: MEYER-SEC-0183
          Title: "11.2. Key Takeaways"
          Text: |-
            - Fnd: Structure matters; affects every aspect of organizational performance (efficiency, effectiveness, culture).
            - Fnd: Seven Principles provide scientific foundation for organizational design: Golden Rule (authority = accountability), Specialization and Teamwork, Precise Domains, Basis for Substructure, Avoid Conflicts of Interests, Cluster by Professional Synergies, Business Within Business.
            - Fnd: Five Building Blocks (Engineers, Service Providers, Coordinators, Sales/Marketing, Audit) provide common language for analyzing and designing organizations.
            - Fnd: Rainbow Analysis diagnostic method reveals structural problems: Gaps, Rainbows, Scattered Campuses, Inappropriate Substructure.
            - Fnd: Teamwork processes essential complement to organization chart; can't specialize if can't team.
            - Fnd: Special situations (self-managed groups, shared people, remote locations, PMO, compliance) can be addressed without compromising Principles.
            - Fnd: Implementation requires participative process, careful planning, patience; benefits develop over time.
            - Fnd: Well-designed structure lasts lifetime, evolving naturally without need for major restructuring.
    - ID: MEYER-SEC-0184
      Title: "12. Conclusion"
      Text: |-
        - Fnd: Organizational structure not just boxes on chart; comprehensive system encompassing organization chart, domains, teamwork processes, culture, resource-governance.
        - Fnd: Science of structure based on timeless principles, not fads or fashions; principles apply across industries, functions, cultures, organization types.
        - Fnd: Structure enables or constrains everything organization does; good people can overcome bad structure, but at great cost; well-designed structure multiplies effectiveness of every person.
        - Fnd: Investment in getting structure right pays dividends forever; structure that embodies Principles becomes self-sustaining, self-correcting system.
        - Rec: Leaders must become students of organizational science; understand principles, apply diagnostic methods, invest in proper design and implementation.
        - Rec: Structure not one-time project; ongoing stewardship responsibility; leaders must continually reinforce principles, resist pressures to compromise, help organization evolve within framework.
        - Fnd: Ultimate goal: organization where everyone empowered entrepreneur, running business within business, collaborating seamlessly across boundaries, continually discovering new ways to add value to customers.
