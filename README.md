# mb-challenge

The project contains a basic microservice that fetches data from an API (https://swapi.dev/) and returns some of the data in an ordered format.

## Running it locally on minikube

```
kubectl create deployment swapi --image=fguendli/swapi-microservice:5cc504ac41ee85baed656abc7aa794b2dd45fc4a
```

## Exposing the service

```
kubectl expose deployment swapi --type=NodePort --port=5000
```

## Enable port-forwarding

```
kubectl port-forward service/swapi 7080:5000
```

## Testing it out

http://localhost:7080/sorted-people

