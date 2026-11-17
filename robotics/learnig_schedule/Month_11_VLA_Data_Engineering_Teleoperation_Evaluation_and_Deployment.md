# Robotics & Physical AI — Month 11: VLA Data Engineering, Teleoperation, Evaluation and Deployment

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
By the end of Month 11, you should be able to explain, implement and defend the following: 
- Primary focus: **VLA Data Engineering, Teleoperation, Evaluation and Deployment**.
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

- **Dataset integrity:** A trajectory contains RGB at 30 Hz, joint state at 100 Hz and command at 20 Hz. Explain timestamp alignment, interpolation and missing-data handling.
- **Closed-loop policy:** A VLA predicts a chunk of actions. Explain when to re-observe, how to abort and why open-loop execution can be unsafe.
- **Humanoid balance:** Explain support polygon and centre-of-mass projection; discuss why contact changes make whole-body control challenging.

## Weekly training blocks
## Week 44 — Robot datasets and demonstration collection
**Expected outcome:** Design high-quality, traceable robot datasets.
**Theory syllabus:** episode schema; timestamps; camera calibration; proprioception; action labels; data quality; split leakage.
**Mathematical foundation:** Derive the equations relevant to Robot datasets and demonstration collection; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Create an episode schema; record 20–50 short scripted/teleop episodes or use a public dataset subset.
**ROS 2 implementation:** Record synchronized RGB, joint state and action data; maintain calibration and frame metadata.
**Simulation exercise:** Replay and inspect episodes; identify dropped frames and timestamp drift.
**Practical assignment:** Produce dataset card with collection protocol and known biases.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Robot datasets and demonstration collection**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: episode schema.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Robot datasets and demonstration collection; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Create an episode schema; record 20–50 short scripted/teleop episodes or use a public dataset subset.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Record synchronized RGB, joint state and action data; maintain calibration and frame metadata.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Replay and inspect episodes; identify dropped frames and timestamp drift.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Produce dataset card with collection protocol and known biases.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenVLA project and implementation](https://github.com/openvla/openvla)
- [OpenVLA paper](https://arxiv.org/abs/2406.09246)
- [RT-1: Robotics Transformer for real-world control at scale](https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/)
- [RT-2 paper](https://arxiv.org/abs/2307.15818)
- [NVIDIA GR00T developer resources](https://developer.nvidia.com/isaac/gr00t)
- [NVIDIA GR00T technical blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
- [YouTube — vision-language-action models for robotics](https://www.youtube.com/results?search_query=vision+language+action+models+robotics+OpenVLA+RT2+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Robot datasets and demonstration collection** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Robot datasets and demonstration collection; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Robot datasets and demonstration collection** to a robotics engineer who has not used this technique.
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

## Week 45 — Behavior cloning and VLA fine-tuning concepts
**Expected outcome:** Understand fine-tuning, action heads and evaluation discipline.
**Theory syllabus:** supervised fine-tuning; LoRA; action normalization; sequence chunking; overfitting; validation.
**Mathematical foundation:** Derive the equations relevant to Behavior cloning and VLA fine-tuning concepts; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Train a small behavior-cloning baseline or follow supported OpenVLA LoRA workflow if compute/data allow.
**ROS 2 implementation:** Serve predictions through a simulation-only action gateway.
**Simulation exercise:** Evaluate unseen object positions, camera changes and paraphrased instructions.
**Practical assignment:** Report success rate, inference latency and per-condition results.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Behavior cloning and VLA fine-tuning concepts**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: supervised fine-tuning.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Behavior cloning and VLA fine-tuning concepts; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Train a small behavior-cloning baseline or follow supported OpenVLA LoRA workflow if compute/data allow.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Serve predictions through a simulation-only action gateway.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Evaluate unseen object positions, camera changes and paraphrased instructions.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Report success rate, inference latency and per-condition results.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenVLA project and implementation](https://github.com/openvla/openvla)
- [OpenVLA paper](https://arxiv.org/abs/2406.09246)
- [RT-1: Robotics Transformer for real-world control at scale](https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/)
- [RT-2 paper](https://arxiv.org/abs/2307.15818)
- [NVIDIA GR00T developer resources](https://developer.nvidia.com/isaac/gr00t)
- [NVIDIA GR00T technical blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
- [YouTube — vision-language-action models for robotics](https://www.youtube.com/results?search_query=vision+language+action+models+robotics+OpenVLA+RT2+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Behavior cloning and VLA fine-tuning concepts** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Behavior cloning and VLA fine-tuning concepts; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Behavior cloning and VLA fine-tuning concepts** to a robotics engineer who has not used this technique.
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

## Week 46 — Closed-loop deployment, monitoring and fail-safe behavior
**Expected outcome:** Integrate a learned policy with deterministic safety and control.
**Theory syllabus:** open-loop vs closed-loop; receding horizon; confidence; drift; out-of-distribution; watchdog; rollback.
**Mathematical foundation:** Derive the equations relevant to Closed-loop deployment, monitoring and fail-safe behavior; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement policy wrapper with schema validation, action clamp, rate limiter and logging.
**ROS 2 implementation:** Create lifecycle-controlled perception/policy/execution nodes and emergency stop handling.
**Simulation exercise:** Inject timeout, invalid action, perception drop and obstacle conditions.
**Practical assignment:** Pass failure-injection tests with no unbounded motion.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Closed-loop deployment, monitoring and fail-safe behavior**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: open-loop vs closed-loop.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Closed-loop deployment, monitoring and fail-safe behavior; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement policy wrapper with schema validation, action clamp, rate limiter and logging.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create lifecycle-controlled perception/policy/execution nodes and emergency stop handling.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Inject timeout, invalid action, perception drop and obstacle conditions.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Pass failure-injection tests with no unbounded motion.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenVLA project and implementation](https://github.com/openvla/openvla)
- [OpenVLA paper](https://arxiv.org/abs/2406.09246)
- [RT-1: Robotics Transformer for real-world control at scale](https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/)
- [RT-2 paper](https://arxiv.org/abs/2307.15818)
- [NVIDIA GR00T developer resources](https://developer.nvidia.com/isaac/gr00t)
- [NVIDIA GR00T technical blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
- [YouTube — vision-language-action models for robotics](https://www.youtube.com/results?search_query=vision+language+action+models+robotics+OpenVLA+RT2+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Closed-loop deployment, monitoring and fail-safe behavior** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Closed-loop deployment, monitoring and fail-safe behavior; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Closed-loop deployment, monitoring and fail-safe behavior** to a robotics engineer who has not used this technique.
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

## Week 47 — Humanoid and whole-body robotics foundations
**Expected outcome:** Understand why humanoid control is harder than arm-only manipulation.
**Theory syllabus:** floating base; contact constraints; balance; ZMP/CMP intuition; whole-body control; gait; joint limits.
**Mathematical foundation:** Derive the equations relevant to Humanoid and whole-body robotics foundations; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Simulate inverted pendulum/ZMP toy model; inspect a public humanoid model and joint tree.
**ROS 2 implementation:** Inspect joint-state and TF conventions for a humanoid model in ROS 2.
**Simulation exercise:** Run a supported humanoid simulation example if GPU permits; otherwise use a reduced-order model.
**Practical assignment:** Write a technical note comparing mobile manipulator and humanoid control stacks.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Humanoid and whole-body robotics foundations**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: floating base.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Humanoid and whole-body robotics foundations; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Simulate inverted pendulum/ZMP toy model; inspect a public humanoid model and joint tree.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Inspect joint-state and TF conventions for a humanoid model in ROS 2.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run a supported humanoid simulation example if GPU permits; otherwise use a reduced-order model.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Write a technical note comparing mobile manipulator and humanoid control stacks.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenVLA project and implementation](https://github.com/openvla/openvla)
- [OpenVLA paper](https://arxiv.org/abs/2406.09246)
- [RT-1: Robotics Transformer for real-world control at scale](https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/)
- [RT-2 paper](https://arxiv.org/abs/2307.15818)
- [NVIDIA GR00T developer resources](https://developer.nvidia.com/isaac/gr00t)
- [NVIDIA GR00T technical blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
- [YouTube — vision-language-action models for robotics](https://www.youtube.com/results?search_query=vision+language+action+models+robotics+OpenVLA+RT2+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Humanoid and whole-body robotics foundations** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Humanoid and whole-body robotics foundations; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Humanoid and whole-body robotics foundations** to a robotics engineer who has not used this technique.
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
**Project name:** Demonstration dataset and guarded learned-policy gateway**
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

1. Design an episode schema for RGB, depth, proprioception, instructions and actions.
2. Explain timestamp synchronization for streams sampled at 30, 100 and 20 Hz.
3. Describe dataset leakage and a correct group-wise split.
4. Explain teleoperation quality controls and how inconsistent demonstrations harm learning.
5. Compare behavior cloning, LoRA fine-tuning and full fine-tuning.
6. Explain action chunking and the trade-off between inference frequency and feedback.
7. Design a guarded policy gateway with timeout, rate limit, bounds and fallback.
8. Explain humanoid balance using support polygon and centre-of-mass concepts.

### Month-specific interview questions

1. What metadata must accompany a robot trajectory to make it reusable?
2. How do you detect dropped frames or clock drift?
3. Why is random frame-level train/test splitting often invalid for robot episodes?
4. How would you design a teleoperation collection protocol?
5. What does LoRA change and what does it leave frozen?
6. How do you choose when to re-observe after a chunked action prediction?
7. What should happen when a learned policy returns NaN or an out-of-range action?
8. Why is humanoid whole-body control more complex than fixed-base arm control?

## Month-end interview question bank
1. Explain **VLA Data Engineering, Teleoperation, Evaluation and Deployment** as though you are in a technical interview.
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
| 44 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 45 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 46 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 47 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
