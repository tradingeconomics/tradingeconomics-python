# GitHub Actions Workflows

This directory contains GitHub Actions workflows for automated testing, validation, and package deployment. Each workflow serves a specific purpose in the CI/CD pipeline.

---

## Workflows Overview

| Workflow                                       | Trigger                     | Purpose                 | Duration   |
| ---------------------------------------------- | --------------------------- | ----------------------- | ---------- |
| [python-publish.yml](#python-publishyml)       | Push to `release` branch    | Publish package to PyPI | ~5-10 min  |
| [tests.yml](#testsyml)                         | Push to `main` or `release` | Run unit tests          | ~3-5 min   |
| [integration-tests.yml](#integration-testsyml) | Manual dispatch             | Run integration tests   | ~10-15 min |

---

## python-publish.yml

**Full Name**: Upload TradingEconomics Python Package

**Trigger**: Automatically runs on every push to the `release` branch

**Purpose**: Build and publish the Python package to PyPI (Python Package Index)

### Workflow Steps

1. **Checkout Code**: Retrieves the repository code
2. **Set up Python**: Configures Python 3.x environment
3. **Install Dependencies**:
   - Updates pip to latest version
   - Installs build tools (setuptools, wheel, twine)
   - Installs package dependencies from `tradingeconomics/requirements.txt`
4. **Test Package**: Runs all unit tests (`python run_tests.py -v`)
   - **Blocks publication if tests fail**
5. **Build Package**: Creates distribution files (source + wheel)
   - `python setup.py sdist bdist_wheel`
6. **Publish Package**: Uploads to PyPI using Twine
   - Uses `PYPI_API_TOKEN` secret for authentication
   - Skips existing versions (idempotent)
7. **Notify Slack**: Sends deployment status to #dev channel

### Required Secrets

- `PYPI_API_TOKEN`: PyPI API token with upload permissions
- `SLACK_WEBHOOK_URL`: Slack webhook URL for notifications

### Security Notes

- Uses token-based authentication (`__token__` username) instead of user credentials
- Token stored securely in GitHub Secrets
- Only runs on protected `release` branch

### When to Use

This workflow is triggered automatically when:

- Merging a pull request into `release` branch
- Pushing directly to `release` branch
- Creating a new release tag that updates `release` branch

**Do not trigger manually** - publication happens automatically on branch updates.

---

## tests.yml

**Full Name**: Unit Tests

**Trigger**: Automatically runs on every push to `main` or `release` branches

**Purpose**: Continuous validation of code quality through automated unit testing

### Workflow Steps

1. **Checkout Code**: Retrieves the repository code
2. **Set up Python**: Configures Python 3.x environment
3. **Install Dependencies**: Installs package requirements
4. **Test Package**: Runs all unit tests (`python run_tests.py -v`)

### Test Coverage

Executes all unit tests located in:

- `tests/calendar/`
- `tests/markets/`
- `tests/indicators/`
- `tests/earnings/`
- `tests/forecasts/`
- And all other module test directories

### What Gets Tested

- **SDK logic validation**: Ensures core functions work correctly
- **Parameter validation**: Tests input sanitization and error handling
- **Data parsing**: Validates output format conversions (dict, DataFrame, raw)
- **Mock responses**: Uses mocked HTTP responses (no real API calls)

### Performance

- **Duration**: 3-5 minutes typically
- **No API quota consumed**: Tests use mocks, not real API
- **No authentication required**: Mock tests don't need API keys

### When It Runs

- Every push to `main` branch (development)
- Every push to `release` branch (pre-publication validation)
- Pull requests targeting these branches (via branch protection rules)

### Failure Handling

If unit tests fail:

- Pull requests cannot be merged (if branch protection enabled)
- Package publication is blocked (python-publish.yml won't proceed)
- Developers are notified via GitHub notifications

---

## integration-tests.yml

**Full Name**: Integration Tests (Manual)

**Trigger**: Manual execution only via `workflow_dispatch`

**Purpose**: Validate SDK against live Trading Economics API

### Workflow Steps

1. **Checkout Code**: Retrieves the repository code
2. **Set up Python**: Configures Python 3.12 environment
3. **Install Dependencies**:
   - Installs package requirements
   - Installs pytest and testing tools
4. **Run Integration Tests**: Executes pytest on `tests/integration/`
   - Uses `--maxfail=1` flag (stops after first failure)
   - Disables warnings for cleaner output
   - Verbose mode enabled (`-v`)

### Test Coverage

Executes integration tests in:

- `tests/integration/calendar/`
- `tests/integration/indicators/`
- `tests/integration/markets/`
- `tests/integration/earnings/`
- And other integration test directories

### What Gets Tested

- **API contract validation**: Ensures API responses match expected schema
- **Real HTTP requests**: Makes actual calls to Trading Economics API
- **Authentication**: Tests login and authorization flows
- **Data integrity**: Validates real-world data structures
- **Error handling**: Tests API error responses (401, 403, 404)

### API Credentials

Integration tests use `guest:guest` credentials by default (configured in `tests/integration/conftest.py`).

For testing premium endpoints, GitHub Secrets would need:

- `apikey`: Trading Economics API key (not currently configured)

### Why Manual Only?

Integration tests are **not automated** for several reasons:

1. **API Quota Consumption**: Each test run consumes API credits
2. **Network Dependency**: Tests fail if API is temporarily unavailable
3. **Rate Limiting**: Frequent automated runs could hit rate limits
4. **Cost Control**: Manual execution prevents unnecessary quota usage
5. **Slow Execution**: Integration tests take 10-15 minutes (vs 3-5 for unit tests)

### How to Run Manually

1. Navigate to **Actions** tab in GitHub repository
2. Select **Integration Tests (Manual)** workflow
3. Click **Run workflow** button
4. Select branch to test (usually `main` or `release`)
5. Click **Run workflow** to start

### When to Run

Recommended scenarios for manual execution:

- Before major releases (validate against production API)
- After API endpoint changes (verify compatibility)
- When investigating production issues (reproduce with real API)
- Testing new features that interact with specific endpoints
- Validating authentication/authorization changes

### Failure Handling

- Stops on first failure (`--maxfail=1`) for quick feedback
- Check workflow logs to see which endpoint/test failed
- Common failures: network issues, API changes, rate limits

---

## Workflow Best Practices

### For Developers

1. **Run unit tests locally** before pushing:

   ```bash
   python run_tests.py -v
   ```

2. **Don't rely on CI for basic validation**: Fix issues locally first

3. **Use integration tests sparingly**: Manual execution only, not for every change

4. **Monitor workflow failures**: Check Actions tab after pushing

### For Maintainers

1. **Update PYPI_API_TOKEN** when rotating credentials
2. **Keep workflows up to date** with latest GitHub Actions versions
3. **Review integration test coverage** periodically
4. **Monitor API quota usage** if integration tests run frequently

### Branch Protection Recommendations

Configure branch protection rules on `main` and `release`:

- ✅ Require status checks to pass (tests.yml)
- ✅ Require branches to be up to date before merging
- ✅ Require pull request reviews
- ❌ Do not require integration tests (manual only)

---

## Troubleshooting

### python-publish.yml Fails at "Test package"

**Cause**: Unit tests are failing

**Solution**:

1. Check workflow logs for test failure details
2. Run `python run_tests.py -v` locally to reproduce
3. Fix failing tests before pushing to `release`

### python-publish.yml Fails at "Publish package"

**Cause**: PyPI authentication or package issues

**Solution**:

1. Verify `PYPI_API_TOKEN` secret is configured correctly
2. Check if version already exists on PyPI (update version in `setup.py`)
3. Validate package metadata in `setup.py`

### tests.yml Takes Too Long

**Cause**: Test suite has grown significantly

**Solution**:

1. Profile slow tests and optimize
2. Consider splitting into multiple jobs for parallel execution
3. Remove redundant or deprecated tests

### integration-tests.yml Fails with 401 Errors

**Cause**: Authentication failure with API

**Solution**:

1. Verify `guest:guest` credentials still work for basic endpoints
2. For premium endpoints, add `apikey` secret to GitHub
3. Check if API endpoint has changed authentication requirements

### integration-tests.yml Fails with Network Errors

**Cause**: GitHub Actions runner cannot reach API

**Solution**:

1. Check Trading Economics API status
2. Verify API endpoint URLs in code
3. Check for firewall or rate limiting issues
4. Retry workflow after a delay

---

## Maintenance Schedule

### Regular Tasks

- **Weekly**: Review failed workflow runs
- **Monthly**: Update Python and dependencies to latest stable versions
- **Quarterly**: Run integration tests to validate API compatibility
- **Annually**: Rotate PyPI API token for security

### When to Update Workflows

Update workflow configurations when:

- New Python versions are released (update `python-version`)
- GitHub Actions deprecate action versions
- New testing requirements emerge
- Dependency installation process changes
- New secrets or environment variables are needed

---

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Package Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [PyPI Token Authentication](https://pypi.org/help/#apitoken)
- [Pytest Documentation](https://docs.pytest.org/)
