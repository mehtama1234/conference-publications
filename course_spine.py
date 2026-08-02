COURSE_TITLE = "Machine Learning Conferences From First Principles"
COURSE_SUBTITLE = "A plain-language course spine for the local ICML 2026 and ICLR 2026 publication map."

INTRO = [
    "Machine learning starts from one simple wish: use examples, feedback, or structure to make better future decisions.",
    "A paper may look like it is about a model, a proof, a dataset, a benchmark, or a system trick. Underneath, it is usually trying to control what information survives as the system learns, reasons, predicts, samples, adapts, or acts.",
    "This page is a long plain-language spine for the conference map. It avoids shorthand where possible, defines necessary words in everyday terms, and explains why the topics matter in topology, robotics, search, hardware, medicine, science, and software.",
]

SECTIONS = [
    {
        "kicker": "Start",
        "title": "The Whole Field Is About Learning A Useful Rule",
        "summary": "A model is a rule that turns inputs into outputs; learning is how that rule is shaped by evidence.",
        "body": [
            "A machine learning system receives examples, measurements, comparisons, rewards, or human feedback. It changes an internal rule so future outputs are more useful.",
            "The rule may classify an image, generate a molecule, choose a tool, rank a search result, guide a robot, summarize a document, or estimate risk. The surface differs, but the core question stays close: what should change inside the system, and what should stay stable?",
            "ICML and ICLR papers often disagree about details, but they share this deeper concern. They ask how to make learning controllable, measurable, efficient, safe, and useful outside the narrow training case.",
        ],
        "applications": ["Search uses learned rules to rank documents and answers.", "Robotics uses learned rules to connect perception to action.", "Medicine uses learned rules to support diagnosis, discovery, and workflow without replacing evidence."],
    },
    {
        "kicker": "Data",
        "title": "Data Is Not Just Fuel",
        "summary": "Data decides what the system can see, what it misses, and which mistakes it repeats.",
        "body": [
            "It is tempting to say more data is always better. That is too simple. Examples can be noisy, biased, stale, duplicated, private, illegal to use, or irrelevant to the deployment setting.",
            "A useful dataset has coverage. It shows the system enough of the cases it will face. It also has boundaries. Some data must be deleted, hidden, weighted less, or kept out because it is unsafe or not allowed.",
            "Many conference papers are really about data control: which examples matter, which order they arrive in, how synthetic data helps or hurts, and how to know whether training material matches the real job.",
        ],
        "applications": ["Clinical ML needs data that reflects patients and measurement conditions, not only clean lab cases.", "Enterprise agents need source permissions and freshness attached to every retrieved fact.", "Low-resource language work needs ways to share evidence without erasing local language differences."],
    },
    {
        "kicker": "Topology",
        "title": "Topology Means The Shape Of Possible Change",
        "summary": "In machine learning, topology is about connected regions, paths, holes, clusters, neighborhoods, and boundaries in data or behavior.",
        "body": [
            "In everyday words, topology asks what is connected to what. Can the model move from one behavior to another through small safe steps? Are two examples close in a meaningful way? Does a data cloud split into separate groups? Is there a hole, loop, or boundary the model should respect?",
            "This matters because learning is movement. Training moves parameters. Adaptation moves behavior. Generation moves from noise to a sample. Planning moves from one state to another. If the path crosses a bad region, the result can fail even if the start and end look reasonable.",
            "Topology appears in representation spaces, graphs, manifolds, clusters, connected components, transport paths, adversarial regions, and physical state spaces. It tells us what kinds of movement are possible without tearing the structure apart.",
            "A topology failure is often easy to describe after the fact: the model treated two separate cases as connected, crossed a safety boundary, averaged two valid answers into one invalid answer, or could not find a path through the allowed region.",
        ],
        "applications": ["Graph learning uses topology to preserve which nodes, documents, proteins, or users are connected.", "Robotics uses topology to know which states are reachable without collision.", "Generative models use topology when moving from noise to valid images, molecules, videos, or actions.", "Security uses topology to find nearby changes that cause wrong behavior."],
    },
    {
        "kicker": "Loss",
        "title": "A Loss Is A Number That Says What Is Wrong",
        "summary": "Training usually follows the direction that makes this number smaller.",
        "body": [
            "A loss function turns a mistake into a number. If the prediction is wrong, the number is high. If the answer is close, the number is lower. Training changes the model to reduce that number.",
            "The hard part is that the loss is only a stand-in for the real goal. A model can reduce a loss while still failing people. It can pass a benchmark by using a shortcut, please a judge while hiding bad reasoning, or optimize a reward that misses the true task.",
            "Much of modern machine learning is therefore about better rulers: losses, rewards, verifiers, constraints, and tests that measure the thing we actually care about.",
        ],
        "applications": ["Preference learning depends on whether the reward matches what people truly want.", "Safety evaluation depends on whether the test visits dangerous cases.", "Scientific modeling depends on whether the score reflects real evidence, not only curve fit."],
    },
    {
        "kicker": "Reasoning",
        "title": "Reasoning Is Work Done Between Question And Answer",
        "summary": "A system may search, decompose, call tools, check, revise, and spend extra compute before answering.",
        "body": [
            "Older evaluation often treated a model answer as immediate. Newer work studies what happens during the run: does the system plan, ask a useful question, call the right tool, test its own result, and recover from a bad step?",
            "This matters because some tasks cannot be solved by a single guess. Code editing, math, science, document work, UI navigation, and multi-step planning need intermediate state.",
            "The conference map shows reasoning becoming an operating problem. The system must decide how much time to spend, what evidence to inspect, which verifier to trust, and when to stop.",
        ],
        "applications": ["Coding agents need repository context, tests, and reviewable edits.", "Scientific agents need source trails and hypothesis checks.", "Document agents need efficient search paths through long collections."],
    },
    {
        "kicker": "Generation",
        "title": "Generation Means Making A Valid Object, Not Just A Plausible Surface",
        "summary": "A generated output must obey the structure of its domain.",
        "body": [
            "A generated sentence must mean something. A generated image must match the prompt. A generated molecule must be chemically possible. A generated robot action must be safe. A generated proof must actually prove.",
            "The deeper problem is validity. The system has to make something that belongs to the allowed world, not merely something that looks similar to training data.",
            "Diffusion, flow, autoregressive, and latent models are different ways to move through a space of possible objects. The same first-principles question applies to all of them: does the path preserve the rules that make the object valid?",
        ],
        "applications": ["Drug discovery needs molecules that can exist, be synthesized, and satisfy safety constraints.", "Video generation needs time consistency, not only sharp single frames.", "Speech generation needs identity, timing, tone, and privacy boundaries."],
    },
    {
        "kicker": "Evaluation",
        "title": "Evaluation Is A Measurement Instrument",
        "summary": "A benchmark is a measuring tool, and every measuring tool has limits.",
        "body": [
            "A score is not the truth. It is a reading. The reading can be noisy, narrow, gamed, stale, or disconnected from real use.",
            "Good evaluation asks what hidden ability the test is trying to measure, what evidence would prove that ability, and which shortcuts could fake it. This is why process traces, rare-case tests, human-calibrated checks, and executable tasks matter.",
            "Evaluation becomes especially hard for agents because the output is not only text. The system may change files, call tools, browse websites, update records, or control machines.",
        ],
        "applications": ["Agent benchmarks need to measure recovery and effort, not only final answers.", "Medical benchmarks need patient-level evidence and failure analysis.", "Safety benchmarks need rare dangerous cases, not only average behavior."],
    },
    {
        "kicker": "Systems",
        "title": "Efficiency Decides What Can Be Used",
        "summary": "A method that is too slow, costly, or memory-hungry may be unusable even if it works on paper.",
        "body": [
            "Machine learning runs on real hardware with time, memory, energy, and money limits. Those limits shape the method.",
            "Compression, quantization, pruning, routing, caching, and smaller updates are not only engineering cleanup. They decide whether a model can run on a phone, serve many users, train under a budget, or adapt without retraining everything.",
            "This connects ICML and ICLR to hardware conferences. The model idea and the machine that runs it cannot be fully separated.",
        ],
        "applications": ["On-device AI needs small, fast models that protect privacy and battery life.", "Large-scale serving needs routing and caching to avoid wasting compute.", "Federated learning needs methods that survive different client devices and network limits."],
    },
    {
        "kicker": "Safety",
        "title": "Safety Is About Boundaries",
        "summary": "A system needs limits on what it can know, say, change, remember, and optimize.",
        "body": [
            "Safety is broader than refusing harmful text. It includes privacy, unlearning, watermarking, distribution shift, adversarial examples, tool misuse, reward hacking, governance, and model behavior after deployment.",
            "The central question is boundary control. What data is allowed? Which actions are allowed? Which outputs need review? Which examples must be forgotten? Which regions of behavior should be impossible to enter?",
            "A safe system is not only a strong model. It is a model inside a set of rules, checks, evidence paths, and recovery procedures.",
        ],
        "applications": ["Enterprise systems need policy, identity, and audit boundaries.", "Public models need misuse resistance and provenance checks.", "Scientific and medical systems need human review before high-stakes action."],
    },
    {
        "kicker": "Fields",
        "title": "Why These Conferences Matter Outside Machine Learning",
        "summary": "The same ideas reappear wherever systems learn, reason, measure, and act.",
        "body": [
            "In search, machine learning decides what information should be retrieved and ranked. In speech, it decides how noisy sound becomes words and speaker meaning. In robotics, it decides how perception becomes motion. In hardware, it decides which model behaviors can run under real cost.",
            "Topology is one bridge across fields. Search has document graphs. Robotics has reachable spaces. Hardware has memory and network connections. Speech has connected time segments and speakers. Machine learning has representation spaces and movement paths.",
            "The importance of ICML and ICLR is that they expose the general problem behind all of these fields: how do we control learned systems so their behavior remains useful when scale, uncertainty, constraints, and real-world use are added?",
        ],
        "applications": ["Science gains tools for discovery, simulation, and causal reasoning.", "Healthcare gains decision support that must preserve evidence and boundaries.", "Software gains agents that must act through tests, tools, and review.", "Robotics gains learned perception and control that must respect physical topology."],
    },
]

READING_PATH = [
    ("index.html", "Theme map"),
    ("math-concepts.html", "Math atlas"),
    ("paper-atlas.html", "Publication concept atlas"),
    ("roadmap.html", "Atlas roadmap"),
    ("icml-vs-iclr-2026.html", "ICML vs ICLR"),
]
