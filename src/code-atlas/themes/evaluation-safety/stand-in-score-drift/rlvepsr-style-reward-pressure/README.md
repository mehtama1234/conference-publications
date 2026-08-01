# RLVepsR Style Reward Pressure

Theme: Evaluation / Safety
Subtheme: Stand-in score drift
Paper family: RLVepsR style reward pressure

What it proves: a score can start as a helpful measuring stick and later become a loophole once the model learns to chase the number.

User knob: training pressure, score loophole size, real-target audit strength.

Failure exposed: the score rises while the real target gets worse.

Evidence: checks after training must show that the score still moves with the real target.

Run: open `../../../../index.html`.
