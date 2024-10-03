Refined Text:

Greetings, everyone. Thank you for joining our second discussion on Chapter Four. Let us proceed directly to the questions. Participants are welcome to write their questions in the chat, raise their hands, or unmute themselves to contribute. Feel free to ask about any specific part of the chapter that you found interesting or any question you have in mind. 

Aon, please go ahead. 

I was trying to compare Figures 4.4 and 4.6. There seems to be considerable overlap between the two sets of diagrams, yet there are also notable differences. I believe there is a clear parallel structure, but some edges differ between the two figures, and I would like to understand the significance of these changes. In both cases, especially in the left-hand diagram, they appear virtually identical between Figures 4.4 and 4.6, assuming I have the numbering correct. While I am unsure if this is too broad of a question, I feel the differences must be meaningful, yet I could not fully comprehend them.

That is an excellent question. At first glance, it is akin to comparing two cities; there may be differences in roads and connections, but overall, they appear very similar. A few key elements are being illustrated here. To provide context for this question, let us refer back to Figure 4.3. This figure serves as a kind of "Rosetta Stone," presenting a Bayesian graph for the discrete time model at the top and a Bayesian graph for the continuous time model below. They are arranged in this manner to highlight their structural similarities, despite differing treatments of time, which we can revisit. The upper section treats variables in terms of discrete sequences of events, while the continuous time section addresses higher derivatives of a variable X.

The important aspect that renders these models similar, aside from their structure, is that in a Bayesian graph, nodes represent variables, and edges represent causal connections. Now, we arrive at the Bayesian message-passing scheme. One notable feature of Bayesian graphs is that since edges indicate the sparsity of causal connections in the model, one only needs to consider edges local to a node. Thus, the traffic at a node is defined entirely by the edges leading into it.

When constructing a Bayesian model, one specifies the causal architecture of the world, and messages are passed between the variables. This model will differ slightly from the one in Figure 4.3 but will emphasize how specific architectures facilitate certain message exchanges and enable different computations. Although some variables, such as π and S, appear in both Figures 4.3 and 4.4, there are also new variables, such as ε and η. 

Figure 4.4 highlights two aspects: on the left, it discusses hierarchy and nesting, while the right illustrates unfolding dynamics over time. The motif on the left, which represents nesting, depicts each unit of four as a level in a nested hierarchical model. In this structure, ε calculates an error, and these errors are passed up to a higher level in the graphs, reflecting a classical predictive processing architecture. Each stacked level performs differencing and passes errors upward.

Conversely, the dynamic motif on the right emphasizes temporal progression. Here, the predictive processing emphasizes dynamics, with observations from current, future, and past time steps converging to calculate ε based on the intersection of incoming observations and hidden state predictions. If the hidden state prediction aligns perfectly with the observation, then ε equals zero. 

In Figure 4.6, the only variation is that we remain within a continuous time setting, leading to a greater number of variables, as observed in the continuous time model. Rather than merely representing past, present, and future time steps, as in Figure 4.4, Figure 4.6 represents different orders of generalized ordinates of motion, specifically the first, second, and third derivatives. Figures 4.4 and 4.6 can be viewed as transpositions of the models presented in Figure 4.3, but now they represent each aspect in terms of the message-passing that reflects computational dynamics.

This illustrates a deeper similarity between these two models. However, it is also challenging due to the introduction of new notation, which may not align perfectly with previous models. Are there any thoughts or further questions on this topic? 

TCC, this is reminiscent of parallax in vision. Chapter Four presents the generative models of active inference. In terms of the textbook structure, Chapters One, Two, and Three introduced active inference from both low and high perspectives. Chapter Four serves as the core of active inference, with discrete and continuous time being further unpacked in Chapters Seven and Eight, respectively. Here, they are closely juxtaposed, emphasizing a significant point: time can be handled in both discrete and continuous manners in active inference. 

While this is an intriguing insight, the challenge lies in the fact that even when discussing similar cognitive functionalities, the notation differs significantly between the two approaches. Using the same notation could lead to confusion, as it would be unclear whether we were discussing discrete or continuous time. Therefore, a new set of vocabulary is necessary, even if it differs slightly; for instance, using Y for observations in continuous time and O for those in discrete time reflects how this chapter presents the material. 

The text aims to introduce both time treatments while consistently emphasizing that both represent different flavors of active inference. The authors will revisit these concepts in Chapters Seven and Eight. However, Chapter Four serves as a dual-stream introduction to the two simplest forms of the generative model.

If no one else has a question, I can ask another. I find myself confused about the structure of policy variables. In the context of hidden states and observed states, I understand they exist in a not fully specified space. However, I struggle with the concept of policy, particularly as it seems to relate to reinforcement learning literature. What is the type of space in which a policy—whether in its discrete version (π) or continuous version (V)—exists? How could this be implemented in a program, and what would be its associated type or shape? 

Excellent question. The variable π represents a list of all policies; it is always a vector that sums to one. This critical feature enables discussions about the likelihood of a policy, which is why habit serves as the prior on policy. Expected free energy updates our prior on policy into a posterior because the shape of that variable, being a list that sums to one, constitutes a probability distribution. 

Affordances represent actions that can be taken at a given moment. For instance, in a grid world, affordances might include moving up, down, left, right, or staying in place. If we consider a single time horizon or time step, the agent's affordances are equivalent to its policy space since it selects the next action. For example, if there are five options and an even prior across those five, the probabilities would be 0.2 each, which could then be sampled or updated into a policy posterior.

