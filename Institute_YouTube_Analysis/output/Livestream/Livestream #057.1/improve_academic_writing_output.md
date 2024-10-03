**Refined Text:**

Greetings, and welcome to our live stream on May 28, 2024. This is episode 57.1 of the Active Inference Institute, an online participatory platform dedicated to communicating, learning, and practicing applied active inference. Please note that this live stream is recorded and archived for future reference. We welcome feedback to enhance our efforts, and we encourage participation from individuals of all backgrounds and perspectives. As a reminder, we will adhere to video etiquette during our discussion. For further information regarding our live streams and other projects, please visit activeinference.org.

In today's session, we will continue our discussion on the paper concerning active data selection and information seeking, featuring contributions from Karl Friston and Thomas Parr. Thank you both for joining us. In episode 57.0, we covered some background information. To commence 57.1, I invite Thomas to lead us into the active data selection setting and the SL Challenge, introducing himself as he sees fit. 

Thank you, and please proceed.

To introduce myself, I am Thomas. I have been engaged in active inference research for several years, dividing my time between research and clinical practice. This dual focus has motivated some of the later aspects of our paper, which relate to clinical challenges we may encounter. The background for this paper originates from a few years ago when I presented at the Australasian Bayesian Network Modeling Society conference in Australia. The conference featured engaging discussions on Bayesian networks applied to various domains, including volcano modeling and coastal erosion. Notably, several clinicians were present, focusing on issues such as respiratory diseases and diagnostics. One of the conference organizers was preparing a special issue on Bayesian networks and invited us to contribute, resulting in this paper. Our objective is to apply principles of active inference and established concepts from influential figures like Stuart Lindley to the problem of experimental design, exploring how these principles can extend beyond biology.

Apologies for speaking too quickly. Carl, would you like to add anything before we proceed?

No, I am simply an interested observer. 

Excellent. Let us move to Chris's questions. As participants pose questions in the live chat, we will address them as well. 

To begin, let us discuss time sampling. How did you incorporate time into your equations and conceptual framework in this paper? 

Time is indeed a fascinating consideration when modeling various processes. Many significant phenomena evolve over time, which raises intriguing questions about how we sample and gather information. A major challenge arises from the fact that some elements change while others remain constant. This leads us to psychological concepts such as inhibition of return, which suggests that the time it takes to revisit something depends on how unexpectedly it may change. This concept is vital in generative models we utilize in both biological and non-biological contexts, as it compels us to consider how to effectively model temporal dynamics.

Historically, much early work in active inference was articulated through continuous time models employing differential equations and generalized coordinates of motion, representing trajectories in terms of position, velocity, and acceleration. More recent investigations have shifted towards discrete time models, viewing phenomena as a sequence of events at specific time points. In this paper, we adopted a slightly different approach, utilizing a basis set of functions to facilitate smooth temporal progressions, thereby blurring the distinction between discrete time steps and continuous changes. 

Time is crucial in how we conceptualize these processes, especially when considering the dynamic nature of change. 

Welcome, Chris. This discussion aligns with figure 4.3 from the textbook. How would you compare it to explore which variables are continuous or discrete? 

Indeed, this paper may not contain explicit figures, but you are correct that the textbook includes relevant distinctions. One of the later figures illustrates a basis set representation for temporal progressions, although I cannot recall the specific figure number. Would you like to summarize the figure currently displayed?

This figure aims to demonstrate, in a relatively straightforward analytic context, what it means to select data points that provide the most information about an underlying model. It begins by showing a function characterized by various parameters, denoted as theta. Some areas exhibit significant variation, while others do not. For instance, the green parameter shows a pronounced peak at zero, while the purple and yellow parameters display smaller peaks. Conversely, there are points where distinguishing between the parameters is challenging. Selecting a data point near zero is more informative than choosing one near the x-axis where they converge. This illustrates the importance of efficient data selection in resolving alternative hypotheses and estimating continuous parameter values.

Continuing this visual progression, we depict various generative models, such as a Bayesian network where the explanatory variable is theta generating data y, alongside a policy variable pi that represents our sampling choices. The subsequent factor graph representation explicitly includes factors that define our probabilistic distributions concerning theta and y. 

The next step involves using a normal or factor graph representation, which facilitates understanding message passing and the contributions of different variables to our estimates. Each square represents a factor, and the edges indicate connections between variables. By employing message passing algorithms, we can derive posterior estimates of variables, including the theta parameter. 

A key aspect here is that we are not only interested in inference but can also interpret these messages in terms of how they contribute to our information gain. The conditional entropy, representing ambiguity, indicates how confident we are in the mapping between parameters and data. Predictive entropy, on the other hand, reflects our uncertainty about future observations before any measurements are made. 

This distinction is particularly relevant in experimental design, as high predictive entropy suggests that if we are already confident about our observations, there may be little value in conducting further experiments. Conversely, if we are uncertain, it is worth seeking additional data points. 

Thank you, Thomas, for that comprehensive overview. We will return to this topic. Let us now consider figure 4.3 from the textbook. 

Yes, this figure illustrates factor graph representations of temporal progressions, where the upper graph shows a series of states transitioning over time. The factors in this model indicate the data generated by specific states, and the relationship between conditional entropy and the mapping from states to outcomes is crucial. 

The lower graph represents continuous time, employing variables such as x for states and their derivatives for rates of change. Understanding these dynamics allows for trajectory construction and anticipatory modeling based on recent past behaviors. 

This discussion emphasizes the importance of selecting appropriate representations for time in generative models. 

Regarding the basis sets, how do they compare in handling time in discrete versus continuous settings? 

