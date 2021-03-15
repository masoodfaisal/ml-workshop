oc import-image ml-workshop-elyra --from='quay.io/ml-aml-workshop/elyra:0.0.1' --reference-policy=local --confirm

oc label is ml-workshop-elyra 'opendatahub.io/notebook-image=true'


