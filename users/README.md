# Adding users to the workshop
We provide a sample 20 user setup: _user1_.._user20_ each with the password _openshift_
These have beeen populated to the file _users.htpasswd_ in this directory.
First we create a secret with those users and their password:
```
oc create secret generic htpass-secret --from-file=htpasswd=users.htpasswd -n openshift-config
```
We've created a custom resource that sets up this htpasswd mechanism on OpenShift - which we apply as follows:
```
oc apply -f htpasswd.cr
```

If you need to give the users access to a preexising project, say a project called _common-project_, that can be done as follows:
```
for i in {1..20}
do
    oc adm policy add-role-to-user admin user$i -n common-project
done
```

If you need to create users with different credentials consult [this blog](https://medium.com/kubelancer-private-limited/create-users-on-openshift-4-dc5cfdf85661) - on which these instructions are based.
