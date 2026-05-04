# DeepSentry

> *"Your logs are lying to you. We're here to catch them in the act."*

![Build Status](https://img.shields.io/badge/build-probably_fine-brightgreen?style=flat-square)
![Tests](https://img.shields.io/badge/tests-aspirational-yellow?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.6%2B-blue?style=flat-square&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-containerized-2496ED?style=flat-square&logo=docker&logoColor=white)
![GPU](https://img.shields.io/badge/GPU-strongly_encouraged-76B900?style=flat-square&logo=nvidia&logoColor=white)
![Anomalies Found](https://img.shields.io/badge/anomalies_found-yes-red?style=flat-square)
![Sleep Lost](https://img.shields.io/badge/engineer_sleep_lost-considerable-8A2BE2?style=flat-square)
![Vibes](https://img.shields.io/badge/vibes-unsupervised-ff69b4?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome_(please)-orange?style=flat-square)

---

DeepSentry is an open-source, unsupervised anomaly detection system for distributed system logs.
It watches your logs so you don't have to. It doesn't sleep. It doesn't blink. It just *stares*.

It learns what "normal" looks like, compresses your log stream through an autoencoder
(fancy talk for "makes logs go small"), then flags anything suspicious with a recurrent
model that has read more log files than any human should ever have to.

It is, in essence, a very paranoid intern that never takes a lunch break.

---

## Why Does This Exist?

Because at 3 AM, when your distributed system starts doing something *weird*, you don't want
to be the one scrolling through 4 million lines of:

```
INFO  [2024-01-15 03:14:07] Block blk_-1608999687919862906 NameSystem.addStoredBlock: blockMap updated
INFO  [2024-01-15 03:14:07] Block blk_-1608999687919862906 NameSystem.addStoredBlock: blockMap updated
INFO  [2024-01-15 03:14:07] Block blk_-1608999687919862906 NameSystem.addStoredBlock: blockMap updated
```
*(x3,000,000)*

DeepSentry reads all of that. DeepSentry processes all of that. DeepSentry does not develop
existential dread about all of that. It is a machine. It is stronger than you.

---

## How It Works

DeepSentry operates in three stages, like a heist movie but with more matrix math:

```
+-----------------------------------------------------------------------+
|                                                                       |
|  STAGE 1 -- THE SETUP                                                 |
|  "Read all the logs. All of them."                                    |
|  Parse raw logs --> tokenize --> train text autoencoder               |
|                                       |                               |
|                                       v                               |
|  STAGE 2 -- THE SQUEEZE                                               |
|  "Make big logs into small math."                                     |
|  Encode entire dataset into latent vectors                            |
|                                       |                               |
|                                       v                               |
|  STAGE 3 -- THE CATCH                                                 |
|  "Wait... that doesn't look right."                                   |
|  Train recurrent anomaly detector --> score deviations                |
|                                                                       |
+-----------------------------------------------------------------------+
```

It's fully unsupervised, meaning nobody told it what "bad" looks like. It figured
that out on its own. Like a dog who's never seen a squirrel but *knows* something
is wrong the moment one appears.

---

## What's Implemented

```
[x]  Raw log parsing and preprocessing    (the suffering)
[x]  Text autoencoder training            (the enlightenment)
[x]  Dataset encoding                     (the compression)
[x]  Anomaly detector training            (the paranoia)
[x]  Batch evaluation and labeled scoring (the judgment)
[x]  Live monitoring pipeline             (the vigil)
[x]  Dockerized execution paths           (the containerized suffering)
```

---

## What's Not Implemented Yet

```
[ ]  Automated tests       -- we believe in the code. The code believes in itself.
[ ]  A real CLI            -- currently shell-only. Very artisanal. Very 2003.
[ ]  Input validation      -- garbage in, garbage detected. Surprisingly functional.
[ ]  CI/CD                 -- the pipeline runs on discipline and good intentions.
[ ]  Experiment tracking   -- model versions live in final_v3_REAL_actual_final2/.
[ ]  More dataset support  -- currently HDFS-flavored. Others may not survive contact.
[ ]  Proper packaging      -- `pip install deepsentry` is a dream we dare to dream.
```

---

## Requirements

```
+----------------+--------------------------------------------------------+
| Requirement    | Notes                                                  |
+----------------+--------------------------------------------------------+
| Python 3.6+    | Because we have some standards                         |
| Docker         | Easiest path to running this without breaking things   |
| CUDA GPU       | Optional, but CPU training is a journey of self-growth |
| Patience       | Unlisted in requirements.txt. Still required.          |
| Coffee         | See: Patience                                          |
+----------------+--------------------------------------------------------+
```

Full pinned dependencies are in [`requirements.txt`](requirements.txt).
They are pinned because software ecosystems are chaos and we have accepted this.

---

## Quick Start

Build the image:

```bash
./build.sh .
```

Point it at your data directory. It must contain a `dockerconfig/` folder with YAML configs.
Yes, config files live inside your data folder. It's a lifestyle choice.

```bash
sh dockerrun/run_prepare.sh /path/to/your/data /root/data
```

Then follow the pipeline stages below until anomalies are detected or your GPU bill arrives,
whichever comes first.

---

## The Full Pipeline

Run these in order. Skipping steps is how anomalies become incidents.

```bash
# 1. Parse and prepare your log data
sh dockerrun/run_prepare.sh /data /root/data

# 2. Train the text autoencoder  (go make coffee, this takes a while)
sh dockerrun/run_text.sh /data /root/data

# 3. Encode the full dataset into latent vectors
sh dockerrun/run_encode.sh /data /root/data

# 4. Train the anomaly detection model  (more coffee)
sh dockerrun/run_anomaly_train.sh /data /root/data

# 5. Evaluate -- get your raw anomaly scores
sh dockerrun/run_anomaly_eval.sh /data /root/data

# 6. Run labeled analysis -- see how well it actually did
sh dockerrun/run_anomaly_eval_labeled.sh /data /root/data

# 7. Go live -- the sentry never sleeps
sh dockerrun/run_live.sh /data /root/data
```

Step 7 is the one where you nervously watch a terminal and wonder if that alert is real
or if you just have a bad `threshold` config value.

---

## Project Layout

```
deepsentry/
|
+-- build.sh                            the beginning of everything
|
+-- dockerrun/
|   +-- run_prepare.sh                  step 1
|   +-- run_text.sh                     step 2  (patience)
|   +-- run_encode.sh                   step 3
|   +-- run_anomaly_train.sh            step 4  (more patience)
|   +-- run_anomaly_eval.sh             step 5
|   +-- run_anomaly_eval_labeled.sh     step 6
|   +-- run_live.sh                     step 7  (the vigil begins)
|
+-- src/
|   +-- tx/
|   |   +-- prepare.py                  log whisperer
|   |   +-- train.py                    neural net chef
|   |   +-- encode.py                   mathematical compressor
|   |
|   +-- an/
|   |   +-- train.py                    anomaly bloodhound trainer
|   |   +-- eval.py                     the reckoning
|   |   +-- analysis.py                 post-mortem analyst
|   |
|   +-- live/
|       +-- main.py                     the eyes that never close
|
+-- sc/
|   +-- subset.py                       for when you want a smaller nightmare
|
+-- ut/
|   +-- logging_setup.py                logs about logs (very meta)
|
+-- t/
|   +-- test_smoke.py                   one (1) test. it's a start.
|
+-- docs/
    +-- book.html                       the full lore
```

---

## Documentation

The full documentation book is at [`docs/book.html`](docs/book.html). It covers setup,
pipeline stages, model architecture, configuration, live monitoring, and troubleshooting.

It was written by people who had read too many log files. It shows, but in a good way.

---

## License and Third-Party Credits

DeepSentry is MIT licensed. Two third-party libraries are vendored in-tree and retain
their own licenses:

- [keras_anomaly_detection](https://github.com/chen0040/keras-anomaly-detection)
  -- without which we'd have to write the hard part ourselves

- [text_autoencoder](https://github.com/erickrf/autoencoder)
  -- without which the logs would remain un-squished

Keep contributions license-friendly, preserve attribution, and don't drop proprietary
code in here. We're watching. That's kind of the whole thing.

---

## Contributing

PRs are welcome. Issues are welcome. Questions are welcome. At minimum:

1. Keep it license-friendly
2. Preserve attribution for vendored code
3. Don't break the one existing test

If you want to add actual tests, you will be celebrated. Statues may be commissioned.

---

## Citation

If DeepSentry catches a production anomaly that saves your job, consider citing
the original paper:

```bibtex
@inproceedings{bursic2019anomaly,
   title={Anomaly detection from log files using unsupervised deep learning},
   author={Bursic, Sathya and Cuculo, Vittorio and D'Amelio, Alessandro},
   booktitle={International symposium on formal methods},
   pages={200--207},
   year={2019},
   organization={Springer}
}
```

Or at minimum, send them a thank-you email. They read a lot of logs so you wouldn't have to.

---

*Built for engineers who've stared at enough log files to start seeing patterns in the void.*
*The void, it turns out, had anomalies.*