**Refined Text:**

Hello and welcome. Today is September 13, 2024, and we are engaged in Active Inference Model Stream 14.1 with Ranway, discussing the value of information and reward specification in active inference. The session will include a presentation followed by a discussion, and we look forward to your comments and questions. Thank you for joining us; we anticipate an enlightening presentation.

I will proceed directly to the presentation. Thank you once again for the invitation. This paper addresses the value of information and aspects of reward specification within active inference, while also touching on predictive dynamics (PD) and predictive coding (PC). The motivation behind this work is straightforward: to comprehend the expected free energy (EF) objective for action planning in active inference. 

The appeal of the EF objective lies in its intuitive decomposition into an expected value term and an epistemic value term. The expected value term encourages the agent to obtain rewards or reach their preferred state in the world, represented as the cross-entropy between predicted future observations given certain actions and the preferred observations. The epistemic value term adds complexity to active inference and is defined as the expected Kullback-Leibler divergence between the future posterior (belief about future states based on future observations) and the predicted distribution of future states. This term quantifies the distance between the future posterior and prior, essentially measuring the amount of belief update. Optimizing this term encourages agents to take actions that maximize the information gained about their environment.

Empirical studies have demonstrated that optimizing this objective leads to intriguing behaviors. For instance, one example from Alex's research compares the state coverage of reward-maximizing agents and active inference agents in a simple environment known as "Mountain Car," where the agent's state is characterized by its position and velocity. The results show that active inference agents cover a significantly larger portion of the state space than their reward-maximizing counterparts. This broader coverage allows agents to develop a more comprehensive model of their environment, which subsequently enhances action selection and increases reward acquisition.

Another example from my own research examines human driving behavior, involving an "ego vehicle" navigating a road alongside a large truck that obscures the view of a potential pedestrian. The ego vehicle, assuming the pedestrian may cross the road, slightly veers left to gain visibility. If it determines that the pedestrian does not exist, it returns to the center of the road and continues at optimal speed without stopping. Such behaviors underscore the importance of encouraging agents to explore and acquire information about their environment, which distinguishes active inference from other decision-making frameworks, such as reinforcement learning (RL).

However, it is worth noting that Bayesian and meta reinforcement learning are known to optimally balance exploration and exploitation. For instance, a common benchmark in meta reinforcement learning involves initializing an agent at the center of a circle, with an unknown goal position along the circumference. The agent must explore the circle to locate the goal, demonstrating a strategy that has already been achieved by meta RL approaches. This raises an important question regarding the relationship between active inference and Bayesian approaches.

The main insight of this paper posits that the expected free energy can be understood as an approximation of the optimal Bayesian RL policy, specifically through the lens of information reward shaping within the EF objective. To elaborate on this, I will provide a brief overview of foundational concepts in Markov Decision Processes (MDPs) and active inference before introducing analytical tools from MDP theory. These tools will enhance our understanding of the value of information and allow us to derive the paper's key findings.

The preliminaries will be concise, as I believe most attendees are already familiar with these topics. The standard formalism for MDPs indicates that an agent's objective is typically to maximize discounted cumulative rewards. I have chosen to utilize an infinite horizon setting with discounting for the sake of analytical simplicity. Notably, classic MDP theory asserts that for any given MDP with known transition probabilities and a known reward function, at least one deterministic stationary Markovian policy exists. The value function associated with the policy can be computed using Bellman equations.

Another essential component is the partially observable MDP (POMDP), which extends MDPs by introducing state variables that are not directly observable to the agent. The agent can, however, observe another correlated signal. Consequently, the optimal policy for POMDPs must be conditioned on the entire history of observations, which can become infinite as time progresses. A crucial result from POMDP theory is that the belief state, derived from the Bayesian belief update, serves as a sufficient statistic for the entire history. Thus, conditioning the policy on the belief state eliminates the need to condition on the entire history, allowing us to define the value function in terms of the belief state.

This belief state perspective is intriguing because it indicates that any given POMDP has an equivalent MDP defined in the belief space. This equivalence ensures that the optimal policy derived from both the belief MDP and the POMDP will yield the same results. The belief MDP will have corresponding belief action rewards and belief transition dynamics. The belief action reward is defined as the weighted average of the state-action reward based on the beliefs.

An interesting characteristic of the belief transition dynamics for EF is its distinction from the base optimal belief transition dynamics, as it does not incorporate counterfactual observations. Instead, the current belief is propagated directly to the next state marginal. This approach is sometimes referred to as "open-loop belief updating," which is analogous to open-loop control, wherein beliefs are updated during planning but not during execution.

The belief MDP framework for EF implies the existence of an optimal deterministic Markovian policy due to its characterization as an MDP. With these precise characterizations, we can refine our main question: how can we interpret the modifications in EF as approximations to the base optimal belief MDP and, consequently, to the base optimal policy? 