When discussing agents that engage in planning, the shape of π expands to the power of the number of time steps. For example, with five affordances and two time steps, π would consist of 25 combinations, representing all two-way combinations of actions.

To clarify, when we see V with a tilde, which represents a trajectory over policies, should we regard this as an unbounded sequence of steps that may not be concretely representable in a program? 

In the continuous time setting, explicit planning is not conducted. The classical computer science approach involves exponential tree searches, where increasing depth leads to exponentially more discrete options. In contrast, in the continuous time setting, planning is implicit. For instance, if we were approximating a wild function through a Taylor series, we might evaluate the function at zero and take the first derivative, allowing for an implicit expansion that includes infinite future planning, though it may not be accurate everywhere. 

Early implementations focused on continuous state space due to its similarity to Bayesian filtering approaches. As researchers sought to incorporate sequential dynamics, they moved into coupled dynamical systems. However, the absence of explicit planning in continuous models led to a shift toward discrete planning environments. These branches eventually converged through hierarchical nested models that incorporated continuous dynamics at lower levels and discrete dynamics at higher levels.

In summary, discrete time settings reflect classical planning, while continuous time does not explicitly engage in planning. In discrete time, agents estimate various branching paths, whereas in continuous time, the agent's movements are determined by derivatives. Each approach has its strengths and weaknesses, which are addressed by constructing hierarchical nested models that incorporate both continuous and discrete time treatments.

Let’s review Figure 4.2, which is particularly useful for building intuition regarding Bayesian graphs. It presents various scenarios, such as one hidden state with one observable (e.g., a real temperature and a thermometer), one hidden state with two observables, and a causal chain. These scenarios reflect how people describe causal sequences in the world. Observables can represent any modality of observation, while hidden states may include latent causal factors, some of which may not have a tangible existence. 

This framework maps onto a significant portion of statistical inferences and serves as a means to visualize causal relationships between observations, hidden states, and actions. These are the major components we seek to connect in a unified model of perception, cognition, and action. 

Has anyone attempted to implement this framework for motor control? 

Yes, motor control has been explored from both human and robotic perspectives, examining movements such as handwriting and gross movements within a warehouse setting. 

Dan, wasn’t this related to what the Hitachi group covered? 

Indeed, that was related to robotics in silico, focusing on simulations rather than physical robots. The visualizations presented were thought-provoking, particularly in illustrating how multi-agent interactions and social norms come into play. 

The red agent represents an active inference agent, while the green altruistic agent aims to minimize the red agent’s deviation, contrasting with the selfish green agent, which seeks to minimize its own path. These are examples of how social characteristics can be integrated into preference distributions and action tendencies of different agents, which is a focus of Chapter Six. 

The structure of the textbook allows for flexibility in reading order. The first five chapters provide foundational epistemic knowledge, while the latter half, beginning with Chapter Six, outlines the modeling process. An alternative approach involves starting with a specific system of interest and reverse-engineering the observations and actions of various agents involved, ultimately leading to the formalizations used.

The brain functions as a system of systems, where multiple causal hypotheses about events are entertained. It is vital to recognize that our experience encompasses more than just internal systems; we exist within ecosystems and social systems. 

The action-perception loop is crucial for understanding how agents interact with their environments. The simultaneous occurrence of action and perception is fundamental; an agent cannot disregard one while engaging with the other. This dynamic interplay is essential for creating a holistic model, even in simple scenarios, such as a rat in a maze. 

I am curious about the relationship between consciousness and behavior. While plants lack brains, their structures exhibit behavior, raising philosophical questions about awareness and responsiveness. 

Active inference posits that every moment represents a branch point, defined by the affordances available. The complexities arise when considering whether non-animal entities exhibit behavior, as this implicates broader definitions of consciousness and cognition. 

The discussion of consciousness invites further exploration into how sensory perception influences intelligence. For example, if a human mind were placed in a dog’s body, would cognitive function change? Similarly, if a mind were transplanted into a cybernetic system, how would this affect consciousness? 

The conversation touches on the essential role of embodiment in intelligence, as our sensory systems continuously inform our cognitive processes. There exists a rich discourse surrounding the interplay between cognitive function and embodiment within the active inference community. 

In examining these philosophical inquiries, we confront the necessity of acknowledging diverse perspectives. The quest for truth encompasses various modalities, from scientific inquiry to intuitive explorations found in poetry. 

Furthermore, the relationship between sensory modalities and intelligence underscores the importance of understanding how our sensory apparatus shapes our cognitive architectures. Our evolutionary history informs the development of cognitive functions, as structures like grid cells arise to navigate the geometries of our environment. 

Finally, regarding the mathematical conventions used in the text, such as bold versus serif fonts, clarification is needed to understand their significance. In particular, the distinction in notation may serve to differentiate between sufficient statistics and underlying variables, though this requires further investigation. 

I appreciate your insights and the resources provided for exploring these concepts further. I look forward to discussing more examples and applications of active inference in the future.

Thank you all for your contributions. I look forward to our next meeting, where we will delve into Chapter Five and further explore the connections within the nervous system. 

List of Changes Made:
1. Enhanced clarity and coherence throughout the text by restructuring sentences and paragraphs.
2. Corrected grammatical errors and improved punctuation.
3. Removed informal language and unnecessary fillers to adopt a more formal academic tone.
4. Streamlined repetitive phrases and concepts for conciseness.
5. Clarified technical terms and concepts for better understanding.
6. Organized content logically, ensuring a flow of ideas and discussions.
7. Maintained the original meaning while improving overall readability and professionalism.
