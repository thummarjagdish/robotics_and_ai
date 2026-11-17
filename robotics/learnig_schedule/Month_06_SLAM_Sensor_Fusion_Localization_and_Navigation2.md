# Robotics & Physical AI — Month 06: SLAM, Sensor Fusion, Localization and Navigation2

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
By the end of Month 6, you should be able to explain, implement and defend the following: 
- Primary focus: **SLAM, Sensor Fusion, Localization and Navigation2**.
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

- **Differential drive:** v=(r/2)(ω_R+ω_L), ω=(r/L)(ω_R−ω_L). Integrate pose and explain how wheel-radius error causes drift.
- **Bayesian localization:** A prior pose estimate and noisy LiDAR observation update a belief. Explain prediction vs correction in an EKF or particle filter.
- **Navigation metrics:** For 20 goals, compute success rate, median completion time, path length and minimum clearance. Explain the trade-off between speed and safety.

## Weekly training blocks
## Week 22 — Odometry, IMU and probabilistic state estimation
**Expected outcome:** Build a fused estimate and understand drift.
**Theory syllabus:** differential-drive odometry; IMU frames/bias; EKF; covariance; observability; timestamp synchronization.
**Mathematical foundation:** Derive the equations relevant to Odometry, IMU and probabilistic state estimation; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement a basic EKF for 2D pose or fuse simulated wheel/IMU data; plot uncertainty.
**ROS 2 implementation:** Configure robot_localization and inspect /odometry/filtered and TF.
**Simulation exercise:** Simulate odometry drift and sensor noise in Gazebo.
**Practical assignment:** Compare wheel-only vs fused estimate against ground truth.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Odometry, IMU and probabilistic state estimation**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: differential-drive odometry.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Odometry, IMU and probabilistic state estimation; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement a basic EKF for 2D pose or fuse simulated wheel/IMU data; plot uncertainty.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Configure robot_localization and inspect /odometry/filtered and TF.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Simulate odometry drift and sensor noise in Gazebo.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Compare wheel-only vs fused estimate against ground truth.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Nav2 Jazzy getting started](https://docs.nav2.org/jazzy/getting_started/)
- [Nav2 concepts and architecture](https://docs.nav2.org/)
- [SLAM Toolbox repository and documentation](https://github.com/SteveMacenski/slam_toolbox)
- [robot_localization documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/robot_localization/)
- [ORB-SLAM3 paper](https://doi.org/10.1109/TRO.2021.3075644)
- [YouTube — ROS 2 Nav2 and SLAM Toolbox](https://www.youtube.com/results?search_query=ROS+2+Nav2+SLAM+Toolbox+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Odometry, IMU and probabilistic state estimation** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Odometry, IMU and probabilistic state estimation; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Odometry, IMU and probabilistic state estimation** to a robotics engineer who has not used this technique.
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

## Week 23 — Mapping and SLAM fundamentals
**Expected outcome:** Explain mapping, localization, loop closure and graph optimization.
**Theory syllabus:** occupancy grids; scan matching; particle filters; pose graphs; loop closure; LiDAR models.
**Mathematical foundation:** Derive the equations relevant to Mapping and SLAM fundamentals; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build an occupancy grid from 2D scans or run SLAM Toolbox on recorded/simulated data.
**ROS 2 implementation:** Launch SLAM Toolbox in synchronous/asynchronous mode as appropriate; save map.
**Simulation exercise:** Drive a simulated robot through a loop and inspect map consistency.
**Practical assignment:** Measure map alignment and explain loop-closure correction.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Mapping and SLAM fundamentals**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: occupancy grids.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Mapping and SLAM fundamentals; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build an occupancy grid from 2D scans or run SLAM Toolbox on recorded/simulated data.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Launch SLAM Toolbox in synchronous/asynchronous mode as appropriate; save map.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Drive a simulated robot through a loop and inspect map consistency.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Measure map alignment and explain loop-closure correction.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Nav2 Jazzy getting started](https://docs.nav2.org/jazzy/getting_started/)
- [Nav2 concepts and architecture](https://docs.nav2.org/)
- [SLAM Toolbox repository and documentation](https://github.com/SteveMacenski/slam_toolbox)
- [robot_localization documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/robot_localization/)
- [ORB-SLAM3 paper](https://doi.org/10.1109/TRO.2021.3075644)
- [YouTube — ROS 2 Nav2 and SLAM Toolbox](https://www.youtube.com/results?search_query=ROS+2+Nav2+SLAM+Toolbox+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Mapping and SLAM fundamentals** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Mapping and SLAM fundamentals; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Mapping and SLAM fundamentals** to a robotics engineer who has not used this technique.
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

## Week 24 — Localization and Nav2 architecture
**Expected outcome:** Configure localization and explain the navigation stack.
**Theory syllabus:** AMCL; map server; lifecycle nodes; planners; controllers; costmaps; behavior trees; recovery.
**Mathematical foundation:** Derive the equations relevant to Localization and Nav2 architecture; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Tune a simple planner/controller configuration and record navigation metrics.
**ROS 2 implementation:** Launch Nav2 in simulation; send NavigateToPose goals and inspect lifecycle transitions.
**Simulation exercise:** Navigate a TurtleBot-like robot through an obstacle world.
**Practical assignment:** Measure success rate, time, path length and minimum obstacle clearance.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Localization and Nav2 architecture**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: AMCL.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Localization and Nav2 architecture; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Tune a simple planner/controller configuration and record navigation metrics.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Launch Nav2 in simulation; send NavigateToPose goals and inspect lifecycle transitions.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Navigate a TurtleBot-like robot through an obstacle world.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Measure success rate, time, path length and minimum obstacle clearance.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Nav2 Jazzy getting started](https://docs.nav2.org/jazzy/getting_started/)
- [Nav2 concepts and architecture](https://docs.nav2.org/)
- [SLAM Toolbox repository and documentation](https://github.com/SteveMacenski/slam_toolbox)
- [robot_localization documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/robot_localization/)
- [ORB-SLAM3 paper](https://doi.org/10.1109/TRO.2021.3075644)
- [YouTube — ROS 2 Nav2 and SLAM Toolbox](https://www.youtube.com/results?search_query=ROS+2+Nav2+SLAM+Toolbox+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Localization and Nav2 architecture** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Localization and Nav2 architecture; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Localization and Nav2 architecture** to a robotics engineer who has not used this technique.
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

## Week 25 — Navigation tuning, recovery and robustness
**Expected outcome:** Diagnose real navigation failures systematically.
**Theory syllabus:** inflation radius; footprint; inflation/cost layers; obstacle layers; controller tuning; behavior tree recovery.
**Mathematical foundation:** Derive the equations relevant to Navigation tuning, recovery and robustness; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Run parameter sweeps and create an experiment table.
**ROS 2 implementation:** Add waypoint following, diagnostics and rosbag recording.
**Simulation exercise:** Test clutter, narrow passages, dynamic obstacles and localization degradation.
**Practical assignment:** Deliver a reproducible Nav2 benchmark with at least 20 goal attempts.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Navigation tuning, recovery and robustness**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: inflation radius.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Navigation tuning, recovery and robustness; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Run parameter sweeps and create an experiment table.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Add waypoint following, diagnostics and rosbag recording.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Test clutter, narrow passages, dynamic obstacles and localization degradation.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Deliver a reproducible Nav2 benchmark with at least 20 goal attempts.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Nav2 Jazzy getting started](https://docs.nav2.org/jazzy/getting_started/)
- [Nav2 concepts and architecture](https://docs.nav2.org/)
- [SLAM Toolbox repository and documentation](https://github.com/SteveMacenski/slam_toolbox)
- [robot_localization documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/robot_localization/)
- [ORB-SLAM3 paper](https://doi.org/10.1109/TRO.2021.3075644)
- [YouTube — ROS 2 Nav2 and SLAM Toolbox](https://www.youtube.com/results?search_query=ROS+2+Nav2+SLAM+Toolbox+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Navigation tuning, recovery and robustness** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Navigation tuning, recovery and robustness; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Navigation tuning, recovery and robustness** to a robotics engineer who has not used this technique.
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

## Week 26 — Integrated autonomous mobile robot project
**Expected outcome:** Integrate sensing, mapping, localization, planning and monitoring.
**Theory syllabus:** system architecture; failure modes; reliability; timing; safety stop; metrics.
**Mathematical foundation:** Derive the equations relevant to Integrated autonomous mobile robot project; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Write an integration test runner and analyze navigation logs.
**ROS 2 implementation:** Create one launch entry point for robot, sensors, localization and Nav2.
**Simulation exercise:** Run a full simulated mission with multiple goals and obstacle changes.
**Practical assignment:** Produce a demo video, bag files, map, parameter set and design note.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Integrated autonomous mobile robot project**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: system architecture.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Integrated autonomous mobile robot project; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Write an integration test runner and analyze navigation logs.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create one launch entry point for robot, sensors, localization and Nav2.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run a full simulated mission with multiple goals and obstacle changes.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Produce a demo video, bag files, map, parameter set and design note.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Nav2 Jazzy getting started](https://docs.nav2.org/jazzy/getting_started/)
- [Nav2 concepts and architecture](https://docs.nav2.org/)
- [SLAM Toolbox repository and documentation](https://github.com/SteveMacenski/slam_toolbox)
- [robot_localization documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/robot_localization/)
- [ORB-SLAM3 paper](https://doi.org/10.1109/TRO.2021.3075644)
- [YouTube — ROS 2 Nav2 and SLAM Toolbox](https://www.youtube.com/results?search_query=ROS+2+Nav2+SLAM+Toolbox+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Integrated autonomous mobile robot project** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Integrated autonomous mobile robot project; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Integrated autonomous mobile robot project** to a robotics engineer who has not used this technique.
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
**Project name:** Autonomous mobile robot with SLAM and Nav2**
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

1. Derive differential-drive forward kinematics and integrate a short trajectory.
2. Explain how wheel radius and wheelbase errors produce odometry drift.
3. Write the EKF prediction and correction steps and identify covariance propagation.
4. Compare EKF, particle-filter localization and graph-based SLAM.
5. Explain scan matching and loop closure.
6. Describe AMCL’s role in a known map.
7. Explain Nav2 planners, controllers, costmaps and behavior-tree orchestration.
8. Design a navigation benchmark with success, time, path length and clearance metrics.

### Month-specific interview questions

1. What is the difference between odometry, localization, mapping and SLAM?
2. Why does an EKF need covariance?
3. What makes a system observable?
4. How does loop closure reduce accumulated drift?
5. What is the difference between SLAM Toolbox and AMCL?
6. How do costmap layers influence obstacle avoidance?
7. How would you debug a robot that reaches goals in RViz but fails in Gazebo?
8. How do you assess navigation safety in dynamic environments?

## Month-end interview question bank
1. Explain **SLAM, Sensor Fusion, Localization and Navigation2** as though you are in a technical interview.
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
| 22 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 23 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 24 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 25 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 26 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
