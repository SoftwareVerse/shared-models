# Shared Models

Package of shared Pydantic models for Userverse services and clients.

## Quick start (GitHub install)

```bash
git clone https://github.com/SoftwareVerse/softwareVerse-shared-python-utils.git
cd softwareVerse-shared-python-utils
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Usage (separate projects)

```bash
# in your other project, with pip
pip install git+https://github.com/SoftwareVerse/softwareVerse-shared-python-utils.git
# with uv
uv add git+https://github.com/SoftwareVerse/softwareVerse-shared-python-utils.git
```

```bash 
# Install a specific release tag (recommended for stability)
# Tags follow semantic versioning (vMAJOR.MINOR.PATCH)
# See: https://github.com/SoftwareVerse/softwareVerse-shared-python-utils/tags
pip install git+https://github.com/SoftwareVerse/softwareVerse-shared-python-utils.git@<tag>

```

```python
from userverse_models import <ModelName>
```

## Tests

```bash
pytest
```

## TODO

- [x] Replace `<tag>` with a real tag from https://github.com/SoftwareVerse/softwareVerse-shared-python-utils/tags
- [ ] Add minimal usage example with real model names
- [ ] Document supported Pydantic version(s)
- [ ] Document compatibility with Python versions
- [ ] Add "Why this package exists" section
- [ ] Add changelog or release process
- [ ] Add shared FastAPI utils section (if still needed)
