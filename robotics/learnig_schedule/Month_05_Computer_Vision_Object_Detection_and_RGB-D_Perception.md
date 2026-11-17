# Robotics & Physical AI — Month 05: Computer Vision, Object Detection and RGB-D Perception

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
By the end of Month 5, you should be able to explain, implement and defend the following: 
- Primary focus: **Computer Vision, Object Detection and RGB-D Perception**.
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

- **Pinhole projection:** u=fₓX/Z+cₓ, v=fᵧY/Z+cᵧ. For known intrinsics, project a 3D point and back-project using depth.
- **Detection evaluation:** Explain why a high confidence score does not imply a correct detection. Calculate IoU and distinguish precision, recall and mAP.
- **RGB-D localization:** Convert a detection centre (u,v) and depth Z to camera-frame XYZ, then apply T_base_camera. State the calibration and synchronization assumptions.

## Weekly training blocks
## Week 18 — Image formation and OpenCV fundamentals
**Expected outcome:** Understand pixels, image geometry and camera calibration.
**Theory syllabus:** pinhole model; intrinsic/extrinsic matrices; distortion; color spaces; filtering; edges; contours.
**Mathematical foundation:** Derive the equations relevant to Image formation and OpenCV fundamentals; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Build image processing scripts; calibrate a webcam; undistort images and quantify reprojection error.
**ROS 2 implementation:** Publish camera images using sensor_msgs/Image and camera_info; inspect image topics.
**Simulation exercise:** Use a simulated camera feed and visualize image processing outputs.
**Practical assignment:** Calibrate camera with checkerboard and document reprojection error.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Image formation and OpenCV fundamentals**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: pinhole model.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Image formation and OpenCV fundamentals; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Build image processing scripts; calibrate a webcam; undistort images and quantify reprojection error.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Publish camera images using sensor_msgs/Image and camera_info; inspect image topics.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Use a simulated camera feed and visualize image processing outputs.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Calibrate camera with checkerboard and document reprojection error.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenCV official tutorials](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
- [OpenCV Bootcamp (free)](https://opencv.org/opencv-free-course/)
- [Ultralytics YOLO documentation](https://docs.ultralytics.com/)
- [Intel RealSense ROS 2 documentation](https://github.com/IntelRealSense/realsense-ros)
- [ROS image_pipeline documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/image_pipeline/)
- [YouTube — camera calibration, OpenCV and object detection](https://www.youtube.com/results?search_query=OpenCV+camera+calibration+object+detection+YOLO+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Image formation and OpenCV fundamentals** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Image formation and OpenCV fundamentals; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Image formation and OpenCV fundamentals** to a robotics engineer who has not used this technique.
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

## Week 19 — Feature extraction, geometry and tracking
**Expected outcome:** Extract useful visual features and estimate motion.
**Theory syllabus:** corners; descriptors; matching; optical flow; homography; epipolar geometry introduction; tracking.
**Mathematical foundation:** Derive the equations relevant to Feature extraction, geometry and tracking; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Implement feature matching and optical flow; compare outlier rejection methods.
**ROS 2 implementation:** Use image_pipeline/cv_bridge to connect OpenCV processing to ROS 2.
**Simulation exercise:** Track a moving object in a Gazebo camera stream.
**Practical assignment:** Estimate planar motion of a calibration target and explain failure cases.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Feature extraction, geometry and tracking**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: corners.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Feature extraction, geometry and tracking; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Implement feature matching and optical flow; compare outlier rejection methods.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Use image_pipeline/cv_bridge to connect OpenCV processing to ROS 2.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Track a moving object in a Gazebo camera stream.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Estimate planar motion of a calibration target and explain failure cases.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenCV official tutorials](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
- [OpenCV Bootcamp (free)](https://opencv.org/opencv-free-course/)
- [Ultralytics YOLO documentation](https://docs.ultralytics.com/)
- [Intel RealSense ROS 2 documentation](https://github.com/IntelRealSense/realsense-ros)
- [ROS image_pipeline documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/image_pipeline/)
- [YouTube — camera calibration, OpenCV and object detection](https://www.youtube.com/results?search_query=OpenCV+camera+calibration+object+detection+YOLO+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Feature extraction, geometry and tracking** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Feature extraction, geometry and tracking; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Feature extraction, geometry and tracking** to a robotics engineer who has not used this technique.
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

## Week 20 — YOLO detection and dataset evaluation
**Expected outcome:** Train or fine-tune an object detector and evaluate it correctly.
**Theory syllabus:** bounding boxes; IoU; precision/recall; mAP; class imbalance; train/val/test split; overfitting.
**Mathematical foundation:** Derive the equations relevant to YOLO detection and dataset evaluation; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Annotate a small dataset; run pretrained YOLO; train a small custom class detector; produce confusion matrix.
**ROS 2 implementation:** Wrap detector in a ROS 2 node that publishes detections with timestamps.
**Simulation exercise:** Run detection against varied simulated lighting, scale and occlusion.
**Practical assignment:** Compare pretrained baseline with fine-tuned model using a held-out test set.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **YOLO detection and dataset evaluation**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: bounding boxes.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to YOLO detection and dataset evaluation; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Annotate a small dataset; run pretrained YOLO; train a small custom class detector; produce confusion matrix.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Wrap detector in a ROS 2 node that publishes detections with timestamps.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Run detection against varied simulated lighting, scale and occlusion.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Compare pretrained baseline with fine-tuned model using a held-out test set.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenCV official tutorials](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
- [OpenCV Bootcamp (free)](https://opencv.org/opencv-free-course/)
- [Ultralytics YOLO documentation](https://docs.ultralytics.com/)
- [Intel RealSense ROS 2 documentation](https://github.com/IntelRealSense/realsense-ros)
- [ROS image_pipeline documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/image_pipeline/)
- [YouTube — camera calibration, OpenCV and object detection](https://www.youtube.com/results?search_query=OpenCV+camera+calibration+object+detection+YOLO+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **YOLO detection and dataset evaluation** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to YOLO detection and dataset evaluation; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **YOLO detection and dataset evaluation** to a robotics engineer who has not used this technique.
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

## Week 21 — Depth cameras, point clouds and 3D perception
**Expected outcome:** Convert RGB-D observations into 3D object locations.
**Theory syllabus:** depth units; point clouds; camera projection; depth holes; transforms; voxelization; filtering; segmentation.
**Mathematical foundation:** Derive the equations relevant to Depth cameras, point clouds and 3D perception; define every symbol and unit, state assumptions, and verify one numerical example.
**Coding exercise:** Project depth pixels to 3D; filter a point cloud; estimate centroid and bounding box.
**ROS 2 implementation:** Subscribe to aligned RGB/depth and PointCloud2 topics; transform detections to base frame.
**Simulation exercise:** Use a simulated RGB-D camera to locate objects relative to robot base.
**Practical assignment:** Report median 3D localization error across known object positions.

### Day-by-day schedule
**Monday — concepts and baseline (1–1.5h)**  
Read the core theory for **Depth cameras, point clouds and 3D perception**. Write a one-page concept map. Define 5 terms in your own words. Baseline task: depth units.
**Tuesday — mathematics and derivation (1–1.5h)**  
Work through the mathematical foundations: Derive the equations relevant to Depth cameras, point clouds and 3D perception; define every symbol and unit, state assumptions, and verify one numerical example.. Hand-derive one small example, state assumptions, and verify units/dimensions.
**Wednesday — coding lab (1–1.5h)**  
Implement: Project depth pixels to 3D; filter a point cloud; estimate centroid and bounding box.. Add at least 3 tests (nominal, boundary, invalid input) and a plot or structured log.
**Thursday — robotics middleware (1–1.5h)**  
ROS 2 exercise: Subscribe to aligned RGB/depth and PointCloud2 topics; transform detections to base frame.. If ROS 2 is not yet installed, write the node/interface contract and run a Python mock; do not skip the design.
**Friday — simulation and debugging (1–1.5h)**  
Simulation exercise: Use a simulated RGB-D camera to locate objects relative to robot base.. Record expected vs observed behavior and at least one failure/edge case.
**Saturday — integrated practical (4–5h)**  
Build the integrated artifact: Report median 3D localization error across known object positions.. Include reproducible setup, a short demo, parameters/configuration, and a README. Spend at least 60 minutes debugging an intentionally varied condition.
**Sunday — assessment and revision (4–5h)**  
Take the weekly written exam below closed-book, answer the interview questions aloud, revise errors, update your notes, and write a 150–250 word engineering retrospective.

### Weekly learning resources
- [OpenCV official tutorials](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
- [OpenCV Bootcamp (free)](https://opencv.org/opencv-free-course/)
- [Ultralytics YOLO documentation](https://docs.ultralytics.com/)
- [Intel RealSense ROS 2 documentation](https://github.com/IntelRealSense/realsense-ros)
- [ROS image_pipeline documentation](https://docs.ros.org/en/ros2_packages/jazzy/api/image_pipeline/)
- [YouTube — camera calibration, OpenCV and object detection](https://www.youtube.com/results?search_query=OpenCV+camera+calibration+object+detection+YOLO+tutorial)

### Weekly written exam (suggested: 45–60 minutes; 20 points)
1. Define and explain the key ideas in **Depth cameras, point clouds and 3D perception** without copying a textbook definition.
2. Derive or calculate a small example using: **Derive the equations relevant to Depth cameras, point clouds and 3D perception; define every symbol and unit, state assumptions, and verify one numerical example.**. Show each step and state assumptions.
3. Draw a block diagram or data-flow diagram for the week’s system and label signals, frames, units and timing.
4. Identify two failure modes in the practical assignment and explain how you would detect each one.
5. Explain the difference between an ideal/theoretical model and the implementation you coded.
6. Read your own code: explain its algorithm, complexity or runtime bottleneck, and one test that protects it.
7. **Applied problem:** change one operating condition (noise, geometry, sample rate, load, obstacle or task goal as appropriate). Predict the effect, then verify it experimentally.
8. Write a concise engineering note (150–250 words): what worked, what failed, evidence, and next action.

### Weekly interview drill (answer aloud; 8–12 minutes)
1. Teach **Depth cameras, point clouds and 3D perception** to a robotics engineer who has not used this technique.
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
**Project name:** RGB-D object detection and 3D localization pipeline**
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

1. Derive the pinhole-camera projection equations and explain camera intrinsics.
2. What do radial and tangential distortion parameters represent?
3. Calculate IoU for two bounding boxes and interpret the result.
4. Distinguish precision, recall, AP and mAP.
5. Explain why dataset leakage produces misleading validation scores.
6. Back-project a pixel and depth value into 3D camera coordinates.
7. Transform a 3D detection into the robot base frame and list calibration assumptions.
8. Explain how you would synchronize image and depth streams.

### Month-specific interview questions

1. What is the difference between camera intrinsic and extrinsic calibration?
2. How can a detector have high confidence but poor localization?
3. How do you select an IoU threshold?
4. What causes false negatives under occlusion or lighting changes?
5. How do you convert a depth pixel into a 3D point?
6. Why must RGB, depth, CameraInfo and TF timestamps be consistent?
7. How do you evaluate synthetic-trained perception on real data?
8. How would you design a ROS 2 perception node with bounded latency?

## Month-end interview question bank
1. Explain **Computer Vision, Object Detection and RGB-D Perception** as though you are in a technical interview.
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
| 18 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 19 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 20 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |
| 21 | 19 | ___ | ___ | ___ | ___ | ___ | Not started |

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
