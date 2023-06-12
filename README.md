# FlaskAppWithDocker
This project was created to study more about creating a simple Flask application and docker.

The project is a basic Python Flask app in Docker which return a fake user.

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone git@github.com:GabrielCasemiro/FlaskAppWithDocker.git
$ docker build -t gabrielcasemiro/flaskappwithdocker .
```

### Run the container
Create a container from the image.
```
$ docker run --name flaskappwithdocker -d -p 8080:8080 gabrielcasemiro/flaskappwithdocker
```

Now visit http://localhost:8080/user/1
```
{
    "age": 25,
    "email": "johndoe@email.com",
    "username": "John Doe"
}
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' flaskappwithdocker
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' flaskappwithdocker
6095273a4e9b
```
