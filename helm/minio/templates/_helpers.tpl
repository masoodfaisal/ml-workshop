{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "ml-aml-workshop.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "postgresdb.name" -}}
{{- default "postgresql" -}}
{{- end -}}

{{- define "minio.name" -}}
{{- default "minio" -}}
{{- end -}}

{{- define "tensorboard.name" -}}
{{- default "tensorboard" -}}
{{- end -}}

{{- define "tfserving.name" -}}
{{- default "tfserving" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "ml-aml-workshop.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{- define "notebook.fullname" -}}
{{- printf "%s-%s" .Release.Name "keras-tensorflow-panda-notebook" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "odhog.fullname" -}}
{{- printf "%s-%s" "ml-aml-workshop" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "odh.fullname" -}}
{{- printf "%s-%s" .Release.Name "odh" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "kafka.fullname" -}}
{{- printf "%s" "kafka-ml-workshop" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "postgresdb.fullname" -}}
{{- printf "%s" "postgres-ml-workshop" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "minio.fullname" -}}
{{- printf "%s" "minio-ml-workshop" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "tensorboard.fullname" -}}
{{- printf "%s" "tensorboard-ml-workshop" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "tfserving.fullname" -}}
{{- printf "%s" "tensorflowserving-ml-workshop" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "ml-aml-workshop.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "ml-aml-workshop.labels" -}}
helm.sh/chart: {{ include "ml-aml-workshop.chart" . }}
{{ include "ml-aml-workshop.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- define "ml-aml-workshop-is.labels" -}}
opendatahub.io/notebook-image: "true"
{{ include "ml-aml-workshop.labels" . }}
{{- end }}

{{- define "postgresdb.labels" -}}
helm.sh/chart: {{ include "ml-aml-workshop.chart" . }}
{{ include "postgresdb.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- define "minio.labels" -}}
helm.sh/chart: {{ include "ml-aml-workshop.chart" . }}
{{ include "minio.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- define "tensorboard.labels" -}}
helm.sh/chart: {{ include "ml-aml-workshop.chart" . }}
{{ include "tensorboard.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- define "tfserving.labels" -}}
helm.sh/chart: {{ include "ml-aml-workshop.chart" . }}
{{ include "tfserving.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Selector labels
*/}}
{{- define "ml-aml-workshop.selectorLabels" -}}
app.kubernetes.io/name: {{ include "ml-aml-workshop.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{- define "postgresdb.selectorLabels" -}}
app.kubernetes.io/name: {{ include "postgresdb.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{- define "minio.selectorLabels" -}}
app.kubernetes.io/name: {{ include "minio.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{- define "tensorboard.selectorLabels" -}}
app.kubernetes.io/name: {{ include "tensorboard.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{- define "tfserving.selectorLabels" -}}
app.kubernetes.io/name: {{ include "tfserving.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

