from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "handbook"

OFF = "https://openfutureforum.com"
YT = "https://www.youtube.com/watch?v="

roles = [
 ("ceo", "CEO", "enterprise direction, accountability, and value creation", "J7_hsGT1yJI", "What CEOs Are Actually Using AI For in 2026?", "/ceo-executive-forum", "/research/ceo-ai-leverage-report"),
 ("cfo", "CFO", "capital allocation, controls, and measurable value", "q-yW5mJKI4M", "How should a CFO measure the return on AI - executive briefing", "/cfo-executive-forum", "/research/cfo-ai-leverage-report"),
 ("ciso", "CISO", "security, identity, resilience, and runtime control", "NV2uJJpVOxg", "How are CISOs adapting to AI driven threats", "/ciso-executive-forum", "/research/ciso-ai-leverage-report"),
 ("cmo", "CMO", "customer value, brand integrity, and commercial learning", "6hOTTAfPpzY", "How CMOs Are Becoming AI-First Operators", "/cmo-executive-forum", "/research/cmo-ai-leverage-report"),
 ("cto", "CTO", "architecture, delivery, reliability, and technical leverage", "Q6tPI-SiJWo", "What does agentic AI actually mean for executives", "/cto-executive-forum", "/research/ai-transformation-report"),
 ("cio", "CIO", "enterprise platforms, adoption, data stewardship, and service quality", "PkzbKF4aXLg", "How is AI changing enterprise software buying?", "/executive-transformation", "/research/ai-transformation-report"),
 ("general-counsel", "General Counsel", "legal exposure, contracting, evidence, and defensible governance", "Y6HZgkvIDMg", "When Should General Counsel Enter the Deal Process?", "/general-counsel-executive-forum", "/research/answers/who-is-liable-when-an-ai-agent-acts"),
 ("chief-people-officer", "Chief People Officer", "work design, skills, incentives, and responsible workforce transition", "7l2Nday-jY4", "Which Human Skills Become More Valuable Because of AI?", "/executive-transformation", "/research/answers/is-ai-replacing-headcount"),
 ("board-director", "Board Director", "oversight, risk appetite, succession, and long-term value", "6wLv9hV16ns", "How should boards govern AI", "/public-board-members", "/research/board-director-ai-governance-report"),
 ("private-equity", "Private Equity Leader", "portfolio value creation, diligence, governance, and repeatable operating advantage", "DOBwN4DRG4k", "How Can Private Equity Firms Measure AI ROI Across Portfolio Companies?", "/private-equity-executive-forum", "/research/investor-ai-report"),
 ("venture-investor", "Venture and CVC Investor", "market judgment, diligence, portfolio support, and responsible scaling", "Mg0NtCWTxgA", "Will AI Replace Your Job or Make You More Valuable?", "/forum-select", "/research/vc-cvc-ai-investment-report"),
 ("founder", "Founder and YC Leader", "product velocity, distribution, unit economics, and founder judgment", "SVlxm-8FQrM", "What Startup CEOs Are Actually Using AI For Right Now", "/yc-founder-executive-forum", "/research/yc-founder-ai-report"),
]

