<!--toc:start-->
- [Role: BTRBK](#role-btrbk)
- [Brainstorming and Future Plans](#brainstorming-and-future-plans)
<!--toc:end-->

# Role: BTRBK

Sets up a host to back up specified Btrfs subvolumes. If there is a wildcard (`*`
character) in a specified suvolume, top level, non hidden subvolumes of the
Btrfs path will be backed up.

Otherwise, specify subvolumes directly. If:

- The subvolume does not exist
- The path is not a subvolume
- 'wildcard' paths exist, but are not subvolumes

The role continues, with a report of possible issues

[`btrbk`](https://digint.ch/btrbk) handles incremental snapshots and
sending data to a remote server.

By default, local snapshots are created in a `.snapshots` folder in the
root of the specified subvolume. Alternately, snapshots can be created in a
`.snapshots` directory on the root of the Btrfs volume.

A remote target can also be specified, with divergent retention policy.

# Brainstorming and Future Plans

- [ ] Remote host backup is de facto a toggle - if `btrbk_remote_host` is
  unset, do not write remote targets to template
- [x] if `btrbk_snapshot_dir` is missing, it is created
    - [ ] Not as a subvolume
    - [ ] distinguish local/global? or antifeature?
