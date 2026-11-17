# Robotics & Physical AI — Month 12: Agentic Robotics, MCP, Task Planning and Capstone Integration

**Course length:** 12-month programme, 52 weeks; 676–910 planned study hours at 13–17.5 hours/week  
**Learner profile:** 10+ years embedded software engineering; STM32/ESP32, RTOS, C/C++, Python, CAN/serial; current GenAI/LLM/RAG/MCP exposure  
**Primary method:** derive → implement → test → simulate → integrate → explain  
**Month gate:** earn at least 70/100 and complete all mandatory practical evidence before moving on. A score below 70 means targeted remediation, not simply re-reading.

**Official program start:** Sunday, 2026-11-15 (Asia/Kolkata). Complete the Month 1 kickoff and baseline on that Sunday; start its Week 01 Monday task on 2026-11-16. Follow the month files in sequence and use the progress tracker to identify the current month and week.

## How to use this file
1. Read the monthly outcomes and establish a baseline.
2. Work through every weekly plan and daily task. Commit code in small increments.
3. On Sunday, take the written exam without notes, answer interview prompts aloud, and update the learning notebook.
4. At month end, submit the project, exam, evidence and self-review for mentor review.

## Study-time contract (13–17.5 hours/week)
- Monday–Friday: 1–1.5 hours/day (5–7.5 hours total).
- Saturday: 4–5 hours (deep lab/integration block).
- Sunday: 4–5 hours (review, written test, interview practice and notes).
- Each weekday block: 15–20 min reading, 10–15 min derivation/notes, 35–60 min coding or lab, and 5 min log/commit; choose the shorter version on a 1-hour day.
- Saturday: 30 min planning, 2.5–3.5 hours building/testing, 45–60 min debugging, and 15–30 min demo/log.
- Sunday: 45–60 min written check, 20–30 min interview practice, 60–90 min revision, and 30–45 min weekly report/next-week plan; use remaining time for the assigned practical.

If a workday is missed, do not silently compress the learning objectives. Move the missed lab into the next Saturday buffer and record the slip in the progress log.

## Monthly outcomes
By the end of Month 12, you should be able to explain, implement and defend the following: 
- Primary focus: **Agentic Robotics, MCP, Task Planning and Capstone Integration**.
- Explain the underlying theory and mathematical assumptions, not just API usage.
- Implement the core algorithm or software pattern in a version-controlled repository.
- Integrate the topic into a ROS 2 node/interface or a well-defined ROS 2-facing adapter.
- Reproduce the result in simulation and evaluate it with metrics.
- Describe one industry use case, one failure mode and one safety/reliability measure.
- Planned effort: **5 weeks × 13–17.5 h = 65–87.5 hours**.

## Prerequisite and setup checklist
- [ ] Ubuntu/Linux development environment is documented; use a version-compatible ROS 2 distribution and simulator pairing.
- [ ] Python virtual environment and dependency lock/requirements are committed.
- [ ] Git repository created with README, license decision, .gitignore, tests and issue tracker.
- [ ] Use a single chosen ROS 2 distribution for the main workspace. Confirm package compatibility before adding simulators or GPU tools.
- [ ] Safety rule: learned/high-level outputs must never directly drive physical actuators without a deterministic validation, limits, watchdog and emergency-stop layer.

## Core theory explained through worked examples

- **Task planning:** Convert “bring me the red mug” into locate→navigate→detect→grasp→navigate→place. Define preconditions, postconditions and failure recovery.
- **MCP boundary:** Treat a language model as an untrusted planner. Validate tool schema, authorization, arguments, state and safety constraints before invoking a robot skill.
- **Multi-agent coordination:** Define ownership, shared-state versioning, deadlock timeout, cancellation and human escalation for two agents competing for one robot.

