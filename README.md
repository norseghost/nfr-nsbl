Yeah, I still don't like vowels

# What

Ansible playbooks to set up my local and remote IT infrastructure

- [x] Enroll: onboard new servers, installing ansible ssh key
- [x] harden:
    - [x] create user, add to sudo group
    - [x] copy ssh pubkey
    - [x] install ufw, let ssh through
- [x] Caddy reverse proxy
    - [x] drop in <service>.caddy config set up
- [x] Headscale orchestrator
   - [x] set up personal and infrastructure users
   - [x] Headscale api key stored in vault
   - [x] `headscale.caddy` service description
   - [x] set a record of service domain on cloudflare
- [-] Tailscale clients
    - [x] enroll new servers
    - [ ] gracefully handle changed parameters
    - [ ] new servers with same names as old need to be removed
- [ ] Docker host
     -  [ ] Add docker.org repository
     -  [ ] Decide which services are Docker appropriate
- [x] UnRAID backups
    - [x] flash backed up daily, if changed
    - [x] Snapshots of selected directories using btrbk
         - [x] Backups to remote server
         - [x] cronjob installed
- [-] Remote backup server
    - [ ] Ensure Btrfs filesystem at backup location (is currently manual)
    - [x] Install btrbk
    - [ ] Install copyparty for read only recovery
        - [ ] photos can be browsed
- [ ] Monitoring
    - [ ] Grafana/Prometheus/alloy probably
- [x] Notifications
    - [x] ntfy.sh
    - [ ] Add drop in templates etc from other hosts
- [ ] OPNSense (a big one)
    - [ ] Add Tailscale subnet router setup via API
    - [ ] Back up settings to NAS (from there to offsite backup)
- [ ] CI/CD pipeline
    - [ ] A local git server (Forgejo probably)
    - [ ] A CI/CD runner. More research is needed
