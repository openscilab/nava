
# Nava Release Instructions

#### Last Update: 2024-04-20

1. Create the `release` branch under `dev`
2. Update all version tags
	1. `setup.py`
	2. `README.md`
	3. `SECURITY.md`
	4. `others/version_check.py`
	5. `others/meta.yaml`
	6. `nava/params.py`
3. Update `CHANGELOG.md`
4. Update `.github/ISSUE_TEMPLATE/bug_report.yml`
   1. Add new version tag to `Nava version` dropbox options
5. Create a PR from `release` to `dev`
	1. Title: `Version x.x` (Example: `Version 0.1`)
	2. Tag all related issues
	3. Labels: `release`
	4. Set milestone
	5. Wait for all CI pass
	6. Need review
6. Merge `dev` branch into `main`
	1. `git checkout main`
	2. `git merge dev`
	3. `git push origin main`
	4. Wait for all CI pass
7. Create a new release
	1. Target branch: `main`
	2. Tag: `vx.x` (Example: `v0.1`)
	3. Title: `Version x.x` (Example: `Version 0.1`)
	4. Copy changelogs
	5. Tag all related issues
8. Bump!!
9. Close this version issues
10. Close milestone