topics = [
 ("strategy", "Set an AI strategy executives can actually govern", "choices about where AI creates advantage and where it should not be used", "Ee1xOnMJS_g", "Who Actually Owns AI — CEO vs CFO vs CIO vs Security Chief", "/research/executive-state-of-ai"),
 ("portfolio", "Build and govern the AI initiative portfolio", "a visible portfolio with owners, hypotheses, dependencies, and stop rules", "tmobMrZFhm0", "How do CFOs decide which AI projects to fund - executive briefing", "/research/answers/how-are-ai-budgets-funded"),
 ("use-case-selection", "Select use cases with executive discipline", "problem value, workflow readiness, data fitness, risk, and adoption effort", "Bqp2ztBiCrg", "Which Private Equity Portfolio Companies Should Adopt AI First?", "/research/executive-ai-statistics"),
 ("roi", "Measure AI value without theater", "baseline economics, attributable change, adoption, quality, risk, and time to value", "u_dBKi3-Cfc", "The 10-Second Test That Exposes Your AI ROI Gap", "/research/answers/what-share-of-portfolios-show-measurable-ai-roi"),
 ("ownership", "Resolve the AI ownership vacuum", "decision rights across business, technology, finance, security, legal, and people leaders", "KZonyHC03AM", "Who Owns AI ROI After the CEO Signs? What 6 Reports Reveal", "/research/definitions/ownership-vacuum"),
 ("operating-model", "Design the AI operating model", "central standards with accountable business ownership and fast local learning", "UGrUu4yoY7Q", "Does your company need a Chief AI Officer", "/research/ai-transformation-report"),
 ("governance", "Move AI governance into operating decisions", "risk-tiered approvals, named owners, evidence, monitoring, and escalation", "s-Foa97q1eM", "How do you move AI governance from policy to runtime", "/research/ai-board-governance"),
 ("agents", "Govern AI agents as operating actors", "bounded authority, tool permissions, observability, human intervention, and shutdown", "8uxiABqZH2E", "What Is the Biggest Mistake Companies Make With AI Agents?", "/research/answers/who-is-liable-when-an-ai-agent-acts"),
 ("identity", "Control agent identity, credentials, and access", "least privilege, short-lived credentials, separation of duties, and traceability", "3_ROOBoqjbY", "How should companies manage credentials and tokens for AI agents", "/research/answers/biggest-ai-security-problem"),
 ("data", "Build a data foundation for accountable AI", "data rights, provenance, quality, minimization, retention, and feedback", "dpPYFnykjDU", "How do you stop AI agents from corrupting their own memory", "/research/executive-state-of-ai"),
 ("vendors", "Buy AI with stronger commercial and risk discipline", "fit, evidence, integration, security, economics, exit options, and accountability", "PkzbKF4aXLg", "How is AI changing enterprise software buying?", "/research/answers/what-ai-vendor-terms-are-companies-demanding"),
 ("security", "Make AI security an enterprise design constraint", "threat modeling, testing, monitoring, incident response, and funding", "FcWE44aBUfQ", "What CISOs Are Actually Worried About With AI Agents", "/research/answers/ai-security-budgets"),
 ("workforce", "Redesign work around human and AI strengths", "tasks, roles, capability building, managerial systems, and fair transition", "JFDfYcjEaRU", "Will AI Replace Middle Management? - Executive Briefing", "/research/answers/is-ai-replacing-headcount"),
 ("adoption", "Lead adoption through workflow change", "participation, enablement, incentives, feedback, and frontline trust", "Jkd4wS4zkuw", "What Happens When Every Employee Gets an AI Agent?", "/executive-transformation"),
 ("board", "Brief the board on AI with decision-grade evidence", "strategy, portfolio economics, material risks, capability, and decisions required", "6wLv9hV16ns", "How should boards govern AI", "/research/board-director-ai-governance-report"),
 ("scale", "Scale AI without losing control", "repeatable platforms, thresholds, reliability, cost visibility, and operating feedback", "0luLLtT54G4", "How do you keep AI agents fast and affordable at scale", "/research/ai-transformation-report"),
 ("communications", "Communicate AI progress without hype", "clear claims, disclosed uncertainty, decision context, and evidence appropriate to the audience", "DT6Fi2UjvsY", "Why Most Companies Still Can’t Prove AI ROI", "/research/definitions/optimism-gap"),
 ("90-day-plan", "Run the first 90 days of executive AI leadership", "a sequenced reset of ownership, portfolio, controls, measurement, and learning", "KcZnCmXtcbE", "How Executives Keep Up With AI Without Falling Behind", "/research/executive-ai-leverage-report"),
]

