# Usage

    uvx cookiecutter https://github.com/haron/deploy-template

# Template components

What it uses and why:

* Your own Linux-based server or VM: cheap and safe from the runaway costs 
  that plague serverless platforms
* Tailscale VPN: secures access to your VM or homelab without exposing SSH 
  to the internet
* Ansible: deploys your project to your server in a language-agnostic way
* GitHub Actions: lets you make quick changes with just GitHub access
* Django ORM: worth using even without the rest of the framework
* `uv`: saves a lot of time installing Python dependencies and managing virtualenvs
* `pre-commit`: easy Git hook install
* `Makefile`: handy project scripting
