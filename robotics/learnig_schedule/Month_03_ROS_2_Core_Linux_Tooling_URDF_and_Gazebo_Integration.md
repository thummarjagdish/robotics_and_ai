# Robotics & Physical AI — Month 03: ROS 2 Core, Linux Tooling, URDF and Gazebo Integration

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
By the end of Month 3, you should be able to explain, implement and defend the following: 
- Primary focus: **ROS 2 Core, Linux Tooling, URDF and Gazebo Integration**.
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

- **ROS graph example:** A camera node publishes /image_raw; an image-processing node subscribes and publishes /detections. Draw the graph, select QoS and explain what happens if sensor QoS is best-effort but consumer requests reliable.
- **URDF example:** A base_link and wheel_link connected by a continuous joint need a correct joint origin, axis and inertial model. Change the axis and observe the motion error.
- **Simulation bridge example:** Bridge /scan from Gazebo to sensor_msgs/msg/LaserScan and /cmd_vel from ROS to Gazebo. Confirm rates, frame_id and simulation clock.

## Weekly training blocks
## Week 09 — ROS 2 graph and communication primitives
**Expected outcome:** Explain nodes, topics, services, actions, parameters, QoS and discovery.
**Theory syllabus:** DDS concepts; message types; QoS reliability/durability/history; executor basics; graph introspection.
**Mathematical foundation:** Derive the equations relevant to ROS 2 graph and communication primitives; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Create Python publisher/subscriber and C++ publisher/subscriber packages; add launch and parameter files.
**ROS 2 implementation:** Complete ROS CLI tutorials; inspect node graph, topics, services, actions and QoS.
**Simulation exercise:** Run turtlesim and a simple sensor/actuator mock system; record with rosbag2.
**Practical assignment:** Diagnose a deliberately mismatched topic name and QoS profile.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **ROS 2 graph and communication primitives**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: DDS concepts.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to ROS 2 graph and communication primitives; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Create Python publisher/subscriber and C++ publisher/subscriber packages; add launch and parameter files.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Complete ROS CLI tutorials; inspect node graph, topics, services, actions and QoS.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run turtlesim and a simple sensor/actuator mock system; record with rosbag2.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Diagnose a deliberately mismatched topic name and QoS profile.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [ROS 2 Jazzy tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [ROS 2 design articles](https://design.ros2.org/)
- [ros2_control documentation](https://control.ros.org/jazzy/index.html)
- [Gazebo Harmonic ROS 2 integration](https://gazebosim.org/docs/harmonic/ros2_integration/)
- [ROS 2 YouTube — nodes, topics, services, actions](https://www.youtube.com/results?search_query=ROS+2+Jazzy+complete+tutorial+nodes+topics+services+actions)
- [Articulated Robotics — ROS 2 tutorial videos](https://www.youtube.com/results?search_query=Articulated+Robotics+ROS+2+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **ROS 2 graph and communication primitives** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to ROS 2 graph and communication primitives; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **ROS 2 graph and communication primitives** to a robotics engineer who has not used this technique.
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

## Week 10 — Packages, workspaces, C++/Python nodes and testing
**Expected outcome:** Build maintainable ROS packages with tests and clean interfaces.
**Theory syllabus:** ament; colcon; package.xml; setup.py/CMake; launch; parameter validation; logging; unit/integration tests.
**Mathematical foundation:** Derive the equations relevant to Packages, workspaces, C++/Python nodes and testing; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build a reusable package with Python and C++ nodes, launch file, config YAML and tests.
**ROS 2 implementation:** Create a custom interface or use standard sensor_msgs/geometry_msgs; run ros2 bag record/play.
**Simulation exercise:** Run a multi-node robot telemetry pipeline and replay a bag.
**Practical assignment:** Write a test that catches invalid parameters and stale sensor timestamps.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Packages, workspaces, C++/Python nodes and testing**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: ament.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Packages, workspaces, C++/Python nodes and testing; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build a reusable package with Python and C++ nodes, launch file, config YAML and tests.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create a custom interface or use standard sensor_msgs/geometry_msgs; run ros2 bag record/play.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run a multi-node robot telemetry pipeline and replay a bag.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Write a test that catches invalid parameters and stale sensor timestamps.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [ROS 2 Jazzy tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [ROS 2 design articles](https://design.ros2.org/)
- [ros2_control documentation](https://control.ros.org/jazzy/index.html)
- [Gazebo Harmonic ROS 2 integration](https://gazebosim.org/docs/harmonic/ros2_integration/)
- [ROS 2 YouTube — nodes, topics, services, actions](https://www.youtube.com/results?search_query=ROS+2+Jazzy+complete+tutorial+nodes+topics+services+actions)
- [Articulated Robotics — ROS 2 tutorial videos](https://www.youtube.com/results?search_query=Articulated+Robotics+ROS+2+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Packages, workspaces, C++/Python nodes and testing** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Packages, workspaces, C++/Python nodes and testing; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Packages, workspaces, C++/Python nodes and testing** to a robotics engineer who has not used this technique.
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

## Week 11 — URDF, xacro, TF and robot description
**Expected outcome:** Model a robot and verify its frame tree.
**Theory syllabus:** links/joints; inertial/collision/visual geometry; xacro; robot_state_publisher; joint_state_publisher; TF tree.
**Mathematical foundation:** Derive the equations relevant to URDF, xacro, TF and robot description; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build a 2-link arm or diff-drive URDF with xacro macros and validate the TF tree.
**ROS 2 implementation:** Launch robot_state_publisher, joint_state_publisher and RViz; inspect frames.
**Simulation exercise:** View the robot in RViz and validate joint motion.
**Practical assignment:** Fix frame naming, inertial and origin mistakes using screenshots and TF output.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **URDF, xacro, TF and robot description**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: links/joints.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to URDF, xacro, TF and robot description; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build a 2-link arm or diff-drive URDF with xacro macros and validate the TF tree.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Launch robot_state_publisher, joint_state_publisher and RViz; inspect frames.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: View the robot in RViz and validate joint motion.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Fix frame naming, inertial and origin mistakes using screenshots and TF output.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [ROS 2 Jazzy tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [ROS 2 design articles](https://design.ros2.org/)
- [ros2_control documentation](https://control.ros.org/jazzy/index.html)
- [Gazebo Harmonic ROS 2 integration](https://gazebosim.org/docs/harmonic/ros2_integration/)
- [ROS 2 YouTube — nodes, topics, services, actions](https://www.youtube.com/results?search_query=ROS+2+Jazzy+complete+tutorial+nodes+topics+services+actions)
- [Articulated Robotics — ROS 2 tutorial videos](https://www.youtube.com/results?search_query=Articulated+Robotics+ROS+2+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **URDF, xacro, TF and robot description** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to URDF, xacro, TF and robot description; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **URDF, xacro, TF and robot description** to a robotics engineer who has not used this technique.
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

## Week 12 — Gazebo Harmonic and ros_gz bridge
**Expected outcome:** Connect ROS 2 control and sensing to a physics simulator.
**Theory syllabus:** physics timestep; collision/contact; sensor plugins; ros_gz_bridge; simulation time; clock and namespaces.
**Mathematical foundation:** Derive the equations relevant to Gazebo Harmonic and ros_gz bridge; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build a launch pipeline for a simulated robot with /clock, /cmd_vel and sensor bridge.
**ROS 2 implementation:** Bridge cmd_vel, joint state, IMU or LaserScan between Gazebo and ROS 2.
**Simulation exercise:** Spawn a mobile robot in a world with a wall and moving obstacle.
**Practical assignment:** Demonstrate reproducible simulated motion and save a rosbag plus world/config.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Gazebo Harmonic and ros_gz bridge**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: physics timestep.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Gazebo Harmonic and ros_gz bridge; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build a launch pipeline for a simulated robot with /clock, /cmd_vel and sensor bridge.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Bridge cmd_vel, joint state, IMU or LaserScan between Gazebo and ROS 2.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Spawn a mobile robot in a world with a wall and moving obstacle.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Demonstrate reproducible simulated motion and save a rosbag plus world/config.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [ROS 2 Jazzy tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [ROS 2 design articles](https://design.ros2.org/)
- [ros2_control documentation](https://control.ros.org/jazzy/index.html)
- [Gazebo Harmonic ROS 2 integration](https://gazebosim.org/docs/harmonic/ros2_integration/)
- [ROS 2 YouTube — nodes, topics, services, actions](https://www.youtube.com/results?search_query=ROS+2+Jazzy+complete+tutorial+nodes+topics+services+actions)
- [Articulated Robotics — ROS 2 tutorial videos](https://www.youtube.com/results?search_query=Articulated+Robotics+ROS+2+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Gazebo Harmonic and ros_gz bridge** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Gazebo Harmonic and ros_gz bridge; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Gazebo Harmonic and ros_gz bridge** to a robotics engineer who has not used this technique.
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

## Week 13 — ROS 2 control foundations and integration test
**Expected outcome:** Understand hardware interfaces and controller-manager architecture.
**Theory syllabus:** ros2_control; command/state interfaces; controller manager; joint trajectory controller; lifecycle and safety limits.
**Mathematical foundation:** Derive the equations relevant to ROS 2 control foundations and integration test; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Create or configure a mock hardware interface and controller; write integration checks.
**ROS 2 implementation:** Launch joint_state_broadcaster and a trajectory controller in simulation.
**Simulation exercise:** Move simulated joints through trajectory commands and test limit enforcement.
**Practical assignment:** Produce an end-to-end launch file with diagnostics, rosbag and clean shutdown.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **ROS 2 control foundations and integration test**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: ros2_control.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to ROS 2 control foundations and integration test; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Create or configure a mock hardware interface and controller; write integration checks.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Launch joint_state_broadcaster and a trajectory controller in simulation.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Move simulated joints through trajectory commands and test limit enforcement.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Produce an end-to-end launch file with diagnostics, rosbag and clean shutdown.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [ROS 2 Jazzy tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [ROS 2 design articles](https://design.ros2.org/)
- [ros2_control documentation](https://control.ros.org/jazzy/index.html)
- [Gazebo Harmonic ROS 2 integration](https://gazebosim.org/docs/harmonic/ros2_integration/)
- [ROS 2 YouTube — nodes, topics, services, actions](https://www.youtube.com/results?search_query=ROS+2+Jazzy+complete+tutorial+nodes+topics+services+actions)
- [Articulated Robotics — ROS 2 tutorial videos](https://www.youtube.com/results?search_query=Articulated+Robotics+ROS+2+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **ROS 2 control foundations and integration test** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to ROS 2 control foundations and integration test; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **ROS 2 control foundations and integration test** to a robotics engineer who has not used this technique.
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
**Project name:** ROS 2 simulated mobile robot system**
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

1. Explain ROS 2 nodes, topics, services and actions using one robot task example.
2. Compare reliable and best-effort QoS for camera and command streams.
3. Describe the ROS 2 executor and a callback-blocking failure mode.
4. Explain package metadata, colcon, ament and launch files.
5. Draw a URDF tree and explain visual, collision and inertial elements.
6. Explain why /tf frame names, timestamps and parent-child direction must be consistent.
7. Describe the ROS-Gazebo bridge and how /clock affects simulation time.
8. Explain command/state interfaces and controller manager in ros2_control.

### Month-specific interview questions

1. How would you diagnose a topic that appears but does not deliver messages?
2. When should a ROS 2 action be used instead of a service?
3. How do you select QoS for a high-rate sensor?
4. How do you test ROS nodes without Gazebo running?
5. What errors can an incorrect URDF inertial tensor cause?
6. How do you debug a broken TF tree?
7. Why is simulation time important for Nav2 and sensor fusion?
8. How would you design a ROS 2 hardware abstraction for a motor controller?

## Month-end interview question bank
1. Explain **ROS 2 Core, Linux Tooling, URDF and Gazebo Integration** as though you are in a technical interview.
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
| 09 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 10 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 11 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 12 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 13 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
