## Cheat Sheet: Managing Applications with Kubernetes

## Basic Commands

| Command                      | Description                                                     |
|------------------------------|-----------------------------------------------------------------|
| kubectl autoscale deployment | Autoscales a Kubernetes Deployment.
| kubectl create configmap	| Creates a ConfigMap resource.
| kubectl get deployments -o wide |	Lists deployments with details.
| kubectl get hpa	| Lists Horizontal Pod Autoscalers (hpa)
| kubectl scale deployment	| Scales a deployment.
| kubectl set image deployment	| Updates the current deployment.
| kubectl rollout	| Manages the rollout of a resource.
| kubectl rollout restart	| Restarts the resource so that the containers restart.
| kubectl rollout undo	| Rollbacks the resource.

## Glossary: Managing Applications with Kubernetes

| Term                      | Definition                                                     |
|------------------------------|-----------------------------------------------------------------|
Cluster Autoscaler	| Also known as CA. An API resource that autoscales the cluster itself, increasing and decreasing the number of available nodes that pods can run on.
Config Map	| An API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume.
Horizontal Pod Autoscaler	| Also known as:HPA An API resource that automatically scales the number of Pod replicas based on targeted CPU utilization or custom metric targets.
Linguistic Analysis |	Detects the tone in a given text.
IBM Cloud catalog	| provides various Services that range from visual recognition to natural language processing and creating chatbots.
Persistent Volume	| An API object that represents a piece of storage in the cluster. Available as a general, pluggable resource that persists beyond the lifecycle of any individual Pod.
Persistent Volume Claim	| Claims storage resources defined in a PersistentVolume so that it can be mounted as a volume in a container.
Rolling Updates	| Provide a way to roll out application changes in an automated and controlled fashion throughout your pods. Rolling updates work with pod templates such as deployments. Rolling updates allow for rollback if something goes wrong.
Secrets	| Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.
Service binding	| is the process needed to consume external Services or backing Services, including REST APIs, databases, and event buses in your applications.
Tone Analyzer Service |	is used for explaining service binding. This IBM Cloud Service uses linguistic analysis to detect tone in a given text.
Vertical Pod Autoscaler also known as VPA	| An API resource that adds resources to an existing machine. A VPA lets you scale a service vertically within a cluster.
Volume	| A directory containing data, accessible to multiple containers in a Pod.
Volume Mount	| entails mounting of the declared volume into a container in the same Pod.
Volume Plugin	| A Volume Plugin enables integration of storage within a Pod.