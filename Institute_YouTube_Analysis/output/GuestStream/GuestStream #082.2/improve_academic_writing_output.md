**Refined Text:**

Hello and welcome. Today is June 3rd, 2024, and we are participating in Active Inference Guest Stream 82.2 with Robert Warden. In this session, we will discuss three-dimensional spatial cognition in bees and bats. Thank you, Robert, for joining us again. I look forward to your presentation.

Thank you, Dan. As mentioned, I will be discussing three-dimensional spatial cognition in small animals, specifically focusing on bees and bats. I will present a demonstration program that illustrates this concept. The program can be accessed via the link provided at the bottom of the screen, allowing you to download and explore it yourself. Additionally, there are several papers related to this work available on the arXiv platform.

This research poses a challenge to classical neuroscience, which posits that all cognitive functions are carried out by the interactions of neurons via synapses. The primary conclusion from this work suggests that neurons may not effectively represent three-dimensional space due to their inherent imprecision and sluggishness. Consequently, a significant challenge for neuroscience is to demonstrate that this hypothesis is incorrect, as the prevailing view is that neurons perform all cognitive tasks. To address this, it is essential to construct a functional neural computational model of three-dimensional space and validate its scalability and performance in a manner analogous to animal behavior. Merely publishing papers and engaging in discussions is insufficient; practical model development is crucial. I believe that the FP neural process model serves as a promising foundation for this endeavor.

Spatial cognition is a critical issue, as the primary function of any animal brain is to manage its physical movements in three-dimensional space. This task is constant and occupies a significant portion of the brain's capacity in most animals. We maintain that animals utilize Bayesian methods to construct and employ a maximum likelihood model of three-dimensional space. My previous livestream discussed how animals generate models in general; however, the specific 3D model of space has gained importance since the Cambrian era, when animals first developed precise sensory data through advanced visual systems and capable limbs. Since that time, there has been substantial evolutionary pressure on animal species to excel in spatial cognition.

It is posited that animals are quite adept at this task. For instance, our conscious awareness of three-dimensional space must stem from processes occurring in our brains, reflecting a precise model of our surrounding environment. Even small insects exhibit remarkable spatial abilities; for example, they can land skillfully on the rim of a coffee cup or any other surface. Hence, modeling three-dimensional spatial cognition is a top priority for neuroscience. While various challenges exist in the field, this is fundamentally the core issue that requires resolution.

To investigate how animals build a three-dimensional model of their surroundings, we must address the immediate problem of the two-dimensional nature of sensory data from vision. While stereopsis—depth perception using two eyes—provides some constraints, these are limited to specific regions around the animal. I believe that animals construct their spatial models through movement, utilizing a form of active inference that necessitates mobility to gather information about space. This is supported by strong Bayesian probability, as the majority of objects in the environment remain stationary while the animal moves, allowing for the computation of object locations through a method known as structure from motion (SFM).

The computational model of SFM is relatively straightforward, involving basic three-dimensional matrix operations to maximize the likelihood of an object existing in a particular location. The demonstration program I am presenting incorporates limited vision and echolocation capabilities, which provide both echo delay and Doppler shift data. We will discuss these features in detail. Both bees and bats can move swiftly among static objects, making SFM an applicable method for determining object locations. The program constructs a 3D spatial model in three distinct ways: firstly, through an optimal Bayesian shape model, which serves as a brute-force calculation. I have addressed this in previous discussions, noting that while this method yields the best possible Bayesian model based on sensory data, it is not necessarily how animals operate. 

Secondly, the model employs dynamic object tracking, allowing the animal to estimate the three-dimensional positions of objects while continuously updating those estimates with each movement. The third model incorporates tracking amidst neural memory noise. It is important to clarify that this computational model is designed at a Mars level two—meaning it is not a neural implementation—but I have included functionality to simulate neural noise. After the demonstration, you may download the program from the provided web address and easily unzip it to begin using it.

I will now transition to demonstrating the program. As I do so, you will observe three distinct windows: the left window displays a three-dimensional view of the space within which a bee or bat is moving; the central window provides health information, guiding you on how to use the various sliders, buttons, and controls; and the right window presents various graphs, which we will review as we progress.

