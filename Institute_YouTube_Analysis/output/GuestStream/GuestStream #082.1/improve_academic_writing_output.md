**Refined Text:**

Greetings and welcome. Today is April 29, 2024. We are currently engaged in Guest Stream 82.1 with Robert Warden, who will discuss Bayesian model-based cognition and the requirement equation. Thank you, Robert, for the introduction and for initiating this presentation and discussion. 

My name is Robert Warden, and I am affiliated with the Theoretical Neurobiology Group at University College London. In this live stream, I will discuss an equation known as the requirement equation, which is closely related to the free energy principle and active inference, though it is not identical. I hope this marks the beginning of a series of live streams where we will explore the application of these concepts to three-dimensional spatial cognition, and eventually to consciousness.

To begin, I will summarize the key ideas. The primary focus of the requirement equation is to address what brains must accomplish rather than how they achieve these outcomes. This approach differs from the free energy principle and active inference; however, I posit that it complements these frameworks. 

The requirement equation is fundamentally a mathematical statement that encapsulates what brains must compute to maximize fitness for their organisms. It does not specify how this computation occurs; it is agnostic to the underlying mechanisms, such as neurons or energy minimization processes. Rather, it posits that to achieve optimal fitness, a brain must engage in specific computations, which I will elucidate shortly. This equation bears similarity to Bayes' theorem but includes additional terms, which will become apparent.

Given that the most fit brains must evolve toward the requirements of this equation, it is important to note that the requirement equation itself is computationally intensive, and brains do not explicitly compute it. Instead, animals produce results that approximate those dictated by the requirement equation. Although we can compute this equation through brute force methods without making assumptions about the computational processes of the brain, this serves as a benchmark against which any cognitive model can be calibrated—particularly those based on free energy and active inference. I contend that these models are approximations of the requirement equation, and we can evaluate their effectiveness by comparing their outcomes with those derived from the requirement equation.

This presentation will unfold in three parts. The first part involves deriving the requirement equation and illustrating its functionality. The second part will demonstrate how the equation can be utilized to test and calibrate active inference models. The third part will provide remarks on internal Bayesian models.

To initiate our exploration, we need to characterize brain function without imposing assumptions about the underlying processes. The first characterization is conceptualizing the brain as a black box that receives sensory input and generates action choices as output. This perspective encompasses a range of sensory data, such as visual and tactile information, which the brain uses to select an action.

We will advance from this black box model to what I term a gray box model. In this model, the brain evaluates a set of possible actions (A_i, where i = 1, 2, 3, etc.) and calculates a real-valued function (f(d, a)) for each action, which depends on both the sensory data (d) and the action being considered. This function represents the expected payoff of a given action under specific circumstances. The brain subsequently compares all potential functions (f) in parallel and selects the action that yields the highest expected payoff. This gray box model assumes the brain examines all alternatives and selects the optimal one while refraining from making further assumptions about how these computations occur.

Next, we can contextualize this framework within real-world scenarios involving probabilities. An animal's life is segmented into various domains, each requiring different decisions. In one domain, we can illustrate an encounter where a state of affairs (S) possesses a prior probability (P(S)). The animal, lacking knowledge of this state, acquires sensory data (D) with a conditional probability (P(D|S)). The animal then employs a decision function (f) to compute f(D, A) for all potential actions (A) it might undertake. Upon selecting an action, the outcome leads to a new state (S') with a conditional probability (P(S'|S, A)). This new state holds a value for the animal, which relates to its lifetime fitness. 

In principle, the brain operates as if it has computed f(D, A) to guide its actions, an assumption that will prove crucial. The mean payoff over numerous encounters in an animal's life is expressed as a function of various probabilities. This expression integrates the probabilities associated with the states of affairs the animal encounters and the corresponding sensory data, leading to the new state and its value.

To derive the requirement equation, we manipulate the formula to yield a sum of functions (J(D)), which closely resembles Bayes' theorem, albeit with additional components. The decision function f is expressed as a weighted sum over states, incorporating both the prior and posterior probabilities. This formulation implies that any brain acting as if it has computed this equation will achieve optimal fitness.

The requirement equation outlines what brains are required to do, indicating that those who act as if they have computed it will attain the highest possible fitness. This suggests that brains evolve to make decisions as if they had computed this equation, which is analogous to Bayesian cognition. This analysis reveals that the assumption of Bayesian cognition is not merely a hypothesis but a logical consequence of the requirements outlined by the equation.

The derivation of the requirement equation shares similarities with partially observable Markov decision processes, and further details can be found in the accompanying paper.

In the second part of this presentation, I will discuss the application of the requirement equation. It is essential to recognize that all terms within the equation are contingent upon external biological factors, such as environmental states, sensory data, and the consequences of actions. The computation of this equation does not necessitate assumptions about the brain's internal processes, providing a significant advantage.

Despite the computationally intensive nature of the requirement equation, we possess the tools to compute it through numerical methods, enabling us to establish benchmarks for animal behavior and cognitive models, including those based on active inference. 

Active inference models differ from the requirement equation in that they make assumptions about brain function, incorporating generative models that simplify the actual processes involved. These models utilize variational fitting techniques to minimize free energy, which may lead to inaccuracies in predicting animal behavior. Thus, we can test the assumptions of active inference models against the requirement equation by comparing the results derived from both approaches in terms of lifetime fitness.

In conclusion, the requirement equation provides a valuable framework for understanding the functional requirements of brains and their evolutionary trajectory toward optimal fitness. Future discussions will focus on applying these concepts to three-dimensional spatial cognition, further elucidating the relationship between cognitive models and biological processes.

**List of Changes Made:**

1. Corrected grammatical errors and improved sentence structure for clarity.
2. Enhanced coherence by organizing the content into clear sections.
3. Removed informal language and casual phrases to maintain a formal academic tone.
4. Clarified complex ideas and concepts, making them more accessible to the reader.
5. Eliminated redundant statements and phrases to improve conciseness.
6. Replaced colloquial terms with more precise academic terminology.
7. Provided a structured summary of the content for better understanding.
8. Ensured that all technical terms are accurately defined and explained in context.
