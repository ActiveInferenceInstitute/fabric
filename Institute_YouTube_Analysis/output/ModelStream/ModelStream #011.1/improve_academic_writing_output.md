Refined Text:

This presentation is focused on the Active Inference Model, specifically Stream 11.1. I am joined by Hadi Vafa, who will discuss the recent paper on the Poisson Variational Autoencoder. The session will include both a presentation and a discussion. Thank you all for attending.

I appreciate the opportunity to share our recent work, which I conducted alongside my postdoctoral mentor, Jake, and Deel, a PhD student in our laboratory. The overarching motivation for this research is our belief that we can gain insights into brain function by studying brain-like artificial neural networks (ANNs). 

To illustrate this, consider an ideal experimental scenario in which we could record every neuron in the brains of various animals as they perform complex tasks in their natural environments. In this scenario, we would also have access to an electron microscopy connectome of every neuron, along with detailed learning dynamics of those brains. While such an experiment is exceedingly difficult—if not impossible—for the foreseeable future, our challenge lies in determining how to analyze such a dataset if it were available. Our proposal is to use ANNs as computational models of the brain to generate knowledge and develop theories that can be applied to analyze this data.

However, a significant challenge arises: if we intend to use ANNs to study the brain, they must be sufficiently brain-like. As the adage goes, “All models are wrong, but some are useful.” The usefulness of these ANNs correlates with their resemblance to biological brains. In this work, I will clarify what I mean by "brain-like," as the term can have various interpretations. My focus will be on models of visual perception, wherein we aim to construct an ANN that accurately perceives visual stimuli.

To create brain-like models, we draw inspiration from neuroscience. Our goal is to narrow our search space, as the domain of all ANNs is vast. Specifically, we will rely on three key inspirations: perception as inference, rate coding, and predictive coding. I will elaborate on each of these concepts.

First, let us consider the notion that perception involves two components: an external component, represented by sensory data (e.g., photons that strike the retina), and an internal component, which encompasses subjective experiences and prior expectations. These two components interact to produce perceptions. This idea is not novel; it can be traced back over a millennium to Alhazen, who posited that "vision occurs in the brain rather than the eyes," and emphasized the significance of subjective elements in perception. More famously, Helmholtz asserted that perception is our best guess regarding the external world based on current sensory evidence and prior experience. 

To illustrate, consider the “Ames room illusion.” Upon viewing this image, one might initially assume that it depicts a tall man and a short man. However, the room is specifically designed to create this illusion. We typically assume rooms are rectangular, but this one is not. The sensory data received from the individual in one corner can be interpreted in two ways: either the room is rectangular and the person is short, or the room is not rectangular, and the person is positioned farther away, creating the illusion of shortness. Our prior expectations lead us to favor the first interpretation, demonstrating how prior expectations can mislead our perceptions.

We can formalize this concept mathematically using Bayesian probability. For instance, consider a latent variable \( Z \) that we can sample from a prior distribution \( P(Z) \) and subsequently condition some likelihood function based on the sampled value to produce an observation \( X \). We can then ask what likely causes underlie the generation of \( X \). This leads us to the inference process, where we compute the Bayesian posterior \( P(Z | X) \). 

Now, let us relate this back to Helmholtz’s assertion that perception is our best guess about the world based on current sensory evidence and prior experiences. The theory of perception as inference posits that when presented with an image, the brain seeks to determine which latent configuration likely caused the current observation, necessitating the computation of a posterior distribution over some latent causes given the observation.

The next concept to consider is rate coding, which addresses how biological neurons communicate and store information. Neurons produce all-or-nothing action potentials, commonly referred to as spikes. The foundational evidence for rate coding dates back to the 1920s when Adrian and Zotterman developed amplifiers to measure spikes. They demonstrated that neuronal firing rates increase in proportion to the magnitude of a stimulus. This relationship is observable in various neuroscience studies, where the baseline firing rate increases in response to a stimulus, effectively encoding the presence of that stimulus.

Finally, the concept of predictive coding frames the brain as a prediction machine. Andy Clark's review succinctly summarizes this notion. The brain is thought to maintain an internal model of the environment, using it to anticipate sensory inputs. When actual sensory inputs are received, they are compared to these predictions, leading to the identification of errors, which are subsequently propagated up the cortical hierarchy to update and refine the internal model. Both predictive coding and perception as inference share overlapping concepts, yet they remain distinct.

In synthesizing these three ideas, we narrow our search space to a model we term the Poisson Variational Autoencoder (P-VAE). The "Poisson" aspect derives from rate coding, as there is a long-standing tradition in computational neuroscience of modeling observed spike counts from biological neurons using a Poisson distribution conditioned on some rate variable. The "Variational Autoencoder" aspect relates to perception as inference, as these architectures are designed to optimize a loss function that aligns with Helmholtz’s insights in modern Bayesian terms.

Before delving into the P-VAE, I will briefly outline the structure of a Variational Autoencoder (VAE). The architecture typically comprises two components. In the simplest VAEs, an input (such as an image) is encoded by an encoder network, also referred to as an inference or recognition network. This process infers some latent representation and posterior distribution conditioned on the input \( X \). Subsequently, we sample from this posterior and decode the latent representation back to the observation.

The key aim is for the encoding process to retain sufficient information about the input image, enabling its reconstruction. The term "autoencoder" signifies that we are mapping an input to itself. The goal is to perform posterior inference, where we approximate the true but intractable posterior with an approximate posterior \( Q \) parameterized by some parameters \( \Theta \). The objective is to minimize the Kullback-Leibler (KL) divergence between \( Q \) and the true posterior \( P \).

The loss function we derive in this context encompasses two components: the reconstruction term, which measures how well the model reconstructs the input, and the KL divergence term, which serves as a regularization term. The evidence lower bound (ELBO) provides a useful framework for this loss function.

In conclusion, by integrating neuroscience principles with modern machine learning techniques, we have developed a model that is more brain-like than its alternatives, demonstrating enhanced sample efficiency and other advantageous features. 

Changes Made:
1. Improved overall clarity and coherence of the text.
2. Corrected grammatical errors and punctuation.
3. Structured the presentation logically with clear section transitions.
4. Removed informal language and replaced it with formal academic terminology.
5. Summarized key concepts and theories for better understanding.
6. Reduced redundancy and wordiness throughout the text.
7. Enhanced the precision of technical descriptions related to models and methods.