deals = [
 ("ai-diligence", "AI diligence for acquisitions and investments", "NV5OP6nMBEs", "What Do Private Equity Firms Look for During Due Diligence?", "/research/dealmakers/private-equity"),
 ("quality-of-earnings", "Connect AI claims to quality of earnings", "H4-1OSARrZY", "Why Does a Quality of Earnings Report Change the Deal Price?", "/research/dealmakers/investment-banking"),
 ("valuation", "Evaluate AI narratives in valuation", "MJToTAQTalM", "How Do Buyers Decide What a Company Is Really Worth?", "/research/answers/how-ai-is-described-in-equity-stories"),
 ("deal-readiness", "Prepare an AI-enabled company for sale", "2CL4sTIYSIY", "How Should a CFO Prepare a Company for a Sale?", "/research/dealmakers/investment-banking"),
 ("deal-governance", "Assign executive ownership across the deal", "SZbxRh0me7o", "Who Owns an M&A Deal: CEO, CFO, General Counsel or Corporate Development?", "/research/dealmakers/general-counsel"),
 ("legal-diligence", "Bring legal judgment into AI deal diligence", "Y6HZgkvIDMg", "When Should General Counsel Enter the Deal Process?", "/research/dealmakers/general-counsel"),
 ("integration", "Integrate AI capabilities after close", "ddQyXeplZY0", "Who Should Lead M&A Integration After the Deal Closes?", "/research/ai-transformation-report"),
 ("portfolio-governance", "Govern AI risk across a private equity portfolio", "0L4MBfjWn10", "How Should Private Equity Firms Govern AI Risk Across the Portfolio?", "/research/investor-ai-report"),
 ("ai-startup-economics", "Assess AI startup pricing and revenue quality", "kmrdgbFETMI", "What Makes a Company Ready for Private Equity Investment?", "/research/answers/how-ai-startups-price"),
 ("deal-failure", "Prevent AI-related deal failure", "yVdmM_Nlfww", "Why Do Good M&A Deals Fail During Due Diligence?", "/research/dealmakers/"),
]

communities = [
 ("peer-learning", "Use peer communities as executive learning infrastructure", "yzJ6ZuIAJ8U", "Why small rooms beat large networks for senior executives", "/ai-executive-community"),
 ("executive-dinners", "Design an executive dinner that creates value", "dMwMKHTNvfg", "What Actually Makes an Executive Dinner Work?", "/private-executive-dinners"),
 ("choosing-events", "Choose executive AI events with intent", "8mjdncOOHK0", "What are the best executive dinner series in Silicon Valley", "/best-ai-executive-events"),
 ("forum-select", "Understand Forum Select", "WYCGsso81Bc", "How does Open Future Forum compare to Chief, Pavilion, and Evanta", "/what-is-forum-select"),
 ("role-forums", "Choose the right role-based forum", "esMFjSkx7qM", "What is Open Future Forum", "/forum-events"),
 ("board-dinners", "Use board peer dinners for governance learning", "hPZ17bidqC0", "What is the Public Board Member Dinner Series", "/public-board-members"),
 ("sponsorship", "Evaluate executive-community sponsorship responsibly", "ttyOofAHIuI", "How should sponsors evaluate a CXO dinner series", "/executive-events"),
 ("joining", "Prepare to join a curated executive community", "rEmXzpWgtUA", "How to Get Invited to Private Events and Peer Groups", "/how-to-join"),
]

reports = [
 ("executive-ai-leverage", "Executive AI Leverage Report companion", "zOjYh3w_6iw", "The Executive AI Leverage Report What 421 Executive Responses Say About AI ROI", "/research/executive-ai-leverage-report"),
 ("ceo-ai-leverage", "CEO AI Leverage Report companion", "a4RteV4FMnU", "The CEO AI Leverage Report", "/research/ceo-ai-leverage-report"),
 ("cfo-ai-leverage", "CFO AI Leverage Report companion", "CgKtQ13oaQE", "What does the new CFO AI Leverage Report reveal about enterprise AI spending", "/research/cfo-ai-leverage-report"),
 ("ciso-ai-leverage", "CISO AI Leverage Report companion", "uRtaim5v7Ro", "What is The CISO AI Leverage Report?", "/research/ciso-ai-leverage-report"),
 ("cmo-ai-leverage", "CMO AI Leverage Report companion", "lRwgJDuivwM", "What is The CMO AI Leverage Report?", "/research/cmo-ai-leverage-report"),
 ("ai-transformation", "AI Transformation Report companion", "Bl9-49OV7js", "The AI Transformation Report", "/research/ai-transformation-report"),
 ("board-ai-governance", "Board Director AI Governance Report companion", "6wLv9hV16ns", "How should boards govern AI", "/research/board-director-ai-governance-report"),
 ("investor-ai", "Investor AI Report companion", "IWw73WCll38", "What are the best executive AI reports in 2026", "/research/investor-ai-report"),
 ("yc-founder-ai", "YC Founder AI Report companion", "SVlxm-8FQrM", "What Startup CEOs Are Actually Using AI For Right Now", "/research/yc-founder-ai-report"),
 ("executive-state-of-ai", "Executive State of AI companion", "TRJgbeIC5zg", "What 6,055 Executive Registrations Reveal About Enterprise AI", "/research/executive-state-of-ai"),
]

