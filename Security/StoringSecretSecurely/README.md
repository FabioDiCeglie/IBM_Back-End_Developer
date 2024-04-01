## VAULT

# Install Vault 

```
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update
sudo apt install vault 
```

# Check Installation 

``` vault ```

# Run Vault server

```  vault server -dev ```

# Set environment variable

Next, you must open a new terminal using Terminal > New Terminal from the top menu, and run the following shell command to specify port 8200 for Vault:

``` export VAULT_ADDR='http://127.0.0.1:8200' ```

``` export VAULT_TOKEN="YOUR ROOT TOKEN HERE" ```

# Check Server

``` vault status ```

You can display your token from a terminal with:

``` echo $VAULT_TOKEN ```

# Vault web UI

Once you are logged in, you can access secrets stored in secret/ by clicking the link.

By default, Vault’s dev server includes KV v2 Secrets Engines at the path secret/, storing secrets within its configured physical storage. Secrets are encrypted before writing to backend storage, so it can never decrypt these values without Vault.

As demonstrated in the video, you will learn to read and write secrets to the server using Python with the help of the hvac library. Before we can do this, we must install the Python package hvac using the Python Package Manager (pip).

# Install hvac

``` python3 -m pip install hvac ```

# Write a secret

``` python3 read_write_vault.py write_secret myapp alice mypassword ```

# Double-check Written Secrets

/secret -> myapp/ ( on Vault UI )

# Read Secret from Vault

``` python3 read_write_vault.py read_secret myapp ```

# Delete Secret from Vault

``` python3 read_write_vault.py delete_secret myapp ```