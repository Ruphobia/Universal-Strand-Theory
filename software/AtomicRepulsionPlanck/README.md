# Universal Strand Theory - Current Model Overview
This project is part of a broader effort to reframe how we think about the fundamental nature of space, matter, and interaction. The theory presented here treats space not as emptiness, but as a physical medium with structure and tension. That structure may be composed of infinitely small strands (or potentially bubbles), and those strands are constantly expanding. This expansion is not just background behavior - it's the engine behind gravity, atomic repulsion, and perhaps even inertia.

## What This Model Does
At its core, this code explores the correlation between repulsion force (as calculated by a modified Lennard-Jones model) and a derived metric: (atomic radius * density) / Planck length

The idea is that space applies outward pressure. Wherever these expanding strands are blocked by matter - at the atomic boundary - they exert a repulsive force. If the strands are allowed to pass through a material (i.e. not blocked), no force is exerted. Thus, the interaction between space and matter becomes a function of how much is blocked - and this depends on both the size and density of the atomic structure.

## About Permeability
This is where permeability comes in. This is not permeability in the classical fluid dynamics or electromagnetics sense - it's a new physical idea. In this model, permeability is how much of the spatial strand medium can pass through a given atomic structure without interacting.

High permeability means space mostly flows through - low repulsion force. Low permeability means space is blocked - high repulsion force.

I currently estimate this permeability value indirectly, by looking at the error in repulsion force prediction using the radius * density / Planck length metric. The residual error - how far off a material is from the predicted force - becomes a proxy for how much the material interacts with the space medium.

This isn't ideal. What I really want is a forward model of permeability:

- Can it be predicted from atomic structure?
- Is it a function of crystal geometry, orbital shells, ionization, or atomic packing?
- Why do materials like diamond have high permeability, and heavy metals like lead and uranium show lower permeability?

## Where This Is Going
Right now, this model shows very strong correlation between the strand interaction metric and observed repulsion forces - well over 95% before introducing permeability.

After accounting for permeability (even crudely), the model can be tuned to hit R = 1.000, meaning perfect correlation across all tested materials. But I'm not satisfied with perfect correlation unless it means something. I want to find the actual underlying property that permeability represents - to describe it physically, not just mathematically.

This code is one part of that journey. I'm hoping others jump in, contribute, challenge, and build on it. Maybe someone with more experience in materials science, condensed matter, or quantum chemistry will see the pattern I'm still trying to surface.

## If You're Reading This
This isn't a final product. This is an experiment - maybe even a new direction in physics. But it's written like an engineer thinks: build what makes sense, then test it. When it stops making sense, rebuild.

If this resonates, clone the repo, start playing, and send a pull request or issue. This isn't about proving a pet theory. It's about finding something true - and maybe simpler - than the stories we've been telling ourselves.

Let's see how deep this goes.