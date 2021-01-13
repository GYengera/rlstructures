
Overview of rlstructures
========================

TL;DR
-----
`rlstructures` is a lightweight Python library that provides simple APIs as well as data structures that make as little assumptions as possible on the structure of your agent or your task while allowing for transparently executing multiple policies on multiple environments in parallel (incl. multiple GPUs).

Why/What?
---------
RL research addresses multiple aspects of RL like hierarchical policies, option-based policies, goal-oriented policies, structured input/output spaces, transformers-based policies, ... and there are currently only few tools to handle this diversity of research projects.

We propose `rlstructures` as a way to:

* Simulate multiple policies, multiple models and multiple environments simultaneously at scale

* Define complex loss functions

* Quickly implement various policies architectures.

The main RLStructures principle is that the users delegate to the library the sampling of trajectories and episodes such that they will spend most of their time on the interesting part of RL research: developing new models and algorithms.

`rlstructures` is easy to use: it has very few simple interfaces that can be learned in one hour by reading the tutorials. It comes with multiple RL algorithms as examples including A2C, PPO, DDQN and SAC. Besides, there are 5 projects already using it (Multitask RL, Exploration, Diversity in RL, Optimization, ...) and helping each other.
Please reach out to us if you intend to use it. We will be happy to help, and potentially to implement missing functionalities.

Install rlstructures
--------------------

There is currently no `PIP` way to install rlstructures. The best is to:
* clone the repository
* then use `PYTHONPATH=rlstructures` when executing your code

Learning to use rlstructures
----------------------------

Learning `rlstructures` can be made in a very few hours (from the feedback from multiple users). It involves the following steps (see the `getting started` Section)


* Learning about **DictTensor** and **TemporalDictTensor** that are the two data structures used everywhere in RLStructures **(15 minutes)**
* Learning about mapping a Gym Environment to a **RLStructure Environment** **(5 minutes)**
* Learning about the **Agent API** allowing one to implement any agent, including recurrent agents **(30 minutes)**. Note that an agent may be parameterized such that one implementation may correspond to different agents :math:`\pi_z`.
* Learning about creating and using **multi-processes batchers** (i.e Batcher and EpisodeBatcher) **(15 minutes)**  -- see [Episode Batcher Tutorial](doc/MultiProcessEpisodeBatcher.md) and [Trajectory Batcher Tutorial](doc/MultiProcessTrajectoryBatcher.md). These batchers are the core objects that will allow you to work at scale.

Now, you can execute a complex policy over an environment in a multi-thread way, and get a simple data structure as an output on which you can compute any complex loss and gradients.

Step-by-Step implementation of classical algorithms
--------------------------------------------------

We also propose a step-by-step tutorial to implement both REINFORCE, and A2C with a simple and a recurrent policy (see `tutorial` section). Following this tutorial will help you to understand the basis of `rlstructures`

Now, you are ready to implement your own algorithms!!

Provided algorithms (as examples)
---------------------------------

We provide multiple implementations of RL algorithms in the `rlaglos` package as illustrative examples. Note that these algorithms have been benchmarked on simple environments only.

* A2C for discrete action space (using recurrent or not recurrent architectures) with GAE (i.e including REINFORCE)

* PPO for discrete action space (using recurrent or not recurrent architectures)

* Dueling DQN for discrete action space (using not recurrent architectures)

* SAC for continuous action space (using not recurrent architectures)

Discussion Group
----------------

* Discussion Group: https://www.facebook.com/groups/834804787067021

Contributing
------------

Contributions to `rlstructures` are greatly appreciated! Particularly:
1) new algorithms
2) execution of batchers over remote computers
3) API simplification
4) .......

Citing
------

.. code-block:: bibtex

    @misc{rlstructures,
        author = {L. Denoyer, D. Rothermel and X. Martinet},
        title = {{RLStructures - A simple library for RL research}},
        year = {2021},
        publisher = {GitHub},
        journal = {GitHub repository},
        howpublished = {\url{https://GitHub.com/FacebookResearch/rlstructures}},
    }

License
-------

:code:`RLStructures` is released under the MIT license. See `LICENSE <https://github.com/facebookresearch/rlstructures/blob/master/LICENSE>`_ for additional details about it, as well as our `Terms of Use <https://opensource.facebook.com/legal/terms>`_ and `Privacy Policy <https://opensource.facebook.com/legal/privacy>`_.
