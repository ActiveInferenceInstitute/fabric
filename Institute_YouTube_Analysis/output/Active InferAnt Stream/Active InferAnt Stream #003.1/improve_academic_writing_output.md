**Refined Text:**

Welcome to Active Infant Stream number 3.1 on systems. It is August 31st, 2024. As usual, I will begin by fetching the origin, committing numerous updates, and pushing them. While this process is ongoing, we will discuss systems within systems and explore various developments in the codebase related to William Blake, the Freedom of Information Act, cognitive sovereignty, and the PMDP social learning framework. 

We will start by making an initial GitHub push. I will copy everything below so we can delete it from here. The GitHub push appears to be complete; let us reload the repository to confirm its status. We can see that the pushes have been successfully recorded, so we have verified everything thrice.

The purpose of this stream, or at least one of them, is to explore various perspectives on the implementation of and interaction with systems. Let us begin by reviewing several code-based developments that I have prepared for this session. Please feel free to write any questions, comments, or ideas in the live chat at any time. I will cover three sections, followed by a fourth section, and I will conclude at that point. Along the way, please do not hesitate to raise any issues or queries you may have.

We are currently in the "zero context system systems" folder, starting with the William Blake folder. Here, we will examine some code methods related to Blake's mentions of systems, discussing their relevance for modern systems design and their applications in the codebase. Within the William Blake folder, there are multiple scripts and folders. The "William Blake resources" folder contains files such as additional references, a bibliography with hundreds of relevant citations, and Blake's works organized by year. Additionally, there is the "Edman edited complete works of Blake and letters," which consists of 29,000 lines, and the PS which contains 88,200 lines. As a reminder, all code bases are indexed, regardless of type, so there is no need to resync here. However, let us double-check; I am using Cursor version 4.3.

The poems are valuable, and we will begin with the Blake mentions. I will right-click to open the integrated terminal and execute the command "Python 3 Blake mentions.py." This script will search for the target terms at the top of the document, focusing on the term "system." To illustrate its generality, it will also include mentions of "Oris" and "Los." Logging is done, and for each of the target terms mentioned, three lines before and three lines after are compiled into a snippet, which is saved into an output file.

Across this document, there are mentions of "system" in Blake's works. Here are nine instances: "from this poll till a system was formed," "I must create a system or be enslaved by another man," "striving with systems to deliver individuals from those systems," "fixing their systems permanent by mathematic power to govern the evil by good," "abolish systems," and "here begins the system of moral virtue named Rahab." 

There are additional mentions involving these characters, but the same principle applies; these documents are much longer with snippets often reminiscent of reading through Blake, as numerous entities and concepts are referenced. The two entity extraction methods utilize a simpler approach, searching for capitalized words—either single or paired—using a regex pattern that identifies capitalized words at the beginning of a line or elsewhere. The entity extraction with SpaCy employs this package for slightly more advanced entity recognition.

These methods ultimately output into the analysis section, generating plots, including a top ten entities histogram and an entity frequency histogram that counts the number of mentions for each entity. This serves as a preliminary exploration of the entities involved and their interactions with the system.

Now, let us transition to the social sciences and active inference. This concept originates from Andrew Pasa's notable work presented at the IC2S2 conference, where he conducted a workshop on an active agents and active inference approach to agent-based modeling in the social sciences. His work is presented in a Google Colab notebook, which is accessible and allows users to run active inference multi-agent network learning simulations directly in their browsers. Although Google Colab is beneficial for one-click execution, it can become unwieldy due to the linear nature of documents that can expand indefinitely, making it difficult to track what has been executed.

Approximately 27 days ago, I contributed by transferring his Colab notebook into a single Python script, condensing approximately 1,500 lines of code for easier execution. In the following days, I engaged in fruitful discussions with Andrew on Discord, breaking down the script into various components. The main.py serves as the primary script that encompasses all simulation aspects, while utilities are divided into categories such as math, data analysis, agent creation, active inference processes, and visualizations. 

This approach facilitates collaboration with Andrew's multi-agent communication network simulation. Agents operate within sub-networks, and the output folder contains methods for visualizing the matrices of different agents. For instance, one matrix maps observations to hidden states. If perfect sensory recognition occurred, we would observe only ones on the diagonals and zeros elsewhere. This aligns with treating a partially observable Markov process as a fully observable one. 

The active inference loop is integral to this simulation, and I will detail its components, methods, and the application of active inference principles. The agent is initialized with matrices representing its beliefs about the world. The agent runs inference loops that update its beliefs and actions based on observations and internal models. Furthermore, the agent adapts its internal models using learning parameters and observations, culminating in simulation and visualization.

To summarize, this stream aims to provide insight into the active inference principles applied within the social sciences, highlighting both theoretical foundations and practical implementations.

**List of Changes Made:**

1. Corrected grammatical errors and punctuation.
2. Improved clarity and coherence by restructuring sentences.
3. Eliminated redundant phrases and trivial statements.
4. Used formal and precise language throughout the text.
5. Enhanced the organization of ideas for better flow and understanding.
6. Condensed lengthy explanations for brevity without losing meaning.
7. Replaced informal language with academic terminology where appropriate.
8. Clarified technical terms and processes for easier comprehension.
9. Removed colloquial expressions to maintain a formal tone.
10. Ensured that all sections are logically connected and contribute to the overall narrative.
