# 🔐 Understanding SSH Keys --- Visual Guide

This document provides a **visual explanation** of how SSH keys work,
including how they authenticate you with GitHub and why they are more
secure than passwords.

------------------------------------------------------------------------

# 🖼️ Diagram 1 --- SSH Keys & How They Work

![SSH Keys
Diagram](/mnt/data/A_two-section_digital_informational_diagram_provid.png)

This diagram shows:

-   The relationship between **private** and **public** keys\
-   How the **user machine** and **server** interact\
-   The overall authentication flow

------------------------------------------------------------------------

# 🖼️ Diagram 2 --- Key Pair Generation & GitHub Authentication

![SSH GitHub Auth
Diagram](/mnt/data/A_two-part_digital_infographic_illustrates_how_SSH.png)

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

If you'd like, I can also: - Generate a **PDF version** - Create **new
diagrams** - Add this to your GitHub documentation