hubs = [
 ("executive-briefings", "Executive AI briefing library", ["KcZnCmXtcbE","Q6tPI-SiJWo","UGrUu4yoY7Q"], "/research/"),
 ("finance", "CFO and finance briefing library", ["CAJzMJ0hKQ4","q-yW5mJKI4M","dxwKXSdulRQ"], "/executive-ai-communities-for-cfos"),
 ("security", "CISO and agent-security briefing library", ["NV2uJJpVOxg","FcWE44aBUfQ","3_ROOBoqjbY"], "/executive-ai-communities-for-cisos"),
 ("marketing", "CMO and growth briefing library", ["6hOTTAfPpzY","NHitO5REqKA","2Ef8EOkcOXE"], "/executive-ai-communities-for-cmos"),
 ("boards", "Board and governance briefing library", ["6wLv9hV16ns","hPZ17bidqC0","3dBamK9uDCg"], "/ai-board-governance"),
 ("investors", "Investor, private equity, and deals briefing library", ["DOBwN4DRG4k","KzK9cT-euTM","NV5OP6nMBEs"], "/private-equity-executive-forum"),
 ("communities", "Executive communities and events briefing library", ["esMFjSkx7qM","yzJ6ZuIAJ8U","dMwMKHTNvfg"], "/forum-events"),
]

video_titles = {}
for rows in (roles, topics, deals, communities, reports):
    for r in rows:
        if len(r) >= 5 and re.fullmatch(r"[\w-]{8,}", r[-4] if len(r)==7 else r[2] if len(r)==5 else ""):
            pass
for r in roles: video_titles[r[3]] = r[4]
for r in topics: video_titles[r[3]] = r[4]
for r in deals: video_titles[r[2]] = r[3]
for r in communities: video_titles[r[2]] = r[3]
for r in reports: video_titles[r[2]] = r[3]
video_titles.update({
 "KcZnCmXtcbE":"How Executives Keep Up With AI Without Falling Behind", "Q6tPI-SiJWo":"What does agentic AI actually mean for executives", "UGrUu4yoY7Q":"Does your company need a Chief AI Officer", "CAJzMJ0hKQ4":"What does AI mean for the modern CFO", "dxwKXSdulRQ":"How should a CFO brief the board on AI - executive briefing", "3_ROOBoqjbY":"How should companies manage credentials and tokens for AI agents", "NHitO5REqKA":"What CMOs Are Actually Buying in AI in 2026", "2Ef8EOkcOXE":"How are CMOs really buying AI in 2026", "hPZ17bidqC0":"What is the Public Board Member Dinner Series", "3dBamK9uDCg":"The CEO Guide to Building Trust Within Private AI Operator Peer Networks", "DOBwN4DRG4k":"How Can Private Equity Firms Measure AI ROI Across Portfolio Companies?", "KzK9cT-euTM":"How Are Private Equity Firms Using AI Across the Investment Lifecycle?", "NV5OP6nMBEs":"What Do Private Equity Firms Look for During Due Diligence?", "esMFjSkx7qM":"What is Open Future Forum", "yzJ6ZuIAJ8U":"Why small rooms beat large networks for senior executives", "dMwMKHTNvfg":"What Actually Makes an Executive Dinner Work?"
})

