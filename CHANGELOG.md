# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- `WinMM` engine
### Changed
- `Python 3.14` added to tests
- `run` function in `NavaThread` updated
- `stop` function in `NavaThread` updated
- `README.md` updated
- Test system modified
- `Python 3.6` support dropped
- GitHub actions are limited to the `dev` and `main` branches
## [0.7] - 2024-10-23
### Changed
- `Python 3.13` added to tests
- `engine` parameter added to `play` function
- `engine` parameter added to `NavaThread` class
- `README.md` modified
- Test system modified
- `NavaThread` exception bug fixed
- `__play_win` function renamed to `__play_winsound`
- `__play_mac` function renamed to `__play_afplay`
- `__play_linux` function renamed to `__play_alsa`
## [0.6] - 2024-06-05
### Added
- `play_cli` function
- `SECURITY.md`
### Changed
- `main` function updated
- OSs local checklist added to pull request template
- Test system modified
- `README.md` modified
## [0.5] - 2024-04-03
### Changed
- `loop` parameter added to `play` function
- `NavaThread` class modified
- `README.md` modified
## [0.4] - 2024-02-19
### Added
- `feature_request.yml` template
- `config.yml` for issue template
### Changed
- Bug report template modified
- `NavaThread.stop` method bug fixed
- Test system modified
- `README.md` modified 
## [0.3] - 2024-01-31
### Added
- `NavaThread` class
- `stop` function
- `stop_all` function
### Changed
- `async_mode` parameter added to `play` function
- Test system modified
- `README.md` modified 
- `Python 3.12` added to `linux_test.yml`, `macOS_test.yml` and `windows_test.yml`
## [0.2] - 2023-07-10
### Added
- Logo
- Anaconda package
### Changed
- `quote` decorator bug fixed
- `path_check` decorator bug fixed
- Test system modified
- `README.md` modified 
## [0.1] - 2023-06-10
### Added
- `README.md`
- `__play_win` function
- `__play_linux` function
- `__play_mac` function
- `quote` function
- `path_check` function
- `play` function


[Unreleased]: https://github.com/openscilab/nava/compare/v0.7...dev
[0.7]: https://github.com/openscilab/nava/compare/v0.6...v0.7
[0.6]: https://github.com/openscilab/nava/compare/v0.5...v0.6
[0.5]: https://github.com/openscilab/nava/compare/v0.4...v0.5
[0.4]: https://github.com/openscilab/nava/compare/v0.3...v0.4
[0.3]: https://github.com/openscilab/nava/compare/v0.2...v0.3
[0.2]: https://github.com/openscilab/nava/compare/v0.1...v0.2
[0.1]: https://github.com/openscilab/nava/compare/bd789cc...v0.1