Upon pressing the start button, you will see a three-dimensional space populated by a bee represented on the left side, with colored circles indicating various objects randomly placed within that space. The lines extending from the bee to the objects represent lines of sight. As you rotate the view, the objects will shift accordingly. Initially, we will not see the bee's internal model of space; rather, we will observe the actual environment. To visualize the bee's internal spatial model, we will press the run button. 

As the bee begins to move along the green line, it collects new lines of sight and estimates the positions of all visible objects. If I restart the program, you will see that the estimated positions are represented as small circles with error bars. The error bars indicate uncertainty in the three-dimensional estimates. This demonstrates that the bee is constructing a relatively accurate model of the spatial positions based on its sensory data.

If I restart again and step through the program incrementally, you will see how the bee's model of space evolves over time. In the early stages, the bee makes increasingly accurate estimates of object locations, with each small white circle representing the bee's estimate and the blue circle indicating the true object location. The error bars illustrate the uncertainty in the estimates across all dimensions. These position estimates are crucial for the bee's ability to navigate effectively, such as when seeking flowers for pollen.

The program computes three different models of spatial cognition as it progresses through the tracking steps. The first is the full Bayesian model, which we are currently demonstrating. The second is the dynamic tracking model, where the bee makes estimations of object positions in three dimensions and updates them with each movement. I can switch to this model now. You will notice that while the objects appear to move slightly, the error bars indicate that the estimates remain largely consistent. 

The third model incorporates tracking with noise, which I will now demonstrate. This model shows that tracking with noise often yields significantly worse estimates than tracking without noise. Currently, I am running the model with a low level of neural noise, but you can adjust this parameter, as well as the bee's visual accuracy, using the sliders.

As I continue stepping through the program, the noisy tracking estimates diverge from the true positions of the objects. When I revert to the tracking model without noise, you will observe that the estimates align closely with the actual object locations. I will restart and run the program again, allowing you to see the graph on the right. This graph compares the tracking model (represented by the black curve) with the noisy tracking model (represented by the red curve). The vertical axis indicates the level of error in depth estimation for the bee. You will notice that tracking yields smaller errors, honing in on the true positions of objects, whereas memory noise results in larger, unpredictable errors. 

Should we rerun the program, you will observe that errors stemming from noisy tracking vary significantly from one run to the next, underscoring the unpredictability of this model. In contrast, the tracking model without noise demonstrates a consistent convergence towards true object positions. This simulation illustrates that while a tracking model serves as a realistic representation of how animals estimate object locations, the introduction of noise can severely degrade accuracy. 

Furthermore, the model can demonstrate how animals utilize their spatial models to detect movement in their environment. When an animal is in motion, it becomes challenging to discern motion within its visual field, as everything appears to move. Consequently, the animal must rely on its three-dimensional model to identify what is genuinely in motion. Efficiency in motion detection decreases significantly when memory noise is present. 

At this juncture, I will conclude this demonstration. While the program also simulates bat cognition, I will not delve into that at this moment. If there is interest later, we can revisit it. To summarize the key points, the 3D view illustrates the animal's track and its lines of sight. I have shown you the actual object locations, the bee's internal spatial model, the shape from motion, and the significance of error bars, particularly in the depth dimension. Additionally, I have highlighted how memory noise impacts model accuracy.

The principal findings indicate that the optimal model any animal can construct from its sensory inputs is quite effective, often surpassing the precision of the raw sensory data. If animals can assume that objects remain stationary, they can accumulate a comprehensive understanding of their environment over time. While dynamic object tracking performs admirably, it only succeeds when spatial memory maintains high precision. The precision levels necessary for accurate tracking are approximately one part in a hundred, which I believe exceeds the capabilities of most neural representations of space.

The subsequent segment of this discussion will explore how to develop a neural model of spatial memory. This brings to mind the famous quote from George Orwell's "Animal Farm": "Two legs bad, four legs good." In this context, we might rephrase it as "Two dimensions easy, three dimensions hard." In two dimensions, a sheet of neurons can effectively represent spatial information. In contrast, representing three-dimensional space poses significant challenges, and several potential memory designs exist. 

