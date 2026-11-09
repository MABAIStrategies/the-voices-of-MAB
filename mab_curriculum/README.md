# MAB Curriculum Architect

This is a separate **local-first curriculum writing agent** for *Strategic AI for Business: The Five Fundamentals*. It does not connect to Gmail, publish lessons, or modify the Executive Correspondence Agent.

## Requirements

- Python 3.10 or newer (standard library only)
- Running Ollama server, with a chat model already pulled locally. The default identifier `qwen3:8b` is only a configurable example, **not** a claim that the model is installed.

## Launch on macOS or Linux

```bash
mkdir -p "$HOME/MAB_Curriculum_Architect"
cp "/absolute/path/to/mab_curriculum_architect.py" "$HOME/MAB_Curriculum_Architect/mab_curriculum_architect.py"
ollama list
python3 "$HOME/MAB_Curriculum_Architect/mab_curriculum_architect.py" test
python3 "$HOME/MAB_Curriculum_Architect/mab_curriculum_architect.py" init
python3 "$HOME/MAB_Curriculum_Architect/mab_curriculum_architect.py" ingest "/absolute/path/to/your_notes.md"
python3 "$HOME/MAB_Curriculum_Architect/mab_curriculum_architect.py" generate --session 1 --kind lesson --model "YOUR_INSTALLED_MODEL"
python3 "$HOME/MAB_Curriculum_Architect/mab_curriculum_architect.py" package --session 1 --model "YOUR_INSTALLED_MODEL"
python3 "$HOME/MAB_Curriculum_Architect/mab_curriculum_architect.py" status
python3 "$HOME/MAB_Curriculum_Architect/mab_curriculum_architect.py" review --id 1 --decision approved --notes "Reviewed for factual accuracy and ready to use"
```

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\MAB_Curriculum_Architect"
Copy-Item "C:\absolute\path\mab_curriculum_architect.py" "$HOME\MAB_Curriculum_Architect\mab_curriculum_architect.py"
ollama list
python "$HOME\MAB_Curriculum_Architect\mab_curriculum_architect.py" test
python "$HOME\MAB_Curriculum_Architect\mab_curriculum_architect.py" generate --session 1 --kind lesson --model "YOUR_INSTALLED_MODEL"
```

## Commands

- `ingest`: Copies a text/Markdown reference into a hash-named `sources/` directory, registers its source ID in SQLite, and keeps the source private to the local machine. Do not ingest sensitive client data you lack permission to use.
- `generate`: Generates one Markdown deliverable in `output/` with provenance IDs, editorial flags, and draft status.
- `package`: Generates six deliverables for the selected session (lesson, script, slides storyboard, exercise, handout, quiz).
- `status`: Reports generated artifacts and approval states.
- `review`: Records human approval or requested changes. It **does not** auto-rewrite or publish the material.
- `test`: Runs local non-model smoke tests.

For a different storage location, set `MAB_CURRICULUM_HOME` to an absolute path in your shell. No cloud APIs or credentials are needed. The local Ollama HTTP API is called at `http://127.0.0.1:11434/api/chat`; the app disallows non-loopback model endpoints by default. Reference excerpts are capped at 18,000 characters per generation; sources exceeding this budget will be partially included. There is no live web verification. Facts not present in references should be treated as provisional, and every output requires instructor approval.
