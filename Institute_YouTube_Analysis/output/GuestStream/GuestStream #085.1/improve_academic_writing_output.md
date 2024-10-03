**Refined Text:**

Greetings and welcome. Today is August 5th, 2024, and this is Active Inference Guest Stream 85.1, focusing on deep learning and active inference, with our guest, David Blumen. We extend our gratitude to David for his presentation, and we anticipate an engaging discussion regarding the application of active inference in developing intelligent agents, exploring its advantages, disadvantages, and potential solutions to existing challenges.

My background encompasses software engineering and artificial intelligence research, with extensive experience in scalable systems and machine learning. I have been dedicated to this project for approximately three years and am eager to share my insights. 

Currently, a significant pursuit within AI research is the creation of an intelligent agent that possesses general intelligence while ensuring it does not pose a threat to humanity. Many researchers are focusing on these critical aspects, and I am particularly enthusiastic about both the development of general intelligence and the preservation of human safety.

To establish a common understanding, I will begin by defining what constitutes an agent. Various definitions exist, but I will adopt a straightforward one: an agent is an entity that, given a set of past observations, generates the next action. Essentially, based on current observations and past experiences, the agent determines its subsequent course of action. 

While I do not possess a rigorous definition of general intelligence—nor do I believe one exists—I suggest that an intelligent agent should exhibit smart behavior across diverse, unfamiliar environments. This entails the ability to understand environmental dynamics, learn from mistakes, avoid local optima, and effectively balance exploration and exploitation. Such an agent should engage in planning, communication, and interaction with other complex entities.

Active inference plays a pivotal role in this discourse. It provides a framework for conceptualizing agents as interacting with their environments in a self-evidencing manner. This means that any object maintaining homeostasis over time can be perceived as minimizing free energy. From the agent's perspective, this involves updating its beliefs to align with its observations to reduce surprise. The agent actively navigates the environment to acquire knowledge and refine its beliefs while positioning itself in areas it anticipates occupying.

This framework allows us to analyze various entities, ranging from biological cells to robots, organizations, or even nations, as if they are conducting Bayesian inference over their inputs and maintaining beliefs about the states they will occupy. 

However, while the generality of this formulation is appealing, it does not elucidate how to construct such agents. There are two main challenges in utilizing this theory for agent development. First, the framework suggests that every agent approximates Bayesian inference, which can be computationally intractable. Active inference acknowledges this limitation by proposing variational inference as an approximation method, but the meaning of "approximate" varies in different contexts. 

Second, the framework posits that agents will occupy states as indicated by their prior beliefs. For instance, animals forage because evolutionary selection has favored those that believe they will find food. While this captures the essence of action and inference, it fails to specify the prior beliefs necessary for a given environment. Thus, when constructing an agent, it becomes crucial to determine its prior beliefs, such as whether it expects to obtain energy or repair a vehicle. 

Typically, in practice, software engineers design a generative model, coding the perceived requirements of the environment and agent, and provide some prior beliefs. However, I propose an alternative approach: instead of designing a generative model, we can learn it. I believe this is essential because the complexity of relevant environments exceeds what humans can feasibly specify.

The concept of learning implies employing a learning system, with neural networks serving as effective tools for this purpose. Our goal is to develop approximate active inference agents capable of exhibiting the array of generally intelligent behaviors. Neural networks are universal function approximators; therefore, rather than constructing a rigid algorithm, we can curate training data and loss functions, manipulating a set of learnable parameters until the desired outcomes are achieved.

The challenge then becomes identifying the necessary training data for developing a generally intelligent agent. I posit that by discovering suitable training data and applying substantial computational resources, we can replicate the successes seen with models like ChatGPT and DALL-E to create a foundational general intelligent agent.

To achieve this, we require an environment for the agent to interact with. Unlike language models, which can be trained on vast textual data, our objective is to train an agent that learns to act based on past observations. This task is inherently more complex, as actions may be motivated by the need to accomplish a goal, learn, or explore. Thus, the environment must facilitate continuous learning opportunities and provide feedback signals, rewarding intelligent behaviors.

One effective strategy for establishing such an environment involves incorporating multiple agents. For instance, in a relatively simple setting, such as a game of Go, the presence of other agents introduces the dynamic of competitive adaptation. As agents become more proficient, so too do their competitors, ensuring that the environment remains challenging and conducive to learning.

However, a fully competitive environment can lead to a "kill or be killed" dynamic, where agents become trapped in local optima. To counter this, I advocate for the integration of cooperative strategies. Cooperation expands the repertoire of potential behaviors, fostering a richer, higher-dimensional behavior space that mitigates the likelihood of stagnation at equilibrium states.

Cooperation can manifest in various forms, leading to complex social dynamics, such as coalition building and trust formation. Yet, learning cooperation poses challenges, particularly in systems with solely selfish agents. Nature addresses this through kinship, where organisms are surrounded by relatives, promoting non-selfish behaviors. For instance, social insects exhibit altruism towards their colonies, as their reproductive success is tied to the collective welfare of the hive.

In summary, my proposal is to create an environment that balances cooperation and competition, enabling the training of agents capable of intelligent behaviors. I have been designing this environment and the necessary training infrastructure as part of my research.

The current version of the environment features several agents parameterized by neural networks, trained from scratch using reinforcement learning. A central component is the heart altar, which serves as the sole source of reward. Agents must efficiently manage their energy expenditure to maximize the energy gained from the environment. 

Through exploration and competition, agents learn to navigate the environment, collect resources, and engage with one another. The heart altar incentivizes cooperative dynamics, as agents must balance personal gain with collective success. Additionally, the system incorporates kinship, allowing agents to share rewards with others based on a defined sharing system, enhancing social dynamics.

As I continue to iterate on this project, I am eager to explore new environments, develop training algorithms, and establish evaluation metrics for assessing agent performance. I welcome collaboration from those interested in contributing to this exciting research.

**List of Changes Made:**
1. Reorganized the structure of the text for improved clarity and flow.
2. Corrected grammatical errors and improved sentence construction.
3. Used more formal and academic language throughout.
4. Eliminated repetitive phrases and simplified complex sentences.
5. Clarified definitions and concepts related to active inference and intelligent agents.
6. Provided a clearer explanation of the methodologies and challenges in the research.
7. Emphasized the significance of cooperation and competition in training agents.
8. Enhanced the description of the environment and training framework for agents.
9. Removed trivial statements and focused on substantive content relevant to the topic.