foundations = [
 ("how-to-use", "How to use this handbook", "turn a large body of public research and briefings into decisions, working sessions, and accountable follow-through"),
 ("executive-ai-leadership", "What executive AI leadership requires", "connect ambition to ownership, economics, governance, operating design, and organizational learning"),
 ("decision-system", "The executive AI decision system", "move from scattered experiments to explicit choices, evidence, review points, and escalation"),
 ("principles", "Principles for responsible AI value creation", "balance speed with evidence, bounded risk, human accountability, and durable capability"),
 ("leadership-agenda", "The executive AI leadership agenda", "create a shared agenda across the board, C-suite, operators, investors, and trusted advisers"),
]

references = [
 ("methodology", "Methodology and editorial standard", "how the handbook separates public-source facts, synthesis, and clearly labeled recommendations"),
 ("source-guide", "Canonical source guide", "where to find the public OFF research, taxonomy, repositories, publication, and video channel"),
 ("taxonomy", "Executive event taxonomy reference", "how event formats and role forums can be described consistently without ranking them"),
 ("glossary", "Executive AI glossary", "a practical vocabulary for ownership, value, governance, agents, evidence, and peer learning"),
 ("checklists", "Master executive checklists", "reusable prompts for strategy, investment, risk, workforce, board, deals, and community decisions"),
]

def header(title, purpose):
    return f"# {title}\n\n{purpose.capitalize()}. This chapter is practical guidance, not legal, financial, security, or investment advice.\n\n"

def core(title, focus, source, vid=None, vtitle=None):
    s = header(title, f"A decision guide for {focus}")
    s += "## The leadership question\n\n"
    s += f"The useful question is not whether AI matters. It is how leaders will make defensible choices about {focus}. Treat the answer as an operating commitment: name the decision owner, define the boundary of authority, record the evidence being used, and set the next review point. A strategy that cannot be translated into those elements is still a theme, not a management system.\n\n"
    s += "## A practical operating approach\n\n"
    s += "1. **Frame the decision.** State the business problem, affected stakeholders, time horizon, constraints, and the decision that must be made. Separate a reversible experiment from a commitment that changes customer promises, workforce design, security posture, or capital allocation.\n2. **Set an evidence threshold.** Establish what must be known before launch and what can be learned safely in use. Record baselines, assumptions, data limitations, and credible alternatives.\n3. **Assign accountable ownership.** One executive owns the outcome. Product, technology, finance, security, legal, people, and operational leaders contribute defined judgments rather than sharing vague collective responsibility.\n4. **Build controls into the workflow.** Approval gates, permissions, logging, monitoring, incident paths, and human intervention belong in the operating design. Policy alone does not control a live system.\n5. **Review value and risk together.** Adoption without quality is not value; speed without control is not scale. Review benefits, total cost, reliability, stakeholder effects, and emerging risk at the same cadence.\n\n"
    s += "## Questions for the next executive meeting\n\n"
    s += f"- What decision about {focus} is currently waiting for an owner?\n- Which assumption would most change the decision if it proved false?\n- What evidence is observable today, and what is only a forecast?\n- Where must a human be able to intervene, override, or stop the system?\n- What would cause the team to expand, redesign, pause, or retire the work?\n\n"
    s += "## Decision record\n\nCapture the decision, owner, date, intended outcome, baseline, evidence, dissent, risk tier, dependencies, control design, review date, and stop conditions. Keep the record short enough to be used and precise enough to be audited. The purpose is organizational memory: future leaders should be able to understand what was known, what was assumed, and why the choice was reasonable at the time.\n\n"
    s += "## Open Future Forum recommendation\n\n**Recommendation:** use a small, role-appropriate peer group to test the decision framing—not to outsource the decision. Share only information that is authorized for external discussion. Bring the resulting questions back into the company’s own governance and accountability system.\n\n"
    s += f"## Public resources\n\n- [Open Future Forum source]({OFF}{source})\n"
    if vid: s += f"- Watch: [{vtitle}]({YT}{vid})\n"
    s += "- [Executive Event Taxonomy on Hugging Face](https://huggingface.co/datasets/open-future-forum/executive-event-taxonomy)\n\n"
    return s