## Weekly training blocks
## Week 48 — Task planning and hierarchical robot architectures
**Expected outcome:** Translate human intent into explicit, verifiable robot skills.
**Theory syllabus:** task decomposition; symbolic state; pre/postconditions; BTs; planners; skill libraries; grounding.
**Mathematical foundation:** Derive the equations relevant to Task planning and hierarchical robot architectures; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement a task planner that maps a command into a typed skill sequence with preconditions.
**ROS 2 implementation:** Create ROS 2 action servers for skills such as navigate, detect, grasp and place.
**Simulation exercise:** Simulate a multi-step mission with injected skill failures and recovery.
**Practical assignment:** Show plan trace, conditions and deterministic fallback for unsupported actions.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Task planning and hierarchical robot architectures**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: task decomposition.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Task planning and hierarchical robot architectures; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement a task planner that maps a command into a typed skill sequence with preconditions.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create ROS 2 action servers for skills such as navigate, detect, grasp and place.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Simulate a multi-step mission with injected skill failures and recovery.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Show plan trace, conditions and deterministic fallback for unsupported actions.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [ROS 2 actions and lifecycle design tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [BehaviorTree.CPP documentation](https://www.behaviortree.dev/)
- [Nav2 behavior tree documentation](https://docs.nav2.org/behavior_trees/index.html)
- [YouTube — MCP servers and agentic systems](https://www.youtube.com/results?search_query=Model+Context+Protocol+MCP+agents+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Task planning and hierarchical robot architectures** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Task planning and hierarchical robot architectures; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Task planning and hierarchical robot architectures** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Week 49 — MCP tools and robot capability exposure
**Expected outcome:** Expose robot status and bounded capabilities through MCP.
**Theory syllabus:** MCP hosts/clients/servers; tools/resources/prompts; schemas; auth; timeouts; audit; least privilege.
**Mathematical foundation:** Derive the equations relevant to MCP tools and robot capability exposure; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build a local MCP server exposing read-only robot status and a mock safe skill tool.
**ROS 2 implementation:** Connect MCP tool calls to ROS 2 actions through a strict adapter, not arbitrary topic publishing.
**Simulation exercise:** Run the workflow against a simulated robot and log every tool call.
**Practical assignment:** Demonstrate invalid arguments, timeout and denied unsafe command handling.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **MCP tools and robot capability exposure**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: MCP hosts/clients/servers.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to MCP tools and robot capability exposure; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build a local MCP server exposing read-only robot status and a mock safe skill tool.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Connect MCP tool calls to ROS 2 actions through a strict adapter, not arbitrary topic publishing.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run the workflow against a simulated robot and log every tool call.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Demonstrate invalid arguments, timeout and denied unsafe command handling.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [ROS 2 actions and lifecycle design tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [BehaviorTree.CPP documentation](https://www.behaviortree.dev/)
- [Nav2 behavior tree documentation](https://docs.nav2.org/behavior_trees/index.html)
- [YouTube — MCP servers and agentic systems](https://www.youtube.com/results?search_query=Model+Context+Protocol+MCP+agents+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **MCP tools and robot capability exposure** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to MCP tools and robot capability exposure; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **MCP tools and robot capability exposure** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Week 50 — Multi-agent coordination and mission execution
**Expected outcome:** Coordinate specialized agents without surrendering safety authority.
**Theory syllabus:** planner/executor/critic roles; shared state; message contracts; conflict resolution; deadlocks; human approval.
**Mathematical foundation:** Derive the equations relevant to Multi-agent coordination and mission execution; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement two or three agents or deterministic services with explicit message schemas and task ownership.
**ROS 2 implementation:** Connect agent outputs to ROS 2 actions with bounded interfaces and mission cancellation.
**Simulation exercise:** Run two simultaneous simulated tasks; test resource conflict and recovery.
**Practical assignment:** Measure task completion, conflicts, retries and operator interventions.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Multi-agent coordination and mission execution**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: planner/executor/critic roles.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Multi-agent coordination and mission execution; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement two or three agents or deterministic services with explicit message schemas and task ownership.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Connect agent outputs to ROS 2 actions with bounded interfaces and mission cancellation.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run two simultaneous simulated tasks; test resource conflict and recovery.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Measure task completion, conflicts, retries and operator interventions.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [ROS 2 actions and lifecycle design tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [BehaviorTree.CPP documentation](https://www.behaviortree.dev/)
- [Nav2 behavior tree documentation](https://docs.nav2.org/behavior_trees/index.html)
- [YouTube — MCP servers and agentic systems](https://www.youtube.com/results?search_query=Model+Context+Protocol+MCP+agents+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Multi-agent coordination and mission execution** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Multi-agent coordination and mission execution; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Multi-agent coordination and mission execution** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Week 51 — Capstone integration, verification and portfolio release
**Expected outcome:** Deliver a reliable end-to-end Physical AI robotics demonstration.
**Theory syllabus:** systems engineering; requirements traceability; verification; repeatability; safety case; documentation.
**Mathematical foundation:** Derive the equations relevant to Capstone integration, verification and portfolio release; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Stabilize code; add tests, CI, reproducible environment and metrics dashboard.
**ROS 2 implementation:** Integrate perception, navigation/manipulation, planner, skill actions and monitoring.
**Simulation exercise:** Run scripted evaluation set with nominal and edge cases; record demo video.
**Practical assignment:** Release tagged GitHub repo, architecture diagram, test report, demo video and retrospective.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Capstone integration, verification and portfolio release**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: systems engineering.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Capstone integration, verification and portfolio release; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Stabilize code; add tests, CI, reproducible environment and metrics dashboard.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Integrate perception, navigation/manipulation, planner, skill actions and monitoring.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run scripted evaluation set with nominal and edge cases; record demo video.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Release tagged GitHub repo, architecture diagram, test report, demo video and retrospective.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [ROS 2 actions and lifecycle design tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [BehaviorTree.CPP documentation](https://www.behaviortree.dev/)
- [Nav2 behavior tree documentation](https://docs.nav2.org/behavior_trees/index.html)
- [YouTube — MCP servers and agentic systems](https://www.youtube.com/results?search_query=Model+Context+Protocol+MCP+agents+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Capstone integration, verification and portfolio release** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Capstone integration, verification and portfolio release; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Capstone integration, verification and portfolio release** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Week 52 — Final assessment, interview defense and next-step plan
**Expected outcome:** Defend engineering decisions and identify gaps honestly.
**Theory syllabus:** trade-off analysis; reliability; uncertainty; sim-to-real; maintainability; ethical/safety considerations.
**Mathematical foundation:** Derive the equations relevant to Final assessment, interview defense and next-step plan; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Fix top-priority defects; prepare clean reproducer and code walkthrough.
**ROS 2 implementation:** Demonstrate lifecycle, actions, diagnostics, bag replay and safe shutdown.
**Simulation exercise:** Present the system and failure analysis to a reviewer.
**Practical assignment:** Complete final written exam, interview defense and evidence-based readiness score.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Final assessment, interview defense and next-step plan**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: trade-off analysis.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Final assessment, interview defense and next-step plan; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Fix top-priority defects; prepare clean reproducer and code walkthrough.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Demonstrate lifecycle, actions, diagnostics, bag replay and safe shutdown.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Present the system and failure analysis to a reviewer.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Complete final written exam, interview defense and evidence-based readiness score.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [ROS 2 actions and lifecycle design tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [BehaviorTree.CPP documentation](https://www.behaviortree.dev/)
- [Nav2 behavior tree documentation](https://docs.nav2.org/behavior_trees/index.html)
- [YouTube — MCP servers and agentic systems](https://www.youtube.com/results?search_query=Model+Context+Protocol+MCP+agents+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Final assessment, interview defense and next-step plan** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Final assessment, interview defense and next-step plan; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Final assessment, interview defense and next-step plan** to a robotics engineer who has not used this technique.
2. What assumptions are hidden in your implementation of this week’s exercise?
3. How would you test the solution on a robot rather than only in a notebook?
4. Describe one bug you encountered or anticipate. How would you isolate it?
5. What metric would you use to decide whether your result is good enough?
6. How does this concept connect to your embedded background (timing, sensors, RTOS, interfaces, safety or fault handling)?

### Weekly pass criteria
- [ ] Written exam score ≥ 14/20 (70%).
- [ ] Coding artifact runs from a clean checkout and has at least 3 meaningful tests.
- [ ] ROS 2 or interface mock is demonstrated with evidence (terminal capture, bag, test or launch log).
- [ ] Simulation result is saved with configuration and at least one edge case.
- [ ] Interview answers are recorded; at least 4/6 are clear, technically correct and evidence-backed.
- [ ] Weekly notes and Git commit/pull request are complete.

### Weekly reviewer feedback
**Score:** ___ / 20 written | ___ / 10 practical | ___ / 10 explanation  
**Strongest evidence:**  
**Misconception / gap:**  
**Corrective assignment:**  
**Reviewer decision:** Pass / Revise / Re-test  

## Month-end practical project
**Project objective:** Build a portfolio-quality artifact that integrates the month’s central concepts and can be reproduced by another engineer.
**Project name:** Agentic mobile-manipulation mission system**
### Minimum acceptance criteria
- [ ] A clear problem statement, requirements and system/block diagram.
- [ ] A mathematical or algorithmic explanation with one worked example.
- [ ] Source code organized into modules; meaningful names, comments and tests.
- [ ] A reproducible setup, configuration and run command.
- [ ] Simulation or offline evaluation with a baseline and at least 3 metrics.
- [ ] Failure analysis: at least 3 failure modes and mitigations.
- [ ] Demo video or terminal walkthrough and 1–3 page engineering report.
- [ ] GitHub README, diagram, dependencies and known limitations.

## Month-end written examination (100 minutes; 40 points)
1. Explain the month’s central system/algorithm from first principles (8 points).
2. Solve a numerical or derivation problem from the worked examples (8 points).
3. Analyze a code/configuration snippet: identify the defect, edge case or performance issue (6 points).
4. Design a practical system block diagram with interfaces, data types, timing and error handling (6 points).
5. Analyze a failure scenario and propose a testable correction (6 points).
6. Write an engineering summary of your project results, including metrics and limitations (6 points).
**Pass:** 28/40 (70%), with no critical safety misconception.

### Month-specific written exam questions

1. Convert a natural-language command into a skill graph with preconditions and postconditions.
2. Compare behavior trees, finite-state machines and task planners for robot mission logic.
3. Describe MCP hosts, clients, servers, tools, resources and prompts.
4. Design a typed tool schema for a safe `navigate_to` or `grasp_object` capability.
5. Explain why an LLM should be treated as an untrusted planner.
6. Design multi-agent ownership and conflict resolution for two agents sharing one robot.
7. Describe timeout, cancellation, retry and human-approval behavior for a mission.
8. Present the capstone architecture and define measurable end-to-end success criteria.

### Month-specific interview questions

1. How do you ground an LLM-generated plan in actual robot capabilities?
2. When would you choose a behavior tree instead of an LLM-generated sequence?
3. What is the MCP tool boundary and how do you validate arguments?
4. How do you prevent arbitrary tool invocation from creating unsafe motion?
5. How should agents share world state without acting on stale information?
6. How do you handle resource contention and deadlocks?
7. What metrics demonstrate reliable task completion over a single demo?
8. Defend the capstone’s architecture, test coverage and safety case.

## Month-end interview question bank
1. Explain **Agentic Robotics, MCP, Task Planning and Capstone Integration** as though you are in a technical interview.
2. Which assumptions in your project are most likely to fail on a real robot?
3. Explain one equation/algorithm you used and derive it at a high level.
4. What measurements prove your implementation works? What would falsify your claim?
5. What is the most important trade-off you made and what alternative did you reject?
6. How do you handle invalid input, timeouts, stale data and component failure?
7. How would you make the system deterministic and reproducible enough for regression testing?
8. What would you change for a production deployment with safety and uptime requirements?
9. Explain one relevant research paper: problem, method, result, limitation and practical lesson.
10. What did you build independently, what did you adapt, and how can another engineer reproduce it?

## Evaluation rubric (100 points)
| Area | Points | Evidence required |
|---|---:|---|
| Theory and mathematical reasoning | 20 | Correct explanation, derivation, assumptions and units |
| Coding quality | 15 | Readable implementation, tests, reproducible environment |
| ROS 2/software integration | 15 | Correct interfaces, launch/config, timing and observability |
| Simulation / experiment quality | 15 | Repeatable trials, baseline and meaningful metrics |
| Practical project outcome | 15 | Functional demonstration and requirements traceability |
| Written exam | 10 | Clear, accurate, structured responses |
| Interview / communication | 5 | Concise explanation and sound trade-offs |
| Notes and engineering discipline | 5 | Complete lab logs, paper notes and weekly retrospective |

### Readiness interpretation
- **90–100: Strong:** can implement and defend the topic with minimal guidance.
- **80–89: Ready:** solid practical ability; a few gaps need targeted practice.
- **70–79: Conditional:** proceed with a remediation ticket and revisit weak concepts.
- **Below 70: Not ready:** repeat the weak week(s), re-test and do not hide gaps behind attendance.
- **Automatic review required:** unsafe actuator behavior, incorrect coordinate-frame assumptions, invalid evaluation methodology or inability to reproduce the result.

## Learning progress tracker
| Week | Planned hours | Actual hours | Written /20 | Practical /10 | Interview /10 | Evidence link | Status |
|---|---:|---:|---:|---:|---:|---|---|
| 48 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 49 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 50 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 51 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 52 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

**Month total:** Planned ___ / 95 hours | Actual ___ hours | Month score ___ / 100 | Decision: Pass / Conditional / Repeat

## Notes to capture this month
For every training day, use the matching template in `../Robotics_Physical_AI_Learner_Notebook.md`. Do not rely on memory: capture equations, units, assumptions, code experiments, ROS graph, simulator configuration, screenshots/links, bugs and corrections.

### Month-end reflection
- What can I now explain without notes?
- What can I implement from a blank file?
- Which result did I validate against a known answer or baseline?
- Which three mistakes taught me the most?
- What remains weak, and what exact exercise will close the gap?
- What evidence should a hiring manager inspect first?
