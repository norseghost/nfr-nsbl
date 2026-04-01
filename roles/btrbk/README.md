# Role: BTRBK

Sets up a host to back up top level, non hidden subvolumes of mounted btrfs
volumes. [btrbk](https://digint.ch/btrbk) handles incremental snapshots and
sending data to a remote server.

By default, local snapshots are created in a `.snapshots` subvolume on the root
of the btrfs volume.

A remote target can also be specified, with divergent retention policy.

# Roadmap and Brainstorming

- [x] Subvolumes under defined btrfs volumes are autodiscovered
    - [ ] This could be a toggle
- [ ] Remote host backup is de facto a toggle - if `btrbk_remote_host` is
  unset, do not write remote targets to template
- [x] if `btrbk_snapshot_dir` is missing, it is created
    - [ ] Should it also be a subvolume?
    - [ ] What if it exists, but is not as configured
    - [ ] Another toggle
- [ ] Needs to fail if:
    - The specified volume isn't Btrfs
    - There are no top level subvolumes to back up
- Consideration: specify non top level subvolumes
