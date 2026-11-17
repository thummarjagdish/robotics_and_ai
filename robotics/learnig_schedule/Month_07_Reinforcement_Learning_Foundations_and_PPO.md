# Robotics & Physical AI — Month 07: Reinforcement Learning Foundations and PPO

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
By the end of Month 7, you should be able to explain, implement and defend the following: 
- Primary focus: **Reinforcement Learning Foundations and PPO**.
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

- **MDP example:** For a grid robot, define states, actions, transition probabilities, rewards, discount and terminal states. Show one Bellman update.
- **Policy gradient:** Explain why the gradient uses log π(a|s) multiplied by return/advantage. Explain baseline subtraction.
- **PPO clipping:** Given probability ratio r and advantage A, compute the clipped surrogate term and explain why clipping limits destructive policy updates.

## Weekly training blocks
## Week 27 — MDPs, returns, value functions and Bellman equations
**Expected outcome:** Formalize robot learning as sequential decision making.
**Theory syllabus:** state/action/reward; policy; transition; discount; return; value/Q; Bellman expectation/optimality.
**Mathematical foundation:** Derive the equations relevant to MDPs, returns, value functions and Bellman equations; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement tabular value iteration and Q-learning on a small gridworld.
**ROS 2 implementation:** Wrap a simple ROS-like robot task behind reset/step abstractions; no physical actuation.
**Simulation exercise:** Run gridworld and a simple continuous-control benchmark.
**Practical assignment:** Show how reward design changes behavior and explain reward hacking.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **MDPs, returns, value functions and Bellman equations**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: state/action/reward.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to MDPs, returns, value functions and Bellman equations; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement tabular value iteration and Q-learning on a small gridworld.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Wrap a simple ROS-like robot task behind reset/step abstractions; no physical actuation.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run gridworld and a simple continuous-control benchmark.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Show how reward design changes behavior and explain reward hacking.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
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
1. Define and explain the key ideas in **MDPs, returns, value functions and Bellman equations** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to MDPs, returns, value functions and Bellman equations; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **MDPs, returns, value functions and Bellman equations** to a robotics engineer who has not used this technique.
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

## Week 28 — Policy gradients and actor-critic
**Expected outcome:** Understand stochastic policies and gradient-based learning.
**Theory syllabus:** REINFORCE; log probability; baseline; advantage; actor-critic; entropy regularization.
**Mathematical foundation:** Derive the equations relevant to Policy gradients and actor-critic; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement REINFORCE and a simple actor-critic baseline in PyTorch.
**ROS 2 implementation:** Design a simulated action interface; record policy observations/actions and episode outcomes.
**Simulation exercise:** Train on CartPole or a simple pendulum task.
**Practical assignment:** Compare learning curves across random seeds and report mean/std.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Policy gradients and actor-critic**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: REINFORCE.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Policy gradients and actor-critic; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement REINFORCE and a simple actor-critic baseline in PyTorch.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Design a simulated action interface; record policy observations/actions and episode outcomes.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Train on CartPole or a simple pendulum task.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Compare learning curves across random seeds and report mean/std.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
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
1. Define and explain the key ideas in **Policy gradients and actor-critic** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Policy gradients and actor-critic; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Policy gradients and actor-critic** to a robotics engineer who has not used this technique.
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

## Week 29 — PPO algorithm and implementation
**Expected outcome:** Implement clipping, advantage estimation and update loops.
**Theory syllabus:** surrogate objective; ratio; clipping; GAE; value loss; entropy; minibatches; rollout buffer.
**Mathematical foundation:** Derive the equations relevant to PPO algorithm and implementation; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Train PPO with Stable-Baselines3, then inspect or implement a minimal PPO update loop.
**ROS 2 implementation:** Export policy inference behind a ROS 2 service/action mock; add rate and bounds checks.
**Simulation exercise:** Train a continuous-control task and visualize policy behavior.
**Practical assignment:** Run ablations on clip range, learning rate or reward scaling.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **PPO algorithm and implementation**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: surrogate objective.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to PPO algorithm and implementation; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Train PPO with Stable-Baselines3, then inspect or implement a minimal PPO update loop.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Export policy inference behind a ROS 2 service/action mock; add rate and bounds checks.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Train a continuous-control task and visualize policy behavior.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Run ablations on clip range, learning rate or reward scaling.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
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
1. Define and explain the key ideas in **PPO algorithm and implementation** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to PPO algorithm and implementation; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **PPO algorithm and implementation** to a robotics engineer who has not used this technique.
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

## Week 30 — Reward engineering, robustness and evaluation
**Expected outcome:** Evaluate policies beyond one successful rollout.
**Theory syllabus:** reward decomposition; termination; curriculum; random seeds; domain randomization; success metrics.
**Mathematical foundation:** Derive the equations relevant to Reward engineering, robustness and evaluation; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build evaluation scripts for success, return, energy/effort and constraint violations.
**ROS 2 implementation:** Create a ROS 2 policy wrapper with watchdog and safe fallback.
**Simulation exercise:** Test policy under randomized mass, friction, latency or observation noise.
**Practical assignment:** Deliver reproducible PPO experiment with config, checkpoints and evaluation table.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Reward engineering, robustness and evaluation**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: reward decomposition.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Reward engineering, robustness and evaluation; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build evaluation scripts for success, return, energy/effort and constraint violations.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Create a ROS 2 policy wrapper with watchdog and safe fallback.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Test policy under randomized mass, friction, latency or observation noise.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Deliver reproducible PPO experiment with config, checkpoints and evaluation table.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
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
1. Define and explain the key ideas in **Reward engineering, robustness and evaluation** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Reward engineering, robustness and evaluation; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Reward engineering, robustness and evaluation** to a robotics engineer who has not used this technique.
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
**Project name:** PPO-trained simulated control policy**
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

1. Define an MDP for a mobile robot and state S, A, P, R and γ.
2. Perform one Bellman update for a small discrete state example.
3. Derive the REINFORCE policy-gradient estimator at a high level.
4. Explain why a baseline reduces variance without biasing the policy gradient.
5. Write the PPO probability ratio and clipped surrogate objective.
6. Explain generalized advantage estimation and its bias/variance trade-off.
7. Design a reward function and identify two reward-hacking risks.
8. Compare learning curves over multiple seeds and explain why one run is insufficient.

### Month-specific interview questions

1. What makes a problem an MDP?
2. Explain value function vs Q-function.
3. Why use stochastic policies in policy-gradient methods?
4. What is the purpose of advantage estimation?
5. What does PPO clipping protect against?
6. How does reward scale affect training?
7. What is the difference between episode return and task success rate?
8. How would you know a policy learned a robust behavior rather than exploiting the simulator?

## Month-end interview question bank
1. Explain **Reinforcement Learning Foundations and PPO** as though you are in a technical interview.
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
| 27 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 28 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 29 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 30 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
