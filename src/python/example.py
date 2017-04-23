from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(context='minikube')
#config.load_kube_config(context='default-admin')
#r = client.configuration.to_debug_report()
#print(r)
#r = client.configuration.auth_settings()
#print(r)


v1=client.CoreV1Api()
print("** Listing pods with their IPs:")
print("===============================================================================================================")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("{0:16} {1:10.10} {2:15.15} {3:25.25} {4}".format(i.status.pod_ip, i.status.phase, i.metadata.namespace, i.metadata.name,  i.spec.node_name))
    print("* Container(s) in Pod:")
    for x, y in zip(i.spec.containers, i.status.container_statuses):
        print("{0:27} {1}".format(x.name,  y.ready))
    print("--------------------------------------------------------------------------------------------------------------------")

print("")
print("")

print("** Listing services and port types:")
print("===============================================================================================================")
svc = v1.list_service_for_all_namespaces(watch=False)
for i in svc.items:
    print("{0:27} {1:15.15} {2}".format(i.metadata.name,  i.metadata.namespace, i.spec.type)) 
    print("* Labels:")
    for k, v in i.metadata.labels.items():
        print("key={0}, value={1}".format(k, v))
    print("*Port details:")
    for x in i.spec.ports:
        print("{0} node port={1} port={2}".format(x.protocol, x.node_port, x.port))
    print("--------------------------------------------------------------------------------------------------------------------")
