# filter_plugins/btrfs.py
def btrfs_subvol_dict(filesystems):
    result = {}
    for fs in filesystems:
        root = next(sv for sv in fs['subvolumes'] if sv['parent'] is None)
        root_mount = root['mountpoints'][0].rstrip('/')
        device = fs['devices'][0]
        for sv in fs['subvolumes']:
            if sv['parent'] is None:
                continue
            abs_path = root_mount + '/' + sv['path'].lstrip('/')
            result[abs_path] = {
                **sv, 'volume_mountpoint': root_mount, 'device': device}
    return result


class FilterModule:
    def filters(self):
        return {'btrfs_subvol_dict': self.btrfs_subvol_dict}

    def btrfs_subvol_dict(self, filesystems):
        return btrfs_subvol_dict(filesystems)
