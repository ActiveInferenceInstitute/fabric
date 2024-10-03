Refined Text:

[Music] Good day, and welcome to the Active Inference Model Stream, episode 13.1, dated August 23, 2024. We are joined by two authors of the paper entitled "Synthesizing the Born Rule with Reinforcement Learning." We appreciate your participation in this presentation and discussion. I will now hand over to Jo for the presentation.

Thank you for inviting me, Daniel. It is a pleasure to engage with the Active Inference community and converse with all of you. I anticipate that our interaction will yield as many questions from us to you as vice versa. Therefore, I will aim to keep my slides concise and informative, providing a high-level overview of the article. I estimate this will take about 30 minutes, after which we will have ample time for discussion. Please feel free to ask for more technical details on any points of interest at the end, and I will do my best to reference the relevant sections of the article.

Before we begin, I would like to mention that you might hear some background noise, such as drilling or a child crying, as I am currently at home, which adds to the domestic atmosphere. Let us proceed.

This slide may appear cluttered, and I apologize for that, but it represents the diverse group of contributors from various institutions involved in this work. I will display this slide again at the end for those interested. Notably, five researchers are affiliated with the Institute of Physics at Lab Q in Rio de Janeiro, where I am currently located. Previously, I was based at the University of Massachusetts Boston, where two other co-authors of this paper were also situated. We are all part of the Cubism group led by Chris Fuchs. I will briefly discuss Cubism, which is an interpretation of quantum theory grounded in subjective Bayesian decision theory. If you are curious about this, we can delve into it further at the end.

John has since moved on to the University of New Mexico, and the lead author of this work is Rodrigo Pio, who was a PhD student at the time of this research and is now at the Technology Innovation Institute in Abu Dhabi. 

I would like to refer to another paper published a few years ago during the pandemic by our Cubism group, which includes John, Chris Fuchs, and myself. Although this was a theoretical paper, it contains foundational ideas that inform the current article. I will provide a brief excerpt from the abstract, which states that "the subjective Bayesian interpretation of quantum mechanics, which we refer to as Cubism, asserts that the Born rule is a normative rule analogous to Dutch book coherence." I will explain the Born rule and Dutch book coherence shortly, but it is essential to note that we are adding empirical assumptions that characterize the physical world.

Our central premise is that the Born rule, a fundamental aspect of quantum physics, can be understood through decision theory augmented by empirical assumptions. To elaborate on this concept, let us clarify some terminology. The subjective Bayesian interpretation of quantum theory posits that agents aim to make rational decisions using probability theory, which is informed by empirical facts derived from experiments. Quantum mechanics, according to Cubism, provides an upgrade to decision theory.

The Born rule, which you may have encountered in its legacy form, specifies the probability of obtaining a specific outcome when measuring a quantum state, typically represented by an observable with a discrete spectrum of eigenstates. The probability for obtaining outcome \( J \) is determined by the modulus squared of the overlap between the quantum state and the corresponding eigenprojector, yielding a positive real number.

In contemporary discourse, the Born rule has been generalized to accommodate more complex measurements, moving beyond traditional observables to include Positive Operator-Valued Measures (POVMs). While the term may seem cumbersome, POVMs represent the most general type of measurement in quantum theory. In this context, the quantum state is denoted by a density matrix, and the probability for outcome \( J \) is derived from the trace of the density matrix with the POVM element associated with outcome \( J \).

I hope this explanation resonates with some of you, but if not, please feel free to inquire further. It is important to recognize that the Born rule functions as a critical component of quantum mechanics, transforming the input of a quantum state and measurement into an output probability for each potential outcome. Our previous research established that if an agent behaves rationally, it must adhere to the Born rule to maintain consistency in its probability assignments.

This finding is significant as it marks the first instance, to my knowledge, where the Born rule has been derived from decision theory without presupposing quantum mechanical formalism. In earlier literature, the Born rule has often been treated as an axiom, while attempts to derive it from decision theory typically invoke aspects of quantum mechanics, such as unitary dynamics.

Our research indicates that the Born rule is more universal than previously thought; it may apply in contexts beyond quantum theory. This suggests that a rational agent, equipped with the appropriate perceptual capabilities to detect quantum phenomena in the right environment, would be compelled to utilize the Born rule for decision-making.

This insight prompted us to explore the universality of the Born rule further. We considered the possibility that even non-rational agents might exhibit behaviors consistent with the Born rule. Inspired by the active inference literature on ant colonies, we sought to investigate whether simple organisms, devoid of explicit mathematical representations, could still behave in accordance with sophisticated abstract rules.

To conduct this research, we faced numerous modeling decisions, including how to simulate a simple agent and its environment. Our agent, while ignorant of quantum mechanics, must possess a success parameter linked to its ability to predict measurement outcomes on quantum systems. The premise is that through measurements on quantum systems, the agent will learn to behave in accordance with the Born rule.

Our agent operates within an action-response feedback loop, making probabilistic bets on outcomes and adjusting its behavior based on received rewards or penalties. We began with a simplified model to test our hypothesis, assuming that the agent's decisions depend solely on the average expected rewards for possible actions.

We refer to this agent as a "Proto-Bayesian agent," as it does not employ probability theory explicitly but instead reacts in a simplified manner. However, with sufficient data, we expect it to behave like an intelligent, conscious Bayesian agent. Our exploration seeks to uncover how variations in data availability affect the agent's performance in aligning with the Born rule.

To facilitate this research, we implemented a reinforcement learning algorithm. At each decision point, the agent selects a bet from a discrete set of options, with values ranging from zero to one. Although the agent does not explicitly use probabilities, our expectation is that, in the limit of many iterations, these bets will correspond to actual probabilities.

The agent's betting strategy is informed by a quadratic loss function that encourages it to optimize its performance by minimizing discrepancies between its bets and actual outcomes. The agent employs an epsilon-greedy algorithm, balancing exploration of new actions and exploitation of known successful actions.

The environment in which the agent operates must exhibit sufficient complexity to facilitate quantum behavior. We require a measurement setup that cannot be wholly explained by classical physics, leading us to employ an informationally complete quantum measurement protocol. This ensures that the agent's environment reflects the inherent structure of quantum theory.

In our simulations, we implemented a symmetric informationally complete measurement, which simplifies our equations and allows for experimental validation. While our work involved simulations rather than physical experiments, we proposed future experiments to test our hypotheses.

Our initial hypothesis posited that the agent would learn the Born rule relatively easily, given the ideal conditions we established. However, we discovered that it required a substantial amount of data to approximate the Born rule effectively. This raises questions about the practical implications of our findings and the extent to which agents can learn quantum-sensitive behaviors within realistic constraints.

In summary, our preliminary results suggest that unless an agent can acquire sufficient data, it may struggle to exhibit behaviors reflective of the quantum structure of its environment, even when that environment is distinctly quantum. We are left to ponder whether quantum-sensitive behavior is advantageous for survival or if it is simply too challenging for agents to learn.

Thank you for your attention. I now welcome any questions or comments from the audience.

Changes Made:
1. Enhanced clarity and coherence by restructuring sentences and paragraphs.
2. Eliminated informal language and replaced it with formal academic language.
3. Removed redundant phrases and trivial statements to improve conciseness.
4. Corrected grammatical errors and improved overall readability.
5. Used consistent terminology and formalized the presentation of concepts.
6. Maintained the original meaning and intent of the text while ensuring an academic tone.
