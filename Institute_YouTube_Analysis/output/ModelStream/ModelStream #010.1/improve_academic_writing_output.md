**Refined Text:**

Greetings and welcome to the Active Inference Model Stream, number 10.1, which is taking place on April 4th, 2024. We are excited to have Bart Benp and Albert Penko with us today to discuss the development of a drone utilizing the RX and Fur frameworks. We have an ongoing RX and Fur learning group at our institute, and many participants are enthusiastic about using even the early versions of this software package to explore exciting mathematical developments. Thank you both for joining us; we look forward to this practical presentation.

Thank you, Daniel, for your kind words and introduction. Welcome to everyone joining us online. As Daniel mentioned, we will focus on building a drone today. Until last week, I had no knowledge of drones; however, I have crafted one with the assistance of my colleagues and aim to share this learning experience with all of you. This will enable you to leverage the capabilities of our RX and Fur toolbox to create your own applications, whether they be drones, autonomous vehicles, or other innovative projects. We will be here to support you throughout this journey.

Let us begin by discussing how we will construct a drone with RX Infer. First, I will briefly introduce myself. My name is Bart Arab, and I am a PhD student and teaching assistant in the BAP research group at the Inov University of Technology. Alongside Albert, who is also present and will monitor the chat for questions, we will be your hosts today, in collaboration with Daniel. This presentation is supported by Reactive Base, which is the overarching organization for RX Infer and all its associated packages. We are currently seeking contributors; if you are interested after this talk, please reach out, and we can familiarize you with our toolbox and environment.

We are from Bias Lab at the AOV University of Technology, located in AOV, known as the City of Light. Our research focuses on building agents, probabilistic graphical models, and applying these to develop various engineering applications aimed at solving real-world problems. Our engine, RX Infer, is a Julia-based platform that facilitates automatic Bayesian inference through reactive message passing. The engine we developed is entirely reactive, meaning it only performs computations when necessary, thus enhancing energy efficiency by conserving resources during idle periods. We will delve deeper into this topic later in the talk.

We will use this toolbox to create a drone capable of flight by employing simplified drone mechanics to navigate from one position to another. I am eager to share this developmental journey with you. The presentation will consist of three parts: first, model specification; second, probabilistic inference; and finally, experimental validation, followed by a question-and-answer session.

To begin, we will start with the model specification, where we will craft a model incorporating drone physics. I will revisit concepts from high school physics to refresh our understanding and construct a generative model of a simplified drone. Following this, we will discuss probabilistic inference, which allows us to compute posteriors based on the model. This inference will serve as the foundation for the control algorithm we will develop, utilizing our RX toolbox. Finally, we will conclude with experiments and address any questions you may have.

Let us commence with model specification. We will explore simplified drone physics, which may serve as a refresher for some and a new learning opportunity for others. Throughout the next few minutes, we aim to provide a foundational understanding of drone operation. We will simplify the model to focus on the forces acting on the drone. We will assume that each rotor produces an upward force, while gravity opposes this force, enabling altitude control. By balancing these forces, we can determine the necessary thrust for the drone to ascend or descend.

In summary, we will calculate the net forces acting on the drone and derive equations for both horizontal and vertical forces based on its orientation. The motors, positioned a distance R from the center of mass, create torque, which we will also compute based on the difference between the forces produced by the rotors. With these equations, we can model the drone's dynamics and predict its motion based on the forces applied.

The movement of the drone can be analyzed through Newton's laws, where force equals mass times acceleration. By integrating acceleration over time, we can derive the drone's velocity and position in both the horizontal and vertical dimensions. Additionally, we will account for angular motion, incorporating angular acceleration and angular velocity into our model.

This foundational understanding allows us to construct a Julia function that encapsulates these equations of motion. The function will take into account the state of the drone, including its position, velocities, angle, and angular velocities, as well as the forces acting on the rotors and environmental factors. This function will compute the new state of the drone based on the specified actions and initial conditions.

Having established the function that models the drone's dynamics, we will proceed to construct a generative model that encapsulates the relationships between various components. This model will represent the state of the drone over time, incorporating uncertainties and noise into the system. We will use RX Infer to implement this model efficiently, allowing us to perform inference and compute marginal distributions over actions and states.

Through message passing, we will efficiently solve the marginalization problem, enabling us to identify the forces required for the drone to transition from one position to another. We will also explore benchmarking results demonstrating the efficiency of RX Infer compared to traditional methods.

In conclusion, we invite collaboration and feedback from the community as we continue to develop and refine RX Infer. If you are interested in contributing or have questions, please do not hesitate to reach out. Thank you for your attention, and we look forward to engaging with you during the Q&A session.

**List of Changes Made:**

1. Replaced informal greetings with a formal introduction.
2. Clarified the roles and contributions of participants.
3. Improved coherence by organizing the content into clear sections.
4. Removed redundant phrases and ensured concise expression.
5. Enhanced clarity by using precise terminology and avoiding casual language.
6. Corrected grammatical errors and improved sentence structure.
7. Maintained a formal tone throughout the text.
8. Streamlined explanations of technical concepts for better understanding.
9. Reorganized the flow of ideas to enhance logical progression.
10. Removed unnecessary filler words and phrases for a more professional presentation.
