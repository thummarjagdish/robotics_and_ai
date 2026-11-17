# Robotics & Physical AI — Month 08: Continuous-Control RL, SAC, Imitation Learning and Isaac Lab

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
By the end of Month 8, you should be able to explain, implement and defend the following: 
- Primary focus: **Continuous-Control RL, SAC, Imitation Learning and Isaac Lab**.
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

- **PPO vs SAC:** Compare on-policy/off-policy data, stochastic policy, replay buffer, entropy and continuous action handling.
- **Behavior cloning:** Train on expert state-action pairs and explain covariate shift when the learner visits states absent from demonstrations.
- **Sim-to-real:** List mass, friction, actuator delay, sensor bias and camera variations to randomize; explain which measurements could calibrate each.

## Weekly training blocks
## Week 31 — Continuous action spaces and SAC theory
**Expected outcome:** Understand off-policy learning and entropy-regularized control.
**Theory syllabus:** Gaussian policies; squashing; replay buffer; twin Q; target networks; entropy temperature.
**Mathematical foundation:** Derive the equations relevant to Continuous action spaces and SAC theory; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Train SAC on Pendulum; plot return, entropy and Q estimates; compare seeds.
**ROS 2 implementation:** Build a safe policy adapter with joint/velocity limits and emergency stop semantics.
**Simulation exercise:** Evaluate SAC on continuous-control benchmarks.
**Practical assignment:** Explain PPO vs SAC in terms of data use, stability and action spaces.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Continuous action spaces and SAC theory**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: Gaussian policies.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Continuous action spaces and SAC theory; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Train SAC on Pendulum; plot return, entropy and Q estimates; compare seeds.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Build a safe policy adapter with joint/velocity limits and emergency stop semantics.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Evaluate SAC on continuous-control benchmarks.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Explain PPO vs SAC in terms of data use, stability and action spaces.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Gymnasium documentation](https://gymnasium.farama.org/)
- [Stable-Baselines3 documentation](https://stable-baselines3.readthedocs.io/)
- [PPO paper — Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
- [SAC paper — Soft Actor-Critic Algorithms and Applications](https://arxiv.org/abs/1812.05905)
- [Spinning Up in Deep RL](https://spinningup.openai.com/en/latest/)
- [YouTube — PPO and SAC explained](https://www.youtube.com/results?search_query=reinforcement+learning+PPO+SAC+robotics+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Continuous action spaces and SAC theory** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Continuous action spaces and SAC theory; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Continuous action spaces and SAC theory** to a robotics engineer who has not used this technique.
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

## Week 32 — Demonstrations, behavior cloning and dataset quality
**Expected outcome:** Learn from expert trajectories before trial-and-error RL.
**Theory syllabus:** supervised imitation; state/action pairing; covariate shift; DAgger concept; dataset balance.
**Mathematical foundation:** Derive the equations relevant to Demonstrations, behavior cloning and dataset quality; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Collect scripted demonstrations; train a behavior-cloning baseline; measure compounding error.
**ROS 2 implementation:** Record ROS 2 joint/pose/action messages to a documented dataset format.
**Simulation exercise:** Replay demonstrations in a simulator and compare policy rollout.
**Practical assignment:** Deliver train/validation split, dataset schema and baseline metric.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Demonstrations, behavior cloning and dataset quality**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: supervised imitation.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Demonstrations, behavior cloning and dataset quality; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Collect scripted demonstrations; train a behavior-cloning baseline; measure compounding error.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Record ROS 2 joint/pose/action messages to a documented dataset format.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Replay demonstrations in a simulator and compare policy rollout.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Deliver train/validation split, dataset schema and baseline metric.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [Gymnasium documentation](https://gymnasium.farama.org/)
- [Stable-Baselines3 documentation](https://stable-baselines3.readthedocs.io/)
- [PPO paper — Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
- [SAC paper — Soft Actor-Critic Algorithms and Applications](https://arxiv.org/abs/1812.05905)
- [Spinning Up in Deep RL](https://spinningup.openai.com/en/latest/)
- [YouTube — PPO and SAC explained](https://www.youtube.com/results?search_query=reinforcement+learning+PPO+SAC+robotics+lecture)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Demonstrations, behavior cloning and dataset quality** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Demonstrations, behavior cloning and dataset quality; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Demonstrations, behavior cloning and dataset quality** to a robotics engineer who has not used this technique.
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

## Week 33 — Isaac Lab environments and robot learning workflow
**Expected outcome:** Build or modify a vectorized robot learning task.
**Theory syllabus:** task config; scene; articulation; observations; actions; reward/termination; reset; vectorized environments.
**Mathematical foundation:** Derive the equations relevant to Isaac Lab environments and robot learning workflow; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Follow official Isaac Lab cartpole or locomotion task; modify one observation or reward term.
**ROS 2 implementation:** Understand the boundary between ROS 2 runtime and offline training; define observation/action contract.
**Simulation exercise:** Run a provided Isaac Lab task; record throughput and environment config.
**Practical assignment:** Reproduce a baseline training run and save checkpoints/logs.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Isaac Lab environments and robot learning workflow**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: task config.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Isaac Lab environments and robot learning workflow; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Follow official Isaac Lab cartpole or locomotion task; modify one observation or reward term.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Understand the boundary between ROS 2 runtime and offline training; define observation/action contract.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run a provided Isaac Lab task; record throughput and environment config.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Reproduce a baseline training run and save checkpoints/logs.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [NVIDIA Isaac Lab documentation](https://docs.nvidia.com/isaaclab/isaac-lab)
- [Isaac Lab GitHub repository](https://github.com/isaac-sim/IsaacLab)
- [NVIDIA Isaac Lab overview](https://developer.nvidia.com/isaac/lab)
- [NVIDIA Isaac Sim learning material](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/index.html)
- [YouTube — Isaac Lab reinforcement learning tutorials](https://www.youtube.com/results?search_query=NVIDIA+Isaac+Lab+reinforcement+learning+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Isaac Lab environments and robot learning workflow** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Isaac Lab environments and robot learning workflow; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Isaac Lab environments and robot learning workflow** to a robotics engineer who has not used this technique.
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

## Week 34 — Train and evaluate PPO/SAC-style robot policies in Isaac Lab
**Expected outcome:** Use a scalable simulator for robot policy training.
**Theory syllabus:** parallel simulation; normalization; curriculum; domain randomization; checkpoint evaluation; sim-to-real gap.
**Mathematical foundation:** Derive the equations relevant to Train and evaluate PPO/SAC-style robot policies in Isaac Lab; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Train a policy for a supported task; compare at least two configurations.
**ROS 2 implementation:** Create an inference-only ROS 2 bridge prototype for policy commands in a mock robot.
**Simulation exercise:** Evaluate in unseen randomized scenarios and compare against nominal scenarios.
**Practical assignment:** Prepare experiment report with hardware/GPU, versions, seeds and metrics.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Train and evaluate PPO/SAC-style robot policies in Isaac Lab**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: parallel simulation.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Train and evaluate PPO/SAC-style robot policies in Isaac Lab; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Train a policy for a supported task; compare at least two configurations.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create an inference-only ROS 2 bridge prototype for policy commands in a mock robot.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Evaluate in unseen randomized scenarios and compare against nominal scenarios.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Prepare experiment report with hardware/GPU, versions, seeds and metrics.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [NVIDIA Isaac Lab documentation](https://docs.nvidia.com/isaaclab/isaac-lab)
- [Isaac Lab GitHub repository](https://github.com/isaac-sim/IsaacLab)
- [NVIDIA Isaac Lab overview](https://developer.nvidia.com/isaac/lab)
- [NVIDIA Isaac Sim learning material](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/index.html)
- [YouTube — Isaac Lab reinforcement learning tutorials](https://www.youtube.com/results?search_query=NVIDIA+Isaac+Lab+reinforcement+learning+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Train and evaluate PPO/SAC-style robot policies in Isaac Lab** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Train and evaluate PPO/SAC-style robot policies in Isaac Lab; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Train and evaluate PPO/SAC-style robot policies in Isaac Lab** to a robotics engineer who has not used this technique.
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

## Week 35 — Sim-to-real readiness and safety case
**Expected outcome:** Identify what must be validated before deploying learned control.
**Theory syllabus:** actuator mismatch; latency; sensor noise; randomization; residual control; safety envelope; rollback.
**Mathematical foundation:** Derive the equations relevant to Sim-to-real readiness and safety case; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement action clipping, rate limits and policy confidence/fallback handling.
**ROS 2 implementation:** Use lifecycle/enable state and watchdog in a policy gateway; never connect an unvalidated policy to hazardous hardware.
**Simulation exercise:** Stress test perturbations and actuator limits in simulation.
**Practical assignment:** Create a deployment-readiness checklist and risk register.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Sim-to-real readiness and safety case**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: actuator mismatch.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Sim-to-real readiness and safety case; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement action clipping, rate limits and policy confidence/fallback handling.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Use lifecycle/enable state and watchdog in a policy gateway; never connect an unvalidated policy to hazardous hardware.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Stress test perturbations and actuator limits in simulation.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Create a deployment-readiness checklist and risk register.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [NVIDIA Isaac Lab documentation](https://docs.nvidia.com/isaaclab/isaac-lab)
- [Isaac Lab GitHub repository](https://github.com/isaac-sim/IsaacLab)
- [NVIDIA Isaac Lab overview](https://developer.nvidia.com/isaac/lab)
- [NVIDIA Isaac Sim learning material](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/index.html)
- [YouTube — Isaac Lab reinforcement learning tutorials](https://www.youtube.com/results?search_query=NVIDIA+Isaac+Lab+reinforcement+learning+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Sim-to-real readiness and safety case** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Sim-to-real readiness and safety case; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Sim-to-real readiness and safety case** to a robotics engineer who has not used this technique.
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
**Project name:** SAC/behavior-cloning policy training in Isaac Lab**
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

1. Write the SAC maximum-entropy objective and explain the entropy term.
2. Explain the role of twin Q networks and target networks.
3. Compare on-policy PPO with off-policy SAC in sample reuse.
4. Explain behavior cloning and covariate shift.
5. Design a data schema for observation-action demonstrations.
6. Explain Isaac Lab environment components: scene, observations, actions, reward, termination and reset.
7. Design domain randomization for mass, friction, delay and sensor noise.
8. Write a sim-to-real readiness checklist with at least five validation gates.

### Month-specific interview questions

1. Why is entropy maximized in SAC?
2. What is a replay buffer and why does SAC use one?
3. Why can behavior cloning fail after small deviations from demonstrations?
4. What is a vectorized environment and what is the benefit?
5. How do you keep action scaling consistent between training and deployment?
6. How would you compare policies fairly across random seeds?
7. What does domain randomization compensate for—and what can it not fix?
8. What safety layer should wrap a learned robot policy?

## Month-end interview question bank
1. Explain **Continuous-Control RL, SAC, Imitation Learning and Isaac Lab** as though you are in a technical interview.
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
| 31 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 32 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 33 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 34 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 35 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
