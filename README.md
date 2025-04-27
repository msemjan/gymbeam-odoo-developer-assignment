# Case Study - Python Developer

## Installation

You need to have [Docker](https://docs.docker.com/engine/install/) and [Docker-Compose](https://docs.docker.com/compose/install/) installed. [Task](https://taskfile.dev/) is also useful to automate running of tasks, but not necessary.

Next, you will need to create a `.env` file. An example is provided for quick setup, so you just need to copy it and edit the values (or leave the default values, but that's not very secure):
```
cp .env.example .env
```

To spin up all the necessary containers run the following command:

```
go-task up
```

The Odoo should run on [`http://localhost:8069/web`](http://localhost:8069/web).

To shut down the containers, run:
```
go-task down
```
