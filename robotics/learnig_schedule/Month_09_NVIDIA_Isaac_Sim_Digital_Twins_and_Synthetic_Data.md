# Robotics & Physical AI — Month 09: NVIDIA Isaac Sim, Digital Twins and Synthetic Data

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
By the end of Month 9, you should be able to explain, implement and defend the following: 
- Primary focus: **NVIDIA Isaac Sim, Digital Twins and Synthetic Data**.
- Explain the underlying theory and mathematical assumptions, not just API usage.
- Implement the core algorithm or software pattern in a version-controlled repository.
- Integrate the topic into a ROS 2 node/interface or a well-defined ROS 2-facing adapter.
- Reproduce the result in simulation and evaluate it with metrics.
- Describe one industry use case, one failure mode and one safety/reliability measure.
- Planned effort: **4 weeks × 13–17.5 h = 52–70 hours**.

## Prerequisite and setup checklist
- [ ] Ubuntu/Linux development environment is documented; use a version-compatible ROS 2 distribution and simulator pairing.
- [ ] Python virtual environment and dependency lock/requirements are committed.
- [ ] Git repository created with README, license decision, .gitignore, tests and issue tracker.
- [ ] Use a single chosen ROS 2 distribution for the main workspace. Confirm package compatibility before adding simulators or GPU tools.
- [ ] Safety rule: learned/high-level outputs must never directly drive physical actuators without a deterministic validation, limits, watchdog and emergency-stop layer.

## Core theory explained through worked examples

- **Digital twin calibration:** Compare simulated joint motion and sensor output with a reference. Track error, timing and physical assumptions; do not claim fidelity without measured evidence.
- **Synthetic dataset:** Randomize pose, lighting, textures and camera; split by scene/condition to avoid near-duplicate leakage.
- **SIL/HIL:** Draw sensor→ROS 2→controller→actuator loop and mark which components are virtual and physical. Identify timing hazards.

