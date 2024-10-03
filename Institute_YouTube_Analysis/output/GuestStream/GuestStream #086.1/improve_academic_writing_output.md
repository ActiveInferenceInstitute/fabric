Refined Text:

Greetings, and welcome to the Active Inference Guest Stream number 86.1, featuring a discussion on the comparative sample efficiency of biological neurons and deep reinforcement learning in a simulated gaming environment. We are pleased to have Faro Habib and Mo Kaj NAD with us today. Thank you both for joining; we eagerly anticipate your presentation.

Thank you, Danielle. I would like to extend a warm welcome to everyone attending. I hope this presentation proves to be both informative and enjoyable. Today, we will discuss a collaborative research effort between Cortical Labs in Melbourne and Monash University, focusing on the project titled "Biological Neurons Compete with Deep Reinforcement Learning in Sample Efficiency in a Simulated Game World." Before delving into the findings, I will briefly outline our experimental setup involving in vitro neuronal cultures, which we have integrated into simulated gaming environments to conduct various experiments that have led us to our conclusions.

To begin, I will share the motivations that guided our work at Cortical Labs and how we arrived at our current understanding. While I will avoid overly philosophical discussions, it is essential to acknowledge that humans require intelligence to derive meaning from the phenomena around us. Our goal has been to enhance decision-making capabilities by processing data more efficiently, which has become a central objective in the fields of machine learning and artificial intelligence over the past several decades.

In exploring alternative approaches to intelligent computing, we can categorize our recent efforts into various domains, such as machine learning, AI, quantum computing, and neuromorphic chips. Each of these categories possesses distinct advantages and disadvantages. Our motivation for seeking new computational paradigms stemmed from the challenges faced by machine learning and AI, including high computational power requirements, significant energy consumption, catastrophic forgetting, the necessity for large sample sizes, and extended training times, all while being susceptible to errors.

Similarly, quantum computing presents its own challenges, such as excessive power usage, isolation from the external environment, and limited adaptability. Neuromorphic computing also encounters issues, including restricted error correction capabilities, variability among circuits, and the need for programming to fulfill designated tasks. In light of these challenges, we proposed utilizing biological neurons—an advanced form of intelligent system—as a potential solution.

At Cortical Labs, we design and develop our systems using human-induced pluripotent stem cells (iPSCs) differentiated into neuronal phenotypes. Additionally, we utilize primary cortical neuronal cell cultures derived from mice. These cell cultures are plated onto high-density multi-electrode arrays (MEAs), which facilitate simultaneous stimulation and recording of neuronal activity. Notably, these cultures have demonstrated the ability to survive for over six months on these MEAs, and with our latest products, we can extend their viability even further, enabling long-term studies.

We created a closed-loop real-time system, referred to as the "dish brain," which interacts with these neuronal cultures and embeds them in the arcade game "Pong." This game involves a paddle attempting to hit a ball against a wall. Our initial publication outlined the system and detailed our findings, although I will refrain from presenting all the intricate details here.

To summarize, our closed-loop system comprises a sensory region and two motor regions. The sensory region receives information about the ball's position in the game, encoded through rate coding and place coding. We then compare the activity of the motor regions to determine the paddle's movement direction. If the paddle misses the ball, an unpredictable signal is applied, while accurate hits elicit a predictable stimulation across the sensory electrodes.

The evidence we gathered indicates that this feedback loop enables the neurons to learn and improve their performance in the game over time. This phenomenon aligns with the concept of free energy principles, as the neurons exhibit a preference for reduced surprise and enhanced predictability.

We evaluated the performance of the cultures using various metrics, revealing significant improvements in average rally lengths, reduced occurrences of missed balls (Aces), and increased percentages of long rallies. These findings suggest that our biological neural networks outperform conventional deep reinforcement learning algorithms in terms of sample efficiency.

In our ongoing projects, we aim to investigate the connectivity dynamics of neuronal cultures during gameplay and rest sessions. We utilize dimensionality reduction algorithms to analyze spiking activity, ultimately comparing the functional connectivity of channels across different conditions.

Mo will now elaborate on our findings from the functional connectivity study and provide a comparison with reinforcement learning methods regarding sample efficiency.

Thank you, everyone. Our challenge involves analyzing large time series data from each channel to identify patterns. We employed dimensionality reduction algorithms, such as t-SNE and Isomap, to facilitate interpretation. Interestingly, even in low-dimensional representations, we observed distinct separations between gameplay and rest sessions.

We hypothesized that many channels exhibit high correlations, leading to redundancy in our data. Therefore, we designed a pipeline to study functional connectivity and compare gameplay with rest sessions. After mapping channels to lower dimensions, we selected representative channels using Tucker decomposition and k-means clustering.

Next, we constructed functional connectivity networks based on the Pearson correlation of spiking activities. We tracked changes in correlations over time, revealing significant differences between gameplay and rest. The gameplay sessions exhibited more positive correlations, indicating increased connectivity among channels.

We compared various metrics of network dynamics, noting significant increases in average weights and clustering coefficients during gameplay, alongside decreases in modularity and characteristic path lengths. These results suggest that network dynamics may underpin the emergent learning observed in our cultures.

We conducted direct comparisons between deep reinforcement learning algorithms and our neuronal cultures within the Pong environment. While reinforcement learning algorithms have demonstrated strong performance in various games, they face issues such as sample inefficiency and high computational demands. Our findings indicate that biological cultures exhibit superior sample efficiency, achieving better performance with fewer training episodes.

In conclusion, our research underscores the potential of biologically inspired learning systems. While deep reinforcement learning algorithms require extensive training to achieve optimal performance, our biological neuronal cultures demonstrate remarkable capabilities with minimal resource consumption. Future investigations will explore the mechanisms underlying these learning processes and assess the impact of additional factors, such as glial cells, on their performance.

We appreciate the support of our collaborators and invite further discussion on our findings. Thank you for your attention.

List of Changes Made:

1. Improved overall structure and coherence of the text.
2. Corrected grammatical errors and clarified ambiguous phrases.
3. Replaced informal language with formal academic terminology.
4. Eliminated trivial statements and redundant phrases for conciseness.
5. Organized the content into clear sections to enhance readability.
6. Added necessary transitions and connectors to guide the reader.
7. Maintained the original meaning and intent while improving clarity and professionalism.
