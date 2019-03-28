# Gardener (for Github)

The gardener generates the grass field at the same time every day.

take a look.

## How to use?
- Create public key
```bash
$ ssh-keygen -t rsa
# Press 'Enter' three times
$ tree ~/.ssh
├── id_rsa      # Private Key
├── id_rsa.pub  # Public Key
└── known_hosts
```

- Copy your `id_rsa.pub` and paste into git-ssh  
<a href=https://github.com/settings/ssh/new>Link</a>

- Fork this repository

- Start your forked repository.
```bash
git clone http://github.com/@your_id/Gardener
cd Gardener
chmod 755 install.py
sudo ./install.py
```

## Done
Thank you for hiring `Gardener`.