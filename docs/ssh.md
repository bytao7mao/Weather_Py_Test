# 🔐 Understanding SSH Keys --- Visual Guide

This document provides a **visual explanation** of how SSH keys work,
including how they authenticate you with GitHub and why they are more
secure than passwords.

------------------------------------------------------------------------

# 🖼️ Diagram 1 --- SSH Keys & How They Work

![SSH Keys
Diagram](ssh_diagram1.png)

This diagram shows:

-   The relationship between **private** and **public** keys\
-   How the **user machine** and **server** interact\
-   The overall authentication flow

------------------------------------------------------------------------

# 🖼️ Diagram 2 --- Key Pair Generation & GitHub Authentication

![SSH GitHub Auth
Diagram](ssh_diagram2.png)

This diagram shows:

-   How your machine generates a **private** and **public key**
-   How the **public key is added to GitHub**
-   How SSH Agent and GitHub authenticate your push
-   How the private key never leaves your system

------------------------------------------------------------------------

# 🧩 How SSH Keys Work Internally

SSH keys use **asymmetric cryptography** to prove your identity without
sending passwords.

### Authentication Steps:

1.  Your machine tries to connect using SSH\
2.  GitHub checks if your **public key** exists on your account\
3.  GitHub sends an encrypted challenge using that key\
4.  Your **private key** decrypts the challenge\
5.  GitHub verifies it → **authentication successful**

------------------------------------------------------------------------

# ⚙️ Role of the SSH Agent

The SSH agent:

-   Loads your private key into memory\
-   Keeps it unlocked for your session\
-   Lets you authenticate without typing anything\
-   Allows `git push` and `git pull` automatically

Commands used:

``` bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

------------------------------------------------------------------------

# 🧑‍💻 Why SSH Is Better Than Passwords

  Passwords                     SSH Keys
  ----------------------------- ---------------------------------------
  Can be guessed                Nearly impossible to brute-force
  Must be typed every time      Automatic authentication
  Sent to server in some form   Private key never leaves your machine
  Lower security                Modern crypto algorithms

------------------------------------------------------------------------

# 🎉 Summary

-   SSH keys authenticate you securely without a password\
-   Public key → GitHub\
-   Private key → stays on your machine\
-   SSH agent allows automatic authentication\
-   Git uses SSH for secure pushes and pulls

------------------------------------------------------------------------

# 🔐 GitHub SSH Setup Guide

This guide explains the exact steps you followed to configure SSH
authentication for GitHub on CentOS/Ubuntu.\
You can save this as documentation for future setups.

------------------------------------------------------------------------

# 🔐 GitHub SSH Setup Guide

Use this if you want to connect to GitHub from CentOS/Ubuntu using SSH instead of HTTPS

## 1️⃣ Check for Existing SSH Keys

Before creating a new SSH key, check whether one already exists:

``` bash
ls -al ~/.ssh
```

You were looking for:

-   `id_rsa`
-   `id_rsa.pub`

------------------------------------------------------------------------

## 2️⃣ Generate a New SSH Key

You generated a fresh SSH key using:

``` bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

When prompted:

-   Press **Enter** to accept the default file location
    (`/root/.ssh/id_rsa`)
-   Press **Enter** again to skip adding a passphrase (optional)

This created:

-   `~/.ssh/id_rsa` → **Private key**
-   `~/.ssh/id_rsa.pub` → **Public key**

------------------------------------------------------------------------

## 3️⃣ Start the SSH Agent

Enable the SSH agent:

``` bash
eval "$(ssh-agent -s)"
```

Add your private key to it:

``` bash
ssh-add ~/.ssh/id_rsa
```

------------------------------------------------------------------------

## 4️⃣ Copy Your Public Key

Display the SSH public key:

``` bash
cat ~/.ssh/id_rsa.pub
```

Copy the entire output (the line beginning with `ssh-rsa`).

------------------------------------------------------------------------

## 5️⃣ Add the Key to GitHub

Go to:

**GitHub → Settings → SSH and GPG Keys → New SSH Key**

Then paste the contents of your `id_rsa.pub` file.

------------------------------------------------------------------------

## 6️⃣ Test SSH Connection to GitHub

Verify that your SSH key works:

``` bash
ssh -T git@github.com
```

Expected response:

    Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.

This confirms that GitHub accepts your key.

------------------------------------------------------------------------

## 7️⃣ Use SSH for Git Operations

### Cloning using SSH:

``` bash
git clone git@github.com:username/repo.git
```

### If you already cloned using HTTPS, change the remote:

``` bash
git remote set-url origin git@github.com:username/repo.git
```

------------------------------------------------------------------------

## 🎉 You're Ready!

Your system is now fully configured to push, pull, and interact with
GitHub using secure SSH authentication --- no passwords required.
