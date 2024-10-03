**Refined Text:**

Greetings, and welcome to the Active Inference Math Stream, session 10.1, held on March 28th or 29th, 2024. Today, we are joined by Thomas Farley, who will discuss the generalized decomposition of multivariate information. The session will include a presentation followed by a discussion. Thank you, Thomas, for being here; we are eager to hear your insights and to engage with questions from the audience.

Thank you for having me. I am excited to discuss this topic with others who share an interest. I believe today is the 29th, as I compiled my materials last night, which indicates we may be one day out of sync. I will be presenting on the generalized decomposition of multivariate information, which is based on a paper I recently published in PLOS ONE. I will provide a link to that paper at the end of my talk for those interested in exploring this topic further.

We will begin with some background information, outlining the intuitions surrounding information theory. I will introduce two key concepts: partial information decomposition (PID) and partial entropy decomposition (PED). For those in the audience who are experts in multivariate information theory, you may choose to watch YouTube videos for a few minutes while we bring others up to speed.

Once we have established the necessary mathematical foundations, I will explain how I have generalized the PID and PED into what I refer to as the generalized information decomposition (GID), which is based on the Kullback-Leibler divergence. After discussing the GID, I will illustrate how it can provide insights into other well-known information-theoretic measures, such as total correlation and Tononi's integrated information. To demonstrate that the GID is indeed a generalization of the PID, I will walk through the derivation of the classic Williams and Beer PID from the GID. This derivation reveals some intriguing mathematical questions that arise during the process.

I will conclude with a brief discussion of future work and how this relates to predictive coding in neuroscience. I am particularly interested in engaging with audience members who possess expertise in active inference or free energy, as there may be insights to uncover that are not immediately apparent from my perspective.

Now, let us begin with the background. This is the Active Inference Stream, so I assume we are all familiar with information theory and complex systems. Information theory has emerged as a lingua franca for complex systems due to its non-parametric and model-free nature, making it particularly useful for nonlinear systems that cannot be easily modeled using linear regression. There are deep and interesting connections between information theory and thermodynamics, which I will not delve into here, but they are worth noting.

The central object of study in information theory is entropy, defined as Shannon's classic entropy function, which is the negative sum of the probability times the logarithm of the probability. In this context, random variables will be denoted using italic uppercase letters, while their support sets will be represented using calligraphic font. The specific states that these random variables can take will be indicated with lowercase italics. This distinction between average random variables and specific instances will be significant as we progress.

In classic Shannon information theory, we iterate over all possible states of a variable, computing the probability of each state multiplied by the logarithm of that probability. This quantifies our average uncertainty regarding the state of the variable. For example, if we consider a coin flip, this quantifies our uncertainty about the outcome. From this foundation, we derive mutual information, which is a pairwise measure of correlation and one of the most fundamental concepts in modern information theory. It can be interpreted as the information that variable X discloses about variable Y, which is the difference between our initial uncertainty about X (the entropy of X) and the uncertainty that remains after learning Y (the conditional entropy).

When we extend this concept to multivariate mutual information, we consider two sources, X1 and X2, which together disclose information about Y. Our prior uncertainty about Y is subtracted by the uncertainty that remains after learning from both X1 and X2. It is crucial to note that the mutual information that X1 and X2 disclose about Y is not trivially reducible to the sum of their individual mutual information values. This indicates the presence of redundancy, where information about Y is duplicated across X1 and X2, leading to double counting when summed.

Conversely, an interesting scenario arises when the joint mutual information exceeds the sum of the marginal mutual informations. This represents synergy, where the information contained in the joint state of X1 and X2 is not captured by their individual states. We can formalize these concepts using logical connectives: redundancy refers to information that can be learned by observing any one of the variables, while synergy is information that can only be acquired by observing the combination of all variables.

This leads us to the partial information decomposition (PID), which seeks to reconcile the joint mutual information with its components by breaking it down into redundancy and synergy, along with unique information terms for each variable. This decomposition also applies to the marginal mutual informations, allowing us to maintain harmony between the joint and marginal values.

The PID can be visualized using a Venn diagram, where the large oval represents the joint mutual information, the circles denote the marginal mutual informations, and the overlapping area signifies redundancy. The unique information reflects the difference between the marginal mutual informations and redundancy, while synergy is the additional information present in the joint state that is absent in the individual states.

However, we often encounter systems with more than two inputs. In such cases, we can generalize the PID for arbitrary numbers of inputs and formulate a finite set of components structured into a partial information lattice. As the number of information sources increases, the lattice grows exponentially more complex, revealing intricate relationships among the information theoretic components.

We can express the decomposition mathematically, indicating that the mutual information disclosed by inputs X1 to XK about Y can be represented as a sum of partial information atoms. Although the specifics of computing the values of these atoms are beyond our current discussion, it suffices to acknowledge their existence and the logical structure connecting them.

Despite the power of the PID, it has limitations, particularly in distinguishing between source elements and target elements. In many complex systems, this distinction is not always clear. To address this, we can apply a mathematical technique that allows us to decompose the mutual information disclosed by the individual parts about their joint state, which leads us to the concept of partial entropy decomposition (PED).

While the PED effectively removes the source-target distinction, it does not adequately represent information in the same way that mutual information does. Entropy is a measure of uncertainty about the state of the whole system, and in some cases, it reaches its maximum when the elements are independent, which contradicts our typical understanding of information.

To overcome this limitation and provide a more general decomposition of multivariate information, I turned to the Kullback-Leibler divergence. This divergence serves as a target-free definition of information and is a generalization of the classic Shannon mutual information. The divergence between two distributions quantifies the information gained when updating beliefs about a system, allowing for the application of any prior and posterior distribution.

The goal is to remix the partial entropy decomposition to instead decompose the Kullback-Leibler divergence. Through algebraic manipulation, we can express the Kullback-Leibler divergence in terms of local entropies, which leads to a localized partial entropy decomposition. This enables us to derive the generalized information decomposition, which represents the difference between two localized partial entropy decompositions.

The generalized information decomposition (GID) allows us to decompose any information theoretic measure that can be expressed in terms of a Kullback-Leibler divergence. For example, the total correlation, a multivariate generalization of mutual information, can be analyzed using the GID to extract insights about lower-order and higher-order interactions within the data.

As a final point, it is important to note that the GID can also recover the original PID. By expressing the joint mutual information in terms of expected values of Kullback-Leibler divergences, we can derive the familiar components of redundancy, unique information, and synergy from the GID framework.

In conclusion, the generalized information decomposition represents a significant advancement in understanding multivariate information structures. I am eager to explore its applications in real data and collaborate with others interested in this field. Thank you for your attention, and I look forward to any questions or discussions.

**List of Changes Made:**

1. Corrected grammatical errors and punctuation throughout the text.
2. Improved clarity and coherence by restructuring sentences and paragraphs.
3. Enhanced academic voice by using formal language and avoiding colloquial expressions.
4. Removed trivial statements and repetitive phrases for conciseness.
5. Ensured a logical flow of ideas and concepts, maintaining the original meaning and intent.
