# Robotics & Physical AI — Month 02: Robot Kinematics, Dynamics and Classical Control

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
By the end of Month 2, you should be able to explain, implement and defend the following: 
- Primary focus: **Robot Kinematics, Dynamics and Classical Control**.
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

- **2R forward kinematics:** x=l₁cosθ₁+l₂cos(θ₁+θ₂), y=l₁sinθ₁+l₂sin(θ₁+θ₂). Evaluate for l₁=0.4 m, l₂=0.3 m, θ₁=30°, θ₂=45°.
- **Jacobian interpretation:** J maps joint rates to end-effector velocity, v=J(q)q̇. Find where det(J) approaches zero for a planar 2R arm and explain loss of one motion direction.
- **PID example:** For a first-order plant, compare P-only and PID tracking. Plot overshoot, settling time and steady-state error; discuss windup under saturation.
- **Dynamics example:** For a damped pendulum, Iθ̈+bθ̇+mgl sinθ=τ. Linearize near θ=0 and identify the state-space matrices.

## Weekly training blocks
## Week 05 — Rigid-body motion and forward kinematics
**Expected outcome:** Derive the pose of a planar serial manipulator.
**Theory syllabus:** joint variables; link frames; DH convention; product of exponentials overview; FK for 2R/3R arms.
**Mathematical foundation:** Derive the equations relevant to Rigid-body motion and forward kinematics; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement FK for 2-link and 3-link arms; verify against hand calculations and randomized tests.
**ROS 2 implementation:** Represent joints and link frames using URDF concepts; publish a joint-state message.
**Simulation exercise:** Animate a 2R arm and sweep joint angles; draw reachable workspace.
**Practical assignment:** Measure the workspace and identify unreachable Cartesian targets.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Rigid-body motion and forward kinematics**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: joint variables.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Rigid-body motion and forward kinematics; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement FK for 2-link and 3-link arms; verify against hand calculations and randomized tests.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Represent joints and link frames using URDF concepts; publish a joint-state message.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Animate a 2R arm and sweep joint angles; draw reachable workspace.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Measure the workspace and identify unreachable Cartesian targets.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Modern Robotics chapters 3–6 and video lectures](https://modernrobotics.northwestern.edu/chapters/)
- [MIT Underactuated Robotics — dynamics and control](https://underactuated.mit.edu/)
- [Robotics Toolbox for Python documentation](https://roboticstoolbox.org/)
- [SymPy mechanics documentation](https://docs.sympy.org/latest/modules/physics/mechanics/index.html)
- [YouTube — forward/inverse kinematics and Jacobian lectures](https://www.youtube.com/results?search_query=robotics+forward+inverse+kinematics+Jacobian+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Rigid-body motion and forward kinematics** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Rigid-body motion and forward kinematics; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Rigid-body motion and forward kinematics** to a robotics engineer who has not used this technique.
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

## Week 06 — Inverse kinematics and Jacobians
**Expected outcome:** Solve target poses and understand singularities.
**Theory syllabus:** geometric/algebraic IK; numerical IK; Jacobian; velocity mapping; singular values; manipulability.
**Mathematical foundation:** Derive the equations relevant to Inverse kinematics and Jacobians; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement closed-form 2R IK and damped least-squares numerical IK; detect near-singular configurations.
**ROS 2 implementation:** Use tf2 to inspect end-effector transforms; publish joint targets in a simple controller node.
**Simulation exercise:** Move the simulated arm to sampled end-effector points; plot tracking error.
**Practical assignment:** Compare elbow-up/down solutions and test near a fully stretched arm.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Inverse kinematics and Jacobians**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: geometric/algebraic IK.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Inverse kinematics and Jacobians; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement closed-form 2R IK and damped least-squares numerical IK; detect near-singular configurations.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Use tf2 to inspect end-effector transforms; publish joint targets in a simple controller node.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Move the simulated arm to sampled end-effector points; plot tracking error.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Compare elbow-up/down solutions and test near a fully stretched arm.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Modern Robotics chapters 3–6 and video lectures](https://modernrobotics.northwestern.edu/chapters/)
- [MIT Underactuated Robotics — dynamics and control](https://underactuated.mit.edu/)
- [Robotics Toolbox for Python documentation](https://roboticstoolbox.org/)
- [SymPy mechanics documentation](https://docs.sympy.org/latest/modules/physics/mechanics/index.html)
- [YouTube — forward/inverse kinematics and Jacobian lectures](https://www.youtube.com/results?search_query=robotics+forward+inverse+kinematics+Jacobian+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Inverse kinematics and Jacobians** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Inverse kinematics and Jacobians; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Inverse kinematics and Jacobians** to a robotics engineer who has not used this technique.
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

## Week 07 — Rigid-body dynamics and actuator models
**Expected outcome:** Connect torque, inertia, friction and motion.
**Theory syllabus:** Newton–Euler and Lagrange formulations; inertia; gravity; Coriolis terms; friction; motor torque-speed limits.
**Mathematical foundation:** Derive the equations relevant to Rigid-body dynamics and actuator models; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Derive and simulate a pendulum and a 1-DOF joint; estimate inertia/friction from synthetic data.
**ROS 2 implementation:** Create a ROS 2 node that accepts torque or velocity commands for a simple simulated plant.
**Simulation exercise:** Simulate a pendulum with gravity, damping and actuator saturation.
**Practical assignment:** Identify damping and inertia from a step-response log.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Rigid-body dynamics and actuator models**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: Newton–Euler and Lagrange formulations.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Rigid-body dynamics and actuator models; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Derive and simulate a pendulum and a 1-DOF joint; estimate inertia/friction from synthetic data.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create a ROS 2 node that accepts torque or velocity commands for a simple simulated plant.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Simulate a pendulum with gravity, damping and actuator saturation.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Identify damping and inertia from a step-response log.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Modern Robotics chapters 3–6 and video lectures](https://modernrobotics.northwestern.edu/chapters/)
- [MIT Underactuated Robotics — dynamics and control](https://underactuated.mit.edu/)
- [Robotics Toolbox for Python documentation](https://roboticstoolbox.org/)
- [SymPy mechanics documentation](https://docs.sympy.org/latest/modules/physics/mechanics/index.html)
- [YouTube — forward/inverse kinematics and Jacobian lectures](https://www.youtube.com/results?search_query=robotics+forward+inverse+kinematics+Jacobian+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Rigid-body dynamics and actuator models** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Rigid-body dynamics and actuator models; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Rigid-body dynamics and actuator models** to a robotics engineer who has not used this technique.
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

## Week 08 — PID, state-space and control evaluation
**Expected outcome:** Design and assess feedback controllers.
**Theory syllabus:** PID; anti-windup; feedforward; transfer functions; state-space; poles; stability; discretization; sampling.
**Mathematical foundation:** Derive the equations relevant to PID, state-space and control evaluation; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement PID with saturation/anti-windup and a state-space simulation; compare rise time, overshoot and steady-state error.
**ROS 2 implementation:** Create a controller node with parameters, command topic and state feedback topic.
**Simulation exercise:** Control a 1-DOF joint or differential-drive heading in simulation.
**Practical assignment:** Tune P/PI/PID under actuator saturation and injected measurement noise.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **PID, state-space and control evaluation**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: PID.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to PID, state-space and control evaluation; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement PID with saturation/anti-windup and a state-space simulation; compare rise time, overshoot and steady-state error.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create a controller node with parameters, command topic and state feedback topic.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Control a 1-DOF joint or differential-drive heading in simulation.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Tune P/PI/PID under actuator saturation and injected measurement noise.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Modern Robotics chapters 3–6 and video lectures](https://modernrobotics.northwestern.edu/chapters/)
- [MIT Underactuated Robotics — dynamics and control](https://underactuated.mit.edu/)
- [Robotics Toolbox for Python documentation](https://roboticstoolbox.org/)
- [SymPy mechanics documentation](https://docs.sympy.org/latest/modules/physics/mechanics/index.html)
- [YouTube — forward/inverse kinematics and Jacobian lectures](https://www.youtube.com/results?search_query=robotics+forward+inverse+kinematics+Jacobian+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **PID, state-space and control evaluation** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to PID, state-space and control evaluation; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **PID, state-space and control evaluation** to a robotics engineer who has not used this technique.
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
**Project name:** Planar manipulator kinematics and PID control bench**
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

1. Derive forward kinematics for a planar 2R arm and calculate one numerical pose.
2. Solve inverse kinematics for elbow-up and elbow-down configurations; identify unreachable targets.
3. Derive the Jacobian and show a singular configuration using determinant or singular values.
4. Explain the difference between geometric and numerical IK.
5. Derive a one-link pendulum equation using Lagrange’s method.
6. Linearize a nonlinear pendulum around an equilibrium and write state-space matrices.
7. Explain PID windup and design anti-windup for a saturated actuator.
8. Compare position, velocity and torque control and state what sensor feedback each needs.

### Month-specific interview questions

1. What is the physical meaning of the Jacobian?
2. How do you identify a manipulator singularity?
3. Why can IK have multiple solutions?
4. How would you choose between pseudoinverse and damped least-squares IK?
5. What assumptions are made in your rigid-body dynamics model?
6. How do inertia and friction affect a step response?
7. How do you tune PID without hiding instability or actuator saturation?
8. How would you validate a controller in simulation before hardware?

## Month-end interview question bank
1. Explain **Robot Kinematics, Dynamics and Classical Control** as though you are in a technical interview.
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
| 05 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 06 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 07 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 08 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
