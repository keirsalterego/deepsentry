# DeepSentry

DeepSentry is an open-source research project for unsupervised anomaly detection in distributed system logs. It learns a baseline of normal behavior from raw log text, compresses the message stream with an autoencoder, and then scores deviations with a recurrent model.

This workspace currently captures the full experimental pipeline from the paper _Anomaly Detection from Log Files Using Unsupervised Deep Learning_ and repackages it with shorter filenames, safer config loading, and clearer docs for open-source use.

## What This Project Does

DeepSentry is built around a three-stage workflow:

1. Parse raw logs into tokenized text and train a text autoencoder.
2. Encode the full dataset into latent vectors.
3. Train and evaluate a recurrent anomaly detector on the encoded sequence.

The project also includes a labeled evaluation path and a live monitoring loop for streaming log input.

## Current Status

Implemented:

- Raw log parsing and preprocessing
- Text autoencoder training
- Dataset encoding with a trained text model
- Time-series anomaly detector training
- Batch evaluation and labeled scoring
- Live monitoring pipeline
- Dockerized execution paths

Still left to implement for a polished release:

- Automated tests for parsing, encoding, training, and evaluation
- A modern CLI interface instead of shell-only entry points
- Better validation for input files and config values
- CI checks for formatting, linting, and basic smoke tests
- Experiment tracking and model version metadata
- Expanded dataset support beyond the current HDFS-focused flow
- A packaging story for installable local development

## Open Source Notes

This repository uses the MIT License. Two third-party components are vendored in-tree and should remain under their respective licenses:

- [keras_anomaly_detection](https://github.com/chen0040/keras-anomaly-detection)
- [text_autoencoder](https://github.com/erickrf/autoencoder)

If you contribute changes, keep the codebase license-friendly, preserve attribution, and avoid adding unrelated proprietary content.

## Requirements

- Python 3.6 or newer for development
- Docker for the easiest project runtime
- A CUDA-enabled GPU if you want to train on larger datasets

The pinned dependencies are listed in [requirements.txt](requirements.txt).

## Manual

Read the full documentation book at [docs/book.html](docs/book.html). It walks from setup to pipeline, model structure, configuration, live monitoring, and troubleshooting.

## Quick Start

Build the image:

```bash
./build.sh .
```

Run a pipeline stage from [dockerrun/](dockerrun):

```bash
sh dockerrun/run_prepare.sh /path/to/data /root/data
```

The container expects the data folder to contain a `dockerconfig/` directory with the YAML configuration files used by [src/config_loader.py](src/config_loader.py).

## Workflow

The main stage order is:

1. Prepare text data with [dockerrun/run_prepare.sh](dockerrun/run_prepare.sh)
2. Train the text model with [dockerrun/run_text.sh](dockerrun/run_text.sh)
3. Encode the dataset with [dockerrun/run_encode.sh](dockerrun/run_encode.sh)
4. Train the anomaly model with [dockerrun/run_anomaly_train.sh](dockerrun/run_anomaly_train.sh)
5. Evaluate raw scores with [dockerrun/run_anomaly_eval.sh](dockerrun/run_anomaly_eval.sh)
6. Run the labeled analysis with [dockerrun/run_anomaly_eval_labeled.sh](dockerrun/run_anomaly_eval_labeled.sh)
7. Launch live monitoring with [dockerrun/run_live.sh](dockerrun/run_live.sh)

## Project Layout

The short filenames in this workspace are:

- [build.sh](build.sh)
- [dockerrun/run_prepare.sh](dockerrun/run_prepare.sh)
- [dockerrun/run_text.sh](dockerrun/run_text.sh)
- [dockerrun/run_encode.sh](dockerrun/run_encode.sh)
- [dockerrun/run_anomaly_train.sh](dockerrun/run_anomaly_train.sh)
- [dockerrun/run_anomaly_eval.sh](dockerrun/run_anomaly_eval.sh)
- [dockerrun/run_anomaly_eval_labeled.sh](dockerrun/run_anomaly_eval_labeled.sh)
- [dockerrun/run_live.sh](dockerrun/run_live.sh)
- [sc/subset.py](sc/subset.py)
- [ut/logging_setup.py](ut/logging_setup.py)
- [t/test_smoke.py](t/test_smoke.py)
- [src/tx/prepare.py](src/tx/prepare.py)
- [src/tx/train.py](src/tx/train.py)
- [src/tx/encode.py](src/tx/encode.py)
- [src/an/train.py](src/an/train.py)
- [src/an/eval.py](src/an/eval.py)
- [src/an/analysis.py](src/an/analysis.py)
- [src/live/main.py](src/live/main.py)

## Book View

A book-style HTML version of the docs is available at [docs/book.html](docs/book.html).

## Citation

If you use this project in academic work, cite the original paper:

```bibtex
@inproceedings{bursic2019anomaly,
   title={Anomaly detection from log files using unsupervised deep learning},
   author={Bursic, Sathya and Cuculo, Vittorio and D’Amelio, Alessandro},
   booktitle={International symposium on formal methods},
   pages={200--207},
   year={2019},
   organization={Springer}
}
```