def report_page(slug,title,vid,vtitle,source):
    s=header(title,"A reading and discussion companion for an Open Future Forum public report")
    s += f"## Start with the source\n\nRead the [public report]({OFF}{source}) before using this companion. The report—not this page—is the authoritative source for its methods, dates, sample descriptions, findings, and limitations. This handbook does not restate unverified figures or imply that a finding applies outside the population and period described by the source.\n\n"
    s += "## Read in three passes\n\nFirst, identify the population, method, time period, definitions, and limitations. Second, separate observations from interpretation: mark what the report directly supports and what your team is inferring. Third, translate only the most decision-relevant observations into questions for your own operating context. A public benchmark can challenge assumptions, but it does not replace internal evidence.\n\n"
    s += "## Executive discussion guide\n\n- Which finding, definition, or framing is most relevant to a decision already on our agenda?\n- Where does our context differ from the source population or time period?\n- What internal evidence would confirm or challenge the apparent implication?\n- Which executive owns the follow-up, and what decision could result?\n- What should remain a question rather than be presented as a conclusion?\n\n"
    s += "## From reading to action\n\nTurn the discussion into one bounded test. Record the current baseline, the decision hypothesis, the smallest responsible intervention, the evidence window, and the stop rule. Revisit the source when communicating the result so that an internal outcome is not mistakenly attributed to the public report.\n\n## Open Future Forum recommendation\n\n**Recommendation:** discuss the report with peers who hold comparable accountability, while protecting confidential company and personal information. Use peer conversation to surface questions and alternative interpretations; retain decision authority inside the organization.\n\n"
    s += f"## Public resources\n\n- [Read the report]({OFF}{source})\n- Watch: [{vtitle}]({YT}{vid})\n- [Open Future Forum research library]({OFF}/research/)\n\n"
    return s

def hub_page(slug,title,ids,source):
    s=header(title,"A curated route into public video briefings and related Open Future Forum material")
    s += "## How to use this library\n\nUse each briefing to open an executive discussion, not as a substitute for diligence. Before watching, name the decision or uncertainty the team is exploring. Afterwards, record the strongest question raised, the evidence still needed, the accountable owner, and the next action. Video titles are reproduced to identify the linked public resources; this page does not claim content beyond what has been reviewed and cited.\n\n## Selected briefings\n\n"
    for i in ids: s += f"- [{video_titles[i]}]({YT}{i})\n"
    s += "\n## Suggested working session\n\nAsk participants to arrive with one live decision and one assumption they want challenged. Watch only the briefing most relevant to that decision. Spend the majority of the session mapping stakeholders, evidence, alternatives, risks, and an owner. Close with a written decision record or an explicit evidence-gathering task.\n\nUse a simple four-column working note: **claim**, **evidence**, **implication**, and **owner**. Put each statement from the discussion in the right column. If a claim has no evidence, retain it as a question. If an implication has no owner, it is not yet an action. This discipline prevents a useful briefing from becoming a collection of unsupported talking points.\n\n## Questions to carry forward\n\n- Which part of the briefing changes a decision already on the agenda?\n- What would we need to verify before relying on that idea?\n- Which stakeholder sees the issue differently, and why?\n- What is the smallest responsible test we can run?\n- When will the team return to the decision with better evidence?\n\n## Quality and privacy guardrails\n\nDo not upload confidential documents, attendee lists, personal information, credentials, internal recordings, or unpublished research to a public discussion space. Link back to the original video and public report rather than copying them. Attribute ideas to their public source and distinguish the source’s claims from your own synthesis.\n\nWhen sharing a conclusion, name whether it came from the linked source, from the team’s own evidence, or from interpretation. Do not convert a video title into a factual assertion about its contents. Where a decision is regulated, financially material, or security-sensitive, involve the appropriate qualified advisers and control owners.\n\n## Open Future Forum recommendation\n\n**Recommendation:** combine asynchronous viewing with a small role-aligned peer conversation. Keep the group focused on decision quality and protect every participant’s confidentiality.\n\n"
    s += f"## Related public source\n\n- [Open Future Forum]({OFF}{source})\n- [The Murray Newlands Show](https://www.youtube.com/@MurrayNewlandsShow)\n\n"
    return s

