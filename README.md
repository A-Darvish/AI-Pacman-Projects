# AI Pacman Projects

This repository contains two projects developed as part of the UC Berkeley AI course. These projects demonstrate the application of various Artificial Intelligence (AI) techniques to enable the Pacman agent to efficiently win the game and track ghosts.

## Overview

The projects leverage a range of AI algorithms and methodologies, including:

### Search Algorithms
- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **Uniform Cost Search (UCS)**
- **A\* Search**

### Adversarial Search
- **Reflex Agent**
- **Minimax Algorithm**
- **Alpha-Beta Pruning**
- **Expectimax Algorithm**

### Markov Decision Processes (MDP) and Reinforcement Learning
- **Asynchronous Value Iteration**
- **Prioritized Sweeping Value Iteration**
- **Q-Learning**
- **Approximate Q-Learning**

### Ghost Tracking and Probabilistic Models
- **Bayesian Network (BN)**
  - Exact and Approximate Inference
- **Posterior Belief Computation**
- **Particle Filtering Algorithm**

## Features

1. **Pacman Gameplay AI**
   - Efficiently navigates the game using search and decision-making algorithms.
   - Handles both deterministic and stochastic scenarios.

2. **Ghost Tracking**
   - Tracks ghost positions probabilistically using particle filtering and Bayesian inference.

3. **Reinforcement Learning**
   - Adapts the Pacman agent’s behavior over time using Q-learning and approximate methods.

4. **Adversarial Agents**
   - Implements game-playing strategies using Minimax, Alpha-Beta Pruning, and Expectimax.

## Project Structure

The repository is organized as follows:

```
|-- Project 1: Search and Adversarial AI
    |-- search.py
    |-- searchAgents.py
    |-- multiAgents.py
    |-- ...

|-- Project 2: Ghost Tracking and Reinforcement Learning
    |-- inference.py
    |-- valueIterationAgents.py
    |-- qlearningAgents.py
    |-- ...

|-- README.md
```

## Prerequisites

- **Python 3.x**
- Recommended: A virtual environment with required libraries installed.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/A-Darvish/AI-Pacman-Projects.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AI_Pacman_Projects
   ```

3. Run specific modules to test different functionalities:
   ```bash
   python pacman.py -p SearchAgent -a fn=ucs
   ```
   Example: Running the Pacman agent with Uniform Cost Search (UCS).

4. For more examples and options:
   ```bash
   python pacman.py -h
   ```

## Credits

These projects are based on the **UC Berkeley AI Course** and were developed as part of the course’s programming assignments.

