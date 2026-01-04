# Generic Models Tests

These tests cover the shared Pydantic models in `src/generic_models`:
- `app_error.py`: `DetailModel` and `AppErrorResponseModel`
- `generic_response.py`: `GenericResponseModel`
- `generic_pagination.py`: enums, pagination params, and paginated response helpers

## How to run
From the repository root:

```bash
pytest tests/generic_models
```
