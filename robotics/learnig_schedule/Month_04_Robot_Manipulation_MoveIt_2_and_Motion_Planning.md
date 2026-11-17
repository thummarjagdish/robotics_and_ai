# Robotics & Physical AI — Month 04: Robot Manipulation, MoveIt 2 and Motion Planning

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
By the end of Month 4, you should be able to explain, implement and defend the following: 
- Primary focus: **Robot Manipulation, MoveIt 2 and Motion Planning**.
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

- **Collision-aware planning:** Plan a path for a 6-DoF arm from start to goal with an obstacle. Explain why a valid joint-space path may still fail when the obstacle geometry changes.
- **Trajectory example:** A joint moves 0→1 rad with max velocity 0.5 rad/s. Compute a lower bound on move time, then add acceleration constraints.
- **Pick-and-place:** Model approach, grasp, attach, lift, transfer, place, detach and retreat. Define preconditions and recovery at each stage.

## Weekly training blocks
## Week 14 — Manipulator planning pipeline
**Expected outcome:** Understand planning scene, robot model, kinematics plugins and planner pipeline.
**Theory syllabus:** configuration space; collision checking; sampling-based planning; OMPL; planning requests; constraints.
**Mathematical foundation:** Derive the equations relevant to Manipulator planning pipeline; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Configure MoveIt 2 for a supported arm; create a planning request client and log planner response.
**ROS 2 implementation:** Run MoveIt Setup Assistant and inspect planning group, end-effector and kinematics configuration.
**Simulation exercise:** Plan collision-free joint and pose goals in RViz/Gazebo.
**Practical assignment:** Compare planning success/time across different start/goal configurations.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Manipulator planning pipeline**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: configuration space.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Manipulator planning pipeline; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Configure MoveIt 2 for a supported arm; create a planning request client and log planner response.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Run MoveIt Setup Assistant and inspect planning group, end-effector and kinematics configuration.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Plan collision-free joint and pose goals in RViz/Gazebo.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Compare planning success/time across different start/goal configurations.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [MoveIt 2 tutorials](https://moveit.picknik.ai/main/index.html)
- [MoveIt 2 tutorial repository](https://github.com/moveit/moveit2_tutorials)
- [OMPL documentation](https://ompl.kavrakilab.org/)
- [Modern Robotics — motion planning and manipulation](https://modernrobotics.northwestern.edu/)
- [YouTube — MoveIt 2 pick and place tutorials](https://www.youtube.com/results?search_query=MoveIt+2+pick+and+place+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Manipulator planning pipeline** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Manipulator planning pipeline; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Manipulator planning pipeline** to a robotics engineer who has not used this technique.
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

## Week 15 — Trajectory generation and time parameterization
**Expected outcome:** Turn geometric paths into feasible time trajectories.
**Theory syllabus:** path vs trajectory; velocity/acceleration limits; time parameterization; interpolation; jerk awareness.
**Mathematical foundation:** Derive the equations relevant to Trajectory generation and time parameterization; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Generate trapezoidal and smooth trajectories; validate joint limits and continuity.
**ROS 2 implementation:** Send FollowJointTrajectory action goals and handle feedback/result.
**Simulation exercise:** Execute joint trajectories in Gazebo and compare desired vs measured state.
**Practical assignment:** Demonstrate trajectory rejection or slowdown for infeasible limits.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Trajectory generation and time parameterization**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: path vs trajectory.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Trajectory generation and time parameterization; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Generate trapezoidal and smooth trajectories; validate joint limits and continuity.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Send FollowJointTrajectory action goals and handle feedback/result.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Execute joint trajectories in Gazebo and compare desired vs measured state.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Demonstrate trajectory rejection or slowdown for infeasible limits.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [MoveIt 2 tutorials](https://moveit.picknik.ai/main/index.html)
- [MoveIt 2 tutorial repository](https://github.com/moveit/moveit2_tutorials)
- [OMPL documentation](https://ompl.kavrakilab.org/)
- [Modern Robotics — motion planning and manipulation](https://modernrobotics.northwestern.edu/)
- [YouTube — MoveIt 2 pick and place tutorials](https://www.youtube.com/results?search_query=MoveIt+2+pick+and+place+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Trajectory generation and time parameterization** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Trajectory generation and time parameterization; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Trajectory generation and time parameterization** to a robotics engineer who has not used this technique.
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

## Week 16 — Grasping, end-effector and planning scene
**Expected outcome:** Model pick/place as a sequence with collision-aware scene updates.
**Theory syllabus:** grasp pose; approach/retreat; grasp width; attached objects; allowed collision matrix; Cartesian path.
**Mathematical foundation:** Derive the equations relevant to Grasping, end-effector and planning scene; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Create a grasp-pose sampler and pick/place state machine; test failure branches.
**ROS 2 implementation:** Use MoveIt planning scene interfaces and action clients for a pick/place task.
**Simulation exercise:** Simulate a cube pick/place task with an attached collision object.
**Practical assignment:** Record at least 20 trials; classify failure: perception, IK, collision, trajectory or gripper.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Grasping, end-effector and planning scene**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: grasp pose.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Grasping, end-effector and planning scene; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Create a grasp-pose sampler and pick/place state machine; test failure branches.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Use MoveIt planning scene interfaces and action clients for a pick/place task.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Simulate a cube pick/place task with an attached collision object.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Record at least 20 trials; classify failure: perception, IK, collision, trajectory or gripper.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [MoveIt 2 tutorials](https://moveit.picknik.ai/main/index.html)
- [MoveIt 2 tutorial repository](https://github.com/moveit/moveit2_tutorials)
- [OMPL documentation](https://ompl.kavrakilab.org/)
- [Modern Robotics — motion planning and manipulation](https://modernrobotics.northwestern.edu/)
- [YouTube — MoveIt 2 pick and place tutorials](https://www.youtube.com/results?search_query=MoveIt+2+pick+and+place+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Grasping, end-effector and planning scene** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Grasping, end-effector and planning scene; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Grasping, end-effector and planning scene** to a robotics engineer who has not used this technique.
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

## Week 17 — MoveIt Task Constructor and robust manipulation
**Expected outcome:** Compose manipulation stages and handle recovery.
**Theory syllabus:** stage-based tasks; serial/container stages; planning alternatives; execution monitoring; recovery.
**Mathematical foundation:** Derive the equations relevant to MoveIt Task Constructor and robust manipulation; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build a staged pick-and-place pipeline and add structured logs and retries.
**ROS 2 implementation:** Use MoveIt Task Constructor examples or supported MoveIt task patterns.
**Simulation exercise:** Run repeated pick/place with randomized object pose.
**Practical assignment:** Achieve a declared success rate and report confidence intervals over repeated trials.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **MoveIt Task Constructor and robust manipulation**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: stage-based tasks.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to MoveIt Task Constructor and robust manipulation; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build a staged pick-and-place pipeline and add structured logs and retries.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Use MoveIt Task Constructor examples or supported MoveIt task patterns.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run repeated pick/place with randomized object pose.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Achieve a declared success rate and report confidence intervals over repeated trials.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [MoveIt 2 tutorials](https://moveit.picknik.ai/main/index.html)
- [MoveIt 2 tutorial repository](https://github.com/moveit/moveit2_tutorials)
- [OMPL documentation](https://ompl.kavrakilab.org/)
- [Modern Robotics — motion planning and manipulation](https://modernrobotics.northwestern.edu/)
- [YouTube — MoveIt 2 pick and place tutorials](https://www.youtube.com/results?search_query=MoveIt+2+pick+and+place+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **MoveIt Task Constructor and robust manipulation** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to MoveIt Task Constructor and robust manipulation; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **MoveIt Task Constructor and robust manipulation** to a robotics engineer who has not used this technique.
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
**Project name:** MoveIt 2 collision-aware pick-and-place cell**
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

1. Explain configuration space and why collision checking is performed in joint space.
2. Compare sampling-based planning and trajectory optimization.
3. Explain the role of OMPL in MoveIt 2.
4. Why is a collision-free geometric path not necessarily a feasible trajectory?
5. Calculate a minimum trajectory duration with velocity and acceleration limits.
6. Describe the planning scene and attached collision objects.
7. Design a robust pick-and-place sequence with preconditions and recovery.
8. Propose metrics for comparing planners over repeated randomized trials.

### Month-specific interview questions

1. How does MoveIt 2 represent a robot and its planning groups?
2. What does a planning scene monitor do?
3. How would you debug planning failure when IK succeeds?
4. Compare joint-space and Cartesian path planning.
5. What is time parameterization and why is it required?
6. How do collision objects become attached to a robot?
7. What are the main failure points in a grasp pipeline?
8. How do you measure manipulation reliability rather than showing one successful demo?

## Month-end interview question bank
1. Explain **Robot Manipulation, MoveIt 2 and Motion Planning** as though you are in a technical interview.
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
| 14 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 15 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 16 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 17 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