For example, a two-dimensional sheet of neurons can represent the third dimension through depth, or a three-dimensional cluster of neurons can encode spatial positions. However, none of these approaches work optimally for object tracking. The challenges arise from neural error rates; if neural information is encoded as firing rates, the precision of representation is limited. Typically, a neuron fires n times within a specific time interval T, and the precision of representation is approximately one part in the square root of n. In most animal brains, n is typically between five and fifty pulses per second. For smaller animals, the time available to update their internal spatial model is often less than one-tenth of a second, resulting in errors of approximately 30%, which are far greater than the one percent accuracy necessary for effective tracking.

In conclusion, there exists a trade-off between speed and precision when neurons represent spatial information. Faster processing leads to reduced precision, and this trade-off presents significant challenges. I believe there is currently no effective neural model for three-dimensional spatial cognition.

The three key points I previously mentioned highlight the significance of spatial cognition, the proficiency of animals in this area, and the longstanding nature of this problem. David Marr identified this challenge in his 40-year-old work on vision. However, advancements in neural models of spatial cognition have been limited. I suspect that many researchers have encountered this issue and opted to pursue other avenues due to the complexity of the memory problem, which results in substantial errors and slow processing. Consequently, spatial cognition remains a central problem within neuroscience, akin to a theory of planetary motion without a sun or a theory of the atom without a nucleus.

How does this relate to active vision? Active vision describes how a three-dimensional spatial model can be inferred from visual input. Numerous papers have explored various aspects of this topic, focusing on two-dimensional scene classification, trade-offs between visual objectives, and three-dimensional robotics. However, none have thoroughly addressed how animal brains practically construct a three-dimensional model. I believe existing active vision models fail to consider neural error rates, which are critical for understanding spatial cognition.

The standard active inference toolkit in MATLAB does not adequately model neural error rates, as it assumes an idealized neuron with precise representations, rendering error rates inconsequential for many applications, including robotics. However, as I have emphasized throughout this presentation, the accuracy of three-dimensional models is paramount, and neural error rates pose significant challenges. 

If we momentarily set aside the neural error issue, we can explore the intriguing trade-offs present in active vision. One essential trade-off is the decision to freeze or move. As demonstrated in the program, an animal must move to infer the three-dimensional positions of surrounding objects through shape from motion. Simultaneously, movement is necessary to achieve practical goals, such as feeding or avoiding predators. Conversely, remaining stationary may conserve energy, facilitate motion detection from the visual field, and enhance stealth. These trade-offs are crucial for the survival and fitness of many animals, necessitating constant evaluation throughout their daily lives.

I will now pivot to a distinct topic. While acknowledging that neural storage of spatial positions is complex, I will propose an alternative method for storing spatial data. Consider a spherical region within the brain with a substantial diameter, capable of holding waves with a minimum wavelength, which I will refer to as lambda. Neurons may couple to these waves as both transmitters and receivers, allowing the wave to persist for a fraction of a second. This mechanism can serve as a working memory for spatial positions, with the potential to store numerous object positions based on the size of the spherical region.

The spatial precision with which an object position is stored can exceed one part in D over lambda, where D represents the diameter. Given that D over lambda can be quite large, achieving precision better than one part in one hundred is feasible for constructing a spatial model. 

In summary, wave-based storage of three-dimensional positions offers numerous computational advantages, including high precision, rapid response times, and minimal spatial distortion. Is there any evidence supporting wave storage in the brain? I believe there are two compelling lines of evidence. The first pertains to the central body of insects, which is a small, conserved structure in the insect brain. The central body consists of a fan-shaped body and an elliptical body, maintaining a remarkably consistent shape across various insect species. This structure is well-suited to accommodate a three-dimensional wave and is involved in multisensory integration, suggesting it may store spatial positions.

The second line of evidence arises from the mammalian thalamus, which is approximately spherical and connected to all sensory data and cortical regions. The shape of the thalamus is highly conserved across species, and its anatomical structure raises questions. The thalamus comprises independent nuclei, such as the pulvinar and the lateral geniculate nucleus (LGN), with weak or nonexistent connections between them. This arrangement implies that thalamic nuclei could migrate outward toward the cortex without compromising synaptic connectivity or computational capability, assuming neurons rely solely on synaptic computation.

