**Refined Text:**

Hello and welcome. This is the Active Inference Guest Stream 79.1, recorded on April 3rd, 2024. We are joined by Roto Canai, who will discuss meta-representations as representations of processes. The format will include a presentation followed by a discussion. Thank you for joining us, and we look forward to the presentation and ensuing conversation. Please proceed.

Thank you for this opportunity to present our recent work. I also appreciate your support for our recently uploaded preprint. In this talk, I aim to elucidate the concept of meta-representations. To clarify my motivation, I will begin with my frustrations regarding theories of consciousness. Many theories of consciousness are often described semantically. For example, in today's discussion, I will primarily focus on higher-order theories of consciousness. While these theories may make sense at a semantic level, implementing such high-level theories using neural networks presents numerous uncertainties.

I propose a constructivist approach: by considering how to implement these theories, we can reveal vagueness and refine the underlying concepts. The main topic of my discussion revolves around higher-order theories of consciousness, which many of you may already be familiar with. Broadly speaking, higher-order theories assert that a mental state becomes conscious not merely through the processing of that state, but by being represented by a higher-order mental state. A higher-order mental state, or representation, refers to a representation of another representation. Intuitively, this concept seems plausible. For instance, when a part of your brain processes the perception of the color red, one might question whether that processing alone is sufficient for a conscious experience of seeing red. However, when there is an additional representation indicating that you are processing something red, this meta-representation appears functionally related to awareness, which seems intuitively sensible.

Yet, upon contemplating the implementation of such meta-representations, the meaning becomes unclear. We strive to find a method to represent meta-representations, but let me explain why this is challenging. A simplistic approach to constructing a meta-representation might involve having an image as input, followed by processing through a neural network to represent the contents of the image. If this initial representation is subsequently transformed by another neural network, it seems naive to claim that this constitutes a meta-representation. This raises the issue that if every representation requires a meta-representation, it creates a perplexing situation.

Another perspective on meta-representation involves examining confidence. In the context of metacognition and cognitive neuroscience, we often gather confidence reports from participants during experiments. For instance, in a color discrimination task, participants may report what they observed, such as distinguishing blue from red. In this case, they utilize first-order information to make a perceptual decision, but they can also report their confidence in perceiving that stimulus. This approach is arguably an improvement over a simplistic transformation as a meta-representation. However, implementing this concept remains relatively straightforward. Researchers working with artificial neural networks often employ a method known as Softmax, which converts representations into a probabilistic interpretation.

Essentially, converting the activation patterns of a layer into a normalized form yielding a probability can reflect confidence. While this transformation appears meaningful regarding how the brain processes uncertainty, it has not satisfactorily characterized meta-representations. The primary solution we propose involves constructing representations of processes rather than merely states. We suggest that any neural network can be perceived as a function mapping input to output, and there is a method to present these functions or processes.

Thus, rather than representing first-order representations, we propose that if we represent the function \( f \) as a meta-representation, it may yield a more insightful interpretation of meta-representation, as this creates a qualitative distinction. To illustrate, I will provide an example utilizing artificial neural networks, which is the central theme of our paper.

I would like to briefly introduce the concept of latent space or embedding for those unfamiliar with this area. In artificial neural networks, there exists the concept of encoders and decoders. For instance, consider an autoencoder neural network trained to reconstruct an input image. This architecture contains a low-dimensional bottleneck, where interesting features emerge, capturing important characteristics of the dataset—in this case, images. Essentially, it produces a compressed representation of the dataset.

Our proposal involves creating a sort of meta-encoder, where both the input and output are neural networks. This allows a neural network to be parameterized or represented by its weights and biases, enabling various methods to convert neural networks into vectors, subsequently reconstructing the neural network. Each point in this space corresponds to a specific neural network or function, forming a space of functions parameterized by latent axes. 

I hope this clarifies the general concept. Next, I will explain the actual experiment we conducted, detailing the construction we employed. We first trained multiple encoders on various stimuli, specializing each first-order neural network in a specific stimulus category—be it visual or auditory stimuli. Each encoder can be represented as a \(1056 \times 16\) matrix, with each column corresponding to a specific aspect of the neural network.

We then used these encoders as inputs to train another autoencoder to represent individual filters, allowing us to compute the representation of the entire network using these two networks. This may seem complex, but the essential point is that we derived a representation of a network at this stage. We subsequently created another meta-encoder using the latent representation of our first network.

We applied t-SNE to visualize the latent representations, revealing that blue dots correspond to visual stimuli and orange dots to auditory stimuli. This visualization indicates a clear separation between the two modalities. Additionally, some clustering of similar shapes can be observed, suggesting that the network specialization may extend to categories such as cars or buses.

We validated our findings by attempting to predict the original dataset based solely on the meta-representations. A clear separation between modalities was evident, with some points indicating successful predictions of specific stimulus categories. This observation suggests that the weight structure of the network encodes information about the type of stimuli the networks were trained on, highlighting the significance of meta-representation.

Moreover, the question arises regarding the feasibility of this approach. Particularly when contrasting vision and audition, it is essential to consider the differences in invariances or equivariances across modalities. For instance, in visual stimuli, object categories remain unchanged under transformations like translation or scaling. In contrast, auditory stimuli may alter based on the input's movement or translation, suggesting modality-specific invariances.

Our research is motivated by classical questions about consciousness. An intriguing example involves bats, which utilize echolocation by emitting and receiving sounds for navigation. This raises questions about whether their experiences can be equated to visual experiences. Notably, an experiment conducted by an American research group at MIT in the 2000s rewired the input from the retina to the auditory cortex, demonstrating that after training on visual input, the auditory cortex developed connectivity patterns resembling those of a typical visual cortex.

This observation indicates that the connectivity reflects the statistics or structure of the data learned, leading to the question of whether the animals perceive the stimuli as visual or auditory. This further emphasizes the need for empirical research to explore the implications of theories of consciousness, such as Integrated Information Theory (IIT).

In conclusion, our approach to meta-representation provides a framework to investigate whether such representations exist in biological systems and to explore the potential functional roles they may serve. We anticipate that this research will contribute to our understanding of consciousness and the underlying cognitive processes.

Thank you for your attention, and I look forward to your questions.

---

**List of Changes Made:**

1. Structured the text into coherent paragraphs for improved readability.
2. Enhanced clarity by replacing informal language with formal academic language.
3. Corrected grammatical errors and punctuation issues.
4. Removed redundant phrases and unnecessary repetition for brevity.
5. Organized the content to present a logical flow of ideas and arguments.
6. Used precise terminology related to the field of cognitive neuroscience and artificial intelligence.
7. Clarified complex concepts with definitions and examples where necessary.
8. Removed filler phrases and maintained a formal tone throughout the text.
