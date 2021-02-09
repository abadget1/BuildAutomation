### Installation
```bash
  git clone "https://github.com/abadget1/BuildAutomation.git"
  
  cd BuildAutomation
  
  touch .env
  
  Open .env file and store your username, password, or API token.
  Also store the path where you'd like to store this project.
  (Format provided at bottom of this READ.ME)  

  source ~/.my_commands.sh
```
### How to use
```bash
  jumpstart <yourfilenamehere>
```
  
### Enviornment file format (.env)
```bash
  GIT_USERNAME = <yourusername>
  GIT_USER     = <your email>
  GIT_PASSWORD = <your password>
  PATH         = <your working directory path>
  TOKEN        = <Github repo access key>
  ```
