"""Synchronous wrapper for the async socket lock.

This module provides a synchronous interface to the async socket lock
for applications that don't use asyncio.
"""

from __future__ import annotations

import asyncio
import threading
from typing import Any, Dict, Optional

from .async_lock import AsyncSocketLock


class SocketLock:
    """Synchronous wrapper for AsyncSocketLock.

    This class provides a synchronous interface to the async socket lock,
    making it easy to use in non-async applications.
    """

    def __init__(
        self,
        name: str,
        lock_dir: Optional[str] = None,
        timeout: int = 21600,  # 6 hours default
        signature_seed: Optional[str] = None,
    ) -> None:
        """Initialize the synchronous socket lock.

        Args:
            name: Name of the lock (used for lock file naming)
            lock_dir: Directory to store lock files (defaults to system temp)
            timeout: Stale lock timeout in seconds (default: 6 hours)
            signature_seed: Custom seed for handshake signature (optional)
        """
        self._async_lock = AsyncSocketLock(name, lock_dir, timeout, signature_seed)
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._thread: Optional[threading.Thread] = None

    @property
    def port(self) -> Optional[int]:
        """Get the port number if lock is acquired."""
        return self._async_lock.port

    @property
    def pid(self) -> Optional[int]:
        """Get the process ID if lock is acquired."""
        return self._async_lock.pid

    def _ensure_loop(self) -> None:
        """Ensure an event loop is running in a background thread."""
        if self._loop is None or not self._loop.is_running():
            self._loop = asyncio.new_event_loop()

            def run_loop():
                asyncio.set_event_loop(self._loop)
                self._loop.run_forever()

            self._thread = threading.Thread(target=run_loop, daemon=True)
            self._thread.start()

            # Wait for loop to start
            while not self._loop.is_running():
                pass

    def _run_async(self, coro):
        """Run an async coroutine in the background loop."""
        self._ensure_loop()
        future = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return future.result()

    def acquire(self) -> None:
        """Acquire the process lock.

        Raises:
            RuntimeError: If another instance is already running or lock fails
        """
        self._run_async(self._async_lock.acquire())

    def try_acquire(self) -> bool:
        """Try to acquire the lock without blocking.

        Returns:
            True if lock was acquired, False if already held
        """
        return self._run_async(self._async_lock.try_acquire())

    def release(self) -> None:
        """Release the process lock."""
        self._run_async(self._async_lock.release())

        # Clean up the event loop
        if self._loop and self._loop.is_running():
            self._loop.call_soon_threadsafe(self._loop.stop)
            if self._thread:
                self._thread.join(timeout=1)
            self._loop = None
            self._thread = None

    def get_lock_info(self) -> Optional[Dict[str, Any]]:
        """Get information about the current lock if one exists.

        Returns:
            Dictionary with lock info (port, pid, timestamp) or None if no valid lock
        """
        return self._run_async(self._async_lock.get_lock_info())

    def __enter__(self) -> "SocketLock":
        """Context manager entry."""
        self.acquire()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.release()