---
urn: urn:gn:kb:kb-gestion-lean6
nombre: kb-gestion-lean6
version: "1.0.1"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre KODA Artifact (core concepts; workshops/practical details pruned); migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/core/gestion/kb_gn_lean6_core_koda.yml (sha256:dc6c9db39320f4ccb3c9f86df5d418418004760bc2235b954b7f99d28f17cdf4); URN KODA legado urn:gorenuble:kb:gestion:lean6:1.0.1; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "felixsanhueza"
creado: 2026-01-29
lang: es
tags: ["gn", "gore-os", "koda", "core", "gestion", "kb", "lean6"]
familia: bok
---
# KODA Artifact (core concepts; workshops/practical details pruned)
# Source: complement/lean6.md

_manifest:
  urn: "urn:gorenuble:kb:gestion:lean6:1.0.1"
  federation:
    visibility: private
    license: UNLICENSED
  resolution:
    canonical_url: "file://knowledge/core/gestion/kb_gn_lean6_core_koda.yml"
  provenance:
    created_by: "felixsanhueza"
    created_at: "2026-01-29"
    source_file: "complement/lean6.md"
    last_modified_at: "2026-01-29"

ID: LEAN6-KODA-CORE-01
Version: 1.0.1
Status: Draft
Human-Creator: felixsanhueza
Human-Editor: felixsanhueza
Model-Collaborator: GPT-5.2
Creation-Date: 2026-01-29
Modification-Date: 2026-01-29
Source: "complement/lean6.md"
Ctx: "Lean Six Sigma concepts; no book chapter structure; workshops + practical activity details removed by request"
Warn: "Contenido derivado de fuente potencialmente protegida por copyright; uso interno; verificar derechos antes de redistribuir."

XRef_Required: "urn:kora:kb:spec:1.0.0"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

    LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
    END_LLM_INSTRUCTIONS

Scope:
  Req: Preserve all non-workshop content with no translation.
  Prohib: Re-introducing workshop instructions, blank templates, step-by-step practical tasks.
  Includes: Method classifications, descriptions, conceptual steps, formulas, tool lists.
  Excludes:
    - Workshops (any section titled "Workshop")
    - Implementation/Task/Blank Templates/Appendix sections
    - Figure/Image blocks and captions
    - Form/template field layouts (e.g., Kanban card template fields)

Metrics:
  Source_Chars: 261913
  Artifact_Chars: 83442
  CR: 3.139
  FS: "100% for included scope (workshop/practical details excluded by design)"

