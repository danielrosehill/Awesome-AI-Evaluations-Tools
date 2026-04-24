# Awesome AI Evaluations & Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github&logoColor=white)](https://github.com/danielrosehill/Awesome-AI-Evaluations-Tools)

A curated list of **open source tools, frameworks, and benchmarks for evaluating AI systems** — LLMs, RAG pipelines, agents, multimodal models, and AI applications.

## Scope

### In Scope
- Open source eval frameworks, harnesses, and platforms
- Benchmark suites and benchmark datasets
- RAG, retrieval, and search evaluation tools
- Agent and tool-use evaluation
- Vision and multimodal evaluation
- Eval-focused observability platforms

### Out Of Scope
- Closed-source / commercial-only platforms with no open core
- General ML observability without eval-specific features
- One-off paper code drops with no maintenance

## Discovery sources

GitHub topic pages used while curating this list:

- <https://github.com/topics/evals>
- <https://github.com/topics/evaluation>
- <https://github.com/topics/evaluation-framework>

---

## Contents

- [Platforms And Software](#platforms-and-software)
- [Benchmarks](#benchmarks)
- [Agentic & Tool Use Evals](#agentic--tool-use-evals)
- [Multimodal Evals](#multimodal-evals)
- [Vision Evals](#vision-evals)
- [RAG & Retrieval](#rag--retrieval)
- [Search](#search)
- [Awesome Lists / Resources](#awesome-lists--resources)
- [List Authorship](#list-authorship)

---

## Platforms And Software

| Project | Description | Stars |
|---|---|---|
| [DeepEval](https://github.com/confident-ai/deepeval) | The LLM evaluation framework. | ![](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) |
| [Phoenix](https://github.com/Arize-ai/phoenix) | AI observability and evaluation platform from Arize. | ![](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) |
| [Opik](https://github.com/comet-ml/opik) | Debug, evaluate, and monitor LLM apps, RAG systems, and agentic workflows with tracing and dashboards. | ![](https://img.shields.io/github/stars/comet-ml/opik?style=social) |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | UK AISI's framework for large language model evaluations. | ![](https://img.shields.io/github/stars/UKGovernmentBEIS/inspect_ai?style=social) |
| [LangWatch](https://github.com/langwatch/langwatch) | Platform for LLM evaluations and AI agent testing. | ![](https://img.shields.io/github/stars/langwatch/langwatch?style=social) |
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | EleutherAI framework for few-shot evaluation of language models. | ![](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=social) |
| [CSET](https://github.com/cisagov/cset) | CISA's Cybersecurity Evaluation Tool. | ![](https://img.shields.io/github/stars/cisagov/cset?style=social) |
| [Harbor](https://github.com/harbor-framework/harbor) | Framework for running agent evaluations and creating RL environments. | ![](https://img.shields.io/github/stars/harbor-framework/harbor?style=social) |
| [Evaluate](https://github.com/huggingface/evaluate) | Hugging Face library for easily evaluating ML models and datasets. | ![](https://img.shields.io/github/stars/huggingface/evaluate?style=social) |
| [OLMES](https://github.com/allenai/olmes) | Reproducible, flexible LLM evaluations from AI2. | ![](https://img.shields.io/github/stars/allenai/olmes?style=social) |
| [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | Open-source evaluation and testing library for LLM agents. | ![](https://img.shields.io/github/stars/Giskard-AI/giskard-oss?style=social) |
| [OpenAI Evals](https://github.com/openai/evals) | Framework for evaluating LLMs and LLM systems plus an open-source registry of benchmarks. | ![](https://img.shields.io/github/stars/openai/evals?style=social) |
| [TensorTrade](https://github.com/tensortrade-org/tensortrade) | RL framework for training, evaluating, and deploying robust trading agents. | ![](https://img.shields.io/github/stars/tensortrade-org/tensortrade?style=social) |
| [EverOS](https://github.com/EverMind-AI/EverOS) | Build, evaluate, and integrate long-term memory for self-evolving agents. | ![](https://img.shields.io/github/stars/EverMind-AI/EverOS?style=social) |
| [OpenEvals](https://github.com/langchain-ai/openevals) | Readymade evaluators for LLM apps from LangChain. | ![](https://img.shields.io/github/stars/langchain-ai/openevals?style=social) |
| [Evalite](https://github.com/mattpocock/evalite) | Evaluate your LLM-powered apps with TypeScript. | ![](https://img.shields.io/github/stars/mattpocock/evalite?style=social) |
| [LightEval](https://github.com/huggingface/lighteval) | Hugging Face's all-in-one toolkit for evaluating LLMs across multiple backends. | ![](https://img.shields.io/github/stars/huggingface/lighteval?style=social) |
| [EvalAI](https://github.com/Cloud-CV/EvalAI) | Platform for evaluating state-of-the-art AI on community challenges. | ![](https://img.shields.io/github/stars/Cloud-CV/EvalAI?style=social) |
| [PyKEEN](https://github.com/pykeen/pykeen) | Python library for learning and evaluating knowledge graph embeddings. | ![](https://img.shields.io/github/stars/pykeen/pykeen?style=social) |
| [RouteLLM](https://github.com/lm-sys/RouteLLM) | Framework for serving and evaluating LLM routers to save costs without compromising quality. | ![](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=social) |
| [Oumi](https://github.com/oumi-ai/oumi) | Easily fine-tune, evaluate, and deploy gpt-oss, Qwen3, DeepSeek-R1, or any open source LLM/VLM. | ![](https://img.shields.io/github/stars/oumi-ai/oumi?style=social) |
| [Ignite](https://github.com/pytorch/ignite) | High-level library to help train and evaluate neural networks in PyTorch flexibly and transparently. | ![](https://img.shields.io/github/stars/pytorch/ignite?style=social) |
| [Bench](https://github.com/arthur-ai/bench) | A tool for evaluating LLMs from Arthur AI. | ![](https://img.shields.io/github/stars/arthur-ai/bench?style=social) |
| [OpenLIT](https://github.com/openlit/openlit) | Open source AI engineering platform: OpenTelemetry-native observability, evaluations, prompt management, guardrails. | ![](https://img.shields.io/github/stars/openlit/openlit?style=social) |
| [GuideLLM](https://github.com/vllm-project/guidellm) | Evaluate and enhance LLM deployments for real-world inference needs. | ![](https://img.shields.io/github/stars/vllm-project/guidellm?style=social) |
| [Vivaria](https://github.com/METR/vivaria) | METR's tool for running evaluations and conducting agent elicitation research. | ![](https://img.shields.io/github/stars/METR/vivaria?style=social) |
| [Helicone](https://github.com/Helicone/helicone) | Open source LLM observability platform — monitor, evaluate, and experiment with one line of code. | ![](https://img.shields.io/github/stars/Helicone/helicone?style=social) |

## Benchmarks

| Project | Description | Stars |
|---|---|---|
| [Bloom](https://github.com/safety-research/bloom) | Evaluate any behavior immediately. | ![](https://img.shields.io/github/stars/safety-research/bloom?style=social) |
| [Dangerous Capability Evaluations](https://github.com/google-deepmind/dangerous-capability-evaluations) | Google DeepMind's evaluation suite for dangerous model capabilities. | ![](https://img.shields.io/github/stars/google-deepmind/dangerous-capability-evaluations?style=social) |
| [RewardBench](https://github.com/allenai/reward-bench) | The first evaluation tool for reward models. | ![](https://img.shields.io/github/stars/allenai/reward-bench?style=social) |
| [OpenBench](https://github.com/groq/openbench) | Provider-agnostic, open-source evaluation infrastructure for language models. | ![](https://img.shields.io/github/stars/groq/openbench?style=social) |
| [Claw-Eval](https://github.com/claw-eval/claw-eval) | Evaluation harness for evaluating LLMs as agents — all tasks human-verified. | ![](https://img.shields.io/github/stars/claw-eval/claw-eval?style=social) |

## Agentic & Tool Use Evals

| Project | Description | Stars |
|---|---|---|
| [Gorilla](https://github.com/ShishirPatil/gorilla) | Training and evaluating LLMs for function calls (tool calls). | ![](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=social) |
| [AgentBench](https://github.com/THUDM/AgentBench) | A comprehensive benchmark to evaluate LLMs as agents (ICLR'24). | ![](https://img.shields.io/github/stars/THUDM/AgentBench?style=social) |
| [fast-agent](https://github.com/evalstate/fast-agent) | Code, build, and evaluate agents with excellent model and Skills/MCP/ACP support. | ![](https://img.shields.io/github/stars/evalstate/fast-agent?style=social) |
| [AgentEvals](https://github.com/langchain-ai/agentevals) | Readymade evaluators for agent trajectories from LangChain. | ![](https://img.shields.io/github/stars/langchain-ai/agentevals?style=social) |
| [any-agent](https://github.com/mozilla-ai/any-agent) | Single interface to use and evaluate different agent frameworks. | ![](https://img.shields.io/github/stars/mozilla-ai/any-agent?style=social) |

## Multimodal Evals

| Project | Description | Stars |
|---|---|---|
| [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) | One-for-all multimodal evaluation toolkit across text, image, video, and audio tasks. | ![](https://img.shields.io/github/stars/EvolvingLMMs-Lab/lmms-eval?style=social) |
| [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | Open-source evaluation toolkit for large multi-modality models — supports 220+ LMMs and 80+ benchmarks. | ![](https://img.shields.io/github/stars/open-compass/VLMEvalKit?style=social) |

## Vision Evals

| Project | Description | Stars |
|---|---|---|
| [OmniDocBench](https://github.com/opendatalab/OmniDocBench) | A comprehensive benchmark for document parsing and evaluation (CVPR 2025). | ![](https://img.shields.io/github/stars/opendatalab/OmniDocBench?style=social) |

## RAG & Retrieval

| Project | Description | Stars |
|---|---|---|
| [Ragas](https://github.com/vibrantlabsai/ragas) | Supercharge your LLM application evaluations. | ![](https://img.shields.io/github/stars/vibrantlabsai/ragas?style=social) |
| [TruLens](https://github.com/truera/trulens) | Evaluation and tracking for LLM experiments and AI agents. | ![](https://img.shields.io/github/stars/truera/trulens?style=social) |

## Search

_(Add entries here.)_

## Awesome Lists / Resources

| Project | Description | Stars |
|---|---|---|
| [Every Eval Ever](https://github.com/evaleval/every_eval_ever) | Shared schema and crowdsourced eval database for comparing AI evaluation results across frameworks. | ![](https://img.shields.io/github/stars/evaleval/every_eval_ever?style=social) |

---

# List Authorship

## List Author

Curated by [Daniel Rosehill](https://danielrosehill.com).

Contributions, corrections, and PRs welcome.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the author has dedicated all copyright and related and neighboring rights to this list to the public domain worldwide under [CC0](https://creativecommons.org/publicdomain/zero/1.0/). Linked projects retain their own licenses.
