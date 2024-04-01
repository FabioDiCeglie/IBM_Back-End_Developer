## OpenSSL

# Decrypt file

``` openssl aes-256-cbc -d -a -pbkdf2 -in encrypted_secretfile -out secrets.txt ```

# Encrypt file

``` openssl aes-256-cbc -a -pbkdf2 -in secrets.txt -out secrets.txt.enc ```

# Changing the Encrypt options

``` openssl aes-256-cbc -a -pbkdf2 -iter 2500 -in secrets.txt -out secrets_2500.txt.enc ```