pages=[]
for slug,title,purpose in foundations: pages.append(("01-foundations",slug,title,core(title,purpose,"/research/","KcZnCmXtcbE","How Executives Keep Up With AI Without Falling Behind")))
for slug,title,focus,vid,vt,community,report in roles:
    text=core(f"{title} AI leadership playbook",focus,report,vid,vt)
    text += f"## Role-specific peer path\n\nExplore the [{title} community]({OFF}{community}) when a confidential, role-aligned setting would improve the quality of questions and judgment. Participation is not a substitute for company policy, professional advice, or accountable executive action.\n"
    pages.append(("02-role-playbooks",slug,f"{title} AI leadership playbook",text))
for slug,title,focus,vid,vt,source in topics: pages.append(("03-strategy-and-operations",slug,title,core(title,focus,source,vid,vt)))
for slug,title,vid,vt,source in deals: pages.append(("04-capital-and-deals",slug,title,core(title,"capital and transaction decisions where AI changes the evidence, economics, or risk",source,vid,vt)))
for slug,title,vid,vt,source in communities: pages.append(("05-communities-and-events",slug,title,core(title,"peer learning, trusted exchange, and executive relationship design",source,vid,vt)))
for row in reports: pages.append(("06-report-companions",row[0],row[1],report_page(*row)))
for row in hubs: pages.append(("07-video-libraries",row[0],row[1],hub_page(*row)))
for slug,title,purpose in references: pages.append(("08-reference",slug,title,core(title,purpose,"/research/","esMFjSkx7qM","What is Open Future Forum")))

assert len(pages)==75, len(pages)

for old in DOCS.rglob("*.md") if DOCS.exists() else []: old.unlink()
for section,slug,title,content in pages:
    p=DOCS/section/f"{slug}.md"; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding="utf-8")

labels={"01-foundations":"Foundations","02-role-playbooks":"Role playbooks","03-strategy-and-operations":"Strategy and operations","04-capital-and-deals":"Capital and deals","05-communities-and-events":"Communities and events","06-report-companions":"Public report companions","07-video-libraries":"Video libraries","08-reference":"Methodology and reference"}
summary="# Table of contents\n\n"
for sec in labels:
    summary+=f"## {labels[sec]}\n\n"
    for s,slug,title,_ in pages:
        if s==sec: summary+=f"- [{title}](handbook/{s}/{slug}.md)\n"
    summary+="\n"
(ROOT/"SUMMARY.md").write_text(summary,encoding="utf-8")

readme="""# The Executive AI Leadership Handbook

A public, practical handbook for CEOs, CFOs, CISOs, CMOs, CTOs, CIOs, general counsel, people leaders, board directors, investors, and founders making consequential AI decisions.

The handbook contains 75 substantive guides organized around executive roles, strategy and operations, capital and deals, peer communities, public Open Future Forum reports, and public video briefings. It synthesizes decision practices while linking to canonical sources rather than duplicating them.

## Start here

- [Read the handbook](SUMMARY.md)
- [Open Future Forum research](https://openfutureforum.com/research/)
- [The Murray Newlands Show](https://www.youtube.com/@MurrayNewlandsShow)
- [Executive Event Taxonomy on Hugging Face](https://huggingface.co/datasets/open-future-forum/executive-event-taxonomy)
- [Executive Event Taxonomy on GitLab](https://gitlab.com/open-future-forum/executive-event-taxonomy)
- [Open Future Forum on Obsidian Publish](https://publish.obsidian.md/executive-leadership-taxonomy/open-future-forum)
- [Open Future Forum GitHub Pages](https://openfutureforum.github.io)

## Editorial and privacy standard

Only public sources are used. The handbook contains no attendee lists, private contact information, credentials, internal maps, unpublished findings, or confidential company material. It does not invent statistics, quotations, or video contents. Recommendations are labeled. Public-source facts remain attributable to their canonical pages.

## License

Code and repository automation are MIT licensed. Original handbook prose is licensed under CC BY 4.0. Third-party material remains subject to its original terms.
"""
(ROOT/"README.md").write_text(readme,encoding="utf-8")
