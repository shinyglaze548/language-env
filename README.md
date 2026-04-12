
# 🌍 AI Language Tutor Environment

## 📌 Overview
This project implements a Reinforcement Learning-style environment for language learning.  
The environment simulates a tutor helping a user learn English ↔ Spanish through structured tasks.

---

## 🚀 Features
- RL-style environment with `reset`, `step`, and `state`
- 3 difficulty levels:
  - 🟢 Easy: Vocabulary translation
  - 🟡 Medium: Sentence translation (partial rewards)
  - 🔴 Hard: Conversation handling
- Deterministic reward system (0.0 – 1.0)
- Lightweight and fast (no heavy dependencies)

---

## 🧠 Environment Design

Each step:
1. The environment provides a task (observation)
2. The agent selects an action (answer)
3. The environment returns:
   - Next observation
   - Reward
   - Done flag

---

## 🧪 Task Details

### 1. Vocabulary (Easy)
Translate single words  
Example: *Hola → Hello*

### 2. Sentence Translation (Medium)
Translate sentences with partial reward support  

### 3. Conversation (Hard)
Select correct response from multiple options  

---

## 🎯 Reward System

| Case | Reward |
|------|--------|
| Correct | 1.0 |
| Partially correct | 0.5 |
| Incorrect | 0.0 |

---
## 🌱 Journey

Started with little to no prior experience in building or deploying RL environments

Faced multiple errors across setup, API integration, and deployment

Learned step-by-step through debugging and iteration

Gradually understood how different components (environment, API, deployment) connect

Successfully built, fixed, and deployed a working project under time pressure

## ⚙️ How to Run

```bash
python inference.py