To address this, we will introduce several concepts from MDP theory, beginning with the policy advantage and model advantage, which can be understood as abstract error measures for the policy and model. The policy advantage, for instance, is defined as the difference between two value functions. If the action taken is similar to that drawn from the policy, the advantage function will be zero, indicating no difference. The model advantage operates similarly but measures the difference in dynamics by comparing next states drawn from different dynamics.

Additionally, we will examine the effective horizon, which serves as an analog of the planning horizon for infinite horizon discounted problems, defined as one over one minus the discount factor. The normalized occupancy measure characterizes the stationary or marginal state-action distribution along the Markov chain of a policy's rollout in a given dynamics.

Using these concepts, we derive a performance difference in mismatched POMDPs, analyzing two optimal policies in their respective MDPs. This comparison is akin to evaluating the EF policy against the base optimal policy, as they share state and action spaces but differ in rewards and dynamics. We will analyze the performance difference between these policies, noting that the regret associated with policy Pi cannot exceed that of policy Pi prime since policy Pi is optimal for its MDP.

This relationship allows us to decompose regret into three terms: the advantage of actions drawn from the superior policy, the model advantage, and the reward advantage. This formulation indicates that if the rewards and dynamics are equivalent, then the regret will be zero. Notably, the coefficients for the reward and policy advantages are linear in the planning horizon, whereas the coefficient for the dynamics difference is quadratic. This suggests that errors in dynamics accumulate more rapidly than those in policy and reward.

With this understanding, we refine our inquiry further: how does the EF objective approximate the base optimal belief MDP, particularly through the reward shaping term compensating for the disadvantages associated with open-loop belief dynamics? 

To explore this, we review the concept of the value of information, which Ronald Howard defined in 1966 as the reward a decision-maker would be willing to forgo to resolve uncertainty. This definition allows for quantifying the value of information as the difference between expected values with and without perfect information. Notably, in POMDPs, agents typically do not have access to perfect information; instead, they receive observations that provide indirect insights about the environment. Thus, we extend the expected value of perfect information to account for observations, resulting in the concept of the expected value of perfect observation.

In this context, the expected value incorporates the canonical linear combination of rewards along with open-loop belief updating. Conversely, the expected value given perfect observation aligns with the base optimal value function. This relationship emphasizes the role of open-loop dynamics as a bridge between the base optimal policy and the active inference policy.

As we increase the planning horizon, the non-negativity of the value of information remains intact. However, this proposition does not elucidate the extent to which the closed-loop policy surpasses the open-loop policy. Furthermore, in practical applications, policies are generally deployed in closed-loop settings, allowing agents to observe the environment and update their beliefs.

When comparing the closed-loop and open-loop policies, we find that the primary contributor to performance differences is the model advantage, specifically the drawbacks of utilizing open-loop dynamics and planning. This leads us to explore the advantages of closed-loop dynamics, which relate directly to information gain.

By examining one-step decision-making, we find that the advantage of closed-loop planning can be expressed as the expected value of perfect observation, which can be bounded by the expected information gain. Extending this over the planning horizon reveals that adjustments to the reward function can compensate for the information loss inherent in open-loop dynamics.

To formalize this argument, we introduce assumptions regarding preference specification, ensuring that the pragmatic value gained after a belief update surpasses the information gain lost. Additionally, we establish assumptions allowing for a fair comparison between the open-loop and EF policies, leading to our main results. We present regret bounds for both policies, demonstrating that while both exhibit linear terms in policy error and quadratic terms in information gain, the EF policy benefits from an additional term that reduces the upper bound by a linear factor in information gain.

This finding illustrates how the EF policy represents an improved approximation of the base optimal policy relative to the open-loop policy. Our discussion will conclude with observations relevant to various communities.

One notable observation is the connection between this view of EF as an approximation of the base optimal policy and previous work in POMDP planning. The introduction of partial observability complicates optimal decision-making, leading researchers to propose various heuristics, including the Dual Mode Controller, which switches between exploration and exploitation modes based on belief entropy.

Another important framework, often referred to as active sensing, emphasizes minimizing belief entropy rather than reward-driven behavior. This approach is particularly relevant in contexts where agents must maximize information gain.

In terms of practical implications, I have been exploring the formulation of active inference and its connection to hierarchical planning. My goal is to develop better planning algorithms for agents, particularly in belief space planning. I aim to leverage tools from variational inference and temporal abstraction to enhance the performance of active inference agents.

In closing, I appreciate your attention and am eager to engage in further discussions.

**List of Changes Made:**

1. Corrected grammatical errors throughout the text.
2. Enhanced clarity by breaking down long sentences and restructuring complex ideas.
3. Removed trivial statements and redundancies to maintain a formal academic tone.
4. Replaced informal phrases with more precise academic language.
5. Improved coherence by ensuring logical flow between ideas and topics.
6. Introduced more structured paragraphs to separate distinct ideas and points.
7. Clarified technical terms and concepts to ensure understanding for a broader audience.
8. Ensured consistency in terminology and phrasing throughout the text.