In summary, the compact structure of the thalamus is more comprehensible if all nuclei are immersed in a shared wave. We have three pieces of evidence for a wave in the brain: the computational neuroscience perspective, the insect central body's shape, and the mammalian thalamus's anatomy. 

It is worth noting that the wave proposed here is likely not an electromagnetic wave, as significant research has explored electromagnetic fields in the brain. However, electromagnetic fields cannot fulfill the role this wave is intended to play; specifically, they cannot store information for fractions of a second or represent three-dimensional space. 

To elaborate further, electromagnetic waves must comply with Maxwell's equations, which dictate that the wavelength multiplied by the frequency equals the speed of light (λf = c). At a frequency of 40 Hz, typical wavelengths would be approximately 8,000 kilometers, far larger than the dimensions of the human brain. Thus, at 40 Hz, electromagnetic waves do not function as memory storage.

In summary, we are in search of a mechanism that is not electromagnetic, potentially involving quantum excitations or other exotic phenomena within the realm of quantum biology. 

I would like to present several take-home questions. Does three-dimensional spatial cognition involve a wave in the brain? Given the evidence I have presented, what is the Bayesian probability of this hypothesis being true? I pose these questions to encourage reflection, as I do not expect immediate answers. I invite you to explore the relevant literature to assess the evidence. 

Alternatively, do you possess a compelling reason why a wave cannot exist in the brain? If so, what is that reason? Furthermore, how do brains compute spatial information? Can neurons alone represent three-dimensional space with sufficient precision? 

On the other hand, if a wave in the brain is a viable hypothesis, it could represent a groundbreaking development in neuroscience, potentially addressing the fundamental unresolved issue of how spatial cognition occurs. I believe this avenue warrants exploration, particularly for young researchers, as it presents a unique research opportunity not yet fully pursued within classical neuroscience. The classical model, which focuses solely on neurons and synapses, is now over 75 years old.

Thus, I advocate for a dual-track research program aimed at constructing two distinct active vision models of three-dimensional spatial cognition. The first is a pure neural model based on the classical neural process model. The question is whether this model can be made functional, or if neural memory errors will hinder its effectiveness. The second model involves a hybrid wave-neural approach. 

In building these models, we can investigate the trade-offs that active inference effectively computes, particularly the balance between freezing and moving. There are several candidate projects for the Active Inference Institute.

Thank you, Robert. I have some questions from the live chat that I would like to address. While I gather everything, could you connect your work to the requirements equation and earlier research? You mentioned a requirements equation-driven calibration for optimal navigation; what does that entail?

To summarize the requirements equation, you can model how brains evolve towards making purely Bayesian calculations of their best models of the world based on sensory data. However, this purely Bayesian calculation is computationally expensive and is often not feasible for most animals. While it can be performed on digital computers, it is not necessarily how animals operate. In our model, the full Bayesian calculation computes the requirements equation based on the sensory data from bees or bats, while the tracking model serves as an approximation that is more efficient yet yields similar results.

Now, I will address some neuroanatomy questions from the live chat. Tim Ritter asks if you assume the wave property applies to all thalamic nuclei or only specific ones, such as the pulvinar or mediodorsal nuclei.

That is an excellent question, and at this stage, I believe the entire thalamus is a roughly spherical structure through which the wave propagates. Thus, all nuclei, including the pulvinar and the LGN, would be immersed in this wave. While it is commonly stated that the thalamus serves as a relay for sensory data to the cortex, there is limited understanding of why this relay is necessary. I suspect that the wave plays a role in the thalamus's function, but further research is needed to clarify this.

Another question from Tim pertains to two-dimensional orientation. Would you expect similar waves in the hippocampus, or is two-dimensional navigation sufficiently manageable without them?

I believe that two-dimensional navigation is relatively straightforward, and the hippocampus is not an ideal structure for wave storage due to its varied shapes across different animals. The core theme lies in the conserved shape of the insect central body, which exhibits less variability in size compared to other primary sensory regions. 

The central body, which constitutes only a small fraction of the insect brain, appears to be adequate for its function. In contrast, primary sensory regions demonstrate substantial variation among species. The mushroom body, located at the top of the insect brain, may serve as an intermediary structure, analogous to mammalian cortex, where cognitive capacities can scale with size due to its repetitive layout.

