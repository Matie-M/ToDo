# Contributing to TaskFlow

First off, thank you for considering contributing to TaskFlow! It's people like you that make TaskFlow such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots if possible**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Provide specific examples to demonstrate the enhancement**
* **Describe the current behavior and expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Development Setup

### Backend Development

1. Create a virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB URL
   ```

4. Run the development server:
   ```bash
   uvicorn server:app --reload
   ```

### Frontend Development

1. Install dependencies:
   ```bash
   cd frontend
   yarn install
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   ```

3. Start the development server:
   ```bash
   yarn start
   ```

## Coding Guidelines

### Python (Backend)

* Follow PEP 8 style guide
* Use type hints where appropriate
* Write docstrings for functions and classes
* Keep functions small and focused
* Use meaningful variable names

### JavaScript/React (Frontend)

* Use functional components with hooks
* Follow the existing component structure
* Use meaningful component and variable names
* Keep components small and focused
* Add PropTypes or TypeScript types
* Follow the design system in design_guidelines.md

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Example Commit Messages

```
Add task filtering by category

- Implement category filter in FilterBar component
- Add category query parameter to backend API
- Update TaskList to handle category filtering
- Add tests for category filtering

Closes #123
```

## Testing

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
yarn test
```

## Documentation

* Update README.md if you change functionality
* Update design_guidelines.md if you change UI/UX
* Add JSDoc comments for complex functions
* Update API documentation for endpoint changes

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing! 🎉