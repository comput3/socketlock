# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-10-21

### Added
- Initial release of socketlock
- Async-first process lock using TCP sockets
- Synchronous wrapper for non-async code
- Application-level handshake protocol for security
- Automatic stale lock cleanup
- Cross-platform support (Linux, macOS, Windows)
- Thread-safe implementation
- Rich error messages with PID and port information
- Comprehensive test suite
- Examples and documentation

[Unreleased]: https://github.com/comput3/socketlock/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/comput3/socketlock/releases/tag/v0.1.0