The use of basis sets typically implies a continuous function, but generalized coordinates of motion can also be viewed as a polynomial basis set. Other basis sets, such as Fourier or cosine bases, may not localize time points effectively but offer frequency-based representations. In this paper, we utilize Gaussian basis functions centered at various time points, allowing for smooth transitions and a flexible representation of nonlinear functions.

Thank you, Thomas. Basis sets are also mentioned in the context of SPM, highlighting their capacity to specify oscillatory patterns and filter data, thereby compressing information related to hypotheses about data structure.

Indeed, employing basis sets facilitates compression, as one can truncate after a certain number of functions. This approach aligns with the concept of autocorrelations over time and offers utility in image processing applications, such as the discrete cosine transform, which allows for the discarding of certain frequency bands without significant information loss.

Let us proceed to Chris's second question. 

Regarding potential algorithmic modifications, could hybrid approaches lead to improved data selection optimization?

Certainly. The effectiveness of hybrid approaches depends on their integration with the appropriate models. Heuristics, from a Bayesian perspective, can enhance efficiency when informed by prior knowledge about the problem structure. If you understand the underlying dynamics, you can formulate a model that requires less reliance on basis sets, allowing for more efficient data selection.

The selection process is crucial, as it aims to optimize the model's fit to the world. The underlying principle remains consistent: finding the best fit is essential in the context of the selected prior. 

Chris or Carl, would you like to contribute? 

I am contemplating the relationship between heuristics and their application in economics. Additionally, I would like clarification on the term "metahuristic." 

A metahuristic typically refers to a heuristic that operates at a higher level, such as a hyperprior in Bayesian contexts. 

Thank you for that clarification. 

Let us shift our focus to the practical aspects of modeling adaptive data sampling. What is the recipe for active inference generative modeling, especially considering any updates since chapter 6? 

The fundamental recipe remains consistent. It involves defining the model's purpose and the questions it addresses. When using models in data contexts, important questions include identifying the best explanatory model among alternatives and estimating specific parameters. This is particularly relevant in computational phenotyping within clinical populations, where understanding belief variation can inform behavioral outcomes.

The figure from chapter 6 illustrates the modeling process and empirical data utilization. The key idea is that if the model predicts behavior effectively, it can inform our understanding of other individuals' cognitive models. 

As we move towards the end of our discussion, we will explore the clinical trial context and relevant future inquiries. Chris posed a question about the integration of active data selection methods with machine learning models, particularly deep learning architectures that typically require large datasets. What challenges arise in this context?

I contend that the reliance on large datasets in machine learning contrasts with the principles we advocate in our paper, which emphasize efficient data utilization. The objective is to design models and data selection strategies that yield informative insights from smaller datasets. Most machine learning models can be viewed as forms of statistical modeling, regardless of their explicit uncertainty representation. 

Hybrid approaches may incorporate neural network architectures as components of Bayesian statistical models. This can enhance efficiency and simplify inference processes. However, a significant challenge is predicting or generating outcomes during active data selection. Generative approaches in machine learning can facilitate this, but the complexity of highly nonlinear models can complicate effective data selection.

This area warrants further exploration, particularly in how clear mappings in deep learning models can inform active data selection strategies. 

The interplay between reliable information sources and adaptive foraging is crucial. Reliability influences an agent's information seeking, while variability in latent states presents challenges. It is essential to understand what is resolvable and to avoid blindly sampling uncertain data. 

I would like to discuss the nature of precision weighting mechanisms. Can high precision in priors obstruct the prediction error from conveying significant information?

Precision can be applied to any probability distribution, influencing how we update beliefs based on prior and likelihood comparisons. A highly precise prior can lead to rigidity in belief updates, potentially diminishing the value of new information. Conversely, a precise likelihood can enhance the salience of certain regions, guiding attention and information seeking.

The concept of prediction error arises when assessing discrepancies between predictions and actual outcomes, with updates weighted by the precision of the likelihood. This relationship is crucial in continuous state models and informs predictive coding frameworks.

Let us also consider the streetlight effect as a metaphor for information seeking. How does this analogy illustrate our discussion?

The streetlight effect describes the tendency to seek information where it is most easily accessible, even if it is not the most informative location. From an active inference perspective, beginning with readily available information is optimal, as it reduces ambiguity. 

Carl or Chris, do you have any insights to add?

I appreciate the analogy; it effectively encapsulates the challenges of information seeking. 

Let us now discuss equation three and its application in Bayesian graphs regarding information gain.

This equation leverages message passing algorithms to efficiently estimate beliefs about variables, considering conditional dependencies in sparse networks. It utilizes the structure of the network to compute information gain about specific variables based on the local blanket surrounding them. 

The relationship between the generative model and the actual data generation process is vital. It is essential to recognize when a model may be incorrect yet still serve as a better explanatory tool due to its simplicity. 

The choice of distribution family impacts information gain and how we sample data. Categorical and continuous models exhibit different forms of information gain, underscoring the significance of selecting the appropriate model for sampling purposes.

This interconnectedness illustrates the iterative nature of model development and the influence of sampling on our understanding of uncertainty and decision-making.

In conclusion, we appreciate your contributions and insights. Next, we will delve into the code and explore its practical applications in relation to clinical trials. Thank you for your participation, and we look forward to our next discussion.

---

**List of Changes Made:**

1. Improved grammatical structure and coherence throughout the text.
2. Replaced colloquial expressions with more formal academic language.
3. Streamlined lengthy sentences for clarity and conciseness.
4. Removed unnecessary repetitions and trivial statements.
5. Clarified complex ideas and concepts for better understanding.
6. Organized the text into clear sections and transitions for better flow.
7. Maintained the original meaning while enhancing academic rigor.
