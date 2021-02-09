### Installation
```bash
  git clone "https://github.com/abadget1/BuildAutomation.git"
  
  cd BuildAutomation
  
  touch .env
  
  Open .env file and store your username, password, and desired file destination. 
  Use the provided format at the bottom of this README.
  
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
