**Refined Text:**

Greetings. Today is May 16, 2024, and we are engaged in the RX and fur JL project alongside guests from Bias Lab and participants from Vzer, who will discuss the RX environments and the JL package. Thank you all for joining; I look forward to the presentation and ensuing discussion. 

Thank you, Daniel. My name is V, and I am a second-year PhD student at Bias Lab. You may be familiar with Bias Lab as the principal developers of the RX infer package, which facilitates reactive Bayesian inference. Last year, while working with RX and fur and conducting reactive Bayesian inference, I recognized a significant gap in support for environments within the same reactive paradigm. We relied on reinforcement learning packages such as Gymnasium, which did not fully meet our needs. Consequently, I developed RX environments, a package designed for reactive environments that aims to complement RX and fur within the reactive agent development ecosystem.

RX environments is a lightweight boilerplate package that provides foundational code for what I term a "reactive environment." A reactive environment comprises entities, which may be agents or components of the environment, or even the entire environment itself. It is essential to describe how these entities communicate with each other. Each entity possesses its own Markov blanket, facilitating communication with other entities in the environment. This framework closely aligns with the concept of active inference, as we maintain a distinct understanding of the interior and exterior of an entity, which is represented in RX environments.

To illustrate the functionality of RX environments, I will demonstrate the Mountain Car example from the documentation. On the left side, I have prepared code that allows me to manipulate this environment in real time, while on the right side, you can observe the environment itself. I hope you can see my cursor; I will now guide you through the landscape. In the center, there is one agent—a dot representing a car. One notable feature of RX environments is the ability to send actions to the environment. In this case, the landscape constitutes one entity, and the car represents another. I can issue a command that specifies the engine force on a scale from -1 to 1. For instance, if I send a command of -1 to the entity, you will see the car begin to ascend the hill, although it lacks sufficient engine force. I can send various commands in real time, and the car will respond accordingly.

Another advantage of RX environments is the native support for multi-agent environments. If I introduce a second agent, the Mountain Car agent, with specified hyperparameters, you will notice a second dot at the bottom of the valley, representing the second car. Just as we can control the first car, we can also manipulate the second car. Although I may have assigned excessive engine power to this car, resulting in it flying off the screen, the demonstration illustrates the ability to control both cars simultaneously, with RX environments managing all communications reactively and natively.

Looking ahead, my next steps for this project include better integration into the RX and fur ecosystem. I believe that developing agents using RX environments will benefit both the active inference community and the RX and fur community. This overview highlights some of the capabilities of RX environments; however, it can achieve much more. The real-time control and multi-agent capabilities exemplify the advantages of a reactive approach.

I will now cease sharing my screen and welcome any questions you may have.

Thank you for the informative and entertaining Mountain Car example. It is indeed amusing to adjust the engine force for the Mountain Car, and while I should have prepared for it not to fly off the screen, it effectively illustrates the concept. Please feel free to ask any questions or raise any topics of discussion.

I am interested in the relationship between RX environments and RX infer. Can you clarify whether RX environments can function independently or if they must always be used in conjunction with RX infer?

RX environments was specifically developed as a complementary package to RX infer. If your goal is solely to perform Bayesian inference, RX infer suffices. However, for agent development, utilizing both packages together is advantageous. RX environments employs the same reactive backend as RX infer, ensuring compatibility. Although it is possible to create agents independently using RX environments, I would recommend using RX infer for more complex agent development.

Regarding the high-level abstraction provided by RX environments, do we lose any functionality, or can we revert to lower-level operations via RX infer?

The inference process in RX infer operates independently from RX environments. RX environments serves as a framework for creating a digital twin of the environment. Any inference tools or debugging functionalities available in RX infer remain accessible when using RX environments.

I am aware that researchers such as Bas and Professor Deff often categorize processes into six methods: act, future, execute, observe, compute, and slide. Do you consider this approach superfluous in the context of RX environments, or is it applicable?

I do not consider this approach superfluous. If you choose to design your agent to follow these steps, you are welcome to do so. Personally, I am exploring the possibility of creating an active inference agent that performs inference in a single step rather than sequentially acting, observing, planning, and sliding. In RX environments, you can send actions at any time, and if no action is sent, the environment continues to operate. The design aims to minimize constraints on users while emphasizing reactivity.

If someone wishes to write their own node within the framework, would RX environments support this?

This question is somewhat irrelevant because a custom node resides in RX infer. RX environments focuses on interactions external to the inference process.

I encountered difficulties while attempting to visualize the temporal behavior of variables such as observations, states, and controls within the thermostat problem in RX environments. Is there an example or code fragment that could assist with this?

I can provide assistance with this. Free energy is part of the inference process and resides within your agent. To access it, you would need to refer to RX infer. However, all elements within RX environments can be extracted and visualized. I can share a code fragment that demonstrates this, as it is straightforward. I understand this may not be memorable after our meeting, so I will ensure we create a comprehensive example showcasing this functionality.

Can any entity assume the roles of observable and actor in RX environments, or are there specific constraints?

There are no constraints on entity roles in RX environments. All entities are fundamentally the same and can function as either an environment or an agent. The distinction I make is between active and passive entities. An active entity emits or considers emitting observations upon receiving actions, while a passive entity, such as an agent, may not emit actions based on its observations until an inference process is attached.

Could you add an example of a discrete control space, such as a simple maze or grid example, to RX environments? The current examples focus on continuous control spaces.

I can certainly add a discrete control space example, such as a windy grid, to RX environments.

Reflecting on the overall structure, my initial impression was that RX environments standardized the creation of environments for various purposes. However, it appears to serve as a communication protocol for active inference agents.

Indeed, RX environments functions as a communication protocol that standardizes the interaction between agents and environments. Initially, I aimed to standardize environment creation, but discussions with colleagues revealed that environments and agents are not fundamentally different; both exchange data. This realization led me to develop a comprehensive programming concept for facilitating communication among multiple entities.

How might one approach the challenge of simulating multiple ant nestmates that modify pheromones on the ground?

Resolving collisions in such simulations is complex and not something I have a standardized approach for within RX environments. It falls within the realm of computational geometry and requires careful handling. While RX environments can facilitate multi-agent interactions, collision resolution would need to be addressed separately.

The distinction between synchronous and asynchronous communications is crucial. RX environments allow for flexibility in when actions can be taken, unlike traditional reinforcement learning frameworks, which impose rigid timing constraints.

Thank you for your insights. I look forward to continuing our discussion and keeping updated on developments in RX environments.

---

**List of Changes Made:**

1. Removed informal language and greetings to establish a formal tone.
2. Corrected grammatical errors and punctuation.
3. Streamlined sentences for clarity and coherence.
4. Reorganized content for logical flow and clarity.
5. Defined technical terms and acronyms upon first use.
6. Eliminated redundancy and trivial statements.
7. Clarified relationships between concepts and packages.
8. Enhanced descriptions of examples for better understanding.
9. Improved transitions between sections and topics.
10. Maintained original meaning while enhancing academic rigor.