There are numerous fascinating questions in neuroanatomy, and pursuing this hypothesis will yield interesting insights. I am not an expert in insect or mammalian neuroanatomy, but many intriguing inquiries await exploration.

Regarding bee spatial cognition, we know that bees utilize various visual cues, including landmark recognition and light polarization. The central body facilitates multisensory integration. How do we conceptualize the complementary or redundant information provided by these different visual aspects?

I believe that both the central body and the thalamus are responsible for multisensory integration. Animals must construct the most accurate three-dimensional spatial model possible, utilizing all available sensory data. While the current program only incorporates basic visual and echolocation inputs, a more comprehensive simulation should integrate all multisensory data into a unified Bayesian maximum likelihood model.

Next, let's discuss egocentric and allocentric navigation. Given that the simplifying assumption is that the world remains a fixed entity, how does this relate to the distinction between egocentric and allocentric perspectives?

This is a pertinent question. I think the reference frame used in the model should be as allocentric as possible, as the wave's persistence indicates that objects are positioned at fixed locations. Nevertheless, the frame of reference must occasionally update every few seconds, as it cannot remain entirely allocentric.

This also connects to the fundamental question of whether to stay or move. For organisms whose eyes cannot move independently of their bodies—like bees—movement becomes a critical factor in gathering spatial information. In contrast, humans possess ocular capabilities that allow for independent eye movement, facilitating high-resolution vision.

The decision to move or remain stationary represents a genuine trade-off. While an animal's movement may enhance the detection of motion in its environment, it can also expose the animal to potential threats. Conversely, remaining stationary may facilitate more effective motion detection but may also increase vulnerability.

I will now read a question from the live chat. User "equal" inquires about how the ability to conceive of other domains of time as a cognitive function might alter spatial awareness.

This is a profound question. The current discussion focuses on short-term memory, specifically fractions of a second. Temporal awareness beyond that interval does not significantly factor into this model. 

In summary, our awareness of chronological time is likely distinct from spatial awareness. Most animals operate in the present moment, concentrating on immediate needs and actions. In contrast, humans can ruminate and speculate about the future.

What directions or future avenues of research do you foresee for this work?

One significant avenue is the exploration of consciousness. A substantial portion of our consciousness relates to spatial awareness, which seems to stem from our internal Bayesian model of our surroundings. This work may contribute to a more satisfactory theory of consciousness compared to traditional neural models.

I am also enthusiastic about the empirical side of insect neuroanatomy, as many avenues for investigation remain. Insects, due to their limited number of neurons, present a unique opportunity to study spatial cognition.

Furthermore, I am interested in understanding how active inference relates to policy selection for movement. This includes decisions about whether to stay or go and which direction to take. By examining the realized empirical trajectories, we can analyze how various factors—such as safety, visual information gain, and other impulses—affect movement decisions.

Thank you for your engaging questions. I hope that attendees will download the program and experiment with it to further explore these concepts. 

Thank you, Robert. I greatly appreciate your insights into the relationship between the requirements equation, spatial cognition, and empirical patterns. This work highlights the interconnectedness of theory and empirical findings, providing a framework for understanding how spatial cognition operates in various contexts.

In closing, I would like to quote physicist Richard Feynman: "If you can't build it, you don't understand it." This sentiment underscores the importance of practical application in scientific inquiry. While we may not yet be able to replicate a bee's cognition, the exploration of these models will enhance our understanding of spatial cognition. Thank you, Robert. I look forward to our next discussion.

**List of Changes Made:**

1. Corrected grammatical errors and improved sentence structure.
2. Enhanced clarity and coherence by restructuring lengthy sentences.
3. Replaced informal phrases with formal academic language.
4. Removed trivial statements to maintain focus on the core topics.
5. Consolidated repetitive ideas to avoid redundancy.
6. Improved transitions between topics for better flow.
7. Clarified complex concepts with simpler language and definitions.
8. Removed unnecessary filler phrases for conciseness.
9. Enhanced precision in terminology to align with academic standards.
10. Organized content into a more logical sequence for improved understanding.