Topics:
  - ID: TOPIC-001
    Cat: "Lean Six Sigma"
    Title: "Classification of the Book"
    Src: "Lean Six Sigma > Introduction > Classification of the Book"
    Text: |-
      All methods presented in this book serve to optimize processes within the company. But what significance and relevance do these methods have in terms of economic efficiency? Do the methods also result in an increase in company value? This question will be examined in more detail below. The creation of value in the company can be measured via the Economic Value Added (EVA).
      As can be seen in Fig. 1.1, an economic value can only be created when the operating profit (Net Operating Profit After Taxes) covers the capital costs. The capital costs are in turn composed of the fixed assets and the Working Capital (WC) as well as the capital cost rate. The lever for increasing company value with the methods of production optimization lies in the area of Working Capital. Working Capital is defined as [1]:
      Working Capital represents both a measure of liquidity, as current assets can usually be quickly converted into liquid funds (unlike fixed assets), and a measure of a company's financing needs. If the WC can be reduced, this leads to a reduction in financing needs and thus to an improvement in capital profitability and improved interest expenses. Based on the definition of WC, the lever of current assets can already be fixed, which can be optimized through operational excellence. The aim is to achieve continuous value enhancement through the application of Lean Management philosophy and the methods of production optimization, thereby strengthening the company sustainably [1, 2].
      The WC is primarily determined by processes that affect inventories, receivables and liabilities. These processes are income management (Order-to-Cash), inventory management (Total-Supply-Chain) and expenditure management (Purchase-to-Pay). The focus below is on inventory management and the associated reduction of stocks. However, it should be considered that a holistic view of the three processes listed must always be taken to avoid isolated solutions. To minimize stocks, various intermediate goals can be formulated. For example, with the help of SMED, the setup time can be shortened or waste and scrap can be reduced by applying Poka Yoke. Also, existing transport routes, warehouses and processes can be optimized through a value stream analysis to achieve a reduction in stock [1].
      In summary, it can be stated that suitable measures, some of which are presented in the book, have a high influence on the economic efficiency of the company. Thus, the inventory and consequently the Working Capital can be reduced. This results in the company's capital costs decreasing and the company value being increased.
      The book is divided into individual self-contained chapters, each presenting methods for optimizing production structures.
  - ID: TOPIC-002
    Cat: "5S"
    Title: "Classification of the Method"
    Src: "Lean Six Sigma > 5S—Seiri, Seiton, Seiso, Seiketsu, Shitsuke > Classification of the Method"
    Text: |-
      5S is a Lean tool for systematically uncovering waste, named after the initial letters of five Japanese terms [1]. The term 5S is usually associated with a tidy and organized workplace and the assurance that this state is maintained [2].
      However, it turns out (Fig. 2.1), that this representation of the goals of 5S is not appropriate, because 5S is more than a method for creating order. 5S is a foundation of every Lean management approach and a prerequisite for the application of the PDCA methodology [2–5].
  - ID: TOPIC-003
    Cat: "5S"
    Title: "Description of the Method"
    Src: "Lean Six Sigma > 5S—Seiri, Seiton, Seiso, Seiketsu, Shitsuke > Description of the Method"
    Text: |-
      The 5S system, or also referred to as 5A in German technical literature [6], can be divided into the following components:
      Seiri: Seiri (Sorting) describes the separation of necessary and unnecessary items at the workplace. Material that is no longer needed is removed from the workplace. This particularly refers to excessive circulating stocks as well as unnecessary, surplus and defective tools, unnecessary machines, faulty parts as well as unneeded papers and documents [1, 6]. The aim is to keep the workplace clear and avoid waste when searching for a tool. This also increases the quality by avoiding damage to the product through the use of the wrong tool [4].
      Seiton: Seiton (Tidying up) describes the creation of a visible order that supports the process. This includes providing the work equipment in perfect condition and ergonomically within reach at a defined and standardized place [1]. It is useful to mark the places, as this way missing tools are noticed.
      Seiso: Seiso (Keeping the workplace clean) describes the general cleanliness of the workplace. Cleanliness allows errors to be detected more quickly and quality defects due to dirt and foreign bodies to be avoided [4]. Signs of wear and tear on the operating equipment become immediately apparent and unplanned machine stops and costly damage can be avoided. An orderly workplace therefore demonstrably leads to higher employee satisfaction [6].
      Seiketsu: The Japanese term Seiketsu refers to the standardization of work processes in individual process steps [1]. New employees can be better trained through prior standardization of the activity. The aim is for work instructions and processes to become routine [6]. In the area of employee induction, Lean management follows a different approach than the classic view. In the classic view, the employee is provided with documents in addition to an induction, from which he can familiarize himself with standards. The Lean management view is that a new employee is trained until he can maintain the standard without documents. In the Western world, Seiketsu is often misunderstood in terms of employee induction. Seiketsu is not intended to ensure the fastest possible induction, but the highest possible quality of work and increased motivation of the employee. The standardization of the activity within the framework of the CIP [4].
      Shitsuke: As part of Shitsuke (always apply and improve), employees and managers have to ensure that the achieved standards are not undercut. In addition, the continuous improvement process should be initiated [4], by having employees develop suggestions for eliminating Muda.
  - ID: TOPIC-004
    Cat: "Lean Six Sigma"
    Title: "Classification of the Method"
    Src: "Lean Six Sigma > Lean Six Sigma > Classification of the Method"
    Text: |-
      Lean Six Sigma is a combination of the goals and techniques of Lean Management and the Six Sigma approach. It thus combines productivity-enhancing measures with quality-focused measures, forming a holistic approach whose goal is to achieve higher success through joint planning and enhancement of both sizes.
      It shows that the demand for quality improvement (Fig. 3.1) and simultaneous cost reduction does not have to be a contradiction. Errors and waste are eliminated through a systematic and fact-based analysis of the processes. A targeted implementation of uniform measurement and project systematics increases customer satisfaction and company value [1–3].
  - ID: TOPIC-005
    Cat: "Lean Six Sigma"
    Title: "Description of the Method"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method"
    Text: |-
      As already shown in the classification, Lean Six Sigma is the combination of techniques of the elements of Lean Management and Six Sigma. A core element is the DMAIC cycle which is divided into five phases and provides a structured analysis process for a defined problem. The phases are Define (D), Measure (M), Analyze (A), Improve (I), and Control (C). This cyclical structure also ensures continuous improvement. Various tools of Lean Management or Six Sigma can be used in each of these phases (Fig. 3.3). The individual phases will now be presented in detail.
  - ID: TOPIC-006
    Cat: "Lean Six Sigma"
    Title: "Define Phase"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Define Phase"
    Text: |-
      In the Define phase, the current situation is described and the goals and the problem are precisely defined. In addition, the schedule and project organization should be determined. A uniform understanding of the Lean Six Sigma project should be created within the entire team. Therefore, a detailed project contract should be created. An important step in this phase is also to define customer requirements, as these are essential for project success.
  - ID: TOPIC-007
    Cat: "Lean Six Sigma"
    Title: "VOC"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Define Phase > VOC"
    Text: |-
      To define customer requirements, the first step is to capture the voice of the customer (Voice of The Customer). This represents a completely unfiltered statement. The aim is to make this statement measurable criteria up to the Project Ys, so that project success can be measured later (Fig. 3.2). The voice of the customer can be determined through market analyses or individual interviews.
      The actual problem of the customer needs to be understood. This results in the customer need. Subsequently, the customer's requirements must be replaced with measurable output criteria. These are also called Critical to Quality (CTQ). This is a feature that has a direct influence on the success of the output (e.g., product).
      * VOC: Voice of the customer (customer statement)
      * Customer requirements: (list of customer needs)
      * CTQs: Critical to Quality (measurable criteria)
      * Project Yields: The apex.
      To the left of the pyramid, an upward-pointing arrow indicates the transition from an "Unfiltered statement" at the bottom to a "Measurable Requirement of the customer" at the top.]
      The example provided for a customer statement is that it takes a very long time until an order release is made; consequently, a specific time limit can be defined for the release process.
  - ID: TOPIC-008
    Cat: "Lean Six Sigma"
    Title: "Project Contract"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Define Phase > Project Contract"
    Text: |-
      At the end of the Define Phase, all information should be recorded in a condensed form in a document. The company situation should be presented to legitimize the project need, including a precisely defined problem statement. A goal description should be recorded according to the SMART (Specific, Measurable, Attainable, Relevant, Time bound) formula. Finally, the financial effect should be defined, and the project team with assigned responsibilities should be named.
  - ID: TOPIC-009
    Cat: "Lean Six Sigma"
    Title: "Measure Phase"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase"
    Text: |-
      The main goal of this phase is to determine the current state, serving as the basis for later process improvement. Critical measurement criteria must be selected, and relevant data must be determined to evaluate success in meeting customer requirements. Data quality is crucial and should be verified for "goodness" through a measurement system analysis (MSA).
  - ID: TOPIC-010
    Cat: "Lean Six Sigma"
    Title: "Measurement System Analysis"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase > Measurement System Analysis"
    Text: |-
      Data collection is carried out by trained individuals using defined tools and uniform methods. A measurement system must be tested for reliability before use to rule out flawed data and false conclusions. An MSA checks the following characteristics:
      * Accuracy ("accuracy")
      * Stability ("stability")
      * Repeatability ("repeatability")
      * Reproducibility ("reproducibility")
      Resolution must also be checked, referring to the smallest possible display difference of the device; it should be of the tolerance. For discrete data, an attributive MSA is used, typically requiring at least two appraisers and 30 numbered parts (including both good and defective samples). Each appraiser measures all parts twice in a random order. A goal of 100% match with the reference value is ideal, though may be sufficient.
  - ID: TOPIC-011
    Cat: "Lean Six Sigma"
    Title: "Process Capability Analysis"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase > Process Capability Analysis"
    Text: |-
      DPMO (Defects Per Million Opportunities) is a metric describing the error rate from a company perspective:
      DPO (Defects Per Opportunities) is used to convert to the later Sigma level:
      From a customer's perspective, the PPM (Parts Per Million) metric is used:
      If there is only one possibility of error per unit, DPMO and PPM are identical. However, for meeting customer demand, it only matters if the product is defect-free. In complex systems, the denominator for DPMO will be significantly larger than for PPM because of multiple error possibilities, making DPMO a "softer" metric. For actual quality evaluation, the "sharper" PPM metric is more suitable.
  - ID: TOPIC-012
    Cat: "Lean Six Sigma"
    Title: "Process Capability Indices"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase > Process Capability Indices"
    Text: |-
      Process capability can be expressed with the metric (dispersion index), which relates process spread to tolerance:
      Because does not reflect the position of the mean value, the level index is used to represent process centering:
      This metric describes the mean value's position within the tolerance. If a mean value shift of occurs, the level index changes (e.g., from without shift to with shift). A value of at least 1.5 is required to meet Six Sigma standards.
  - ID: TOPIC-013
    Cat: "Lean Six Sigma"
    Title: "Sigma Level"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase > Sigma Level"
    Text: |-
      To determine the sigma level, the error rate is converted into the yield ():
      This corresponds to a yield of . The sigma level is read using a Z-table. Process sigma is divided into Sigma Short Term and Sigma Long Term. Long-term values account for environmental influences and wear, so a shift of is added to the calculation.
  - ID: TOPIC-014
    Cat: "Lean Six Sigma"
    Title: "Analysis"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Analysis"
    Text: |-
      The objective is to identify root causes of the problem and verify if their resolution solves the process problem. Measured data is structured and assessed in two steps: finding main influencing variables and determining cause-effect relationships. Common methods include:
      * Distribution diagrams
      * Cause-effect diagram
      * Pareto diagram
      * Flow diagrams
      * Control Charts
      * Regression analyses
      * Hypothesis test
      * Design of Experiment (DoE)
  - ID: TOPIC-015
    Cat: "Lean Six Sigma"
    Title: "Pareto diagram"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Analysis > Pareto diagram"
    Text: |-
      This bar chart arranges individual values from largest to smallest. It is based on the Pareto principle, suggesting that of problems can be traced back to of the causes.
  - ID: TOPIC-016
    Cat: "Lean Six Sigma"
    Title: "Improve"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Improve"
    Text: |-
      In this phase, impact forecasts are reviewed and solutions for process optimization are selected. It involves determining how input variables and parameters should be set, considering disturbance variables. Activities include testing the solution, checking effectiveness, and creating action plans for sustainable implementation. Solutions are evaluated based on cost-benefit ratio, difficulty, implementation time, and risks.
  - ID: TOPIC-017
    Cat: "Lean Six Sigma"
    Title: "Control"
    Src: "Lean Six Sigma > Lean Six Sigma > Description of the Method > Control"
    Text: |-
      The final phase stabilizes the optimized process and monitors results long-term. A control system is used to recognize deviations and initiate corrective measures, such as internal audits or test plans. Cost savings should be demonstrated via before-and-after comparisons. Successful findings should be communicated company-wide to benefit other projects.
      Phase Target Six Sigma tools Lean tools
      DEFINE Identification of requirements; determining financial impact; defining participants; considering process influences; coordinating changes. Project profile, VoC, QFD, Kano model; Stakeholder analysis; SIPOC; Communication plan. Value added analysis
      MEASURE Mapping the process; working out quality-critical influences; preparation/measurement of data; determination of process capability and sigma level. Quality tree (CTQ); Data collection plan, sample survey; Quality control chart, process capability analysis. Value stream analysis, cycle time diagram
      ANALYZE Root cause analysis; comparison of process performance with best practice. FMEA, DoE, Brainstorming, Ishikawa diagram, hypothesis tests, regression analyses; Benchmarking. Seven types of waste, 5 times Why? (5W)
      IMPROVE Determination of starting points; implementing improvement actions; installation of continuous improvement routine. Evaluate and select suitable tools; Simulation, piloting. 5S, SMED, Kanban, TPM; Kaizen (KVP)
      CONTROL Long-term safeguarding of the results achieved. PDCA, quality plan, project repetition plan. SOP, Poka Yoke
  - ID: TOPIC-018
    Cat: "Lean Six Sigma"
    Title: "Measure Phase"
    Src: "Lean Six Sigma > Lean Six Sigma > Measure Phase"
    Text: |-
      The main goal of the phase is to determine the current state. This serves as the basis for later process improvement. Critical measurement criteria must be selected and the relevant data determined to evaluate success in meeting customer requirements [5]. The quality of the data is crucial. This should be checked for its goodness with a measurement system analysis (MSA).
  - ID: TOPIC-019
    Cat: "Lean Six Sigma"
    Title: "Measurement System Analysis"
    Src: "Lean Six Sigma > Lean Six Sigma > Measure Phase > Measurement System Analysis"
    Text: |-
      The collection of data for later analysis is carried out by trained individuals, based on clear instructions and within the framework of uniform methods, using defined measuring tools. This step is important as this procedure leads to a corresponding reliability of the system and the data obtained from it. Before a measurement system can be used, it must first be tested for reliability to rule out that the recorded data are not flawed. The subsequent phases build on this data, thus false conclusions can be accordingly ruled out. A measurement system analysis checks the following characteristics of a measurement system [4]:
      * Accuracy (“accuracy”),
      * Stability (“stability”),
      * Repeatability (“repeatability”) and
      * Reproducibility (“reproducibility”).
      In addition to the criteria mentioned above, it is also necessary to check the Resolution (resolution). The resolution refers to the smallest possible display difference of the measuring device. It should be less than or equal to 5 % of the Tolerance in order to record the quantity to be measured in sufficient detail [6]. An attributive measurement system analysis (MSA) is applied to discrete data. At least two appraisers and usually 30 numbered parts to be analyzed are required. Care should be taken to include both good parts and defective parts in the sample to be measured. Each appraiser must then measure all parts contained in the sample twice, in a random order. After the measurement results have been recorded, they are compared with the reference value. The goal of a good measurement system analysis is a 100 % match, although a limit value of at least 90 % may be sufficient [2].
  - ID: TOPIC-020
    Cat: "Lean Six Sigma"
    Title: "Process Capability Analysis"
    Src: "Lean Six Sigma > Lean Six Sigma > Measure Phase > Process Capability Analysis"
    Text: |-
      The DPMO (Defects Per Million Opportunities) is a metric that describes the error rate and is considered from a company’s perspective. The DPMO is defined as [7]:
      The DPO (Defects Per Opportunities) can also be calculated later on, as this metric is used to convert to the later Sigma level. This metric is defined as follows [7]:
      If an evaluation is to be carried out primarily from the customer’s perspective, the PPM (Parts Per Million) metric is used. It is defined as [8]:
      If there is only one possibility of error—because there is only one characteristic—the DPMO and PPM metrics are the same. For meeting customer demand, it is not crucial whether a product has one or more defects, it is only important that the product is defect-free. Therefore, the PPM metric is a customer-driven metric and is used in the automotive industry as a requirement for suppliers. In contrast, the DPMO is used as an internal metric because it offers a better comparison between different complex systems. This results from the fact that the metric not only evaluates the number of defective units, but also relates these to the possibilities of error. This allows for fine-tuning. However, it should be noted that the error rate (DPMO) is the “softer” metric. This is because the denominator, due to the number of error possibilities, which results from the multiplication of the number of units and the possible number of errors per unit, will always be significantly larger than the denominator of the PPM. This, in turn, means that the overall metric is always smaller than the PPM. Therefore, for the actual evaluation of the quality level, the “sharpest” metric—the PPM—is more suitable [8].
      Not only with the determination and consideration of the DPMO and the PPM can a statement be made about the quality capability of the process. To get a more accurate assessment of the capability, the following process capability indices must be determined.
  - ID: TOPIC-021
    Cat: "Lean Six Sigma"
    Title: "Process Capability Indices"
    Src: "Lean Six Sigma > Lean Six Sigma > Measure Phase > Process Capability Indices"
    Text: |-
      The measure of process capability can be expressed with the metric . This evaluates the reliability of a process to achieve the required goals. For this, the process spread is related to the tolerance. This metric is also described by Töpfer as the dispersion index.
      The dispersion index characterizes the basic suitability of a process to deliver values with small dispersion in relation to the length of the tolerance interval. The metric can be calculated by [9, 10]:
      The disadvantage of the dispersion index is that it does not reflect the position of the mean value. This can lead to the dispersion being kept within a narrow range (high value), but the process is still not specification-compliant. A high value is a necessary but not sufficient condition to achieve a high process sigma value. For this, an additional consideration of the process centering is required, which is described by the level index and thus represents the second metric for evaluating the process capability [2]. The metric can be calculated as follows [9, 10]:
      This metric thus describes the position of the mean value within the tolerance. If a mean value shift of occurs, the level index changes, but the dispersion index does not. This deteriorates from a (without shift) to (with shift). This means that a value of at least 1.5 must be achieved to meet the requirement of Six Sigma [9, 10]. Once the required measurements have been determined, the next step is to analyze them in more detail.
  - ID: TOPIC-022
    Cat: "Lean Six Sigma"
    Title: "Sigma Level"
    Src: "Lean Six Sigma > Lean Six Sigma > Measure Phase > Sigma Level"
    Text: |-
      To determine the sigma level based on the determined metrics DPMO or DPO and PPM, the error rate is converted into the yield (Yield).
      This corresponds to a yield of 11 %
      To determine the sigma level, the calculated value can now be read off using the Z-table (Fig. 3.9).
      The process sigma level is divided into Sigma Short Term and Sigma Long Term. The difference between a short-term process capability (Sigma Short Term) and the long-term process capability (Sigma Long Term) is based on the fact that the short-term value does not take into account external influences [4]. This means that in the long term, a process is less reliable because environmental influences or wear and tear are present. Therefore, a sigma of 1.5 is added to the Long Term, which expresses the shift due to unreliability. When determining via the DPMO, the table outputs the Sigma Long Term. However, when calculating via the Z-table of the normal distribution, the Sigma Short Term is determined [11].
  - ID: TOPIC-023
    Cat: "Lean Six Sigma"
    Title: "Analysis"
    Src: "Lean Six Sigma > Lean Six Sigma > Analysis"
    Text: |-
      The objective of this phase can be described as follows.
      Identify the root causes of the problem and then verify whether their resolution solves the process problem [5].
      To do this, the measured data must be structured, evaluated, analyzed, and assessed [12]. This phase can be divided into two steps. First, the main influencing variables must be found and then the cause-effect relationships must be determined and represented. Qualitative and statistical methods can be used for this. At the end, the effects and causes on the target variable must be known in order to develop them in the next phase [8].
      * Distribution diagrams,
      * Cause-effect diagram,
      * Pareto diagram,
      * Flow diagrams,
      * Control Charts,
      * Regression analyses,
      * Hypothesis test and
      * Design of Experiment
  - ID: TOPIC-024
    Cat: "Lean Six Sigma"
    Title: "Pareto diagram"
    Src: "Lean Six Sigma > Lean Six Sigma > Analysis > Pareto diagram"
    Text: |-
      The insights gained in the Measure phase can be graphically analyzed using a Pareto diagram. This is a bar chart in which the individual values are arranged and cumulated in size from left (largest value) to right (smallest value). This form of presentation allows the existing resources to be focused on the essential influencing variables. This form of analysis is based on the Pareto principle, according to which 80 % of the problems can be traced back to 20 % of the causes [13].
  - ID: TOPIC-025
    Cat: "Lean Six Sigma"
    Title: "Improve"
    Src: "Lean Six Sigma > Lean Six Sigma > Improve"
    Text: |-
      In this phase, a review and concretization of the impact forecasts should be carried out again, as the data basis was significantly improved in the previous phase. If the results achieved do not reach the defined target level, the cycle must be run through again [10].
      The goal of this phase is to recognize, evaluate, and select solutions for successful optimization [5]. It must be determined how the process input variables and process parameters, taking into account the disturbance variables, are to be set. The activities of this phase also include testing the solution, checking its effectiveness, and the subsequent sustainable implementation using action and measure plans [8, 12]. However, the solution should be evaluated beforehand in terms of cost-benefit ratio, degree of difficulty, time required for implementation, and possible risks [14].
  - ID: TOPIC-026
    Cat: "Lean Six Sigma"
    Title: "Control"
    Src: "Lean Six Sigma > Lean Six Sigma > Control"
    Text: |-
      The goal of the final phase is to stabilize the optimized process and check the pursued target level (Fig. 3.3) [10]. To monitor the process results and ensure them in the long term, a control system is needed that directly recognizes deviations and initiates appropriate corrective measures. This can be done through internal audits of the quality management or in the form of previously created test plans [12]. In addition to the control system, the cost savings should also be demonstrated by a before-and-after comparison, using the optimized rejects. If the results are satisfactory, the findings must be communicated throughout the company so that other projects can also benefit from them [5]. After the project is completed, further improvement activities should be implemented to thus directly enter the improvement process (CIP) [10].
      Target Six Sigma tools Lean tools
      DEFINE PHASE
      Identification of customer requirements and value creation from the customer's perspective, definition of a process plan Project profile, VoC, QFD, Kano model Value added analysis
      Determining the financial impact and savings potential of the planned project
      Determining the requirements of all participants in the process under consideration Stakeholder analysis
      Considering the influences and possibilities of the process with regard to its suppliers and customers SIPOC
      Coordinating the planned changes with all parties involved and defining the communication structure Communication plan
      MEASURE PHASE
      Mapping the current process, in particular value creation Value stream analysis, cycle time diagram
      Working out quality-critical influences Quality tree (CTQ)
      Preparation and measurement of all required data Data collection plan, sample survey
      Determination of the process capability and the current sigma level Quality control chart, process capability analysis
      ANALYZE PHASE
      Carrying out the root cause analysis to determine process influences FMEA, DoE, Brainstorming, Ishikawa diagram, hypothesis tests, regression analyses Seven types of use, 5 times Why? (5W)
      Comparison of process performance with best practice Benchmarking
      IMPROVE PHASE
      Determination of suitable starting points for process improvement Evaluate and select suitable tools
      Implementing improvement actions Simulation, piloting 5S, SMED, Kanban, TPM
      Installation of a continuous improvement routine Kaizen (KVP )
      CONTROL PHASE
      Long-term safeguarding of the results achieved PDCA, quality plan, project repetition plan SOP, Poka, Yoke
  - ID: TOPIC-027
    Cat: "Poka Yoke"
    Title: "Classification of the Method"
    Src: "Lean Six Sigma > Poka Yoke > Classification of the Method"
    Text: |-
      By enforcing the One-Piece-Flow and the desire to be able to produce flawlessly, it is necessary to make the manufacturing processes more reliable and to reduce errors. The goal of the Poka-Yoke method is to prevent errors in assembly in particular through an appropriate process design. The method follows the principle of error source prevention—since no errors can occur without an error source.
      Together with the production evolution towards Lean Management, the Poka-Yoke method was invented in Japan in 1961 by Shigeo Shingo. Shigeo Shingo was a quality engineer at Toyota who coined Poka Yoke through the term Poka Yoke [1]. Baka Yoke translates as “foolproof” and quickly spread in organizations like the Arakawa Body Company.
      An employee of the Arakawa Body Company, who was told that her workplace was “foolproof”, found the term derogatory and the term was renamed Poka Yoke “avoidance of unintentional errors” [2].
      Lean Management is characterized by Kaizen and the avoidance of “Muda” (Waste). Figure 4.1 shows the three essential drivers for successful production—it can be seen that Poka Yoke is classified in terms of product quality compared to other process optimization methods [3]. The essential factors for successful production listed in Fig. 4.1 do condition each other, but are not negatively correlated. While it is possible to improve the quality of products by accepting a longer throughput time, both factors can also be optimized equally through the use of the right methods and an appropriate management approach. Furthermore, Poka Yoke can contribute to increased throughput time through the approach of error source prevention, as potential rework becomes obsolete.
  - ID: TOPIC-028
    Cat: "Poka Yoke"
    Title: "Description of the Method"
    Src: "Lean Six Sigma > Poka Yoke > Description of the Method"
    Text: |-
      The Zero-Error-Production aimed at by Shigeo Shingo through the application of Poka Yoke is based on a basic idea with three components [4]:
      1. Cause Analysis:
      In the cause analysis, the process is checked in advance for possible incorrect actions and not resulting errors for their causes. Due to the analysis of the actions with regard to errors, a higher avoidance of errors is possible.
      2. 100% Inspection:
      Through the implementation of the Poka Yoke, all parts in a process are checked for certain potential incorrect actions, or the process is designed in such a way that the incorrect action does not occur. Due to the simplicity of the facilities, it is also economically possible to check each individual part and not just a sample.
      3. Immediate Corrective Actions:
      Because the system is designed in such a way that errors are not allowed, the initiation of necessary corrective measures takes place immediately. Furthermore, Wildemann divides Poka Yoke into three subsystems, which allow the discovery and reporting of incorrect actions to follow one another in time [5].
      different methods, such as creativity techniques. Other approaches can be the standardization of functions or visualizations at workplaces.
  - ID: TOPIC-029
    Cat: "Poka Yoke"
    Title: "Do Phase"
    Src: "Lean Six Sigma > Poka Yoke > Description of the Method > Do Phase"
    Text: |-
      5. Create action plan
      After the planning phase has been completed and the analysis is finished, the team creates an action plan in which responsibilities, deadlines, and budgets are defined.
      6. Implement action plan
      The team implements the measures of the action plan. Both progress and quality need to be controlled, documented, and if necessary, measures initiated.
  - ID: TOPIC-030
    Cat: "Poka Yoke"
    Title: "Check Phase"
    Src: "Lean Six Sigma > Poka Yoke > Description of the Method > Check Phase"
    Text: |-
      7. Measure effects
      After all activities created in the action plan have been implemented, the team checks through appropriate measurements whether the desired effects have actually occurred. This allows the degree of goal achievement to be specified. Deviations in the realized improvements can—if necessary—be corrected by a new iteration of the DEMING cycle. Special attention should be paid to the implementation of the planned measures during the new iteration.
  - ID: TOPIC-031
    Cat: "Poka Yoke"
    Title: "Act Phase"
    Src: "Lean Six Sigma > Poka Yoke > Description of the Method > Act Phase"
    Text: |-
      8. Standardization and assurance of the result
      The purpose and goal of the last step of the improvement cycle is to define a standard for the respective process. For the standard to be successfully implemented within the process, appropriate training for the employees may need to be carried out. Audits of the work method ensure the long-term guarantee of the improvement of the overall process.
  - ID: TOPIC-032
    Cat: "Poka Yoke"
    Title: "References"
    Src: "Lean Six Sigma > Poka Yoke > References"
    Text: |-
      1. Gutenberg E (1983) Grundlagen der Betriebswirtschaftslehre. Die Produktion (3), 24th ed. Springer, Berlin
      2. Böhrs H (1967) Wirtschaften mit der Zeit als Kernstück der REFA-Lehre. In: Böhrs H (Ed) Arbeitsstudien in der Betriebswirtschaft. Gabler, Wiesbaden, S 13–48
      3. Zollondz H-D (2013) Grundlagen Lean Management. Einführung in Geschichte, Begriffe, Systeme, Techniken sowie Gestaltungs- und Implementierungsansätze eines modernen Managementparadigmas. Oldenbourg (Edition Management), München
  - ID: TOPIC-033
    Cat: "Line Balancing"
    Title: "Classification of the Method"
    Src: "Lean Six Sigma > Line Balancing > Classification of the Method"
    Text: |-
      In order to withstand cost pressure in manufacturing, measures are necessary to efficiently utilize and operate the lines. Therefore, one goal must be to eliminate conflicts such as bottlenecks or underutilizations or waiting times in manufacturing. A bottleneck (or also Bottleneck) usually occurs at the workstation where the processing of the process steps (the workload) takes the longest. The so-called "Work-In-Progress (WIP) inventory" is created by processing the process steps at this station. It includes all goods that are still in the processing phase. Conversely, unused times (idle times) occur at workstations with a lower temporal workload, as these workstations always have to wait for further assignment of work by the upstream workstations with longer process times. The idle time then refers to the time when a unit is unproductive or unused (but ready for operation). This is exactly where the method of Line Balancing comes into play.
      The goal of Line Balancing is to optimize the value chain and eliminate waste [1]. In terms of production, Line Balancing aims to trim the production chain to flow production in One-Piece-Flow (single production) and to the TPS-typical pull principle [2]. In German, Line Balancing stands for cycle timing, so Line Balancing is essentially nothing more than aligning the cycle times of all workstations in the process to the customer demand to be achieved. Simply put: If you have to produce a part every 20 s to meet customer demand, then each individual station in the production chain—ideally One-Piece-Flow—should also only need 20 s.
      Line Balancing thus serves to optimally utilize human and machine resources based on customer demand [1]. The practical goal of the method is therefore to determine the number of workstations and to assign the various tasks to the workstations in such a way that a uniform temporal workload per station is created, in order to achieve a synchronized flow of parts between the workstations or the associated units (see Fig. 6.1).
      * Product quality: Chapter III Lean Six Sigma, Chapter IV Poka Yoke, Chapter V SMED.
      * Kaizen core: Chapter II 5S.
      * Throughput time: Chapter VI Line balancing (highlighted).
      * Functional flexibility/Center base: Chapter VII Spaghetti diagram, Chapter VIII Value stream, Chapter IX Kanban.]
      The even flow then also means that the idle times of the stations and the "Work-In-Progress inventory" are minimized.
      Line Balancing has its origins in the Toyota Production System (TPS) and is also located in the Lean sector. A primary assignment of this method can be seen in connection with specialized Lean Six Sigma tools for improving series production. Another special feature of this method is that optimizations are primarily carried out through mathematical analyses. Therefore, some current users trace the orientation of this tool back to M.E. Salveson, who is considered one of the pioneers for the development of mathematically specialized Lean Six Sigma tools due to his research. His considerations on the problem of the "assembly line balancing problem" were groundbreaking for the development of the Line Balancing method [3]. Today it has a more central importance in the context of the Toyota production systems, whose methods include Line Balancing as well as other mathematically oriented Six Sigma methods, which include, among others, Just in Time, Total Productive Maintenance [4].
  - ID: TOPIC-034
    Cat: "Line Balancing"
    Title: "Description of the Method"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method"
    Text: |-
      Line Balancing refers to the smoothing of very irregular production orders in terms of quantity and temporal sequence from the existing customer orders [5]. The main concern of line balancing is to balance the individual workstations in production so that no station becomes a bottleneck, leading to high Work-In-Progress inventory and increasing idle time. The following general procedure according to Fig. 6.2 is suggested.
      Before starting with line balancing measures, it is necessary to capture the current, non-optimized production process (Step 1, actual analysis).
      Only then will the two essential measures for line balancing begin. On the one hand, waste in the sense of the 7 (or 8) types of waste must be recognized and ideally eliminated. In addition, work redistribution (cycling) is then carried out to adapt all workstations to the required customer demand. In a final step, it is recommended to standardize the implemented improvements/changes to ensure the sustainability of the measures [1].
  - ID: TOPIC-035
    Cat: "Line Balancing"
    Title: "Actual Analysis"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis"
    Text: |-
      To analyze the actual situation, it is necessary to analyze the value chain or process chain [6]. This includes the temporal recording of cycle times per activity, the number of activities at each workstation, and the number of workstations. The own Overall Equipment Effectiveness (OEE) must be known. In addition, customer demand is also absolutely necessary. These terms are explained in the following [1].
  - ID: TOPIC-036
    Cat: "Line Balancing"
    Title: "Activities"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis > Activities"
    Text: |-
      Activities refer to all the steps an employee needs to perform his work. This includes active work, but also, for example, walking distances. Therefore, every single action must be recorded in terms of time. Accordingly, all activities are divided into three categories [7]:
      * value-adding activities (e.g., turning, welding, screwing),
      * necessary but non-value-adding activities (e.g., set-up, emptying containers),
      * non-value-adding activities (e.g., waiting, searching, rework).
      The correct time recording per activity is done per manufactured single piece. For example, a housing must be screwed for each finished product, and this activity takes 30 s.
  - ID: TOPIC-037
    Cat: "Line Balancing"
    Title: "Customer Cycle"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis > Customer Cycle"
    Text: |-
      The customer cycle is the ratio between the available production time and the customer order quantity. The customer cycle thus represents the time limit for each process. If the time is above the customer cycle, a bottleneck occurs. If the time is below the customer cycle, the opposite results. More is produced than the customer needs, leading to overproduction [1].
  - ID: TOPIC-038
    Cat: "Line Balancing"
    Title: "OEE – Overall Equipment Effectiveness"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis > OEE – Overall Equipment Effectiveness"
    Text: |-
      The OEE reflects a key figure that combines the number of units, speed, production time, and quality. As a key figure, the OEE (Overall Equipment Effectiveness, Total Plant Effectiveness) provides information about the total losses and makes them visible to the employees. In order to work with the OEE, the optimum for the plant must be defined beforehand. This must run without interruption, must not lose any quality, and must always work at the highest possible speed. With this target value, the degree achieved by the real plant can be compared and thus the effectiveness can be determined [8].
  - ID: TOPIC-039
    Cat: "Line Balancing"
    Title: "Cycle and Takt Time"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis > Cycle and Takt Time"
    Text: |-
      The actual analysis is particularly about the correct time recording of the individual cycle and takt times. Takt time is understood as the time for a single activity per part at a workstation. The cycle time describes the time in which a finished part leaves the work system or a workstation. It thus describes the complete run per part.
      In Line Balancing, it is about determining the required cycle time. The required cycle time is the necessary customer takt to meet the customer demand, considering the own total plant effectiveness (OEE).
      A customer takt of, for example, 100 s means that a finished part must leave the work system every 100 s in order to be able to meet the customer demand. In practice, however, no plant runs continuously without loss and at full effectiveness, so the OEE must be taken into account in the calculation to compensate for the "loss factors". In this way, the required cycle time can be determined in order to still be able to maintain the customer takt. To compensate for the losses over time, the actual required cycle time is always lower, since an OEE of 100% is almost impossible in the real environment and thus losses always have to be compensated [1].
  - ID: TOPIC-040
    Cat: "Line Balancing"
    Title: "Work Distribution Diagram"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method > Presentation of Analysis Results > Work Distribution Diagram"
    Text: |-
      The work distribution diagram (AVD) is suitable for displaying the times of individual work processes at the workstations. A column with the individual tasks is displayed for each workstation. The tasks are then color-coded into value-adding (green), non-value-adding (red), necessary (yellow), and periodic tasks (blue). Figure 6.3 graphically illustrates the structure of a work distribution diagram.
      In Fig. 6.3, the *upper dashed line* corresponds to the Customer Takt and the *lower line* to the required Cycle Time. It can be seen that some stations are significantly above the required times and some are even below. The goal of Line Balancing is to adjust the workload per station to the required cycle time, but at least below the customer takt.
  - ID: TOPIC-041
    Cat: "Line Balancing"
    Title: "Operation List"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method > Presentation of Analysis Results > Operation List"
    Text: |-
      The operation list is a tabular enumeration of operations of the entire work process [9]. It contains all operations listed in the Project Structure Plan. Each operation is assigned a letter. In addition, a predecessor is determined for each operation, i.e., the previous activity that is the prerequisite for the start of the respective operation must be determined. Furthermore, a duration is assigned to each operation. The operation list forms the basis of a network plan. It clarifies parallel work aspects and the overlap between work packages or time intervals [9]. The following Fig. 6.4 shows this graph.
      Process Activity Time [min] Predecessor
      A Process 1 4 -
      B Process 2 8 A
      C Process 3 10 A
      D Process 4 2 A, B
  - ID: TOPIC-042
    Cat: "Line Balancing"
    Title: "Network Planning Technique"
    Src: "Lean Six Sigma > Line Balancing > Description of the Method > Presentation of Analysis Results > Network Planning Technique"
    Text: |-
      After breaking down the manufacturing process into various process steps or operations and listing these operations in the Operation List, the network planning technique follows.
      Here, *circles* are labeled with letters that are supposed to represent the operations. These are then connected with *arrows* depending on the order. A *rectangle* with the corresponding duration is then drawn on each *circle* or operation. The network planning technique describes the temporal and final chaining of actions. It illustrates the order and duration of these operations. Figure 6.5 shows a Network Plan.
  - ID: TOPIC-043
    Cat: "Spaghetti Diagram"
    Title: "Classification of the Method"
    Src: "Lean Six Sigma > Spaghetti Diagram > Classification of the Method"
    Text: |-
      To analyze and illustrate waste (“Muda”) in an existing process, in addition to the value stream analysis, the so-called spaghetti diagram (also spaghetti chart) can be used. The spaghetti diagram is part of the tools for process analysis [1].
      Thus, the diagram is used to represent material flows in order to eliminate the types of waste “transport” and “movement” and thus create a process that is as lean as possible. The method primarily supports the goal of reducing throughput times and thus increases the functional flexibility of the production system (Fig. 7.1).
  - ID: TOPIC-044
    Cat: "Spaghetti Diagram"
    Title: "Description of the Method"
    Src: "Lean Six Sigma > Spaghetti Diagram > Description of the Method"
    Text: |-
      The starting point in process analysis using the spaghetti diagram is the layout of the work area. Therefore, it is important to define a clearly selected area for analysis. Once a sketch of the floor plan has been created, the process can be observed. Here too, a so-called “Gemba Walk”—a Japanese term meaning “the real place”—is suitable for capturing the process. The objects of observation can be the distances covered by the employees, but also the paths of the materials within the production process or even the flow of documents within a process. The application of this process analysis creates a high level of transparency within the existing process. This reveals efficiency losses due to the distances covered by the employees, but also losses caused by a suboptimal layout. The distances covered are drawn into the diagram by lines in the existing layout. The efficiency loss is thus usually made visible by very tangled lines in the diagram. These unproductive sequences must then be eliminated using various measures [1–3].
  - ID: TOPIC-045
    Cat: "Spaghetti Diagram"
    Title: "Application of the Spaghetti Diagram"
    Src: "Lean Six Sigma > Spaghetti Diagram > Application of the Spaghetti Diagram"
    Text: |-
      The following six steps are required to visualize the spaghetti diagram and efficiency losses (Fig. 7.2).
      1. Definition of the local dimension—Define: In the first step, a work area to be analyzed should be defined. Care should be taken to ensure that the process to be considered has a clear start and end point and that this is ideally located in a clearly defined work area. If a slightly larger work area is chosen, which extends over several halls, for example, it makes sense to divide the diagram into two individual diagrams, as it otherwise becomes too complex. Once the work area is defined, the layout can be recorded. It is advisable to work as true to scale as possible. Existing drawings of the floor plans (e.g., factory layout) should be used for this. Furthermore, it is always necessary to conduct a walk-through on site (Gemba). Only here can the exact dimensions be checked and any changes that were not listed in the drawing be uncovered. The scale drawing allows not only the conclusion in which area the efficiency losses occur, but also allows an exact measurement [2].
      2. Definition of the temporal dimension—Define: After the location has been defined, it is necessary to determine the temporal dimension. This should also be precisely defined in advance. The observation period must be chosen so that a clear statement about the process can be made in the analysis. If the observation period is too short, not enough information is recorded and therefore no reliable statement about the efficiency of the process is possible. Furthermore, in production companies that operate in shift work, it is necessary to extend the observation period to the various shifts. Different colors can be chosen to draw the lines, so that it is recognizable in the analysis which paths were taken by which shift. This opens up the possibility of comparing the two groups in the analysis, in order to eliminate possible efficiency losses between them [2].
      3. Determination of the observation object—Define: Furthermore, in this step, the object to be analyzed must also be defined. For example, should a material be analyzed through the respective process steps or should the paths of the employees be recorded? The previous definition of the observation object is intended to reduce the later complexity.
      4. Drawing of the process flow—Record: Once the temporal and spatial dimensions are defined, the layout is created and the observation object is defined, the drawing of the paths taken into the layout can begin. It is important to draw all the paths taken into the diagram exactly. Even if paths are taken twice, they must be recorded in the diagram. This may seem confusing, but it is essential for the later evaluation and uncovering of waste.
      5. Evaluation of the spaghetti diagram—Analyze: The scale layout allows a qualitative as well as quantitative assessment of the current process flow and its efficiency in the evaluation. One sign of waste occurring within the process can be the distance traveled, which is determined by the quantitative analysis. For this, the distances drawn into the layout are read off due to the scale drawing. Another method to identify waste is the qualitative evaluation. This is done based on the lines drawn into the layout. An indicator is a high frequency of lines, long path lines, and frequent crossing of lines. If the visual evaluation shows a very tangled diagram, this is often a sign of a high degree of waste [2].
      6. Define measures—Perform: After the diagram has been evaluated quantitatively and qualitatively, measures must be defined to free the process from waste and thus design a process that is as efficient as possible. A table can be used for this, in which the measures to be carried out are prioritized. It is often advisable to classify the measures according to their integration effort and to implement the so-called “quick-wins” directly. If changes to the layout are also planned, these should be implemented at a later point in time and possibly re-evaluated after a further analysis, after the “quick-wins” have been implemented.
      7. Repetition—Iterate: The last step is to conduct another recording of the process to check the implemented measures. Even with this repeated process recording, it is advisable to record it to scale. This allows the measures taken to be evaluated quantitatively and the increase in efficiency to be clearly measured. The step of repeated recording is particularly important, as often an improvement of the process on one side can lead to a deterioration on the other side.
  - ID: TOPIC-046
    Cat: "Spaghetti Diagram"
    Title: "Advantages and Disadvantages of the Spaghetti Diagram"
    Src: "Lean Six Sigma > Spaghetti Diagram > Advantages and Disadvantages of the Spaghetti Diagram"
    Text: |-
      The biggest advantage of the diagram is that no prior knowledge is required. The user can start recording immediately after drawing the layout. Furthermore, no prior knowledge is required for the evaluation. The diagram simply shows where waste occurs. This is also another major advantage of the diagram. It visualizes the process and, above all, its execution for the user in the best possible way. This way, waste can be eliminated directly in the process and, if necessary, faulty executions of the process (e.g., incorrect routes) can be eliminated. Another advantage that the Spaghetti Diagram offers is the focus on the two types of waste “Transport” and “Motion”. These two types of waste can be specifically eliminated. A major disadvantage of this diagram is the quickly occurring lack of clarity. If larger processes are analyzed or many routes have to be covered within the process, the diagram can often be difficult to evaluate. Therefore, the Define phase is a very important step to clearly delineate the process to be considered and its object of observation, thus reducing the lack of clarity to a minimum [3].
  - ID: TOPIC-047
    Cat: "Value Stream Analysis"
    Title: "Classification of the Method"
    Src: "Lean Six Sigma > Value Stream Analysis > Classification of the Method"
    Text: |-
      The value stream analysis is a method that has its roots in the Toyota Production System (TPS). The method means seeing the whole in order to improve the whole. The focus here is on the whole, meaning that analysis should also be carried out outside of production in order to gain a holistic understanding of the situation and opportunities for improvement. Thus, value stream analysis can enable a holistic transparent representation of the processes, with the aim of eliminating waste and thus significantly improving the responsiveness of production as well as increasing the profitability and efficiency [1–3].
      Value stream analysis therefore primarily focuses on optimizing throughput times while simultaneously increasing the flexibility of the production system in the manufacture of different products according to customer specifications (Fig. 8.1).
  - ID: TOPIC-048
    Cat: "Value Stream Analysis"
    Title: "Description of the Method"
    Src: "Lean Six Sigma > Value Stream Analysis > Description of the Method"
    Text: |-
      When creating a value stream analysis, it is necessary to start with a categorization of the prevailing products. If possible, a product or a product family should be chosen that needs to be analyzed in the production process. This should be followed by a customer demand analysis, which can be carried out based on the sales figures of the past fiscal year. In the next step, the actual value stream recording in production can begin, after which potential improvements can be analyzed (Fig. 8.2) [4].
  - ID: TOPIC-049
    Cat: "Value Stream Analysis"
    Title: "Product Family Formation"
    Src: "Lean Six Sigma > Value Stream Analysis > Product Family Formation"
    Text: |-
      Before starting with the value stream analysis, it must first be determined which product is to be analyzed. A value stream is always a link of the processes for exactly one product. If many different products, which take different paths through production, were drawn into a value stream analysis, this would lead to an overlay of connections in which nothing can be recognized anymore. To prevent this, the subdivision of the product spectrum according to production-relevant similar criteria must begin. This results in the product families. These are a segment that is separated from the factory and analyzed. To create such product families, the use of a product family matrix or the evaluation based on the production process/product family similarity is recommended [1].
  - ID: TOPIC-050
    Cat: "Value Stream Analysis"
    Title: "Customer Needs Analysis"
    Src: "Lean Six Sigma > Value Stream Analysis > Customer Needs Analysis"
    Text: |-
      The overarching goal of value stream analysis is to orient production towards the customer demand. For this, the customer perspective must be adopted in the analysis. This means that after defining the product families, the customer must be analyzed. The customer cycle helps in aligning the production rhythm and sales rhythm. The cycle brings the market feeling into production and makes the production rhythm transparent. The cycle time should always exactly match the customer cycle, as too high a time leads to non-fulfillment of customer demand and too short a time leads to overproduction. The customer cycle is the beat that is dictated by the market and with which production should work as best as possible [4]. The customer cycle can be calculated as follows [4]:
      The calculated customer cycle and the resulting transparent production rhythm assume that there is not a high fluctuation in demand. If demand fluctuations occur, this places high demands on the flexibility of production. Flexibility can often only be achieved by decoupling production from the customer cycle by creating stocks. However, it is also possible to initiate upstream measures. For example, sales can influence ordering behavior through quantity and time-limited discounts [4].
  - ID: TOPIC-051
    Cat: "Value Stream Analysis"
    Title: "Value Stream Recording"
    Src: "Lean Six Sigma > Value Stream Analysis > Value Stream Recording"
    Text: |-
      The first step should be to start recording the material flow. The process is generally carried out upstream. Therefore, the recording starts with the customer and continues in the opposite direction to the actual material flow. The second step is to record the information flow. This should start at the customer order acceptance, as this represents the direct interface to the customer [5].
      The recorded times are entered on the jump line, which is located under the drawing. This line consists of two levels. The upper level is used to describe the material flow using the storage range, and the lower level is used to describe the process using the processing time. At the end of the timeline, the total throughput time and the sum of the processing times are entered. The timeline allows an evaluation regarding the maximum achievable and the actual existing throughput time. A large distance from the actual to the theoretical throughput time leads to high inventories, which often cause problems with the logistical target specifications (delivery time, deadline compliance). If the throughput time is considered in relation to the processing time, a statement can be made about how much of the processing time the object under consideration has spent in the production system. This value serves as an assessment of the extent to which flow production has already been implemented [4, 6].
      A second analysis, the cycle-oriented view, allows an assessment of the Degree of Coordination of the production units. The Cycle Coordination Diagram can be used as a tool here (Fig. 8.3) This allows the difference between the theoretical cycles and the actual cycle times to be represented. The Cycle Time of a process indicates the time requirement per piece and thus the capacitive performance of this process. The smaller the cycle time, the greater the capacity. Thus, the capacity offer can be represented by the cycle times, using a bar chart, over the entire Value Stream. In addition, the Customer Cycle can also be entered to visualize where capacities may be lacking and where they are sufficiently available. The largest bar in the diagram is the bottleneck of the line, as it determines the maximum possible output. The diagram results in a Capacity Profile of the value stream [4, 7].
  - ID: TOPIC-052
    Cat: "Value Stream Analysis"
    Title: "Potential Analysis"
    Src: "Lean Six Sigma > Value Stream Analysis > Potential Analysis"
    Text: |-
      In the potential analysis, waste in the value stream should be made visible and eliminated. Wastes are activities that do not contribute to the value enhancement of the product. From the Toyota Production System and according to Taiichi Ohno, wastes can be divided into seven categories. These are [8–10]:
      * Waste due to overproduction: This means that the quantity produced exceeds the quantity demanded. Overproduction is one of the most serious wastes as it conditions the others. Overproduction can, for example, result from too high batch sizes.
      * Waste due to inventories: High inventories lead to increased capital commitment and an increase in storage or parking space. Furthermore, high inventories conceal problems that are prevalent in production. This can, for example, be caused by a wrong production strategy or lack of overview/transparency within production and the associated poor control possibility.
      * Waste due to transport: Transport often arises due to spatial separation of successive production steps or due to necessary intermediate storage due to downtimes. Causes include a poor layout, among other things.
      * Waste due to movement: This is caused by unnecessary distances covered by the employee. This can be caused by poor ergonomics at the workplace and the associated frequent rotation of the body or by a secondary activity, such as placing a container.
      * Waste due to waiting times: Waiting times often arise due to lack of material and machine downtimes. These often cause an uneven degree of utilization of employees in upstream or downstream process steps. A common reason is also poor takt time of the processes, which can be made visible in the takt alignment diagram.
      * Waste due to the production process: These are wastes that can, for example, be caused by too long setup or travel distances. But also the setup time counts as non-value adding activities to the wastes within the production process.
      * Waste due to errors: These are faulty parts that may have to be reworked in an additional step or completely removed from the production process.
  - ID: TOPIC-053
    Cat: "Kanban"
    Title: "Classification of the Method"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > Classification of the Method"
    Text: |-
      Muda describes any activity that consumes resources but does not create value, therefore the goal of any efficiency increase of a process is to minimize Muda. In manufacturing processes, the Just-In-Time manufacturing (JIT manufacturing) is desirable. This requires that the right parts in a flow process must be available at the right time, in the required quantity, at the right place [1]. This can be ensured with the help of a Kanban system (Fig. 9.1).
      The system is now a globally used control method. The reason for this popularity lies in the reduction of complexity, low susceptibility to interference as well as decentralization and the associated reduced control effort within production [2]. It ensures that production runs smoothly in the sense of lean management with minimal throughput times and high production flexibility [3].
  - ID: TOPIC-054
    Cat: "Kanban"
    Title: "Description of the Methodology"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > Description of the Methodology"
    Text: |-
      The Kanban system was developed by Ohno in 1950. It is the oldest principle of coordinated, self-regulating work systems. The Kanban system is often described in literature as the supermarket principle. As soon as a product is taken from the shelf, the resulting gap must be filled again. This view can also be transferred to production. If a part is consumed by a process, a gap is created. The upstream process must then ensure that the gap is filled as quickly as possible. This creates a clearly recognizable customer-supplier relationship [4].
      The basic model of the Kanban control in parts production consists of a linear arrangement of workstations to a Kanban line. Each workstation has a buffer in the form of an outbound store. The information flow runs backwards along the Kanban line. When a customer order is received, this information is passed on to the first process where the raw material is located. The material flow, on the other hand, runs forward until the required product, demanded by the customer order, is completed. When an order is received, it can be served in the first step from the finished goods warehouse. The gap that arises there must be filled according to the supermarket principle and thus triggers a production order to the upstream workstation. The activities of generating and consuming the parts are continued until the first process of the chain [4].
      The difference to the Push system is that in the Kanban (=Pull system) only the removed quantity is refilled. The Kanban cards serve the information flow between the individual control loops. The following two basic types of Kanban can be distinguished (Fig. 9.2):
      * The Production Kanban circulates exclusively between the source and the Buffer storage. The cards contain data regarding the containers, the transport routes (from the source to the sink), the delivery time as well as the parts information [4]. They trigger production orders at the source [5].
      * The Transport Kanban, on the other hand, circulates between the source and Buffer storage. It triggers a transport of parts to supply the consuming point from the buffer storage. If the supplier is also included in the Kanban system, the Kanban card takes over the function of the order form [5].
  - ID: TOPIC-055
    Cat: "Kanban"
    Title: "1-Card System"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > 1-Card System"
    Text: |-
      The basic model of the Kanban consists of a 1-card system. This is particularly suitable when the distance between two consecutive processing stations is so small that the output warehouse of the first process can be merged with the input warehouse of the following one. In the system, there is only one card that takes on two functions. On the one hand, transport and on the other hand, production. If a workstation removes a full container from the upstream buffer storage, the production kanban card attached to the container is passed on to the upstream process or placed in a collection box located in the buffer storage. The cards from the collection box must then be collected by an employee. The card triggers a production order and the removed quantity, with the corresponding card, is refilled in the buffer. This restores the initial state [6].
  - ID: TOPIC-056
    Cat: "Kanban"
    Title: "2-Card System"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > 2-Card System"
    Text: |-
      The 2-card system is mostly used when a container has to be fetched from a far-off place or when the transport quantity of containers differs from the quantity of the production order [4]. Here, the cards are differentiated into transport and production kanban (Fig. 9.3) [7].
      If a place has consumed a container, it must be refilled from the preceding buffer storage. The starting point of consideration here is the consumer, the so-called sink. As soon as a container has been emptied, the employee removes a transport kanban from the designated collection box and goes with the empty container and the card to the buffer storage. There, he places the container in the designated place. In the next step, the employee removes a full container. Before the container can be transported to the sink, he must exchange the production kanban attached to the full container with the carried transport kanban and pay attention to the match of the information on both cards. The removed production kanban must now be placed in the collection box provided at the buffer storage. An employee of the source collects the cards from the collection box at short time intervals, which then triggers the production. The empty containers are transported to the source and are filled as a result of the production order and then provided in the buffer storage [5]. The transport kanban regulates the information flow and the production kanban the material flow [4].
  - ID: TOPIC-057
    Cat: "Kanban"
    Title: "Conditions for a Kanban System"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > Conditions for a Kanban System"
    Text: |-
      For a manual Kanban System to work successfully, several aspects must be considered and adhered to. It is particularly important to define a high quality standard and to maintain this standard through suitable quality assurance measures, as it must be prevented that faulty parts enter the Kanban container and are transported to the next process. Another aspect that must be considered is that production may only be carried out due to a demand from the upstream process. This means that production should only be initiated by receiving a Kanban Card. In addition, only the exact quantity that is requested according to the card should be produced to avoid overproduction. The last important condition that should prevail for the system to work successfully is that the entire production must work in a standardized and stable manner. If there are frequent machine failures during production, this can result in the subsequent processes no longer being able to be supplied according to their needs. Thus, production can come to a complete standstill [3]. The prerequisites can be summarized as follows [8]:
      * The material flow must correspond to the flow principle in order to avoid strong demand fluctuations. If these cannot be prevented, this leads to high demand peaks that cannot be covered by the Kanban containers and the material flow breaks off.
      * In order to produce economically with a high variety of variants, short setup times are essential.
      * A high level of quality control is necessary to avoid delivering faulty parts to the downstream process, so that no supply gaps occur due to the low stocks [4].
      * It is recommended to produce variants or similar products that have a similar sequence of processing steps in order to keep the setup effort low [4].
  - ID: TOPIC-058
    Cat: "Kanban"
    Title: "E-Kanban"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > E-Kanban"
    Text: |-
      It has already emerged that there are some deficiencies in traditional Kanban with regard to transparency, material booking and the lack of connection to the IT system [9]. The rapidly developing information and communication technology offers very good conditions for the Kanban System. Information can be transmitted digitally. For this purpose, physical Kanban Cards are still used, but they contain a barcode. By scanning this code, the data can be read out and transferred to the system for recording incoming and outgoing parts. The reproduction is controlled by the stock in the system [10]. In addition, the economic efficiency of the container sizes can be checked [11]. The principle is identical to the reorder point system known from procurement planning [10]. With an E-Kanban board, the information regarding the quantity of empty or full containers in circulation can be viewed digitally in the internal network through terminals located in the company. With the IT connection of the Kanban, a simpler supplier connection can also be implemented. As soon as a container in the system is set to the status empty, an order is sent. When a full container is accepted, it can be scanned and thus directly registered in the system. If the data is updated daily, this results in enormous advantages for the supplier. The supplier can use the data to precisely analyze consumer behavior, which in turn leads to shorter replenishment times [12]. The advantage of the E-Kanban system is a (almost) paperless and faster flow of information. By registering the current stocks in the system and the resulting accurate material consumption booking, Kanban orders can be better prioritized depending on the order situation. In addition, scanning the barcodes provides accurate documentation of the parts and therefore also a very good possibility of product tracking [9], which is becoming increasingly important in today’s times. The E-Kanban can be used using other techniques for automatic identification and data capture (Auto-ID) such as “Radio Frequency Identification” (RFID).
  - ID: TOPIC-059
    Cat: "Kanban"
    Title: "Signal Kanban—Kanban Board"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > Signal Kanban—Kanban Board"
    Text: |-
      A variant of the Kanban system is the formation of batch sizes and the resulting bundling of orders. The idea is not to trigger production as soon as an empty container arrives, but to wait until a critical amount of orders is reached. The most common way to implement this is the traffic light system. A board is divided into three different zones: a green, yellow, and red area. Each part gets a column, which starts with red at the bottom and ends with green at the top. Incoming Kanban cards are pinned to the board. When enough cards are collected to reach the green area, production begins. If the cards are only in the yellow area, in the middle, it is up to individual decision whether the order should be executed depending on the workload. It is important to note that a sufficient quantity of full containers must be kept in the buffer storage to serve the incoming orders. This in turn requires storage space equivalent to the bundled batches, and can therefore only be used if there is a small number of different end products. The advantage of the Kanban board is the visualization of the control impulses of the material flow and the transparency thus created [4].
  - ID: TOPIC-060
    Cat: "Kanban"
    Title: "Visualization in the Kanban System"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > Visualization in the Kanban System"
    Text: |-
      Visualization in the production principle is an important component. It enables self-control and presents the services provided well for the employees. This allows them to directly identify with their performance. It serves as motivation to achieve the defined goals, as well as the process of continuous improvement (CIP) [13].
      Increased transparency prevents *waste*, increases productivity, and enhances the competitiveness of the company.
      The flow of information provided to the employee has a tremendous impact on job satisfaction. Visualization helps align the actions, thinking, and behavior of employees with the company's defined goals [13].
  - ID: TOPIC-061
    Cat: "Kanban"
    Title: "Dimensioning"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > Dimensioning"
    Text: |-
      The central question for the design of a Kanban system is:
      How many Kanbans, i.e., control elements, must be put into circulation to achieve reliable material availability? [14]
      The number of cards depends on several parameters. There is the quantity of parts or the content per Kanban, and the replenishment quantity. It must be clearly defined whether a single production or a collection in batches takes place. Other aspects are the replenishment time and a necessary safety stock [14]. The inventory should be large at the introduction of the system and can then be reduced step by step, e.g., in the sense of Kaizen [4]. This increased inventory in the initial phase, however, ensures that the unproductivity of one’s own company and the suppliers can be compensated [3]. Then, a safety factor should be included in the design of the system. However, in the sense of the Lean concept, this is a waste and should be reduced to 1 as quickly as possible. The last parameter is the initial inventory. This represents the starting size and is always reached when production has not produced for a longer period of time [14]. The number of Kanbans can be calculated as follows [14]:
      In case of fluctuating consumption, the average consumption should be replaced by a value for the maximum consumption to gain additional security in the design. Before the system can be introduced, it should be tested through a simulation [14].
      Footnotes:
      1. RT = Replenishment time; SS = Safety stock.
      SF = Safety factor; PK = Parts per Kanban.
      = Average consumption.
  - ID: TOPIC-062
    Cat: "Kanban"
    Title: "Summary"
    Src: "Lean Six Sigma > Value Stream Analysis > Kanban > Summary"
    Text: |-
      In summary, it can be stated that the Kanban system and the resulting self-regulation of production significantly reduce planning and control effort. In addition, the responsiveness of production can be greatly increased [9]. A high supply security of the material can be guaranteed with minimal stocks. Furthermore, the Kanban system is a simple, easily understandable system that shows a high level of employee involvement [15]. If there is a disruption at the workplace or with the operating resources, this usually leads directly to a standstill in production. In addition, strong demand fluctuations cannot be compensated by the Kanban system [15].
