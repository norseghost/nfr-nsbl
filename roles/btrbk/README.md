<!--toc:start-->
- [Role: BTRBK](#role-btrbk)
- [Brainstorming and Future Plans](#brainstorming-and-future-plans)
<!--toc:end-->

# Role: BTRBK

Sets up a host to back up specified subvolumes. If there is a wildcard (`*`
character) in a specified suvolume, top level, non hidden subvolumes of the
Btrfs path will be backed up

[`btrbk`](https://digint.ch/btrbk) handles incremental snapshots and
sending data to a remote server.

By default, local snapshots are created in a `.snapshots` folder in the
root of the specified subvolume. Alternately, snapshots can be created in a
`.snapshots` directory on the root of the Btrfs volume.

A remote target can also be specified, with divergent retention policy.

# Brainstorming and Future Plans

- [x] Subvolumes under defined Btrfs volumes are auto-discovered
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
