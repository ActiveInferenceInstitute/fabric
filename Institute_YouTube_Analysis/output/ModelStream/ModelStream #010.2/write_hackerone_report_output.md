```
**Title:** Introduction of RX Environments for Reactive Agent Development in Active Inference

## Summary:
The RX Environments package provides a lightweight framework for creating reactive environments that enable the development of agents in a multi-agent setting. It complements the RX Infer package by allowing entities to communicate and interact in real time, breaking away from the constraints of traditional reinforcement learning models.

## Description:
RX Environments is designed to facilitate the creation of environments that support reactive behavior, allowing agents to communicate and act independently at any moment. Unlike traditional reinforcement learning frameworks, such as Gymnasium, which require synchronized actions and observations, RX Environments permits asynchronous interactions between agents and their environments. 

In the demo presented, a Mountain Car environment showcases the capability of controlling multiple agents in real time. Each agent can send commands to the environment, resulting in immediate changes to their state. This reactive design mirrors the principles of active inference, where the interior state of each entity is influenced by its interactions with external factors.

The package is intended to be used alongside RX Infer, but it can also function independently for those who wish to create agents without the need for Bayesian inference.

## Steps To Reproduce:
1. Install the RX Environments package and its dependencies.
2. Create a Mountain Car environment using the provided boilerplate code.
3. Initialize two agents within the environment and send commands to control their engine force.
4. Observe the agents' responses in real time as you adjust their commands.

## Supporting Material/References:

## Impact:
The introduction of RX Environments significantly enhances the flexibility and capability of agent-based modeling in active inference. By allowing asynchronous communication and real-time interaction, it opens new avenues for research and application in robotics, reinforcement learning, and multi-agent systems, potentially leading to more robust and adaptive behaviors in real-world applications.
```
