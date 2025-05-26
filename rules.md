# DraftLine Project Coding Standards & Guidelines

## 🏗️ Project Structure

1. **Repository Organization**
   - Follow the structure outlined in the project documentation
   - Keep related files together (e.g., components, tests, styles)
   - Use clear, descriptive names for files and directories

2. **Version Control**
   - Use feature branches following the pattern: `feature/{short-description}-{issue-number}`
   - Create pull requests for all changes, no direct commits to main
   - Write clear, descriptive commit messages using conventional commits
   - Keep PRs focused and small in scope

## 🧪 Testing & Quality

1. **Test-Driven Development (TDD)**
   - Write tests before implementing features (Red-Green-Refactor)
   - Maintain high test coverage (>80%)
   - Use descriptive test names that explain the expected behavior

2. **Code Quality**
   - Follow Python's PEP 8 style guide for backend code
   - Use ESLint and Prettier for frontend code consistency
   - Run linters and formatters before committing
   - Document complex logic with clear comments

## 🔄 Development Workflow

1. **Branching Strategy**
   - `main`: Production-ready code only
   - `staging`: Pre-production testing
   - `feature/*`: New features and enhancements
   - `bugfix/*`: Bug fixes
   - `hotfix/*`: Critical production fixes

2. **Pull Requests**
   - Link PRs to relevant GitHub issues
   - Include screenshots for UI changes
   - Request reviews from at least one team member
   - All tests must pass before merging

## 🛠️ Technical Standards

1. **Backend (FastAPI)**
   - Use Pydantic models for request/response validation
   - Implement proper error handling and status codes
   - Document API endpoints using OpenAPI/Swagger
   - Use async/await for I/O bound operations

2. **Frontend (React/Next.js)**
   - Use functional components with TypeScript
   - Implement proper state management (Context API/Redux)
   - Follow component composition patterns
   - Optimize for performance (code-splitting, lazy loading)

3. **Database**
   - Use migrations for schema changes (Alembic)
   - Implement proper indexing for query performance
   - Follow the data model defined in `datamodel.md`
   - Use transactions for multi-step operations

## 🔒 Security

1. **Authentication & Authorization**
   - Use Supabase Auth for all authentication
   - Implement role-based access control (RBAC)
   - Never expose sensitive data in logs or responses
   - Validate all user inputs

2. **API Security**
   - Use HTTPS for all API calls
   - Implement rate limiting
   - Sanitize all inputs to prevent injection attacks
   - Use environment variables for sensitive configuration

## 📚 Documentation

1. **Code Documentation**
   - Document all public APIs and components
   - Keep docstrings up-to-date
   - Include examples for complex functions

2. **Project Documentation**
   - Keep `README.md` updated with setup instructions
   - Document architectural decisions in `docs/decisions`
   - Maintain an up-to-date API reference

## 🚀 Deployment & CI/CD

1. **Environment Variables**
   - Use `.env` files for local development
   - Never commit sensitive data to version control
   - Document all required environment variables

2. **CI/CD Pipeline**
   - Run tests on every push
   - Automate deployment to staging after successful tests
   - Require manual approval for production deployments
   - Monitor deployments for errors

## 🤝 Team Collaboration

1. **Code Reviews**
   - Be constructive and respectful in reviews
   - Focus on code quality and maintainability
   - Suggest improvements with clear explanations
   - Respond to review comments promptly

2. **Communication**
   - Use project management tools (Shortcut) for tracking work
   - Keep discussions in the relevant channels
   - Document decisions that affect the codebase

## 📅 Sprint Planning

1. **Sprint Cadence**
   - Follow the sprint schedule in `sprintplan.md`
   - Break down work into 1-2 day tasks
   - Update task status daily
   - Conduct regular retrospectives

2. **Backlog Management**
   - Keep the backlog prioritized
   - Break large stories into smaller, manageable tasks
   - Estimate work using story points
   - Update ticket status promptly

## 📊 Monitoring & Performance

1. **Application Monitoring**
   - Implement logging for key operations
   - Set up error tracking
   - Monitor performance metrics
   - Set up alerts for critical issues

2. **Performance Optimization**
   - Profile and optimize slow queries
   - Implement caching where appropriate
   - Optimize asset loading
   - Monitor and optimize database performance

---

*Last updated: May 25, 2025*
*Version: 1.0.0*
