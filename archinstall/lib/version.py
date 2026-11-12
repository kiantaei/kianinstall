from importlib.metadata import version

# kianinstall is a fork of Arch Linux's archinstall (maintained for Kian OS).
# Report the fork identity first; fall back cleanly when the fork is vendored
# (e.g. /opt/kianinstall on Kian OS media) and has no installed dist metadata.
_FALLBACK = 'kianinstall (vendored fork of archinstall)'


def get_version() -> str:
	for dist in ('kianinstall', 'archinstall'):
		try:
			return version(dist)
		except Exception:
			pass
	return _FALLBACK
