# Robotics & Physical AI — Month 01: Robotics Mathematics, Python Numerics and Engineering Thinking

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
By the end of Month 1, you should be able to explain, implement and defend the following: 
- Primary focus: **Robotics Mathematics, Python Numerics and Engineering Thinking**.
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

- **Frame transform example:** Let a point in a camera frame be p_C = [0.2, 0.1, 1.0, 1]^T. If the camera is translated 0.1 m along base X and rotated 90° about Z, calculate p_B = T_BC p_C. Write the transform and verify with NumPy.
- **Derivative example:** For x(t)=0.5t², derive v(t)=t and a(t)=1. Approximate velocity with finite differences at Δt=0.1 s and discuss truncation/noise.
- **Probability example:** A range sensor returns samples around 2.0 m. Estimate sample mean and variance; explain why variance matters to localization.
- **Optimization example:** Fit y=ax+b to noisy samples. Minimize J(a,b)=Σ(yᵢ−axᵢ−b)² and compare normal-equation vs gradient-descent results.

## Weekly training blocks
## Week 01 — Vectors, coordinate geometry and linear algebra
**Expected outcome:** Represent robot position, direction and coordinate frames with vectors and matrices.
**Theory syllabus:** vector operations; dot/cross products; norms; basis; matrix multiplication; rank; inverse; eigen intuition.
**Mathematical foundation:** Derive the equations relevant to Vectors, coordinate geometry and linear algebra; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement a 2D/3D vector and matrix utility with unit tests; plot points, lines and coordinate frames.
**ROS 2 implementation:** Use ROS geometry_msgs concepts; publish a static pose or inspect geometry_msgs/Pose data in a tiny ROS 2 Python node.
**Simulation exercise:** Animate a point and heading in a 2D matplotlib world; compare local and world coordinates.
**Practical assignment:** Convert a point from a sensor frame to a robot frame using a hand-computed transform.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Vectors, coordinate geometry and linear algebra**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: vector operations.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Vectors, coordinate geometry and linear algebra; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement a 2D/3D vector and matrix utility with unit tests; plot points, lines and coordinate frames.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Use ROS geometry_msgs concepts; publish a static pose or inspect geometry_msgs/Pose data in a tiny ROS 2 Python node.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Animate a point and heading in a 2D matplotlib world; compare local and world coordinates.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Convert a point from a sensor frame to a robot frame using a hand-computed transform.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Modern Robotics — free textbook, videos and software](https://modernrobotics.northwestern.edu/)
- [MIT Underactuated Robotics notes and lecture videos](https://underactuated.mit.edu/)
- [3Blue1Brown — linear algebra visual intuition (YouTube search)](https://www.youtube.com/results?search_query=3Blue1Brown+Essence+of+Linear+Algebra)
- [MIT OpenCourseWare — multivariable calculus (YouTube search)](https://www.youtube.com/results?search_query=MIT+OpenCourseWare+multivariable+calculus)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Vectors, coordinate geometry and linear algebra** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Vectors, coordinate geometry and linear algebra; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Vectors, coordinate geometry and linear algebra** to a robotics engineer who has not used this technique.
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

## Week 02 — Rotations, homogeneous transforms and frames
**Expected outcome:** Compose rigid transforms and explain why frame conventions matter.
**Theory syllabus:** SO(2), SO(3), rotation matrices, Euler angles, quaternions, homogeneous transforms, inverse transforms.
**Mathematical foundation:** Derive the equations relevant to Rotations, homogeneous transforms and frames; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build transform composition/inversion functions; test orthogonality and determinant; compare Euler and quaternion representations.
**ROS 2 implementation:** Inspect /tf and /tf_static; create a broadcaster/listener exercise if ROS 2 is available.
**Simulation exercise:** Visualize a two-link coordinate frame chain and rotate the end frame.
**Practical assignment:** Transform a camera-measured object point into the base frame with a known extrinsic transform.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Rotations, homogeneous transforms and frames**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: SO(2), SO(3), rotation matrices, Euler angles, quaternions, homogeneous transforms, inverse transforms..
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Rotations, homogeneous transforms and frames; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build transform composition/inversion functions; test orthogonality and determinant; compare Euler and quaternion representations.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Inspect /tf and /tf_static; create a broadcaster/listener exercise if ROS 2 is available.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Visualize a two-link coordinate frame chain and rotate the end frame.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Transform a camera-measured object point into the base frame with a known extrinsic transform.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Modern Robotics — free textbook, videos and software](https://modernrobotics.northwestern.edu/)
- [MIT Underactuated Robotics notes and lecture videos](https://underactuated.mit.edu/)
- [3Blue1Brown — linear algebra visual intuition (YouTube search)](https://www.youtube.com/results?search_query=3Blue1Brown+Essence+of+Linear+Algebra)
- [MIT OpenCourseWare — multivariable calculus (YouTube search)](https://www.youtube.com/results?search_query=MIT+OpenCourseWare+multivariable+calculus)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Rotations, homogeneous transforms and frames** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Rotations, homogeneous transforms and frames; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Rotations, homogeneous transforms and frames** to a robotics engineer who has not used this technique.
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

## Week 03 — Calculus, derivatives and numerical integration
**Expected outcome:** Relate position, velocity and acceleration to robot motion.
**Theory syllabus:** limits; derivatives; chain rule; partial derivatives; gradients; integrals; Euler and Runge–Kutta integration.
**Mathematical foundation:** Derive the equations relevant to Calculus, derivatives and numerical integration; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Numerically differentiate a trajectory; integrate constant and varying acceleration; compare Euler vs RK4 error.
**ROS 2 implementation:** Create a node publishing a time-stamped scalar position and finite-difference velocity.
**Simulation exercise:** Simulate a 1D mass and a moving 2D point with time-step sensitivity.
**Practical assignment:** Estimate velocity from encoder-like sampled position data; quantify noise amplification.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Calculus, derivatives and numerical integration**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: limits.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Calculus, derivatives and numerical integration; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Numerically differentiate a trajectory; integrate constant and varying acceleration; compare Euler vs RK4 error.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create a node publishing a time-stamped scalar position and finite-difference velocity.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Simulate a 1D mass and a moving 2D point with time-step sensitivity.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Estimate velocity from encoder-like sampled position data; quantify noise amplification.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Modern Robotics — free textbook, videos and software](https://modernrobotics.northwestern.edu/)
- [MIT Underactuated Robotics notes and lecture videos](https://underactuated.mit.edu/)
- [3Blue1Brown — linear algebra visual intuition (YouTube search)](https://www.youtube.com/results?search_query=3Blue1Brown+Essence+of+Linear+Algebra)
- [MIT OpenCourseWare — multivariable calculus (YouTube search)](https://www.youtube.com/results?search_query=MIT+OpenCourseWare+multivariable+calculus)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Calculus, derivatives and numerical integration** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Calculus, derivatives and numerical integration; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Calculus, derivatives and numerical integration** to a robotics engineer who has not used this technique.
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

## Week 04 — Probability, uncertainty and optimization foundations
**Expected outcome:** Describe noisy measurements and solve a small least-squares problem.
**Theory syllabus:** random variables; Gaussian; expectation; variance; covariance; Bayes rule; least squares; gradient descent.
**Mathematical foundation:** Derive the equations relevant to Probability, uncertainty and optimization foundations; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Generate noisy data; estimate mean/covariance; fit a line with least squares and gradient descent.
**ROS 2 implementation:** Create a ROS 2 node that publishes a noisy sensor message and logs running statistics.
**Simulation exercise:** Compare true vs noisy robot path and a fitted line/trajectory.
**Practical assignment:** Calibrate a synthetic sensor offset and scale using recorded samples.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Probability, uncertainty and optimization foundations**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: random variables.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Probability, uncertainty and optimization foundations; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Generate noisy data; estimate mean/covariance; fit a line with least squares and gradient descent.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create a ROS 2 node that publishes a noisy sensor message and logs running statistics.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Compare true vs noisy robot path and a fitted line/trajectory.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Calibrate a synthetic sensor offset and scale using recorded samples.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Modern Robotics — free textbook, videos and software](https://modernrobotics.northwestern.edu/)
- [MIT Underactuated Robotics notes and lecture videos](https://underactuated.mit.edu/)
- [3Blue1Brown — linear algebra visual intuition (YouTube search)](https://www.youtube.com/results?search_query=3Blue1Brown+Essence+of+Linear+Algebra)
- [MIT OpenCourseWare — multivariable calculus (YouTube search)](https://www.youtube.com/results?search_query=MIT+OpenCourseWare+multivariable+calculus)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Probability, uncertainty and optimization foundations** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Probability, uncertainty and optimization foundations; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Probability, uncertainty and optimization foundations** to a robotics engineer who has not used this technique.
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
**Project name:** Robotics math and pose-transform toolkit**
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

1. Derive a homogeneous transform for a 90° rotation about Z plus a translation; state whether it maps sensor-to-base or base-to-sensor.
2. Prove or numerically test that a valid rotation matrix is orthonormal and has determinant +1.
3. Compare Euler angles and quaternions; explain one singularity or interpolation issue.
4. Estimate velocity from sampled position and explain how measurement noise affects the derivative.
5. Compute sample mean, variance and covariance for a noisy range sensor; interpret the units.
6. Derive the least-squares line fit and explain when the normal equation becomes poorly conditioned.
7. Compare Euler and RK4 integration on a simple dynamic system as the time step changes.
8. Explain how you would unit-test a transform library against an independent reference.

### Month-specific interview questions

1. Explain active vs passive coordinate transforms.
2. How do you detect a wrong frame direction in a TF tree?
3. Why must a rotation matrix be orthonormal?
4. When is a quaternion preferable to Euler angles?
5. Why does numerical differentiation amplify measurement noise?
6. What does covariance tell a localization system?
7. How would you validate a numerical optimizer?
8. Explain a robotics equation from this month using units and a numerical example.

## Month-end interview question bank
1. Explain **Robotics Mathematics, Python Numerics and Engineering Thinking** as though you are in a technical interview.
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
| 01 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 02 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 03 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 04 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
