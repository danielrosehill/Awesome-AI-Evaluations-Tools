# Awesome AI Evaluations & Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github&logoColor=white)](https://github.com/danielrosehill/Awesome-AI-Evaluations-Tools)

A list of **open source tools, frameworks, and benchmarks for evaluating AI systems** — LLMs, RAG pipelines, agents, multimodal models, and AI applications.

## Scope

### In Scope
- Open source eval frameworks, harnesses, and platforms
- Benchmark suites and benchmark datasets
- RAG, retrieval, and search evaluation tools
- Agent and tool-use evaluation
- Browser / web-agent evaluation
- Vision and multimodal evaluation
- Grounding, hallucination, bias, sycophancy, refusal/safety evaluation
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

## Machine-readable index

A flat CSV of every entry below — with categorization, stars, last-commit date, and description — is generated weekly via GitHub Actions and stored at [`data/repos.csv`](./data/repos.csv). Use it for filtering, sorting, or importing into a spreadsheet.

---

## Contents

- [Platforms And Software](#platforms-and-software)
- [Benchmarks](#benchmarks)
- [Agentic & Tool Use Evals](#agentic--tool-use-evals)
- [Browser & Web Agent Evals](#browser--web-agent-evals)
- [Coding Evals](#coding-evals)
- [Multimodal Evals](#multimodal-evals)
- [Vision Evals](#vision-evals)
- [RAG & Retrieval](#rag--retrieval)
- [Grounding & Hallucination](#grounding--hallucination)
- [Bias & Fairness (Cultural, Political, Social)](#bias--fairness-cultural-political-social)
- [Sycophancy & Dissent](#sycophancy--dissent)
- [Refusal & Safety](#refusal--safety)
- [Search](#search)
- [Awesome Lists / Resources](#awesome-lists--resources)
- [List Authorship](#list-authorship)

---

## Platforms And Software

| Project | Description | Stars | Updated |
|---|---|---|---|
| [DeepEval](https://github.com/confident-ai/deepeval) | The LLM evaluation framework. | ![](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) | ![](https://img.shields.io/github/last-commit/confident-ai/deepeval) |
| [Phoenix](https://github.com/Arize-ai/phoenix) | AI observability and evaluation platform from Arize. | ![](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) | ![](https://img.shields.io/github/last-commit/Arize-ai/phoenix) |
| [Opik](https://github.com/comet-ml/opik) | Debug, evaluate, and monitor LLM apps, RAG systems, and agentic workflows with tracing and dashboards. | ![](https://img.shields.io/github/stars/comet-ml/opik?style=social) | ![](https://img.shields.io/github/last-commit/comet-ml/opik) |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | UK AISI's framework for large language model evaluations. | ![](https://img.shields.io/github/stars/UKGovernmentBEIS/inspect_ai?style=social) | ![](https://img.shields.io/github/last-commit/UKGovernmentBEIS/inspect_ai) |
| [LangWatch](https://github.com/langwatch/langwatch) | Platform for LLM evaluations and AI agent testing. | ![](https://img.shields.io/github/stars/langwatch/langwatch?style=social) | ![](https://img.shields.io/github/last-commit/langwatch/langwatch) |
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | EleutherAI framework for few-shot evaluation of language models. | ![](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=social) | ![](https://img.shields.io/github/last-commit/EleutherAI/lm-evaluation-harness) |
| [Harbor](https://github.com/harbor-framework/harbor) | Framework for running agent evaluations and creating RL environments. | ![](https://img.shields.io/github/stars/harbor-framework/harbor?style=social) | ![](https://img.shields.io/github/last-commit/harbor-framework/harbor) |
| [Evaluate](https://github.com/huggingface/evaluate) | Hugging Face library for easily evaluating ML models and datasets. | ![](https://img.shields.io/github/stars/huggingface/evaluate?style=social) | ![](https://img.shields.io/github/last-commit/huggingface/evaluate) |
| [OLMES](https://github.com/allenai/olmes) | Reproducible, flexible LLM evaluations from AI2. | ![](https://img.shields.io/github/stars/allenai/olmes?style=social) | ![](https://img.shields.io/github/last-commit/allenai/olmes) |
| [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | Open-source evaluation and testing library for LLM agents. | ![](https://img.shields.io/github/stars/Giskard-AI/giskard-oss?style=social) | ![](https://img.shields.io/github/last-commit/Giskard-AI/giskard-oss) |
| [OpenAI Evals](https://github.com/openai/evals) | Framework for evaluating LLMs and LLM systems plus an open-source registry of benchmarks. | ![](https://img.shields.io/github/stars/openai/evals?style=social) | ![](https://img.shields.io/github/last-commit/openai/evals) |
| [EverOS](https://github.com/EverMind-AI/EverOS) | Build, evaluate, and integrate long-term memory for self-evolving agents. | ![](https://img.shields.io/github/stars/EverMind-AI/EverOS?style=social) | ![](https://img.shields.io/github/last-commit/EverMind-AI/EverOS) |
| [OpenEvals](https://github.com/langchain-ai/openevals) | Readymade evaluators for LLM apps from LangChain. | ![](https://img.shields.io/github/stars/langchain-ai/openevals?style=social) | ![](https://img.shields.io/github/last-commit/langchain-ai/openevals) |
| [Evalite](https://github.com/mattpocock/evalite) | Evaluate your LLM-powered apps with TypeScript. | ![](https://img.shields.io/github/stars/mattpocock/evalite?style=social) | ![](https://img.shields.io/github/last-commit/mattpocock/evalite) |
| [LightEval](https://github.com/huggingface/lighteval) | Hugging Face's all-in-one toolkit for evaluating LLMs across multiple backends. | ![](https://img.shields.io/github/stars/huggingface/lighteval?style=social) | ![](https://img.shields.io/github/last-commit/huggingface/lighteval) |
| [EvalAI](https://github.com/Cloud-CV/EvalAI) | Platform for evaluating state-of-the-art AI on community challenges. | ![](https://img.shields.io/github/stars/Cloud-CV/EvalAI?style=social) | ![](https://img.shields.io/github/last-commit/Cloud-CV/EvalAI) |
| [PyKEEN](https://github.com/pykeen/pykeen) | Python library for learning and evaluating knowledge graph embeddings. | ![](https://img.shields.io/github/stars/pykeen/pykeen?style=social) | ![](https://img.shields.io/github/last-commit/pykeen/pykeen) |
| [RouteLLM](https://github.com/lm-sys/RouteLLM) | Framework for serving and evaluating LLM routers to save costs without compromising quality. | ![](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=social) | ![](https://img.shields.io/github/last-commit/lm-sys/RouteLLM) |
| [Oumi](https://github.com/oumi-ai/oumi) | Easily fine-tune, evaluate, and deploy gpt-oss, Qwen3, DeepSeek-R1, or any open source LLM/VLM. | ![](https://img.shields.io/github/stars/oumi-ai/oumi?style=social) | ![](https://img.shields.io/github/last-commit/oumi-ai/oumi) |
| [Ignite](https://github.com/pytorch/ignite) | High-level library to help train and evaluate neural networks in PyTorch flexibly and transparently. | ![](https://img.shields.io/github/stars/pytorch/ignite?style=social) | ![](https://img.shields.io/github/last-commit/pytorch/ignite) |
| [Bench](https://github.com/arthur-ai/bench) | A tool for evaluating LLMs from Arthur AI. | ![](https://img.shields.io/github/stars/arthur-ai/bench?style=social) | ![](https://img.shields.io/github/last-commit/arthur-ai/bench) |
| [OpenLIT](https://github.com/openlit/openlit) | Open source AI engineering platform: OpenTelemetry-native observability, evaluations, prompt management, guardrails. | ![](https://img.shields.io/github/stars/openlit/openlit?style=social) | ![](https://img.shields.io/github/last-commit/openlit/openlit) |
| [GuideLLM](https://github.com/vllm-project/guidellm) | Evaluate and enhance LLM deployments for real-world inference needs. | ![](https://img.shields.io/github/stars/vllm-project/guidellm?style=social) | ![](https://img.shields.io/github/last-commit/vllm-project/guidellm) |
| [Vivaria](https://github.com/METR/vivaria) | METR's tool for running evaluations and conducting agent elicitation research. | ![](https://img.shields.io/github/stars/METR/vivaria?style=social) | ![](https://img.shields.io/github/last-commit/METR/vivaria) |
| [Helicone](https://github.com/Helicone/helicone) | Open source LLM observability platform — monitor, evaluate, and experiment with one line of code. | ![](https://img.shields.io/github/stars/Helicone/helicone?style=social) | ![](https://img.shields.io/github/last-commit/Helicone/helicone) |
| [EvalScope](https://github.com/modelscope/evalscope) | Streamlined and customizable framework for efficient large model (LLM, VLM, AIGC) evaluation and performance benchmarking. | ![](https://img.shields.io/github/stars/modelscope/evalscope?style=social) | ![](https://img.shields.io/github/last-commit/modelscope/evalscope) |
| [Eval (ai-twinkle)](https://github.com/ai-twinkle/Eval) | High-performance LLM evaluation framework with parallel API calls — up to 17× faster than sequential tools. | ![](https://img.shields.io/github/stars/ai-twinkle/Eval?style=social) | ![](https://img.shields.io/github/last-commit/ai-twinkle/Eval) |
| [simple-llm-eval](https://github.com/cyberark/simple-llm-eval) | Simple LLM evaluation using LLM-as-a-judge, from CyberArk. | ![](https://img.shields.io/github/stars/cyberark/simple-llm-eval?style=social) | ![](https://img.shields.io/github/last-commit/cyberark/simple-llm-eval) |
| [Evidently](https://github.com/evidentlyai/evidently) | Open-source ML and LLM observability framework — evaluate, test, and monitor any AI-powered system. | ![](https://img.shields.io/github/stars/evidentlyai/evidently?style=social) | ![](https://img.shields.io/github/last-commit/evidentlyai/evidently) |
| [ai-eval](https://github.com/stellarlinkco/ai-eval) | Prompt evaluation and optimization system for LLM applications. | ![](https://img.shields.io/github/stars/stellarlinkco/ai-eval?style=social) | ![](https://img.shields.io/github/last-commit/stellarlinkco/ai-eval) |
| [neuro-judge](https://github.com/furqan1pk/neuro-judge) | LLM-as-a-Judge evaluation framework — multi-model, multi-criteria, with cost tracking and HTML reports. | ![](https://img.shields.io/github/stars/furqan1pk/neuro-judge?style=social) | ![](https://img.shields.io/github/last-commit/furqan1pk/neuro-judge) |
| [OpenJudge](https://github.com/agentscope-ai/OpenJudge) | Unified framework for holistic evaluation and quality rewards. | ![](https://img.shields.io/github/stars/agentscope-ai/OpenJudge?style=social) | ![](https://img.shields.io/github/last-commit/agentscope-ai/OpenJudge) |
| [One-Eval](https://github.com/OpenDCAI/One-Eval) | Automated system for LLM evaluation via agents. | ![](https://img.shields.io/github/stars/OpenDCAI/One-Eval?style=social) | ![](https://img.shields.io/github/last-commit/OpenDCAI/One-Eval) |
| [GAGE](https://github.com/HiThink-Research/GAGE) | Unified evaluation engine for LLMs, MLLMs, audio, and diffusion models. | ![](https://img.shields.io/github/stars/HiThink-Research/GAGE?style=social) | ![](https://img.shields.io/github/last-commit/HiThink-Research/GAGE) |
| [OpenCompass](https://github.com/open-compass/opencompass) | LLM evaluation platform supporting a wide range of models over 100+ datasets. | ![](https://img.shields.io/github/stars/open-compass/opencompass?style=social) | ![](https://img.shields.io/github/last-commit/open-compass/opencompass) |
| [Langfuse](https://github.com/langfuse/langfuse) | Open source LLM engineering platform — observability, metrics, evals, prompt management, playground, datasets. | ![](https://img.shields.io/github/stars/langfuse/langfuse?style=social) | ![](https://img.shields.io/github/last-commit/langfuse/langfuse) |
| [MLflow](https://github.com/mlflow/mlflow) | Open source AI engineering platform for agents, LLMs, and ML models — debug, evaluate, monitor, optimize. | ![](https://img.shields.io/github/stars/mlflow/mlflow?style=social) | ![](https://img.shields.io/github/last-commit/mlflow/mlflow) |
| [Agenta](https://github.com/Agenta-AI/agenta) | Open-source LLMOps platform — prompt playground, prompt management, LLM evaluation, and observability. | ![](https://img.shields.io/github/stars/Agenta-AI/agenta?style=social) | ![](https://img.shields.io/github/last-commit/Agenta-AI/agenta) |
| [Ollama Grid Search](https://github.com/dezoito/ollama-grid-search) | Multi-platform desktop application to evaluate and compare LLM models, written in Rust and React. | ![](https://img.shields.io/github/stars/dezoito/ollama-grid-search?style=social) | ![](https://img.shields.io/github/last-commit/dezoito/ollama-grid-search) |
| [Speculators](https://github.com/vllm-project/speculators) | Unified library for building, evaluating, and storing speculative decoding algorithms for LLM inference in vLLM. | ![](https://img.shields.io/github/stars/vllm-project/speculators?style=social) | ![](https://img.shields.io/github/last-commit/vllm-project/speculators) |
| [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval) | Automatic evaluator for instruction-following language models — LLM-based, fast, cheap, replicable. | ![](https://img.shields.io/github/stars/tatsu-lab/alpaca_eval?style=social) | ![](https://img.shields.io/github/last-commit/tatsu-lab/alpaca_eval) |
| [continuous-eval](https://github.com/relari-ai/continuous-eval) | Data-driven evaluation framework for LLM applications. | ![](https://img.shields.io/github/stars/relari-ai/continuous-eval?style=social) | ![](https://img.shields.io/github/last-commit/relari-ai/continuous-eval) |
| [Eureka ML Insights](https://github.com/microsoft/eureka-ml-insights) | Microsoft framework for standardizing evaluations of large foundation models. | ![](https://img.shields.io/github/stars/microsoft/eureka-ml-insights?style=social) | ![](https://img.shields.io/github/last-commit/microsoft/eureka-ml-insights) |
| [SumEval](https://github.com/chakki-works/sumeval) | Well-tested multilingual evaluation framework for text summarization. | ![](https://img.shields.io/github/stars/chakki-works/sumeval?style=social) | ![](https://img.shields.io/github/last-commit/chakki-works/sumeval) |
| [HELM](https://github.com/stanford-crfm/helm) | Stanford CRFM's Holistic Evaluation of Language Models framework for transparent, reproducible evaluations. | ![](https://img.shields.io/github/stars/stanford-crfm/helm?style=social) | ![](https://img.shields.io/github/last-commit/stanford-crfm/helm) |
| [Promptimize](https://github.com/preset-io/promptimize) | Prompt engineering evaluation and testing toolkit from Preset. | ![](https://img.shields.io/github/stars/preset-io/promptimize?style=social) | ![](https://img.shields.io/github/last-commit/preset-io/promptimize) |
| [MiroEval](https://github.com/MiroMindAI/MiroEval) | Unified evaluation framework from MiroMind AI. | ![](https://img.shields.io/github/stars/MiroMindAI/MiroEval?style=social) | ![](https://img.shields.io/github/last-commit/MiroMindAI/MiroEval) |
| [OmniEvalKit](https://github.com/OpenBMB/OmniEvalKit) | Modular toolbox for evaluating LLMs and their omni-extensions across modalities, languages, and tasks. | ![](https://img.shields.io/github/stars/OpenBMB/OmniEvalKit?style=social) | ![](https://img.shields.io/github/last-commit/OpenBMB/OmniEvalKit) |
| [promptfoo](https://github.com/promptfoo/promptfoo) | CLI and library for testing, evaluating, and red-teaming LLM apps — test-driven prompt engineering. | ![](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) | ![](https://img.shields.io/github/last-commit/promptfoo/promptfoo) |
| [FastChat](https://github.com/lm-sys/FastChat) | Platform for training, serving, and evaluating LLMs — home of Chatbot Arena and MT-Bench. | ![](https://img.shields.io/github/stars/lm-sys/FastChat?style=social) | ![](https://img.shields.io/github/last-commit/lm-sys/FastChat) |

## Benchmarks

| Project | Description | Stars | Updated |
|---|---|---|---|
| [Bloom](https://github.com/safety-research/bloom) | Evaluate any behavior immediately. | ![](https://img.shields.io/github/stars/safety-research/bloom?style=social) | ![](https://img.shields.io/github/last-commit/safety-research/bloom) |
| [Dangerous Capability Evaluations](https://github.com/google-deepmind/dangerous-capability-evaluations) | Google DeepMind's evaluation suite for dangerous model capabilities. | ![](https://img.shields.io/github/stars/google-deepmind/dangerous-capability-evaluations?style=social) | ![](https://img.shields.io/github/last-commit/google-deepmind/dangerous-capability-evaluations) |
| [RewardBench](https://github.com/allenai/reward-bench) | The first evaluation tool for reward models. | ![](https://img.shields.io/github/stars/allenai/reward-bench?style=social) | ![](https://img.shields.io/github/last-commit/allenai/reward-bench) |
| [OpenBench](https://github.com/groq/openbench) | Provider-agnostic, open-source evaluation infrastructure for language models. | ![](https://img.shields.io/github/stars/groq/openbench?style=social) | ![](https://img.shields.io/github/last-commit/groq/openbench) |
| [Claw-Eval](https://github.com/claw-eval/claw-eval) | Evaluation harness for evaluating LLMs as agents — all tasks human-verified. | ![](https://img.shields.io/github/stars/claw-eval/claw-eval?style=social) | ![](https://img.shields.io/github/last-commit/claw-eval/claw-eval) |
| [genai-bench](https://github.com/sgl-project/genai-bench) | Benchmark tool for comprehensive token-level performance evaluation of LLM serving systems. | ![](https://img.shields.io/github/stars/sgl-project/genai-bench?style=social) | ![](https://img.shields.io/github/last-commit/sgl-project/genai-bench) |
| [Sparse Frontier](https://github.com/PiotrNawrot/sparse-frontier) | Evaluation framework for training-free sparse attention in LLMs. | ![](https://img.shields.io/github/stars/PiotrNawrot/sparse-frontier?style=social) | ![](https://img.shields.io/github/last-commit/PiotrNawrot/sparse-frontier) |
| [med-lm-envs](https://github.com/MedARC-AI/med-lm-envs) | Automated LLM evaluation suite for medical tasks. | ![](https://img.shields.io/github/stars/MedARC-AI/med-lm-envs?style=social) | ![](https://img.shields.io/github/last-commit/MedARC-AI/med-lm-envs) |
| [MedEvalKit](https://github.com/alibaba-damo-academy/MedEvalKit) | A unified medical evaluation framework. | ![](https://img.shields.io/github/stars/alibaba-damo-academy/MedEvalKit?style=social) | ![](https://img.shields.io/github/last-commit/alibaba-damo-academy/MedEvalKit) |
| [OpenHands Benchmarks](https://github.com/OpenHands/benchmarks) | Benchmark suite for evaluating the OpenHands coding agent. | ![](https://img.shields.io/github/stars/OpenHands/benchmarks?style=social) | ![](https://img.shields.io/github/last-commit/OpenHands/benchmarks) |
| [SkillsBench](https://github.com/benchflow-ai/skillsbench) | Benchmark for evaluating agent skills across a wide range of tasks. | ![](https://img.shields.io/github/stars/benchflow-ai/skillsbench?style=social) | ![](https://img.shields.io/github/last-commit/benchflow-ai/skillsbench) |
| [article-extraction-benchmark](https://github.com/scrapinghub/article-extraction-benchmark) | Benchmark for article extraction libraries from Scrapinghub. | ![](https://img.shields.io/github/stars/scrapinghub/article-extraction-benchmark?style=social) | ![](https://img.shields.io/github/last-commit/scrapinghub/article-extraction-benchmark) |
| [GameWorld](https://github.com/gameworld-project/gameworld) | Game-based benchmark environment for evaluating AI agents. | ![](https://img.shields.io/github/stars/gameworld-project/gameworld?style=social) | ![](https://img.shields.io/github/last-commit/gameworld-project/gameworld) |
| [BIG-bench](https://github.com/google/BIG-bench) | Beyond the Imitation Game collaborative benchmark — 200+ tasks probing LLM capability and limitations. | ![](https://img.shields.io/github/stars/google/BIG-bench?style=social) | ![](https://img.shields.io/github/last-commit/google/BIG-bench) |

## Agentic & Tool Use Evals

| Project | Description | Stars | Updated |
|---|---|---|---|
| [Gorilla](https://github.com/ShishirPatil/gorilla) | Training and evaluating LLMs for function calls (tool calls). | ![](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=social) | ![](https://img.shields.io/github/last-commit/ShishirPatil/gorilla) |
| [AgentBench](https://github.com/THUDM/AgentBench) | A comprehensive benchmark to evaluate LLMs as agents (ICLR'24). | ![](https://img.shields.io/github/stars/THUDM/AgentBench?style=social) | ![](https://img.shields.io/github/last-commit/THUDM/AgentBench) |
| [fast-agent](https://github.com/evalstate/fast-agent) | Code, build, and evaluate agents with excellent model and Skills/MCP/ACP support. | ![](https://img.shields.io/github/stars/evalstate/fast-agent?style=social) | ![](https://img.shields.io/github/last-commit/evalstate/fast-agent) |
| [AgentEvals](https://github.com/langchain-ai/agentevals) | Readymade evaluators for agent trajectories from LangChain. | ![](https://img.shields.io/github/stars/langchain-ai/agentevals?style=social) | ![](https://img.shields.io/github/last-commit/langchain-ai/agentevals) |
| [any-agent](https://github.com/mozilla-ai/any-agent) | Single interface to use and evaluate different agent frameworks. | ![](https://img.shields.io/github/stars/mozilla-ai/any-agent?style=social) | ![](https://img.shields.io/github/last-commit/mozilla-ai/any-agent) |
| [Strands Agents Evals](https://github.com/strands-agents/evals) | Comprehensive evaluation framework for AI agents and LLM applications. | ![](https://img.shields.io/github/stars/strands-agents/evals?style=social) | ![](https://img.shields.io/github/last-commit/strands-agents/evals) |
| [AgentCPM](https://github.com/OpenBMB/AgentCPM) | End-to-end infrastructure for training and evaluating various LLM agents. | ![](https://img.shields.io/github/stars/OpenBMB/AgentCPM?style=social) | ![](https://img.shields.io/github/last-commit/OpenBMB/AgentCPM) |
| [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench) | Evaluating memory in LLM agents via incremental multi-turn interactions (ICLR 2026). | ![](https://img.shields.io/github/stars/HUST-AI-HYZ/MemoryAgentBench?style=social) | ![](https://img.shields.io/github/last-commit/HUST-AI-HYZ/MemoryAgentBench) |
| [HaluMem](https://github.com/MemTensor/HaluMem) | Operation-level hallucination evaluation benchmark tailored to agent memory systems. | ![](https://img.shields.io/github/stars/MemTensor/HaluMem?style=social) | ![](https://img.shields.io/github/last-commit/MemTensor/HaluMem) |
| [HarnessLab](https://github.com/polskiTran/HarnessLab) | Benchmark that evaluates the harness around the LLM — context management, retry policies, tool selection, memory architecture. | ![](https://img.shields.io/github/stars/polskiTran/HarnessLab?style=social) | ![](https://img.shields.io/github/last-commit/polskiTran/HarnessLab) |
| [ResearchHarness](https://github.com/black-yt/ResearchHarness) | Lightweight harness for tool-using LLM agents with fair benchmark evaluation and personal assistant workflows. | ![](https://img.shields.io/github/stars/black-yt/ResearchHarness?style=social) | ![](https://img.shields.io/github/last-commit/black-yt/ResearchHarness) |
| [iris-eval mcp-server](https://github.com/iris-eval/mcp-server) | Agent eval standard for MCP — score output quality, catch safety failures, enforce cost budgets. | ![](https://img.shields.io/github/stars/iris-eval/mcp-server?style=social) | ![](https://img.shields.io/github/last-commit/iris-eval/mcp-server) |
| [agenttrace](https://github.com/luoyuctl/agenttrace) | Local TUI and CLI for evaluating AI coding agent sessions with health scores, slow-run diagnostics, and CI regression gates. | ![](https://img.shields.io/github/stars/luoyuctl/agenttrace?style=social) | ![](https://img.shields.io/github/last-commit/luoyuctl/agenttrace) |
| [AIOpsLab](https://github.com/microsoft/AIOpsLab) | Microsoft holistic framework for designing, developing, and evaluating autonomous AIOps agents. | ![](https://img.shields.io/github/stars/microsoft/AIOpsLab?style=social) | ![](https://img.shields.io/github/last-commit/microsoft/AIOpsLab) |

## Browser & Web Agent Evals

| Project | Description | Stars | Updated |
|---|---|---|---|
| [WebArena](https://github.com/web-arena-x/webarena) | Realistic and reproducible web environment for building and evaluating autonomous agents. | ![](https://img.shields.io/github/stars/web-arena-x/webarena?style=social) | ![](https://img.shields.io/github/last-commit/web-arena-x/webarena) |
| [VisualWebArena](https://github.com/web-arena-x/visualwebarena) | Benchmark for evaluating multimodal agents on realistic visual web tasks. | ![](https://img.shields.io/github/stars/web-arena-x/visualwebarena?style=social) | ![](https://img.shields.io/github/last-commit/web-arena-x/visualwebarena) |
| [Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web) | Dataset and benchmark for developing and evaluating generalist agents for the web. | ![](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web?style=social) | ![](https://img.shields.io/github/last-commit/OSU-NLP-Group/Mind2Web) |
| [BrowserGym](https://github.com/ServiceNow/BrowserGym) | Gym environment for web task automation and agent evaluation in real browsers. | ![](https://img.shields.io/github/stars/ServiceNow/BrowserGym?style=social) | ![](https://img.shields.io/github/last-commit/ServiceNow/BrowserGym) |
| [WebShop](https://github.com/princeton-nlp/WebShop) | Simulated e-commerce environment for evaluating language-grounded web-interaction agents. | ![](https://img.shields.io/github/stars/princeton-nlp/WebShop?style=social) | ![](https://img.shields.io/github/last-commit/princeton-nlp/WebShop) |
| [MiniWoB++](https://github.com/Farama-Foundation/miniwob-plusplus) | Classic benchmark of 100+ small web-interaction tasks for evaluating web-using agents. | ![](https://img.shields.io/github/stars/Farama-Foundation/miniwob-plusplus?style=social) | ![](https://img.shields.io/github/last-commit/Farama-Foundation/miniwob-plusplus) |

## Coding Evals

| Project | Description | Stars | Updated |
|---|---|---|---|
| [SWE-bench](https://github.com/SWE-bench/SWE-bench) | Benchmark for evaluating LLMs on real-world GitHub issue resolution. | ![](https://img.shields.io/github/stars/SWE-bench/SWE-bench?style=social) | ![](https://img.shields.io/github/last-commit/SWE-bench/SWE-bench) |

## Multimodal Evals

| Project | Description | Stars | Updated |
|---|---|---|---|
| [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) | One-for-all multimodal evaluation toolkit across text, image, video, and audio tasks. | ![](https://img.shields.io/github/stars/EvolvingLMMs-Lab/lmms-eval?style=social) | ![](https://img.shields.io/github/last-commit/EvolvingLMMs-Lab/lmms-eval) |
| [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) | Open-source evaluation toolkit for large multi-modality models — supports 220+ LMMs and 80+ benchmarks. | ![](https://img.shields.io/github/stars/open-compass/VLMEvalKit?style=social) | ![](https://img.shields.io/github/last-commit/open-compass/VLMEvalKit) |
| [FlagEvalMM](https://github.com/flageval-baai/FlagEvalMM) | Flexible framework for comprehensive evaluation of multimodal models from BAAI. | ![](https://img.shields.io/github/stars/flageval-baai/FlagEvalMM?style=social) | ![](https://img.shields.io/github/last-commit/flageval-baai/FlagEvalMM) |
| [EASI](https://github.com/EvolvingLMMs-Lab/EASI) | Evaluation framework for large multimodal models. | ![](https://img.shields.io/github/stars/EvolvingLMMs-Lab/EASI?style=social) | ![](https://img.shields.io/github/last-commit/EvolvingLMMs-Lab/EASI) |
| [EmoBench-M](https://github.com/Emo-gml/EmoBench-M) | Benchmark for evaluating emotion recognition capabilities of multimodal LLMs. | ![](https://img.shields.io/github/stars/Emo-gml/EmoBench-M?style=social) | ![](https://img.shields.io/github/last-commit/Emo-gml/EmoBench-M) |
| [multimodalhugs](https://github.com/GerrySant/multimodalhugs) | Multimodal training and evaluation framework built on Hugging Face. | ![](https://img.shields.io/github/stars/GerrySant/multimodalhugs?style=social) | ![](https://img.shields.io/github/last-commit/GerrySant/multimodalhugs) |
| [OmniSafeBench-MM](https://github.com/jiaxiaojunQAQ/OmniSafeBench-MM) | Safety benchmark for multimodal large language models. | ![](https://img.shields.io/github/stars/jiaxiaojunQAQ/OmniSafeBench-MM?style=social) | ![](https://img.shields.io/github/last-commit/jiaxiaojunQAQ/OmniSafeBench-MM) |
| [MMT-Bench](https://github.com/OpenGVLab/MMT-Bench) | Comprehensive multimodal benchmark for evaluating LMMs across massive multitask AGI scenarios. | ![](https://img.shields.io/github/stars/OpenGVLab/MMT-Bench?style=social) | ![](https://img.shields.io/github/last-commit/OpenGVLab/MMT-Bench) |
| [MME-Emotion](https://github.com/FunAudioLLM/MME-Emotion) | Multimodal emotion understanding evaluation benchmark. | ![](https://img.shields.io/github/stars/FunAudioLLM/MME-Emotion?style=social) | ![](https://img.shields.io/github/last-commit/FunAudioLLM/MME-Emotion) |

## Vision Evals

| Project | Description | Stars | Updated |
|---|---|---|---|
| [OmniDocBench](https://github.com/opendatalab/OmniDocBench) | A comprehensive benchmark for document parsing and evaluation (CVPR 2025). | ![](https://img.shields.io/github/stars/opendatalab/OmniDocBench?style=social) | ![](https://img.shields.io/github/last-commit/opendatalab/OmniDocBench) |

## RAG & Retrieval

| Project | Description | Stars | Updated |
|---|---|---|---|
| [Ragas](https://github.com/vibrantlabsai/ragas) | Supercharge your LLM application evaluations. | ![](https://img.shields.io/github/stars/vibrantlabsai/ragas?style=social) | ![](https://img.shields.io/github/last-commit/vibrantlabsai/ragas) |
| [TruLens](https://github.com/truera/trulens) | Evaluation and tracking for LLM experiments and AI agents. | ![](https://img.shields.io/github/stars/truera/trulens?style=social) | ![](https://img.shields.io/github/last-commit/truera/trulens) |
| [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | Open-source framework for RAG evaluation and optimization with AutoML-style automation. | ![](https://img.shields.io/github/stars/Marker-Inc-Korea/AutoRAG?style=social) | ![](https://img.shields.io/github/last-commit/Marker-Inc-Korea/AutoRAG) |
| [RAG Experiment Accelerator](https://github.com/microsoft/rag-experiment-accelerator) | Microsoft framework for running experiments and evaluations on RAG pipelines. | ![](https://img.shields.io/github/stars/microsoft/rag-experiment-accelerator?style=social) | ![](https://img.shields.io/github/last-commit/microsoft/rag-experiment-accelerator) |
| [RAG-grounding-eval](https://github.com/hriday1/RAG-grounding-eval) | Evaluation harness for measuring grounding quality in RAG systems. | ![](https://img.shields.io/github/stars/hriday1/RAG-grounding-eval?style=social) | ![](https://img.shields.io/github/last-commit/hriday1/RAG-grounding-eval) |

## Grounding & Hallucination

| Project | Description | Stars | Updated |
|---|---|---|---|
| [TruthfulQA](https://github.com/sylinrl/TruthfulQA) | Benchmark measuring whether a language model is truthful in generating answers to questions. | ![](https://img.shields.io/github/stars/sylinrl/TruthfulQA?style=social) | ![](https://img.shields.io/github/last-commit/sylinrl/TruthfulQA) |
| [HaluEval](https://github.com/RUCAIBox/HaluEval) | Large-scale hallucination evaluation benchmark for LLMs. | ![](https://img.shields.io/github/stars/RUCAIBox/HaluEval?style=social) | ![](https://img.shields.io/github/last-commit/RUCAIBox/HaluEval) |
| [FActScore](https://github.com/shmsw25/FActScore) | Fine-grained atomic evaluation of factual precision in long-form text generation. | ![](https://img.shields.io/github/stars/shmsw25/FActScore?style=social) | ![](https://img.shields.io/github/last-commit/shmsw25/FActScore) |
| [SelfCheckGPT](https://github.com/potsawee/selfcheckgpt) | Zero-resource black-box hallucination detection for LLMs via self-consistency. | ![](https://img.shields.io/github/stars/potsawee/selfcheckgpt?style=social) | ![](https://img.shields.io/github/last-commit/potsawee/selfcheckgpt) |
| [RAGTruth](https://github.com/ParticleMedia/RAGTruth) | Hallucination corpus for developing trustworthy RAG — word-level annotations on model outputs. | ![](https://img.shields.io/github/stars/ParticleMedia/RAGTruth?style=social) | ![](https://img.shields.io/github/last-commit/ParticleMedia/RAGTruth) |

## Bias & Fairness (Cultural, Political, Social)

| Project | Description | Stars | Updated |
|---|---|---|---|
| [BBQ](https://github.com/nyu-mll/BBQ) | Bias Benchmark for QA — measures social bias across nine demographic categories. | ![](https://img.shields.io/github/stars/nyu-mll/BBQ?style=social) | ![](https://img.shields.io/github/last-commit/nyu-mll/BBQ) |
| [StereoSet](https://github.com/moinnadeem/StereoSet) | Measuring stereotypical bias in pretrained language models. | ![](https://img.shields.io/github/stars/moinnadeem/StereoSet?style=social) | ![](https://img.shields.io/github/last-commit/moinnadeem/StereoSet) |
| [CrowS-Pairs](https://github.com/nyu-mll/crows-pairs) | Challenge dataset measuring social bias in masked language models. | ![](https://img.shields.io/github/stars/nyu-mll/crows-pairs?style=social) | ![](https://img.shields.io/github/last-commit/nyu-mll/crows-pairs) |
| [CDEval](https://github.com/astrodrew/CDEval) | Benchmark for measuring the cultural dimensions of LLMs along Hofstede-style axes. | ![](https://img.shields.io/github/stars/astrodrew/CDEval?style=social) | ![](https://img.shields.io/github/last-commit/astrodrew/CDEval) |
| [OpinionQA](https://github.com/tatsu-lab/opinions_qa) | Evaluating alignment of LLM opinions with U.S. demographic and political groups. | ![](https://img.shields.io/github/stars/tatsu-lab/opinions_qa?style=social) | ![](https://img.shields.io/github/last-commit/tatsu-lab/opinions_qa) |
| [WorldValuesBench](https://github.com/Demon702/WorldValuesBench) | Benchmark for evaluating multicultural value alignment in LLMs, grounded in the World Values Survey. | ![](https://img.shields.io/github/stars/Demon702/WorldValuesBench?style=social) | ![](https://img.shields.io/github/last-commit/Demon702/WorldValuesBench) |
| [BLEnD](https://github.com/nlee0212/BLEnD) | Benchmark for LLMs on everyday knowledge in diverse cultures and languages — probes American/Western-centric bias. | ![](https://img.shields.io/github/stars/nlee0212/BLEnD?style=social) | ![](https://img.shields.io/github/last-commit/nlee0212/BLEnD) |

## Sycophancy & Dissent

| Project | Description | Stars | Updated |
|---|---|---|---|
| [sycophancy-eval](https://github.com/meg-tong/sycophancy-eval) | Evals for measuring sycophancy in LLMs (from Anthropic's "Towards Understanding Sycophancy" paper). | ![](https://img.shields.io/github/stars/meg-tong/sycophancy-eval?style=social) | ![](https://img.shields.io/github/last-commit/meg-tong/sycophancy-eval) |

## Refusal & Safety

Includes general safety red-team tooling, over-refusal (exaggerated safety), jailbreak-resistance, and culturally-specific refusal benchmarks (e.g., Chinese-model behavior on politically sensitive topics).

| Project | Description | Stars | Updated |
|---|---|---|---|
| [HarmBench](https://github.com/centerforaisafety/HarmBench) | Standardized evaluation framework for automated red teaming and robust refusal. | ![](https://img.shields.io/github/stars/centerforaisafety/HarmBench?style=social) | ![](https://img.shields.io/github/last-commit/centerforaisafety/HarmBench) |
| [Rogue](https://github.com/qualifire-dev/rogue) | AI Agent Evaluator & Red Team Platform. | ![](https://img.shields.io/github/stars/qualifire-dev/rogue?style=social) | ![](https://img.shields.io/github/last-commit/qualifire-dev/rogue) |
| [Moonshot](https://github.com/aiverify-foundation/moonshot) | Simple and modular tool to evaluate and red-team any LLM application. | ![](https://img.shields.io/github/stars/aiverify-foundation/moonshot?style=social) | ![](https://img.shields.io/github/last-commit/aiverify-foundation/moonshot) |
| [Agent Security Sandbox](https://github.com/X-PG13/agent-security-sandbox) | Benchmark for evaluating defenses against indirect prompt injection in tool-using LLM agents. | ![](https://img.shields.io/github/stars/X-PG13/agent-security-sandbox?style=social) | ![](https://img.shields.io/github/last-commit/X-PG13/agent-security-sandbox) |
| [AgentDefense-Bench](https://github.com/arunsanna/AgentDefense-Bench) | Comprehensive security benchmark for evaluating infrastructure-layer defenses in MCP-based AI agent systems. | ![](https://img.shields.io/github/stars/arunsanna/AgentDefense-Bench?style=social) | ![](https://img.shields.io/github/last-commit/arunsanna/AgentDefense-Bench) |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Dynamic environment to evaluate attacks and defenses for LLM agents. | ![](https://img.shields.io/github/stars/ethz-spylab/agentdojo?style=social) | ![](https://img.shields.io/github/last-commit/ethz-spylab/agentdojo) |
| [XSTest](https://github.com/paul-rottger/xstest) | Test suite for identifying exaggerated safety behaviours (over-refusal) in LLMs. | ![](https://img.shields.io/github/stars/paul-rottger/xstest?style=social) | ![](https://img.shields.io/github/last-commit/paul-rottger/xstest) |
| [SORRY-Bench](https://github.com/SORRY-Bench/sorry-bench) | Benchmark for systematically evaluating LLM safety refusal across 45 potentially unsafe topics. | ![](https://img.shields.io/github/stars/SORRY-Bench/sorry-bench?style=social) | ![](https://img.shields.io/github/last-commit/SORRY-Bench/sorry-bench) |
| [StrongREJECT](https://github.com/alexandrasouly/strongreject) | Rigorous benchmark for evaluating LLM jailbreak attacks and their effectiveness. | ![](https://img.shields.io/github/stars/alexandrasouly/strongreject?style=social) | ![](https://img.shields.io/github/last-commit/alexandrasouly/strongreject) |
| [Do-Not-Answer](https://github.com/Libr-AI/do-not-answer) | Dataset of questions LLMs should refuse, designed to evaluate safeguards. | ![](https://img.shields.io/github/stars/Libr-AI/do-not-answer?style=social) | ![](https://img.shields.io/github/last-commit/Libr-AI/do-not-answer) |
| [WildGuard](https://github.com/allenai/wildguard) | AI2's open, lightweight moderation tool for evaluating prompt harmfulness and refusal. | ![](https://img.shields.io/github/stars/allenai/wildguard?style=social) | ![](https://img.shields.io/github/last-commit/allenai/wildguard) |
| [CValues](https://github.com/X-PLUG/CValues) | Chinese LLM values benchmark — measures safety and responsibility across Chinese cultural/political context. | ![](https://img.shields.io/github/stars/X-PLUG/CValues?style=social) | ![](https://img.shields.io/github/last-commit/X-PLUG/CValues) |
| [Flames](https://github.com/AI45Lab/Flames) | Highly-adversarial Chinese values alignment benchmark for evaluating refusal on sensitive topics. | ![](https://img.shields.io/github/stars/AI45Lab/Flames?style=social) | ![](https://img.shields.io/github/last-commit/AI45Lab/Flames) |
| [SafetyBench](https://github.com/thu-coai/SafetyBench) | First comprehensive benchmark evaluating LLM safety in Chinese and English across seven harm categories. | ![](https://img.shields.io/github/stars/thu-coai/SafetyBench?style=social) | ![](https://img.shields.io/github/last-commit/thu-coai/SafetyBench) |

## Search

_(Add entries here.)_

## Awesome Lists / Resources

| Project | Description | Stars | Updated |
|---|---|---|---|
| [Every Eval Ever](https://github.com/evaleval/every_eval_ever) | Shared schema and crowdsourced eval database for comparing AI evaluation results across frameworks. | ![](https://img.shields.io/github/stars/evaleval/every_eval_ever?style=social) | ![](https://img.shields.io/github/last-commit/evaleval/every_eval_ever) |
| [llm-benchmark](https://github.com/terryyz/llm-benchmark) | A list of LLM benchmark frameworks. | ![](https://img.shields.io/github/stars/terryyz/llm-benchmark?style=social) | ![](https://img.shields.io/github/last-commit/terryyz/llm-benchmark) |

---

# List Authorship

## List Author

Maintained by [Daniel Rosehill](https://danielrosehill.com).

Contributions, corrections, and PRs welcome.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the author has dedicated all copyright and related and neighboring rights to this list to the public domain worldwide under [CC0](https://creativecommons.org/publicdomain/zero/1.0/). Linked projects retain their own licenses.