## Weekly training blocks
## Week 36 — Isaac Sim foundations and USD scene graph
**Expected outcome:** Navigate the simulator and construct a valid scene.
**Theory syllabus:** USD stages/prims; assets; physics scenes; articulations; materials; sensors; timeline.
**Mathematical foundation:** Derive the equations relevant to Isaac Sim foundations and USD scene graph; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Create a scene with floor, robot, objects and sensor; script a scene setup where possible.
**ROS 2 implementation:** Launch Isaac Sim with its supported ROS 2 bridge setup; inspect topic exchange.
**Simulation exercise:** Import a supported robot asset and validate articulation behavior.
**Practical assignment:** Deliver a scene file, version notes and reproducible launch steps.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Isaac Sim foundations and USD scene graph**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: USD stages/prims.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Isaac Sim foundations and USD scene graph; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Create a scene with floor, robot, objects and sensor; script a scene setup where possible.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Launch Isaac Sim with its supported ROS 2 bridge setup; inspect topic exchange.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Import a supported robot asset and validate articulation behavior.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Deliver a scene file, version notes and reproducible launch steps.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [NVIDIA Isaac Sim documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/)
- [Isaac Sim ROS 2 tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html)
- [NVIDIA synthetic data generation documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html)
- [NVIDIA Isaac Sim getting started learning path](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/index.html)
- [YouTube — Isaac Sim digital twin and Replicator](https://www.youtube.com/results?search_query=NVIDIA+Isaac+Sim+Replicator+synthetic+data+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Isaac Sim foundations and USD scene graph** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Isaac Sim foundations and USD scene graph; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Isaac Sim foundations and USD scene graph** to a robotics engineer who has not used this technique.
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

## Week 37 — Robot assets, physics and sensor realism
**Expected outcome:** Build a digital twin that is useful for testing.
**Theory syllabus:** mass/inertia; collision meshes; joints; friction; contact; motor limits; sensor noise; rate.
**Mathematical foundation:** Derive the equations relevant to Robot assets, physics and sensor realism; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Compare nominal vs perturbed mass/friction; document calibration parameters.
**ROS 2 implementation:** Publish joint states, TF, camera, IMU or LiDAR to ROS 2 as supported.
**Simulation exercise:** Compare simulated sensor outputs against expected geometry and rates.
**Practical assignment:** Create a digital-twin validation table with model assumptions and known gaps.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Robot assets, physics and sensor realism**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: mass/inertia.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Robot assets, physics and sensor realism; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Compare nominal vs perturbed mass/friction; document calibration parameters.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Publish joint states, TF, camera, IMU or LiDAR to ROS 2 as supported.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Compare simulated sensor outputs against expected geometry and rates.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Create a digital-twin validation table with model assumptions and known gaps.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [NVIDIA Isaac Sim documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/)
- [Isaac Sim ROS 2 tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html)
- [NVIDIA synthetic data generation documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html)
- [NVIDIA Isaac Sim getting started learning path](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/index.html)
- [YouTube — Isaac Sim digital twin and Replicator](https://www.youtube.com/results?search_query=NVIDIA+Isaac+Sim+Replicator+synthetic+data+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Robot assets, physics and sensor realism** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Robot assets, physics and sensor realism; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Robot assets, physics and sensor realism** to a robotics engineer who has not used this technique.
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

## Week 38 — Synthetic data and Replicator
**Expected outcome:** Generate labeled training data with controlled variation.
**Theory syllabus:** domain randomization; semantic/instance segmentation; bounding boxes; depth; annotations; dataset versioning.
**Mathematical foundation:** Derive the equations relevant to Synthetic data and Replicator; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Generate a small labeled dataset; validate annotation schema and class balance.
**ROS 2 implementation:** Publish generated images or metadata to a ROS 2 test consumer if applicable.
**Simulation exercise:** Create randomized lighting, pose, material and camera configurations.
**Practical assignment:** Train/evaluate a detector on synthetic data and test on a separate real/sim-real set.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Synthetic data and Replicator**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: domain randomization.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Synthetic data and Replicator; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Generate a small labeled dataset; validate annotation schema and class balance.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Publish generated images or metadata to a ROS 2 test consumer if applicable.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Create randomized lighting, pose, material and camera configurations.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Train/evaluate a detector on synthetic data and test on a separate real/sim-real set.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [NVIDIA Isaac Sim documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/)
- [Isaac Sim ROS 2 tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html)
- [NVIDIA synthetic data generation documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html)
- [NVIDIA Isaac Sim getting started learning path](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/index.html)
- [YouTube — Isaac Sim digital twin and Replicator](https://www.youtube.com/results?search_query=NVIDIA+Isaac+Sim+Replicator+synthetic+data+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Synthetic data and Replicator** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Synthetic data and Replicator; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Synthetic data and Replicator** to a robotics engineer who has not used this technique.
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

## Week 39 — SIL/HIL, scenario testing and digital twin evaluation
**Expected outcome:** Use the twin as a test bench, not just a visualization.
**Theory syllabus:** software-in-loop; hardware-in-loop; scenario coverage; deterministic replay; sensor timing; fault injection.
**Mathematical foundation:** Derive the equations relevant to SIL/HIL, scenario testing and digital twin evaluation; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Write automated scenarios and compare outcomes across simulator runs.
**ROS 2 implementation:** Connect ROS nodes to Isaac Sim via ROS 2 bridge and record bags.
**Simulation exercise:** Run nominal, edge and fault-injection scenarios.
**Practical assignment:** Deliver a scenario test suite with pass/fail criteria and known fidelity limitations.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **SIL/HIL, scenario testing and digital twin evaluation**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: software-in-loop.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to SIL/HIL, scenario testing and digital twin evaluation; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Write automated scenarios and compare outcomes across simulator runs.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Connect ROS nodes to Isaac Sim via ROS 2 bridge and record bags.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run nominal, edge and fault-injection scenarios.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Deliver a scenario test suite with pass/fail criteria and known fidelity limitations.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [NVIDIA Isaac Sim documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/)
- [Isaac Sim ROS 2 tutorials](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/index.html)
- [NVIDIA synthetic data generation documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html)
- [NVIDIA Isaac Sim getting started learning path](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/index.html)
- [YouTube — Isaac Sim digital twin and Replicator](https://www.youtube.com/results?search_query=NVIDIA+Isaac+Sim+Replicator+synthetic+data+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **SIL/HIL, scenario testing and digital twin evaluation** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to SIL/HIL, scenario testing and digital twin evaluation; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **SIL/HIL, scenario testing and digital twin evaluation** to a robotics engineer who has not used this technique.
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
**Project name:** Isaac Sim digital twin and synthetic-data pipeline**
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

1. Explain USD stages, prims and the scene graph in Isaac Sim.
2. Describe how mass, inertia, friction and collision geometry affect simulation fidelity.
3. Design a calibration experiment for one simulated joint and one sensor.
4. Explain how camera, IMU and LiDAR rates and noise affect robot behavior.
5. Design a synthetic-data randomization matrix and label schema.
6. Explain why train/validation splits should be separated by scenes or conditions.
7. Compare software-in-the-loop and hardware-in-the-loop testing.
8. Design a scenario suite with nominal, boundary and fault-injection cases.

### Month-specific interview questions

1. What is a digital twin, and what evidence is required to claim fidelity?
2. How do visual meshes differ from collision meshes?
3. What causes a simulated joint to move differently from hardware?
4. What is domain randomization in synthetic data generation?
5. How do you validate labels generated by a simulator?
6. What is the difference between SIL and HIL?
7. How do deterministic replay and fixed seeds improve debugging?
8. How would you report known limitations of a digital twin to a customer?

## Month-end interview question bank
1. Explain **NVIDIA Isaac Sim, Digital Twins and Synthetic Data** as though you are in a technical interview.
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
| 36 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 37 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 38 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 39 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

**Month total:** Planned ___ / 76 hours | Actual ___ hours | Month score ___ / 100 | Decision: Pass / Conditional / Repeat

## Notes to capture this month
For every training day, use the matching template in `../Robotics_Physical_AI_Learner_Notebook.md`. Do not rely on memory: capture equations, units, assumptions, code experiments, ROS graph, simulator configuration, screenshots/links, bugs and corrections.

### Month-end reflection
- What can I now explain without notes?
- What can I implement from a blank file?
- Which result did I validate against a known answer or baseline?
- Which three mistakes taught me the most?
- What remains weak, and what exact exercise will close the gap?
- What evidence should a hiring manager inspect first?
